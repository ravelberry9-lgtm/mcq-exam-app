"""Async voice-tutor service (uvicorn). Text/SSE endpoints now; audio in/out layers on top of these.
Run: uvicorn voice_service.server:app --host 0.0.0.0 --port $PORT"""
import asyncio
import base64
import json
import os
import re
import random
import time
from contextlib import asynccontextmanager

from fastapi import Depends, FastAPI, File, Form, Header, HTTPException, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from sqlalchemy import create_engine, text
from sse_starlette.sse import EventSourceResponse

from answers import parse_answer
from auth import verify_token
from content import NotesIndex, load_note_rows, make_chunks
from questions import next_question, record_answer
import ledger
import stt
import tts
import turn as turnlib
from tutor import ask, feedback_text, question_text

DB_URL = os.environ.get("DATABASE_URL", "sqlite:///app_v3.db").replace("postgres://", "postgresql://", 1)
SECRET = os.environ["SECRET_KEY"]
ORIGINS = [o for o in os.environ.get("APP_ORIGINS", "").split(",") if o]
DAILY_CAP = float(os.environ.get("DAILY_COST_CAP_USD", "3"))
STATE: dict = {}
LLM_USD_PER_CALL = float(os.environ.get("LLM_USD_PER_CALL", "0.002"))  # rough, for the cap only
LOCKS: dict = {}
MAX_AUDIO_BYTES = 1_000_000  # ~30 s of 16 kHz mono 16-bit
SESSIONS: dict = {}  # device_id -> {"q": current question, "lang": "te"}


@asynccontextmanager
async def lifespan(_):
    STATE["engine"] = create_engine(DB_URL, pool_pre_ping=True)
    STATE["index"] = NotesIndex(make_chunks(load_note_rows(STATE["engine"])))
    ledger.init(STATE["engine"])
    yield

app = FastAPI(lifespan=lifespan)
app.add_middleware(CORSMiddleware, allow_origins=ORIGINS, allow_methods=["*"], allow_headers=["*"])


@app.middleware("http")
async def limit_body(request, call_next):
    cl = request.headers.get("content-length")
    if cl and cl.isdigit() and int(cl) > MAX_AUDIO_BYTES + 100_000:
        from fastapi.responses import JSONResponse
        return JSONResponse({"detail": "too large"}, status_code=413)
    return await call_next(request)


def device(authorization: str = Header(default="")) -> str:
    d = verify_token(SECRET, authorization.removeprefix("Bearer ").strip())
    if not d:
        raise HTTPException(401, "bad or expired token")
    return d


@app.get("/health")
def health():
    return {"ok": True, "chunks": STATE["index"].N}


class AskIn(BaseModel):
    text: str = Field(max_length=1000)
    subject: str = "ap_history"
    history: list[dict] = Field(default_factory=list, max_length=12)


def clean_history(h):
    out = []
    for m in h[-6:]:
        if isinstance(m, dict) and m.get("role") in ("user", "assistant") and isinstance(m.get("content"), str):
            out.append({"role": m["role"], "content": m["content"][:1000]})
    return out


@app.post("/api/ask")
async def api_ask(body: AskIn, dev: str = Depends(device)):
    if ledger.spent(STATE["engine"], dev) >= DAILY_CAP:
        raise HTTPException(429, "daily limit")

    async def gen():
        t0 = time.time()
        try:
            async for kind, val in ask(STATE["index"], body.text, clean_history(body.history), body.subject):
                yield {"event": kind, "data": json.dumps(val, ensure_ascii=False)}
        finally:
            ledger.add(STATE["engine"], dev, LLM_USD_PER_CALL)
        yield {"event": "done", "data": json.dumps({"ms": int((time.time() - t0) * 1000)})}
    return EventSourceResponse(gen())


class QIn(BaseModel):
    subject: str = "ap_history"
    chapter_id: int | None = None
    lang: str = "te"


@app.post("/api/question")
def api_question(body: QIn, dev: str = Depends(device)):
    with STATE["engine"].connect() as c:
        sid = c.execute(text("SELECT id FROM subjects WHERE slug=:s"), {"s": body.subject}).scalar()
        q = next_question(c, dev, sid, body.chapter_id, rng=random)
    if not q:
        raise HTTPException(404, "no questions")
    SESSIONS[dev] = {"q": q, "lang": body.lang}
    return {"question_id": q["id"], "speak": question_text(q, body.lang), "difficulty": q["difficulty"]}


