"""Text-to-speech. Returns mp3 bytes. Provider is pluggable via TTS_PROVIDER (openai for now)."""
import os
import re
import httpx

MAX_CHARS = 600


def clean_for_speech(t: str) -> str:
    t = re.sub(r"\[RR:[^\]]*\]|<[^>]+>|[*_#`]", " ", t or "")
    return re.sub(r"\s+", " ", t).strip()[:MAX_CHARS]


async def synth_openai(text: str) -> bytes:
    key = os.environ["OPENAI_API_KEY"]
    body = {"model": os.environ.get("TTS_MODEL", "gpt-4o-mini-tts"), "voice": os.environ.get("TTS_VOICE", "nova"),
            "input": text, "response_format": "mp3",
            "instructions": "Warm, calm, clear teacher. Natural Telugu and English; pace slightly slow for study."}
    async with httpx.AsyncClient(timeout=30) as c:
        r = await c.post("https://api.openai.com/v1/audio/speech", headers={"Authorization": f"Bearer {key}"}, json=body)
    if r.status_code >= 400:
        raise RuntimeError(f"tts HTTP {r.status_code}")
    return r.content


PROVIDERS = {"openai": synth_openai}
# rough USD per 1,000 characters, for the spend cap only
COST_PER_1K_CHARS = {"openai": 0.015}


async def synth(text: str, provider: str | None = None) -> tuple[bytes, float]:
    p = provider or os.environ.get("TTS_PROVIDER", "openai")
    t = clean_for_speech(text)
    if not t:
        return b"", 0.0
    return await PROVIDERS[p](t), COST_PER_1K_CHARS[p] * len(t) / 1000
