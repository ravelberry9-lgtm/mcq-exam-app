"""Live (speech-to-speech) tutor.

The browser talks to OpenAI Realtime directly over WebRTC (low delay, natural interruption). This service only
  1. creates the call, so the API key never reaches the browser, and
  2. runs the tools the model calls: notes search, next quiz question, answer grading.
Grading, progress and the spend cap stay in code, never in the model.
"""
import json
import os
import random

import httpx
from sqlalchemy import text

from questions import next_question, record_answer
from tutor import feedback_text, pick_lang

MODEL = os.environ.get("REALTIME_MODEL", "gpt-realtime-2.1-mini")
FALLBACK_MODEL = "gpt-realtime-2.1"
VOICE = os.environ.get("REALTIME_VOICE", "marin")
# Deliberately generous per-minute estimates. They only drive the daily cap, not billing.
USD_PER_MIN = {"gpt-realtime-2.1-mini": 0.04, "gpt-realtime-2.1": 0.12}
TRANSCRIBE_LANG = os.environ.get("RT_TRANSCRIBE_LANG", "te")
STRONG = 15.0  # same threshold as the text tutor: below this a notes match is only a weak hint

INSTRUCTIONS = """You are a warm, patient voice tutor for a Telugu-speaking APPSC Group 1 and Group 2 aspirant. Talk like a good teacher having a conversation: short, natural, friendly. No lists, no markdown, no symbols, nothing that sounds like reading a document.

LANGUAGE
- Mirror her language: Telugu, English, or mixed Telugu with English terms, exactly as she speaks. If she mixes, you mix. Pronounce Telugu names and terms the Telugu way.
- Keep replies to roughly 2 to 5 sentences unless she asks for detail. Ask at most one question at a time.

HOW TO ANSWER STUDY QUESTIONS
- For any history or exam question, FIRST call search_notes with the key Telugu term(s). Answer from what the notes say, and say it is from her notes (for example 'నీ నోట్స్ ప్రకారం...' or 'as per your notes').
- If the notes do not cover it (search returns nothing or a weak match), say so plainly, then answer from general knowledge and call it general knowledge ('ఇది నోట్స్‌లో లేదు, సాధారణంగా...'). Never present general knowledge as her notes. Never invent dates, names or numbers; if unsure, say you are unsure.
- If what you heard is noise, a fragment, or not Telugu or English, do NOT answer it as if she asked something. Say briefly 'సరిగ్గా వినపడలేదు, మళ్ళీ చెప్పండి' (or the English equivalent) and wait. Never invent a question for her.
- You are hearing speech, and names can be misheard. If a word sounds like a term from the notes, use your judgment, and when it matters ask 'Did you mean ...?'. If you really did not catch something, ask her to say it again.

QUIZ MODE
- When she asks for a question or a quiz, call next_question. Read the question, then read EVERY option one by one with its letter: say 'ఎ', 'బి', 'సి', 'డి' (A, B, C, D) when speaking Telugu, or A, B, C, D in English. Never skip the options or the letters. She can also tap the A/B/C/D buttons on screen. Then stop and wait.
- When she answers (she may say ఎ, బి, సి, డి, or A, B, C, D, or the option text; single letters are easy to mishear), work out which option she means. If it is clear, call check_answer with that letter. If it is unclear (she says something that could be two options, or she is thinking aloud), ask which option, do NOT guess. If she says she wants to skip, call skip_question.
- After check_answer, tell her whether she was right, give the correct answer and the short explanation from the tool in your own words, then offer the next question.
- If she asks a doubt in the middle of a question, answer it, then remind her of the options. Grading is done only by the tools, never by you.

Her vocabulary for this course (words she may say): {vocab}"""

TOOLS = [
    {"type": "function", "name": "search_notes",
     "description": "Search her own study notes (AP history). Call before answering any study question. Pass the key terms, in Telugu when possible.",
     "parameters": {"type": "object", "properties": {"query": {"type": "string"}}, "required": ["query"]}},
    {"type": "function", "name": "next_question",
     "description": "Get the next practice question (adaptive to her level). Returns the question and options to read aloud.",
     "parameters": {"type": "object", "properties": {}}},
    {"type": "function", "name": "check_answer",
     "description": "Grade her answer to the current practice question. letter is A, B, C, D or E. Call only when she clearly chose an option.",
     "parameters": {"type": "object", "properties": {"letter": {"type": "string"}}, "required": ["letter"]}},
    {"type": "function", "name": "skip_question",
     "description": "She wants to skip the current practice question. Returns the correct answer to tell her.",
     "parameters": {"type": "object", "properties": {}}},
]
TOOL_NAMES = {t["name"] for t in TOOLS}


def instructions(vocab) -> str:
    return INSTRUCTIONS.format(vocab=", ".join(vocab[:60]) if vocab else "(none)")