class AIn(BaseModel):
    text: str


@app.post("/api/answer")
def api_answer(body: AIn, dev: str = Depends(device)):
    s = SESSIONS.get(dev)
    if not s:
        raise HTTPException(409, "no active question")
    q, lang = s["q"], s["lang"]
    opts = q["options_te"] if lang == "te" and q["options_te"] else q["options_en"]
    kind, letter = parse_answer(body.text, len(opts), opts)
    if kind == "repeat":
        return {"kind": "repeat", "speak": question_text(q, lang)}
    if kind == "skip":
        return {"kind": "skip", "speak": feedback_text(q, "-", lang)[1]}
    if kind == "unclear":
        return {"kind": "unclear", "speak": "సరిగ్గా అర్థం కాలేదు. A, B, C, D లో ఏది?" if lang == "te" else "Sorry, which option: A, B, C or D?"}
    ok, speak = feedback_text(q, letter, lang)
    with STATE["engine"].begin() as c:
        record_answer(c, dev, q["id"], ok)
    SESSIONS.pop(dev, None)
    return {"kind": "graded", "correct": ok, "picked": letter, "speak": speak}


TELUGU = re.compile(r"[\u0C00-\u0C7F]")
MSG = {
    "te": {"cap": "ఈ రోజు వాయిస్ పరిమితి అయిపోయింది. రేపు మళ్ళీ మాట్లాడుకుందాం.",
           "stt": "క్షమించండి, నాకు వినిపించలేదు. మళ్ళీ చెప్పండి.",
           "busy": "ఒక్క నిమిషం, ముందు ప్రశ్న పూర్తి చేస్తాను.",
           "fail": "క్షమించండి, ఇప్పుడు సమాధానం ఇవ్వలేకపోతున్నాను. మళ్ళీ ప్రయత్నించండి."},
    "en": {"cap": "Today's voice limit is reached. Let's continue tomorrow.",
           "stt": "Sorry, I couldn't hear that. Please say it again.",
           "busy": "One moment, I'm still finishing the last one.",
           "fail": "Sorry, I can't answer right now. Please try again."},
}


def _ev(kind, data):
    return {"event": kind, "data": json.dumps(data, ensure_ascii=False)}


async def _speak(text_, spend):
    try:
        audio, usd = await tts.synth(text_)
        spend[0] += usd
        return base64.b64encode(audio).decode() if audio else None
    except Exception:
        return None  # the text still shows on screen; never break the turn over audio


