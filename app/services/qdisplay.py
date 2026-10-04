"""Display helpers for questions in the older (non-``ds``) templates: practice, exam, results.

The data has questions with only one language (e.g. all 3,402 chapter questions have Telugu options and no English
ones). These helpers never invent text; they only decide which stored language to show and how, so a question or option
is never blank because the *other* language is empty.

``bi_kind(en, te)`` returns:
  ``both``  both languages present and different: render both, the page language preference hides one;
  ``same``  identical text: render once;
  ``en`` / ``te``  only that language exists: render it once, always visible (the fallback);
  ``none``  nothing stored.
"""
from .learn import strip_option_prefix

KEYS = "abcde"


def _s(v):
    return v.strip() if isinstance(v, str) else ""


def bi_kind(en, te):
    en, te = _s(en), _s(te)
    if en and te:
        return "same" if en == te else "both"
    return "en" if en else ("te" if te else "none")


def option_items(question):
    """Options a..e that have text in at least one language, with the imported 'a) ' prefix removed."""
    en = question.options_en or {}
    te = question.options_te or {}
    out = []
    for k in KEYS:
        e, t = strip_option_prefix(_s(en.get(k))), strip_option_prefix(_s(te.get(k)))
        if e or t:
            out.append({"key": k, "en": e, "te": t, "kind": bi_kind(e, t)})
    return out


def option_item(question, key):
    for o in option_items(question):
        if o["key"] == (key or "").lower():
            return o
    return None


def is_answerable(question):
    """A question can be asked only if its correct answer is one of the options that exist."""
    return any(o["key"] == (question.correct_answer or "").lower() for o in option_items(question))
