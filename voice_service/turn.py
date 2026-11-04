"""One voice turn: decide what the learner meant, produce events (text + sentences). No audio here, so it is testable."""
import re
from answers import parse_answer
from tutor import ask, feedback_text, question_text

QUIZ = re.compile(r"\b(quiz|question|test me|practice|next)\b|ప్రశ్న|క్విజ్|ప్రాక్టీస్|నెక్స్ట్|తరువాత|తర్వాత", re.I)


def pick_answer(transcripts, n_opts, options):
    """Combine all recognizers. Returns (kind, letter). Disagreeing letters => unclear (ask again)."""
    results = [parse_answer(t, n_opts, options) for t in transcripts]
    letters = {l for k, l in results if k == "answer"}
    if len(letters) == 1:
        return "answer", letters.pop()
    if len(letters) > 1:
        return "unclear", None
    for want in ("repeat", "skip"):
        if any(k == want for k, _ in results):
            return want, None
    return "unclear", None


def looks_like_quiz_request(transcripts):
    return any(QUIZ.search(t) and len(t.split()) <= 8 for t in transcripts)


def merged_for_llm(transcripts):
    if len(transcripts) == 1:
        return transcripts[0]
    lines = "\n".join(f"- {t}" for t in transcripts)
    return ("(Several speech recognizers heard the learner differently. Use the version that makes sense, "
            "or ask her to repeat if they conflict on something that matters.)\n" + lines)


def _script_ok(t):
    """True if the text is (almost) all Telugu or Latin letters. A recognizer that heard Hindi/Marathi/etc. is wrong for this learner."""
    letters = [ch for ch in t if ch.isalpha()]
    if not letters:
        return False
    good = sum(1 for ch in letters if "\u0c00" <= ch <= "\u0c7f" or ch.isascii())
    return good / len(letters) >= 0.8


def usable(transcripts):
    ok = [t for t in transcripts if _script_ok(t)]
    return ok or transcripts


def best_for_search(transcripts):
    """One clean transcript for notes search: prefer the one with most Telugu letters, then the longest."""
    def score(t):
        return (sum("\u0c00" <= ch <= "\u0c7f" for ch in t), len(t))
    return max(transcripts, key=score)
