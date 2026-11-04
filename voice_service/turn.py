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
