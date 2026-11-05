"""AI check for one MCQ: a second opinion from the OpenAI API, on demand, after she has answered.

The key never reaches the browser. The question is read from the database by id (the client sends only the id), so the
button cannot be used to send arbitrary text to OpenAI. Results are cached per question and each device has a daily limit,
which bounds the spend. The AI verdict is advice only: it never changes the stored answer key or her progress.
"""
import json
import os
import threading
import urllib.error
import urllib.request
from datetime import date

from flask import Blueprint, current_app, jsonify, request

from ..db import db
from ..models import Question
from ..services.device import device_id

bp = Blueprint("ai_check", __name__)

API_URL = "https://api.openai.com/v1/chat/completions"
_LOCK = threading.Lock()
_CACHE: dict = {}      # question id -> result dict (the verdict about a stored question does not change)
_USAGE: dict = {}      # (device id, ISO date) -> calls today


def _model() -> str:
    return os.environ.get("AI_CHECK_MODEL", "gpt-4.1-mini")


def _daily_max() -> int:
    try:
        return max(1, int(os.environ.get("AI_CHECK_DAILY_MAX", "60")))
    except ValueError:
        return 60


SYSTEM = """You are a careful exam-content reviewer for APPSC Group 1 and Group 2 (Andhra Pradesh) preparation.
You are given one multiple-choice question with the answer key and explanation stored in the question bank.
Work out the correct answer yourself first, then compare it with the stored key.

Reply with ONE JSON object and nothing else:
{"verdict": "agrees" | "disagrees" | "unsure",
 "your_answer": "a" | "b" | "c" | "d" | "e" | "",
 "te": "2 to 4 short sentences in simple Telugu: is the stored answer right, and why",
 "en": "the same in 2 to 4 short English sentences",
 "issues": ["each real problem you see: wrong key, two correct options, ambiguous wording, factual error in the explanation, or a date or name that needs checking"]}

Rules:
- Use "agrees" only when you are confident the stored key is correct. Use "unsure" when it depends on a fact you cannot verify, or the question is ambiguous. Use "disagrees" only when you are confident the key is wrong.
- Never invent dates, names or numbers. If you are not sure of a fact, say so in the text and use "unsure".
- "issues" is an empty list when you found nothing wrong.
- Keep Telugu names and terms in Telugu script."""


def _options_text(q) -> str:
    out = []
    en, te = (q.options_en or {}), (q.options_te or {})
    for k in sorted(set(en) | set(te)):
        parts = [x for x in (te.get(k), en.get(k)) if x]
        out.append(f"{str(k).upper()}) " + "  /  ".join(dict.fromkeys(parts)))
    return "\n".join(out)


def _user_prompt(q) -> str:
    qt = "  /  ".join(dict.fromkeys(x for x in (q.question_te, q.question_en) if x))
    ex = "  /  ".join(dict.fromkeys(x for x in (q.explanation_te, q.explanation_en) if x)) or "(none stored)"
    return (f"QUESTION:\n{qt}\n\nOPTIONS:\n{_options_text(q)}\n\n"
            f"STORED ANSWER KEY: {str(q.correct_answer).upper()}\n\nSTORED EXPLANATION:\n{ex[:2500]}")


def _call_openai(messages) -> dict:
    """One chat completion. Raises RuntimeError with a short reason on any failure."""
    key = os.environ.get("OPENAI_API_KEY", "").strip()
    if not key:
        raise RuntimeError("not_configured")
    body = json.dumps({"model": _model(), "messages": messages, "temperature": 0.1, "max_tokens": 700,
                       "response_format": {"type": "json_object"}}).encode()
    req = urllib.request.Request(API_URL, data=body, headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=25) as r:
            data = json.loads(r.read())
    except urllib.error.HTTPError as e:
        current_app.logger.error("ai_check openai http %s %s", e.code, e.read()[:300])
        raise RuntimeError("upstream_%s" % e.code)
    except Exception as e:  # network, timeout, bad JSON
        current_app.logger.error("ai_check openai error %r", e)
        raise RuntimeError("upstream_error")
    try:
        return json.loads(data["choices"][0]["message"]["content"])
    except Exception:
        raise RuntimeError("bad_reply")


def _clean(raw: dict, stored_key: str) -> dict:
    verdict = raw.get("verdict") if raw.get("verdict") in ("agrees", "disagrees", "unsure") else "unsure"
    mine = str(raw.get("your_answer", "")).strip().lower()[:1]
    # Consistency guard: a verdict of agrees/disagrees must match what the model's own answer says.
    if verdict == "agrees" and mine and mine != stored_key:
        verdict = "unsure"
    if verdict == "disagrees" and mine and mine == stored_key:
        verdict = "unsure"
    issues = [str(i)[:300] for i in (raw.get("issues") or []) if str(i).strip()][:5] if isinstance(raw.get("issues"), list) else []
    return {"verdict": verdict, "your_answer": mine.upper(), "stored_answer": stored_key.upper(),
            "te": str(raw.get("te", ""))[:900], "en": str(raw.get("en", ""))[:900], "issues": issues}


@bp.route("/api/ai/check", methods=["POST"])
def ai_check():
    payload = request.get_json(force=True, silent=True)
    qid = payload.get("question_id") if isinstance(payload, dict) else None
    if not isinstance(qid, int) or isinstance(qid, bool) or qid < 1:
        return jsonify({"error": "bad_request"}), 400
    q = db.session.get(Question, qid)
    if q is None:
        return jsonify({"error": "not_found"}), 404

    with _LOCK:
        cached = _CACHE.get(qid)
    if cached:
        return jsonify({**cached, "cached": True})

    dev, today = device_id(), date.today().isoformat()
    with _LOCK:
        used = _USAGE.get((dev, today), 0)
        if used >= _daily_max():
            return jsonify({"error": "limit"}), 429
        _USAGE[(dev, today)] = used + 1
        for k in [k for k in _USAGE if k[1] != today]:   # forget yesterday
            _USAGE.pop(k, None)

    try:
        raw = _call_openai([{"role": "system", "content": SYSTEM}, {"role": "user", "content": _user_prompt(q)}])
    except RuntimeError as e:
        with _LOCK:   # a failed call does not count against her limit
            _USAGE[(dev, today)] = max(0, _USAGE.get((dev, today), 1) - 1)
        reason = str(e)
        return jsonify({"error": "not_configured" if reason == "not_configured" else "unavailable"}), 503
    res = _clean(raw, str(q.correct_answer).strip().lower())
    res["model"] = _model()
    with _LOCK:
        if len(_CACHE) > 5000:
            _CACHE.clear()
        _CACHE[qid] = res
    return jsonify(res)
