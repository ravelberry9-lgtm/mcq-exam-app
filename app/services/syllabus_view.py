"""Read-only learner view of the canonical AP History structure (units -> chapters -> subtopics).

Nothing here writes. Question counts come from the content team's own note_target_slug prefix ("u1-c02-..." = canonical
chapter 2), so the 1,3xx imported questions are reachable by canonical chapter without any schema change or backfill.
Practice and notes open the legacy chapter that actually holds those questions, so every number shown is reachable.
"""
from collections import defaultdict

from sqlalchemy import func

from ..db import db
from ..models import LEARNER_VISIBLE_STATUS, Question, Subject, SyllabusChapter, SyllabusSubtopic, SyllabusUnit

SUBJECT_SLUG = "ap_history"


def _prefix(slug):
    return slug[:7] if slug and len(slug) >= 7 else None   # "u1-c02-"


def _subject():
    return Subject.query.filter_by(slug=SUBJECT_SLUG).first()


def is_loaded():
    sub = _subject()
    return bool(sub and SyllabusChapter.query.filter_by(subject_id=sub.id).first())


def _question_index(subject_id):
    """{ 'u1-c02': {'count': n, 'legacy': {chapter_id: n}} } from imported questions."""
    rows = (db.session.query(Question.note_target_slug, Question.chapter_id, func.count(Question.id))
            .filter(Question.subject_id == subject_id, Question.note_target_slug.isnot(None))
            .group_by(Question.note_target_slug, Question.chapter_id).all())
    idx = defaultdict(lambda: {"count": 0, "legacy": defaultdict(int)})
    for slug, cid, n in rows:
        p = _prefix(slug)
        if not p:
            continue
        idx[p[:6]]["count"] += n
        if cid:
            idx[p[:6]]["legacy"][cid] += n
    return idx


def _entry(ch, idx):
    key = ch.slug[:6]
    q = idx.get(key, {"count": 0, "legacy": {}})
    legacy = max(q["legacy"], key=q["legacy"].get) if q["legacy"] else None
    return {"chapter": ch, "question_count": q["count"], "legacy_chapter_id": legacy}


def outline():
    """None when the canonical structure has not been seeded yet."""
    sub = _subject()
    if not sub or not SyllabusChapter.query.filter_by(subject_id=sub.id).first():
        return None
    idx = _question_index(sub.id)
    units = []
    for u in SyllabusUnit.query.filter_by(subject_id=sub.id).order_by(SyllabusUnit.unit_num).all():
        chs = (SyllabusChapter.query.filter_by(subject_id=sub.id, unit_id=u.id).order_by(SyllabusChapter.chapter_num).all())
        units.append({"unit": u, "chapters": [_entry(c, idx) for c in chs]})
    supp = (SyllabusChapter.query.filter_by(subject_id=sub.id, classification="supplementary")
            .order_by(SyllabusChapter.sort_order, SyllabusChapter.id).all())
    return {"subject": sub, "units": units, "supplementary": [_entry(c, {}) for c in supp],
            "core_count": sum(len(u["chapters"]) for u in units)}


def chapter_detail(slug):
    sub = _subject()
    if not sub:
        return None
    ch = SyllabusChapter.query.filter_by(subject_id=sub.id, slug=slug).first()
    if not ch:
        return None
    subs = SyllabusSubtopic.query.filter_by(chapter_id=ch.id).order_by(SyllabusSubtopic.sort_order, SyllabusSubtopic.id).all()
    entry = _entry(ch, _question_index(sub.id) if ch.is_core else {})
    unit = db.session.get(SyllabusUnit, ch.unit_id) if ch.unit_id else None
    from . import expanded_view as xv
    native = Question.query.filter(Question.syllabus_chapter_id == ch.id, Question.review_status == LEARNER_VISIBLE_STATUS).count()
    return {"subject": sub, "chapter": ch, "unit": unit, "subtopics": subs, **entry,
            "has_expanded": xv.has_notes(ch), "native_count": native}