def session_config(model: str, vocab, full: bool = True) -> dict:
    cfg = {"type": "realtime", "model": model, "instructions": instructions(vocab),
           "audio": {"output": {"voice": VOICE}}, "tools": TOOLS, "tool_choice": "auto"}
    if full:
        cfg["audio"]["input"] = {
            "noise_reduction": {"type": "near_field"},
            # No prompt here: a vocabulary prompt gets echoed back as the "transcript" when the audio is short or quiet.
            # Language hint: without it short Telugu phrases get "heard" as Japanese/Polish/etc. ("" = auto-detect)
            "transcription": {"model": "gpt-4o-transcribe", **({"language": TRANSCRIBE_LANG} if TRANSCRIBE_LANG else {})},
            # Plain server VAD with a high threshold: room noise on a phone must not start a turn.
            "turn_detection": {"type": "server_vad", "threshold": float(os.environ.get("RT_VAD_THRESHOLD", "0.6")),
                               "prefix_padding_ms": 300, "silence_duration_ms": int(os.environ.get("RT_VAD_SILENCE_MS", "800"))},
        }
    return cfg


async def create_call(sdp: str, vocab):
    """Forward the browser's WebRTC offer to OpenAI with the server-side key. Returns (answer_sdp, model_used).
    Tries the full config, then a minimal one, then the full-size model, and reports what OpenAI said if all fail."""
    key = os.environ["OPENAI_API_KEY"]
    attempts = [(MODEL, True), (MODEL, False)]
    if MODEL != FALLBACK_MODEL:
        attempts.append((FALLBACK_MODEL, False))
    last = ""
    for model, full in attempts:
        cfg = session_config(model, vocab, full)
        async with httpx.AsyncClient(timeout=20) as c:
            r = await c.post("https://api.openai.com/v1/realtime/calls", headers={"Authorization": f"Bearer {key}"},
                             files={"sdp": (None, sdp, "application/sdp"), "session": (None, json.dumps(cfg), "application/json")})
        if r.status_code < 300:
            return r.text, model
        last = f"{model} full={full}: {r.status_code} {r.text[:300]}"
    raise RuntimeError("realtime call failed: " + last)


# ── tools (plain functions, no model involved) ────────────────────────────────

def _options(q, lang):
    o = q["options_te"] if lang == "te" and q["options_te"] else q["options_en"]
    return o


def run_tool(engine, index, sessions, dev, name, args):
    args = args if isinstance(args, dict) else {}
    if name == "search_notes":
        query = str(args.get("query", ""))[:300]
        hits = index.search(query, k=3, subject="ap_history") if query.strip() else []
        if not hits:
            return {"strong": False, "results": [], "hint": "Nothing in her notes. Say so, then answer from general knowledge."}
        strong = hits[0][1] >= STRONG
        return {"strong": strong,
                "hint": "Strong match: answer from these notes." if strong else
                        "Weak match only. If a term here sounds like what she said, ask 'Did you mean ...?'. Otherwise say the notes do not cover it.",
                "results": [{"chapter": c.chapter_title_te or c.chapter_title_en, "section": c.heading, "text": c.text[:900]}
                            for c, _ in (hits if strong else hits[:2])]}
    if name == "next_question":
        with engine.connect() as c:
            sid = c.execute(text("SELECT id FROM subjects WHERE slug='ap_history'")).scalar()
            q = next_question(c, dev, sid, rng=random)
        if not q:
            return {"error": "no questions available"}
        lang = pick_lang(q, "te")
        sessions[dev] = {"q": q, "lang": lang}
        qt = q["question_te"] if lang == "te" and q["question_te"] else q["question_en"]
        return {"question": qt, "language": lang,
                "options": {k.upper(): v for k, v in _options(q, lang).items()}}
    if name in ("check_answer", "skip_question"):
        sess = sessions.get(dev)
        if not sess:
            return {"error": "There is no active question. Offer her a new one."}
        q, lang = sess["q"], sess["lang"]
        opts = _options(q, lang)
        if name == "skip_question":
            sessions.pop(dev, None)
            return {"skipped": True, "correct_letter": q["correct_answer"].upper(),
                    "correct_text": opts.get(q["correct_answer"], ""), "explanation": feedback_text(q, "-", lang)[1]}
        letter = str(args.get("letter", "")).strip().lower()[:1]
        if letter not in opts:
            return {"error": f"'{letter.upper()}' is not an option. Ask her which option she means."}
        ok, speak = feedback_text(q, letter, lang)
        with engine.begin() as c:
            record_answer(c, dev, q["id"], ok)
        sessions.pop(dev, None)
        return {"correct": ok, "picked": letter.upper(), "correct_letter": q["correct_answer"].upper(),
                "correct_text": opts.get(q["correct_answer"], ""), "explanation": speak}
    return {"error": "unknown tool"}