@app.post("/api/voice/turn")
async def voice_turn(audio: UploadFile = File(...), lang: str = Form("te"), dev: str = Depends(device)):
    raw = await audio.read(MAX_AUDIO_BYTES + 1)
    if len(raw) > MAX_AUDIO_BYTES:
        raise HTTPException(413, "audio too long")
    try:
        pcm = stt.wav_to_pcm(raw)
    except Exception:
        raise HTTPException(400, "need 16 kHz mono 16-bit WAV")
    if len(pcm) < 3200:  # < 0.1 s
        raise HTTPException(400, "audio too short")
    lock = LOCKS.setdefault(dev, asyncio.Lock())
    if lock.locked():
        raise HTTPException(409, "previous turn still running")
    await lock.acquire()  # no await between the check and this line, so two requests cannot both pass
    lang = lang if lang in MSG else "te"

    async def gen():
        _tasks = []

        def mk(coro):
            tk = asyncio.create_task(coro)
            _tasks.append(tk)
            return tk
        spend = [0.0]
        try:
            spend[0] = (len(pcm) / 32000 / 60 * sum(stt.PER_MIN.get(p, 0.01) for p in stt.enabled()) + LLM_USD_PER_CALL)
            try:
                if ledger.spent(STATE["engine"], dev) >= DAILY_CAP:
                    yield _ev("sentence", {"text": MSG[lang]["cap"], "audio": None}); yield _ev("done", {"capped": True}); return
                try:
                    heard, errs = await stt.transcribe(pcm)
                except Exception:
                    heard, errs = [], {}
                if not heard:
                    print("stt errors:", dev, errs, flush=True)
                    yield _ev("error", {"code": "stt", "providers": sorted(errs)})
                    yield _ev("sentence", {"text": MSG[lang]["stt"], "audio": await _speak(MSG[lang]["stt"], spend)})
                    yield _ev("done", {}); return
                texts = [h["text"] for h in heard]
                if any(TELUGU.search(t) for t in texts): lang_ = "te"
                else: lang_ = "en" if lang == "te" and not TELUGU.search(" ".join(texts)) and len(" ".join(texts).split()) > 2 else lang
                yield _ev("transcript", {"heard": heard})
                sess = SESSIONS.get(dev)
                out = []  # sentences to speak, in order
                if sess:
                    q = sess["q"]; qlang = sess["lang"]
                    opts = q["options_te"] if qlang == "te" and q["options_te"] else q["options_en"]
                    kind, letter = turnlib.pick_answer(texts, len(opts), opts)
                    if kind == "answer":
                        ok, sp = feedback_text(q, letter, qlang)
                        with STATE["engine"].begin() as c:
                            record_answer(c, dev, q["id"], ok)
                        SESSIONS.pop(dev, None)
                        yield _ev("graded", {"correct": ok, "picked": letter})
                        out = [sp]
                    elif kind == "repeat":
                        out = [question_text(q, qlang)]
                    elif kind == "skip":
                        SESSIONS.pop(dev, None); out = [feedback_text(q, "-", qlang)[1]]
                    # unclear: fall through to doubt/clarify below
                if not out and turnlib.looks_like_quiz_request(texts):
                    with STATE["engine"].connect() as c:
                        sid = c.execute(text("SELECT id FROM subjects WHERE slug='ap_history'")).scalar()
                        q = next_question(c, dev, sid, rng=random)
                    if q:
                        SESSIONS[dev] = {"q": q, "lang": lang_}
                        yield _ev("question", {"question_id": q["id"]})
                        out = [question_text(q, lang_)]
                if out:
                    tasks = [mk(_speak(t, spend)) for t in out]
                    for t, task in zip(out, tasks):
                        yield _ev("sentence", {"text": t, "audio": await task})
                else:
                    if sess and kind == "unclear" and len(texts[0].split()) <= 3:
                        msg = "సరిగ్గా అర్థం కాలేదు. A, B, C, D లో ఏది?" if sess["lang"] == "te" else "Sorry, which option: A, B, C or D?"
                        yield _ev("sentence", {"text": msg, "audio": await _speak(msg, spend)}); yield _ev("done", {}); return
                    tasks = []
                    async for kind_, val in ask(STATE["index"], turnlib.merged_for_llm(texts)):
                        if kind_ == "meta":
                            yield _ev("meta", val)
                        else:
                            task = mk(_speak(val, spend)); tasks.append((val, task))
                            # emit earlier sentences as soon as their audio is ready
                            while tasks and tasks[0][1].done():
                                t, tk = tasks.pop(0); yield _ev("sentence", {"text": t, "audio": tk.result()})
                    for t, tk in tasks:
                        yield _ev("sentence", {"text": t, "audio": await tk})
                yield _ev("done", {})
            except Exception as e:
                yield _ev("error", {"code": "internal", "detail": type(e).__name__})
                yield _ev("sentence", {"text": MSG[lang]["fail"], "audio": None})
                yield _ev("done", {})
        finally:
            for tk in _tasks:
                if not tk.done():
                    tk.cancel()
            try:
                ledger.add(STATE["engine"], dev, spend[0], 1)
            except Exception:
                pass
            lock.release()

    return EventSourceResponse(gen())


class TIn(BaseModel):
    text: str


@app.post("/api/tts")
async def api_tts(body: TIn, dev: str = Depends(device)):
    if ledger.spent(STATE["engine"], dev) >= DAILY_CAP:
        raise HTTPException(429, "daily limit")
    audio, usd = await tts.synth(body.text[:600])
    ledger.add(STATE["engine"], dev, usd)
    return {"audio": base64.b64encode(audio).decode() if audio else None}
