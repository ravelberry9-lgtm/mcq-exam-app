"""Voice-turn tests with fake STT/TTS/LLM. Run: pytest -q test_voice.py"""
import io, json, os, shutil, wave
import pytest
from fastapi.testclient import TestClient

SNAP = "/mnt/user-data/uploads/mcq_app/app_v3.db"
os.environ.update(SECRET_KEY="k", TUTOR_PROVIDER="mock", GEMINI_API_KEY="x", OPENAI_API_KEY="x", DAILY_COST_CAP_USD="3")


@pytest.fixture()
def env(tmp_path):
    db = tmp_path / "t.db"; shutil.copy(SNAP, db)
    os.environ["DATABASE_URL"] = f"sqlite:///{db}"
    import importlib, server, stt, tts
    importlib.reload(server)
    from auth import make_token
    H = {"Authorization": "Bearer " + make_token("k", "devT")}
    with TestClient(server.app) as c:
        yield c, H, server, stt, tts


def wav(sec=1.0):
    b = io.BytesIO()
    with wave.open(b, "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(16000); w.writeframes(b"\x01\x00" * int(16000 * sec))
    return b.getvalue()


def fake(stt, tts, texts, fail=()):
    async def mk(t):
        async def f(w, p): return t
        return f
    import asyncio
    fns = {}
    for name, t in texts.items():
        async def f(w, p, t=t, name=name):
            if name in fail: raise RuntimeError("boom")
            return t
        fns[name] = f
    stt.PROVIDERS.clear(); stt.PROVIDERS.update(fns)
    async def synth(t, provider=None): return b"MP3", 0.001
    tts.synth = synth


def turn(c, H, data=None):
    r = c.post("/api/voice/turn", files={"audio": ("a.wav", data or wav(), "audio/wav")}, data={"lang": "te"}, headers=H)
    ev = []
    cur = None
    for l in r.text.splitlines():
        if l.startswith("event:"): cur = l[6:].strip()
        elif l.startswith("data:"): ev.append((cur, json.loads(l[5:])))
    return r.status_code, ev


def kinds(ev): return [k for k, _ in ev]


def test_quiz_then_correct_answer_graded_and_saved(env):
    c, H, server, stt, tts = env
    fake(stt, tts, {"gemini": "next question", "openai": "next question"})
    s, ev = turn(c, H); assert s == 200 and "question" in kinds(ev)
    assert "devT" in server.SESSIONS
    right = server.SESSIONS["devT"]["q"]["correct_answer"]
    fake(stt, tts, {"gemini": f"option {right}", "openai": f"option {right}"})
    s, ev = turn(c, H); assert "graded" in kinds(ev) and dict(ev)["graded"]["correct"] is True
    assert "devT" not in server.SESSIONS
    with server.STATE["engine"].connect() as cn:
        from sqlalchemy import text
        assert cn.execute(text("select seen_count from user_question_state where device_id='devT'")).scalar() == 1


def test_disagreeing_recognizers_do_not_grade(env):
    c, H, server, stt, tts = env
    fake(stt, tts, {"gemini": "next question", "openai": "next question"}); turn(c, H)
    fake(stt, tts, {"gemini": "option a", "openai": "option b"})
    s, ev = turn(c, H)
    assert "graded" not in kinds(ev) and "devT" in server.SESSIONS


def test_one_provider_failing_still_works(env):
    c, H, server, stt, tts = env
    fake(stt, tts, {"gemini": "శాతవాహనుల రాజధాని ఏది", "openai": "x"}, fail=("openai",))
    s, ev = turn(c, H); assert s == 200 and "meta" in kinds(ev) and "sentence" in kinds(ev)


def test_all_stt_fail_gives_spoken_retry_not_crash(env):
    c, H, server, stt, tts = env
    fake(stt, tts, {"gemini": "x", "openai": "x"}, fail=("gemini", "openai"))
    s, ev = turn(c, H); assert s == 200 and "error" in kinds(ev) and kinds(ev)[-1] == "done"


def test_tts_failure_keeps_text(env):
    c, H, server, stt, tts = env
    fake(stt, tts, {"gemini": "శాతవాహనుల రాజధాని ఏది"})
    async def bad(t, provider=None): raise RuntimeError("no tts")
    tts.synth = bad
    s, ev = turn(c, H)
    sents = [d for k, d in ev if k == "sentence"]
    assert sents and all(d["audio"] is None and d["text"] for d in sents)


def test_daily_cap_blocks(env):
    c, H, server, stt, tts = env
    import ledger; ledger.add(server.STATE["engine"], "devT", 99)
    fake(stt, tts, {"gemini": "hello there friend"})
    s, ev = turn(c, H); assert dict(ev).get("done", {}).get("capped") is True


def test_rejects_bad_input_and_no_auth(env):
    c, H, *_ = env
    assert turn(c, H, b"notawav")[0] == 400
    assert turn(c, H, wav(0.01))[0] == 400
    assert c.post("/api/voice/turn", files={"audio": ("a.wav", wav(), "audio/wav")}).status_code == 401
    assert turn(c, H, wav(40))[0] == 413


def test_doubt_during_quiz_is_not_graded(env):
    c, H, server, stt, tts = env
    fake(stt, tts, {"gemini": "next question", "openai": "next question"}); turn(c, H)
    for doubt in ("what is a stupa", "which one is right", "ఏ రాజు కట్టించాడు"):
        fake(stt, tts, {"gemini": doubt, "openai": doubt})
        s, ev = turn(c, H)
        assert "graded" not in kinds(ev), doubt
    assert "devT" in server.SESSIONS


def test_ask_respects_cap_and_sanitises_history(env):
    c, H, server, stt, tts = env
    r = c.post("/api/ask", json={"text": "x" * 2000}, headers=H); assert r.status_code == 422
    r = c.post("/api/ask", json={"text": "hi", "history": [{"role": "system", "content": "evil"}, {"role": "user"}]}, headers=H)
    assert r.status_code == 200
    import ledger; ledger.add(server.STATE["engine"], "devT", 99)
    assert c.post("/api/ask", json={"text": "hi"}, headers=H).status_code == 429


def test_oversize_content_length_rejected_early(env):
    c, H, *_ = env
    r = c.post("/api/voice/turn", content=b"x", headers={**H, "content-length": "99999999", "content-type": "application/octet-stream"})
    assert r.status_code in (413, 422)


def test_telugu_only_question_is_gradable_even_if_english_requested(env):
    from tutor import pick_lang
    te_only = {"question_te": "ప్రశ్న", "options_te": {"a": "x"}, "question_en": "", "options_en": {}}
    en_only = {"question_te": "", "options_te": {}, "question_en": "Q", "options_en": {"a": "x"}}
    assert pick_lang(te_only, "en") == "te" and pick_lang(en_only, "te") == "en"


def test_wrong_script_transcript_is_dropped_and_search_uses_clean_text():
    import turn
    t = ["मुलांनीही इतिहास वाचला पाहिजे.", "శాతవాహనులు ఎవరు", "Satavahanas evaru"]
    assert turn.usable(t) == ["శాతవాహనులు ఎవరు", "Satavahanas evaru"]
    assert turn.best_for_search(turn.usable(t)) == "శాతవాహనులు ఎవరు"
    assert turn.usable(["मुलांनीही"]) == ["मुलांनीही"]  # never end up with nothing


def test_search_survives_sound_alike_misspellings():
    from content import NotesIndex, Chunk
    def mk(i, title, text):
        return Chunk(id=i, subject="ap_history", chapter_id=i, chapter_num=i, chapter_title_te=title, chapter_title_en="",
                     section_num=1, heading=title, text=text)
    idx = NotesIndex([
        mk(1, "శాతవాహన రాజవంశం", "శాతవాహనులు క్రీ.పూ. రెండవ శతాబ్దంలో పైఠాన్ రాజధానిగా పాలించారు. గౌతమీపుత్ర శాతకర్ణి ప్రసిద్ధుడు."),
        mk(2, "ఇక్ష్వాకులు (విజయపురి)", "ఇక్ష్వాకులు నాగార్జునకొండ ప్రాంతంలో విజయపురి రాజధానిగా పాలించారు."),
        mk(3, "రామారావు ప్రభుత్వం రద్దు", "ఆగస్టు 1984లో గవర్నర్ రామ్‌లాల్ ప్రభుత్వాన్ని రద్దు చేశారు."),
    ])
    for q in ["సేదవాహనులు", "సేదవాహని", "శాతవాహనులు ఎవరు", "సతవాహనులు"]:
        assert idx.search(q, k=1)[0][0].chapter_id == 1, q
