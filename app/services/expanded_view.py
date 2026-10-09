"""Read-only learner view of the expanded chapter notes and the canonical chapter's native question bank.

Nothing here writes. Package section numbers are shown only as "Section n" of the expanded notes; the older app note sections
are reached only through approved explicit mappings, never by reusing a number.
"""
from ..db import db
from ..models import (Chapter, ExpandedNote, ExpandedNoteAppMap, Question, Subject, SyllabusChapter, SyllabusSubtopic,
                      LEARNER_VISIBLE_STATUS)

KIND_ORDER = {"core": 0, "group1": 1, "revision": 2, "addendum": 3, "addendum_group1": 4}


def chapter_by_slug(slug):
    return SyllabusChapter.query.filter_by(slug=slug).first()


def _paras(text):
    return [p for p in (text or "").split("\n\n") if p.strip()]


def _view(n):
    return {"row": n, "paras_en": _paras(n.body_en), "paras_te": _paras(n.body_te),
            "sources": [s for s in (n.sources or []) if s.get("url") or s.get("label")]}


def _notes(ch):
    return ExpandedNote.query.filter_by(syllabus_chapter_id=ch.id).order_by(ExpandedNote.sort_order, ExpandedNote.id).all()


def index(ch):
    rows = _notes(ch)
    groups = {k: [r for r in rows if r.kind == k] for k in KIND_ORDER}
    return {"chapter": ch, "groups": groups, "total": len(rows)}


def has_notes(ch):
    return db.session.query(ExpandedNote.id).filter_by(syllabus_chapter_id=ch.id).first() is not None


def page(ch, anchor_id):
    rows = _notes(ch)
    by_id = {r.anchor_id: r for r in rows}
    note = by_id.get(anchor_id)
    if note is None:
        return None
    core = [r for r in rows if r.kind == "core"]
    out = {"chapter": ch, "view": _view(note), "kind": note.kind, "connected_core": [], "expanded": [], "prev": None, "next": None,
           "related_old": []}
    if note.kind == "core":
        out["expanded"] = [_view(r) for r in rows if r.kind in ("addendum", "addendum_group1") and anchor_id in (r.core_connections or [])]
        i = core.index(note)
        out["prev"] = core[i - 1] if i > 0 else None
        out["next"] = core[i + 1] if i < len(core) - 1 else None
        subj_id = note.subject_id
        for m in ExpandedNoteAppMap.query.filter_by(expanded_note_id=note.id, status="approved"):
            old = Chapter.query.filter_by(subject_id=subj_id, chapter_num=m.source_chapter_num).first()
            if old:
                out["related_old"].append({"chapter_id": old.id, "section": m.app_section_num, "relation": m.relation})
    elif note.kind in ("addendum", "addendum_group1"):
        out["connected_core"] = [by_id[c] for c in (note.core_connections or []) if c in by_id]
    return out


def native_questions(ch, subtopic_slug=None):
    q = Question.query.filter(Question.syllabus_chapter_id == ch.id, Question.review_status == LEARNER_VISIBLE_STATUS)
    if subtopic_slug:
        sub = SyllabusSubtopic.query.filter_by(slug=subtopic_slug, chapter_id=ch.id).first()
        if sub is None:
            return None
        q = q.filter(Question.subtopic_id == sub.id)
    return q.order_by(Question.id).all()
