"""Speech-to-text ensemble. Providers run in parallel; the first good answer starts the turn,
the others get a short grace window so disagreement can be detected. Keys never appear in errors."""
import asyncio
import base64
import io
import json
import os
import time
import wave

import httpx

PROVIDER_TIMEOUT = 20
GRACE_S = float(os.environ.get("STT_GRACE_S", "0.7"))
VOCAB = [l.strip() for l in os.environ.get("STT_VOCAB", "").split("|") if l.strip()]


class NotConfigured(Exception):
    pass


def need(name: str) -> str:
    v = os.getenv(name, "").strip()
    if not v:
        raise NotConfigured(name)
    return v


async def run_sarvam(wav: bytes, pcm: bytes) -> str:
    key = need("SARVAM_API_KEY")
    data = {"model": os.getenv("SARVAM_MODEL", "saaras:v3"), "mode": "transcribe"}
    if os.getenv("SARVAM_LANG"):
        data["language_code"] = os.environ["SARVAM_LANG"]
    async with httpx.AsyncClient(timeout=PROVIDER_TIMEOUT) as c:
        r = await c.post(
            "https://api.sarvam.ai/speech-to-text",
            headers={"api-subscription-key": key},
            files={"file": ("utt.wav", wav, "audio/wav")},
            data=data,
        )
    if r.status_code >= 400:
        raise RuntimeError(f"HTTP {r.status_code}: {r.text[:200]}")
    return r.json().get("transcript", "")


async def run_openai(wav: bytes, pcm: bytes) -> str:
    key = need("OPENAI_API_KEY")
    data = {"model": os.getenv("OPENAI_STT_MODEL", "gpt-4o-transcribe"), "response_format": "json"}
    if os.getenv("OPENAI_STT_LANG"):
        data["language"] = os.environ["OPENAI_STT_LANG"]
    if VOCAB:
        data["prompt"] = "Telugu-English study conversation. Terms: " + ", ".join(VOCAB[:60])
    async with httpx.AsyncClient(timeout=PROVIDER_TIMEOUT) as c:
        r = await c.post(
            "https://api.openai.com/v1/audio/transcriptions",
            headers={"Authorization": f"Bearer {key}"},
            files={"file": ("utt.wav", wav, "audio/wav")},
            data=data,
        )
    if r.status_code >= 400:
        raise RuntimeError(f"HTTP {r.status_code}: {r.text[:200]}")
    return r.json().get("text", "")


async def run_gemini(wav: bytes, pcm: bytes) -> str:
    import websockets

    key = need("GEMINI_API_KEY")
    model = os.getenv("GEMINI_STT_MODEL", "gemini-3.5-transcribe-live")
    langs = [x.strip() for x in os.getenv("GEMINI_LANGS", "").split(",") if x.strip()]
    cfg: dict = {"languageCodes": langs}  # empty list = automatic language detection
    if os.getenv("GEMINI_USE_VOCAB") == "1" and VOCAB:
        cfg["customVocabulary"] = VOCAB[:60]  # field name taken from the Python SDK; unverified over raw WebSocket
    base = os.getenv("GEMINI_WS_URL") or (
        "wss://generativelanguage.googleapis.com/ws/"
        "google.ai.generativelanguage.v1beta.GenerativeService.BidiGenerateContent"
    )
    url = f"{base}?key={key}"

    def parse(raw) -> dict:
        if isinstance(raw, bytes):
            raw = raw.decode("utf-8", "replace")
        return json.loads(raw)

    seen: list[str] = []  # what Gemini actually sent, shown if no transcript arrives

    def note(msg: dict):
        sc = msg.get("serverContent") or msg.get("server_content") or {}
        tag = "+".join(sorted(msg)) + (":" + "+".join(sorted(sc)) if sc else "")
        if tag not in seen and len(seen) < 8:
            seen.append(tag)

    try:
        async with websockets.connect(url, max_size=None) as ws:
            await ws.send(json.dumps({"setup": {
                "model": f"models/{model}",
                "generationConfig": {"responseModalities": ["TEXT"]},
                "inputAudioTranscription": cfg,
            }}))
            while True:  # wait for setupComplete
                msg = parse(await asyncio.wait_for(ws.recv(), 10))
                note(msg)
                if "error" in msg:
                    raise RuntimeError("Gemini setup error: " + json.dumps(msg["error"])[:300])
                if "setupComplete" in msg or "setup_complete" in msg:
                    break

            padded = pcm + b"\x00" * 32000  # 1 s of silence so speech-end detection can fire
            step = 3200  # 100 ms of 16 kHz 16-bit mono
            for i in range(0, len(padded), step):
                await ws.send(json.dumps({"realtimeInput": {"audio": {
                    "data": base64.b64encode(padded[i:i + step]).decode(),
                    "mimeType": "audio/pcm;rate=16000",
                }}}))
            await ws.send(json.dumps({"realtimeInput": {"audioStreamEnd": True}}))

            finals: list[str] = []
            interim = ""
            deadline = time.time() + 22
            while time.time() < deadline:
                try:
                    msg = parse(await asyncio.wait_for(ws.recv(), 1.2 if finals else 6))
                except asyncio.TimeoutError:
                    break  # nothing more arriving
                note(msg)
                if "error" in msg:
                    raise RuntimeError("Gemini error: " + json.dumps(msg["error"])[:300])
                sc = msg.get("serverContent") or msg.get("server_content") or {}
                it = sc.get("inputTranscription") or sc.get("input_transcription")
                if it and it.get("text"):
                    finals.append(it["text"])
                im = sc.get("interimInputTranscription") or sc.get("interim_input_transcription")
                if im and im.get("text"):
                    interim = im["text"]
                if sc.get("turnComplete") or sc.get("turn_complete"):
                    break
            text = "".join(finals) or interim
            if not text.strip():
                raise RuntimeError("no transcript returned; messages seen: " + "; ".join(seen))
            return text
    except Exception as e:  # keep the key out of any message
        raise RuntimeError(str(e).replace(key, "***")) from None


