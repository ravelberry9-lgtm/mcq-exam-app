"""Safe import of a *prepared* MCQ package (one JSONL per chapter, produced under content/.../05_claude_import).

Rules (same spirit as content_import.py):

* Preview is the default; ``apply=True`` is required to write.
* Add-only. Existing questions (legacy or earlier imports) are never modified or deleted.
* Everything is validated first; one invalid record in a package refuses nothing silently: it is *skipped and reported*.
* Idempotent: a record whose ``import_ref`` is already in the database is reported as ``already_imported`` and skipped.
* Duplicates (exact stem, same stem+answer, or near-identical stem with the same correct option) against the subject's
  existing questions, and inside the package, are skipped and reported with their source ids.
* The subject and chapter are resolved by slug / chapter number and the chapter title is asserted, so a package prepared
  against another database (different ids) can never land in the wrong chapter.
* Writes happen in one transaction.
"""
import hashlib
import json
import re
from pathlib import Path

from ..db import db
from ..models import Chapter, Note, Question, Subject

REQUIRED_TEXT = ("question_en", "question_te", "explanation_en", "explanation_te")
OPT_KEYS = ("a", "b", "c", "d")
_TELUGU = re.compile(r"[ఀ-౿]")
_WS = re.compile(r"\s+")
_PUNCT = re.compile(r"[^\wఀ-౿ ]+", re.U)


class McqImportError(Exception):
    pass


def load_prepared(path):
    recs = []
    with open(path, encoding="utf-8") as f:
        for n, line in enumerate(f, 1):
            if line.strip():
                try:
                    recs.append(json.loads(line))
                except ValueError as e:
                    raise McqImportError(f"{path}: line {n} is not valid JSON ({e})")
    return recs


def norm(s):
    return _WS.sub(" ", _PUNCT.sub(" ", (s or "").lower())).strip()


def _tokens(s):
    return set(norm(s).split())


def _answer_text(rec_or_q, lang="en"):
    opts = rec_or_q["options_" + lang] if isinstance(rec_or_q, dict) else getattr(rec_or_q, "options_" + lang)
    ans = rec_or_q["correct_answer"] if isinstance(rec_or_q, dict) else rec_or_q.correct_answer
    return norm((opts or {}).get(ans))


def q_hash(rec):
    return hashlib.md5(norm(rec["question_en"]).encode("utf-8")).hexdigest()


def validate(rec):
    """Return a list of problems (empty list = valid)."""
    errs = []
    for k in REQUIRED_TEXT:
        if not (rec.get(k) or "").strip():
            errs.append(f"missing {k}")
    for lang in ("en", "te"):
        opts = rec.get("options_" + lang)
        if not isinstance(opts, dict) or sorted(opts) != list(OPT_KEYS):
            errs.append(f"options_{lang} must have exactly keys a-d")
            continue
        for k in OPT_KEYS:
            if not (opts[k] or "").strip():
                errs.append(f"options_{lang}.{k} empty")
    if rec.get("correct_answer") not in OPT_KEYS:
        errs.append("correct_answer must be lowercase a-d")
    if rec.get("difficulty") not in ("E", "M", "H"):
        errs.append("difficulty must be E/M/H")
    # a Telugu text in an English field (or the reverse) is the known "needs repair" defect
    for k in ("question_en", "explanation_en"):
        if _TELUGU.search(rec.get(k) or ""):
            errs.append(f"{k} contains Telugu text")
    if isinstance(rec.get("options_en"), dict):
        for k, v in rec["options_en"].items():
            if _TELUGU.search(v or ""):
                errs.append(f"options_en.{k} contains Telugu text")
    for k in ("question_te",):
        if rec.get(k) and not _TELUGU.search(rec[k]):
            errs.append(f"{k} has no Telugu text")
    if isinstance(rec.get("options_te"), dict):
        for k, v in rec["options_te"].items():
            same_as_en = (rec.get("options_en") or {}).get(k, "").strip() == (v or "").strip()  # proper noun / code
            if v and not same_as_en and not _TELUGU.search(v) and not re.search(r"\d", v) and len(v) > 3:
                errs.append(f"options_te.{k} has no Telugu text")
    if not rec.get("import_ref"):
        errs.append("missing import_ref")
    if not isinstance(rec.get("source_trace"), dict) or not rec["source_trace"].get("combined_id"):
        errs.append("missing source_trace")
    return errs


def _resolve_target(rec):
    subj = Subject.query.filter_by(slug=rec["subject_slug"]).first()
    if not subj:
        raise McqImportError(f"subject '{rec['subject_slug']}' not found")
    ch = Chapter.query.filter_by(subject_id=subj.id, chapter_num=rec["chapter_num"]).first()
    if not ch:
        raise McqImportError(f"chapter {rec['chapter_num']} of '{subj.slug}' not found")
    want = norm(rec["chapter_title_en"])
    if norm(ch.title_en) != want:
        raise McqImportError(f"chapter {rec['chapter_num']} is titled '{ch.title_en}', package expects '{rec['chapter_title_en']}'")
    return subj, ch


