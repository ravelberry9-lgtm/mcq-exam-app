"""Pluggable tutor LLM. Set TUTOR_PROVIDER=gemini|openai and TUTOR_MODEL. Streams text deltas."""
import json
import os
import httpx


async def stream_chat(system: str, messages: list[dict], provider: str | None = None, model: str | None = None):
    provider = (provider or os.environ.get("TUTOR_PROVIDER", "gemini")).lower()
    if provider == "openai":
        key = os.environ["OPENAI_API_KEY"]
        body = {"model": model or os.environ.get("TUTOR_MODEL", "gpt-4.1-mini"), "stream": True,
                "messages": [{"role": "system", "content": system}] + messages}
        async with httpx.AsyncClient(timeout=60) as c:
            async with c.stream("POST", "https://api.openai.com/v1/chat/completions",
                                headers={"Authorization": f"Bearer {key}"}, json=body) as r:
                if r.status_code >= 400:
                    body_ = (await r.aread()).decode("utf-8", "replace")[:300]
                    raise RuntimeError(f"openai {r.status_code} {body_}")
                async for line in r.aiter_lines():
                    if line.startswith("data: ") and line[6:] != "[DONE]":
                        d = json.loads(line[6:])["choices"][0]["delta"].get("content")
                        if d:
                            yield d
    elif provider == "gemini":
        key = os.environ["GEMINI_API_KEY"]
        m = model or os.environ.get("TUTOR_MODEL", "gemini-2.5-flash")
        body = {"systemInstruction": {"parts": [{"text": system}]},
                "contents": [{"role": "user" if x["role"] == "user" else "model", "parts": [{"text": x["content"]}]} for x in messages]}
        url = f"https://generativelanguage.googleapis.com/v1beta/models/{m}:streamGenerateContent?alt=sse"
        async with httpx.AsyncClient(timeout=60) as c:
            async with c.stream("POST", url, headers={"x-goog-api-key": key}, json=body) as r:
                if r.status_code >= 400:
                    body_ = (await r.aread()).decode("utf-8", "replace")[:300]
                    raise RuntimeError(f"gemini {r.status_code} model={m} {body_}")
                async for line in r.aiter_lines():
                    if line.startswith("data: "):
                        for p in json.loads(line[6:]).get("candidates", [{}])[0].get("content", {}).get("parts", []):
                            if p.get("text"):
                                yield p["text"]
    elif provider == "mock":
        for w in (messages[-1]["content"][:60] + " ").split(" "):
            yield w + " "
    else:
        raise ValueError(f"unknown provider {provider}")