PROVIDERS = {"sarvam": run_sarvam, "openai": run_openai, "gemini": run_gemini}
# approximate USD per audio minute, used only for the spend cap
PER_MIN = {"sarvam": 0.006, "openai": 0.006, "gemini": 0.009}


def enabled() -> list[str]:
    want = [x.strip() for x in os.environ.get("STT_PROVIDERS", "gemini,openai,sarvam").split(",") if x.strip()]
    keys = {"sarvam": "SARVAM_API_KEY", "openai": "OPENAI_API_KEY", "gemini": "GEMINI_API_KEY"}
    return [p for p in want if p in PROVIDERS and os.getenv(keys[p])]


def pcm_to_wav(pcm: bytes) -> bytes:
    buf = io.BytesIO()
    with wave.open(buf, "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(16000); w.writeframes(pcm)
    return buf.getvalue()


def wav_to_pcm(b: bytes) -> bytes:
    with wave.open(io.BytesIO(b)) as w:
        if (w.getnchannels(), w.getsampwidth(), w.getframerate()) != (1, 2, 16000):
            raise ValueError("need 16 kHz mono 16-bit WAV")
        return w.readframes(w.getnframes())


async def transcribe(pcm: bytes, providers: list[str] | None = None, providers_fns: dict | None = None):
    """Return (list of {provider,text,ms}, errors dict). Waits for the first success, then GRACE_S for the rest."""
    fns = providers_fns or PROVIDERS
    names = providers or enabled()
    if not names:
        raise NotConfigured("no speech-to-text provider key set")
    wav = pcm_to_wav(pcm)

    async def one(n):
        t0 = time.perf_counter()
        try:
            t = await asyncio.wait_for(fns[n](wav, pcm), PROVIDER_TIMEOUT)
            t = (t or "").strip()
            if not t:
                raise RuntimeError("empty transcript")
            return n, {"provider": n, "text": t, "ms": round((time.perf_counter() - t0) * 1000)}, None
        except Exception as e:
            return n, None, f"{type(e).__name__}: {str(e)[:160]}"

    tasks = [asyncio.create_task(one(n)) for n in names]
    good, errs, pending = [], {}, set(tasks)
    try:
        deadline = None
        while pending:
            timeout = None if deadline is None else max(0.0, deadline - time.perf_counter())
            done, pending = await asyncio.wait(pending, timeout=timeout, return_when=asyncio.FIRST_COMPLETED)
            if not done:
                break  # grace window over
            for d in done:
                n, ok, err = d.result()
                if ok: good.append(ok)
                else: errs[n] = err
            if good and deadline is None:
                deadline = time.perf_counter() + GRACE_S
    finally:
        for t in pending:
            t.cancel()
    return good, errs