def _similar(a_tokens, b_tokens):
    if not a_tokens or not b_tokens:
        return 0.0
    return len(a_tokens & b_tokens) / len(a_tokens | b_tokens)


def _existing_index(subject_id):
    rows = Question.query.filter_by(subject_id=subject_id).all()
    idx = []
    for q in rows:
        idx.append({"id": q.id, "ref": q.import_ref, "stem": norm(q.question_en), "tok": _tokens(q.question_en),
                    "ans": _answer_text(q, "en"), "ans_te": _answer_text(q, "te"), "stem_te": norm(q.question_te)})
    return idx


def _dup_of(rec, index):
    stem, tok, ans = norm(rec["question_en"]), _tokens(rec["question_en"]), _answer_text(rec, "en")
    stem_te, ans_te = norm(rec["question_te"]), _answer_text(rec, "te")
    for e in index:
        if stem and stem == e["stem"]:
            return e, "same English stem"
        if stem_te and e["stem_te"] and stem_te == e["stem_te"]:
            return e, "same Telugu stem"
        if ans and ans == e["ans"] and _similar(tok, e["tok"]) >= 0.8:
            return e, "near-identical stem with the same correct answer"
    return None, None


def run(path, apply=False):
    """Preview (default) or apply one prepared chapter file. Returns a report dict."""
    recs = load_prepared(path)
    rep = {"file": Path(path).name, "records": len(recs), "to_import": 0, "imported": 0, "already_imported": 0,
           "invalid": [], "duplicates": [], "note_exact": 0, "note_chapter_fallback": 0, "applied": bool(apply)}
    if not recs:
        return rep
    targets = {(r["subject_slug"], r["chapter_num"]) for r in recs}
    if len(targets) != 1:
        raise McqImportError("a prepared file must target exactly one chapter")
    subj, ch = _resolve_target(recs[0])
    for r in recs:
        if r.get("subject_id") not in (None, subj.id) or r.get("chapter_id") not in (None, ch.id):
            # ids in the package were resolved against one database; refuse rather than trust them elsewhere
            raise McqImportError(f"package ids (subject {r.get('subject_id')}, chapter {r.get('chapter_id')}) do not match "
                                 f"this database (subject {subj.id}, chapter {ch.id})")
    sections = {n for (n,) in db.session.query(Note.section_num).filter(Note.chapter_id == ch.id)}
    index = _existing_index(subj.id)
    have_refs = {e["ref"] for e in index if e["ref"]}
    new_rows = []
    for r in recs:
        ref = r.get("import_ref")
        if ref in have_refs:
            rep["already_imported"] += 1
            continue
        errs = validate(r)
        if errs:
            rep["invalid"].append({"import_ref": ref, "source": (r.get("source_trace") or {}).get("combined_id"), "problems": errs})
            continue
        dup, why = _dup_of(r, index)
        if dup:
            rep["duplicates"].append({"import_ref": ref, "source": r["source_trace"]["combined_id"],
                                      "duplicate_of_question_id": dup["id"], "duplicate_of_ref": dup["ref"], "reason": why})
            continue
        num = r.get("note_section_num")
        exact = num is not None and num in sections
        rep["note_exact" if exact else "note_chapter_fallback"] += 1
        row = Question(
            subject_id=subj.id, chapter_id=ch.id, source_type="chapter", q_hash=q_hash(r), difficulty=r["difficulty"],
            question_en=r["question_en"].strip(), question_te=r["question_te"].strip(),
            options_en={k: r["options_en"][k] for k in OPT_KEYS}, options_te={k: r["options_te"][k] for k in OPT_KEYS},
            correct_answer=r["correct_answer"], explanation_en=r["explanation_en"].strip(),
            explanation_te=r["explanation_te"].strip(), note_section_num=num if exact else None,
            note_target_slug=r.get("note_target_slug"), source_trace=r["source_trace"], import_ref=ref)
        new_rows.append(row)
        # later records in the same package are also checked against this one
        index.append({"id": None, "ref": ref, "stem": norm(r["question_en"]), "tok": _tokens(r["question_en"]),
                      "ans": _answer_text(r, "en"), "ans_te": _answer_text(r, "te"), "stem_te": norm(r["question_te"])})
    rep["to_import"] = len(new_rows)
    if apply and new_rows:
        try:
            db.session.add_all(new_rows)
            db.session.commit()
        except Exception:
            db.session.rollback()
            raise
        rep["imported"] = len(new_rows)
    return rep
