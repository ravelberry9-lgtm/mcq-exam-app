"""Tutor brain: grounded answers from notes, source labels, MCQ flow. Grading stays in code."""
import re
from llm import stream_chat

SYSTEM = """You are a warm, patient spoken tutor for an APPSC Group 1/2 aspirant. Reply the way a teacher talks: short, natural, no markdown, no lists, no symbols.
Match the learner's language: Telugu, English, or mixed Telugu with English terms.
Rules:
1. Answer FIRST from the NOTES block. If the notes cover it, say it is from her notes.
2. If the notes do not cover it, say so plainly ('నోట్స్‌లో ఇది లేదు' / 'not in your notes') and answer from general knowledge, saying it is general knowledge. Never present general knowledge as her notes.
3. If unsure of a fact, say you are unsure. Never invent dates, names or numbers.
4. The learner is speaking, and speech recognition makes mistakes. If her words look garbled or you are not sure what she asked, do NOT guess: say you did not catch it and ask her to say it again (a topic name is enough).
5. Keep answers under about 80 words unless she asks for detail. Ask at most one question at the end."""

MIN_SENT = 15
ABBREV_END = re.compile(r"(క్రీ\.\s?శ|క్రీ\.\s?పూ|క్రీ|\bca|\bc|\bBC|\bAD|\bDr|\bSt|\bNo)\.$")
SENT_END = re.compile(r"(?<=[.!?।])\s+")


def build_prompt(question: str, hits):
    if hits:
        notes = "\n\n".join(f"[{c.chapter_title_te or c.chapter_title_en} · {c.heading}]\n{c.text}" for c, _ in hits)
    else:
        notes = "(no matching notes found)"
    return f"NOTES:\n{notes}\n\nLEARNER: {question}"


def source_label(hits, min_score=15.0):
    """Honest label for the UI/voice: notes only if the best hit is strong enough."""
    if hits and hits[0][1] >= min_score:
        c = hits[0][0]
        return {"source": "notes", "chapter": c.chapter_title_te or c.chapter_title_en, "section": c.heading}
    return {"source": "general", "chapter": None, "section": None}


async def ask(index, question, history=None, subject="ap_history", llm=stream_chat, search_text=None):
    """Yield ('meta', label) then ('sentence', text) items, sentence-by-sentence so TTS can start early."""
    hits = index.search(search_text or question, k=3, subject=subject)
    label = source_label(hits)
    yield "meta", label
    use = hits if label["source"] == "notes" else []
    msgs = (history or [])[-6:] + [{"role": "user", "content": build_prompt(question, use)}]
    buf = ""
    async for d in llm(SYSTEM, msgs):
        buf += d
        parts = SENT_END.split(buf)
        pend = ""
        for s in parts[:-1]:
            pend = (pend + " " + s).strip()
            if len(pend) >= MIN_SENT and not ABBREV_END.search(pend):
                yield "sentence", pend
                pend = ""
        buf = (pend + " " + parts[-1]) if pend else parts[-1]
    if buf.strip():
        yield "sentence", buf.strip()


def feedback_text(q, letter, lang="te"):
    ok = letter == q["correct_answer"]
    opts = q["options_te"] if lang == "te" and q["options_te"] else q["options_en"]
    ans = opts.get(q["correct_answer"], "")
    expl = (q.get("explanation_te") if lang == "te" else q.get("explanation_en")) or q.get("explanation_en") or q.get("explanation_te") or ""
    expl = re.sub(r"\{\s*\"source_label\".*?\}", " ", expl, flags=re.S)  # internal metadata blobs
    expl = re.sub(r"<[^>]+>|\[RR:[^\]]*\]", " ", expl)
    expl = re.sub(r"\s+", " ", expl).strip()[:400]
    if lang == "te":
        head = "సరైన సమాధానం!" if ok else f"కాదు. సరైన సమాధానం {q['correct_answer'].upper()}: {ans}."
    else:
        head = "Correct!" if ok else f"Not quite. The answer is {q['correct_answer'].upper()}: {ans}."
    return ok, (head + " " + expl).strip()


def question_text(q, lang="te"):
    t = q["question_te"] if lang == "te" and q["question_te"] else q["question_en"]
    o = q["options_te"] if lang == "te" and q["options_te"] else q["options_en"]
    return t + " " + " ".join(f"{k.upper()}) {v}." for k, v in o.items())


def pick_lang(q, want="te"):
    """Language the question can actually be asked in. Many questions are Telugu-only (or English-only)."""
    has_te = bool(q.get("question_te")) and bool(q.get("options_te"))
    has_en = bool(q.get("question_en")) and bool(q.get("options_en"))
    if want == "en" and has_en: return "en"
    if want == "te" and has_te: return "te"
    return "te" if has_te else "en"
