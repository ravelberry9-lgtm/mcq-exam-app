"""Data access for the design-system journey: Learn -> Section -> Topic -> Notes -> Practice.

Terminology: the prototype's "topic" is a ``Chapter`` row; a "section" is an ``ExamSection``
(a block of an exam paper such as "Indian History, 30 marks") that groups subjects.
Nothing here writes to the database except the small progress helpers at the bottom.
"""
import re
from datetime import datetime

import bleach
from sqlalchemy import func

from ..db import db
from ..models import (
    Chapter, ChapterProgress, Exam, ExamPaper, ExamSection, ExamSyllabusItem,
    Note, Question, Subject,
)

# ── safe HTML for notes ─────────────────────────────────────────────
# Migrated notes contain script/style/onclick (134 rows at audit time), so every note body is
# sanitised again at render time, whatever the admin editor did when it was saved.
NOTE_TAGS = [
    "p", "br", "hr", "h1", "h2", "h3", "h4", "h5", "h6", "ul", "ol", "li",
    "strong", "b", "em", "i", "u", "s", "span", "div",
    "table", "thead", "tbody", "tr", "th", "td", "blockquote", "pre", "code",
    "a", "img", "sup", "sub",
]


def clean_note_html(html, keep_class=False):
    """Sanitise note HTML for display. ``style``/``id`` are always dropped; ``class`` only when
    the subject ships its own note stylesheet (AP history), so imported classes cannot clash
    with the app's own CSS."""
    star = ["class"] if keep_class else []
    attrs = {
        "*": star,
        "a": ["href", "title"],
        "img": ["src", "alt", "width", "height"],
        "td": ["colspan", "rowspan"],
        "th": ["colspan", "rowspan"],
    }
    out = bleach.clean(html or "", tags=NOTE_TAGS, attributes=attrs, protocols=["http", "https", "mailto"], strip=True)
    # drop the *content* of script/style blocks that bleach(strip=True) leaves as bare text
    return out


def strip_blocks(html):
    """Remove <script>/<style> elements together with their text before bleach runs."""
    return re.sub(r"<(script|style)\b[^>]*>.*?</\1\s*>", "", html or "", flags=re.I | re.S)


def render_note_html(html, keep_class=False):
    return clean_note_html(strip_blocks(html), keep_class)


# ── display helpers (no data is modified) ───────────────────────────
_RECOVERED = re.compile(r"recovered|^\s*chapter\s*\(", re.I)
_OPT_PREFIX = re.compile(r"^\s*\(?[a-eA-E][\)\.]\s*")


def display_title(chapter):
    """Chapter titles migrated from placeholders read 'Chapter (recovered, sn_id=14)'. Show a
    neutral 'Chapter N' instead; the admin can rename the row."""
    if _RECOVERED.search(chapter.title_en or ""):
        return f"Chapter {chapter.chapter_num}", f"అధ్యాయం {chapter.chapter_num}"
    return chapter.title_en, chapter.title_te


def strip_option_prefix(text):
    """Imported options start with their own letter ('a) ...'); the UI draws the letter badge."""
    return _OPT_PREFIX.sub("", text or "", count=1).strip()


# ── hub / section ───────────────────────────────────────────────────
def get_exam():
    return (Exam.query.filter_by(slug="appsc_group_2", active=True).first()
            or Exam.query.filter_by(active=True).order_by(Exam.id).first())


def _counts_by_subject():
    ch = dict(db.session.query(Chapter.subject_id, func.count(Chapter.id)).group_by(Chapter.subject_id).all())
    q = dict(db.session.query(Question.subject_id, func.count(Question.id)).group_by(Question.subject_id).all())
    return ch, q


def hub(exam=None):
    """Return {'exam': Exam|None, 'papers': [...]} or a flat subject list when no exam is seeded."""
    ch_by_subj, q_by_subj = _counts_by_subject()
    exam = exam or get_exam()
    if exam is None:
        subjects = Subject.query.order_by(Subject.sort_order, Subject.id).all()
        flat = [{
            "subject": s, "chapter_count": ch_by_subj.get(s.id, 0), "question_count": q_by_subj.get(s.id, 0),
            "href_kind": "subject", "available": ch_by_subj.get(s.id, 0) > 0,
        } for s in subjects]
        return {"exam": None, "papers": [], "flat": flat}

    papers = []
    for paper in ExamPaper.query.filter_by(exam_id=exam.id).order_by(ExamPaper.paper_num).all():
        sections = []
        for sec in ExamSection.query.filter_by(paper_id=paper.id).order_by(ExamSection.sort_order).all():
            subject_ids = _section_subject_ids(sec.id)
            cc = sum(ch_by_subj.get(i, 0) for i in subject_ids)
            qc = sum(q_by_subj.get(i, 0) for i in subject_ids)
            sections.append({"section": sec, "chapter_count": cc, "question_count": qc, "available": cc > 0})
        # Mains rules (duration, negative marking, question format) are NOT published here: the seeded
        # values are unverified. They stay hidden until a paper is explicitly marked verified.
        papers.append({"paper": paper, "sections": sections, "is_prelims": paper.paper_num == 0})
    return {"exam": exam, "papers": papers, "flat": []}


def _section_subject_ids(section_id):
    rows = (db.session.query(Chapter.subject_id)
            .join(ExamSyllabusItem, ExamSyllabusItem.chapter_id == Chapter.id)
            .filter(ExamSyllabusItem.section_id == section_id)
            .distinct().all())
    return [r[0] for r in rows]


def topics_for_section(section):
    """Chapters of a section, grouped by subject, in syllabus order."""
    items = (db.session.query(Chapter)
             .join(ExamSyllabusItem, ExamSyllabusItem.chapter_id == Chapter.id)
             .filter(ExamSyllabusItem.section_id == section.id)
             .order_by(ExamSyllabusItem.sort_order, Chapter.chapter_num).all())
    return group_chapters(items)


def topics_for_subject(subject):
    items = Chapter.query.filter_by(subject_id=subject.id).order_by(Chapter.chapter_num).all()
    return group_chapters(items)


def group_chapters(chapters, device_id=None):
    if not chapters:
        return []
    ids = [c.id for c in chapters]
    note_n = dict(db.session.query(Note.chapter_id, func.count(Note.id)).filter(Note.chapter_id.in_(ids)).group_by(Note.chapter_id).all())
    q_n = dict(db.session.query(Question.chapter_id, func.count(Question.id)).filter(Question.chapter_id.in_(ids)).group_by(Question.chapter_id).all())
    subj = {s.id: s for s in Subject.query.filter(Subject.id.in_({c.subject_id for c in chapters})).all()}
    groups, order = {}, []
    for c in chapters:
        if c.subject_id not in groups:
            groups[c.subject_id] = {"subject": subj.get(c.subject_id), "topics": []}
            order.append(c.subject_id)
        en, te = display_title(c)
        groups[c.subject_id]["topics"].append({
            "chapter": c, "title_en": en, "title_te": te,
            "note_count": note_n.get(c.id, 0), "question_count": q_n.get(c.id, 0),
        })
    return [groups[i] for i in order]


def attach_status(groups, device_id):
    ids = [t["chapter"].id for g in groups for t in g["topics"]]
    rows = ChapterProgress.query.filter(ChapterProgress.device_id == device_id, ChapterProgress.chapter_id.in_(ids)).all() if ids else []
    st = {r.chapter_id: r.status for r in rows}
    for g in groups:
        for t in g["topics"]:
            t["status"] = st.get(t["chapter"].id, "not_started")
    return groups


# ── topic / notes / practice ────────────────────────────────────────
def topic_context(chapter):
    subject = db.session.get(Subject, chapter.subject_id)
    en, te = display_title(chapter)
    notes = Note.query.filter_by(chapter_id=chapter.id).order_by(Note.section_num).all()
    mcq = Question.query.filter_by(chapter_id=chapter.id, source_type="chapter").count()
    return {"chapter": chapter, "subject": subject, "title_en": en, "title_te": te, "note_count": len(notes), "mcq_count": mcq}


def chapter_questions(chapter_id):
    # chapter practice shows chapter questions only; PYQs belong to the PYQ stage and are never presented as chapter questions
    return Question.query.filter_by(chapter_id=chapter_id, source_type="chapter").order_by(Question.id).all()


def question_view(q):
    """Everything the template needs for one question, with display-only clean-up applied."""
    keys = sorted({k for k in list((q.options_en or {}).keys()) + list((q.options_te or {}).keys())
                   if (q.options_en or {}).get(k) or (q.options_te or {}).get(k)})
    options = [{
        "key": k,
        "en": strip_option_prefix((q.options_en or {}).get(k)),
        "te": strip_option_prefix((q.options_te or {}).get(k)),
    } for k in keys]
    return {
        "id": q.id, "difficulty": q.difficulty, "options": options,
        # provenance comes from the row itself; an exam name is not stored, so PYQs are never attributed to one
        "is_pyq": q.source_type == "pyq" or bool((q.pyq_year or "").strip() or (q.pyq_paper or "").strip()),
        "pyq_year": (q.pyq_year or "").strip(), "pyq_paper": (q.pyq_paper or "").strip(),
        "q_en": (q.question_en or "").strip(), "q_te": (q.question_te or "").strip(),
        "x_en": (q.explanation_en or "").strip(), "x_te": (q.explanation_te or "").strip(),
    }


# ── progress (device-scoped, no login) ──────────────────────────────
def record_section(device_id, chapter_id, section_num):
    prog = ChapterProgress.query.filter_by(device_id=device_id, chapter_id=chapter_id).first()
    if prog is None:
        prog = ChapterProgress(device_id=device_id, chapter_id=chapter_id, status="in_progress")
        db.session.add(prog)
    if prog.status in (None, "not_started"):
        prog.status = "in_progress"
    prog.current_section = section_num
    prog.last_opened_at = datetime.utcnow()
    db.session.commit()
    return prog


def resume_for(device_id):
    """Most recently opened, unfinished chapter for this device, or None."""
    prog = (ChapterProgress.query
            .filter(ChapterProgress.device_id == device_id, ChapterProgress.status == "in_progress")
            .order_by(ChapterProgress.last_opened_at.desc()).first())
    if prog is None:
        return None
    chapter = db.session.get(Chapter, prog.chapter_id)
    if chapter is None:
        return None
    total = Note.query.filter_by(chapter_id=chapter.id).count()
    return {"chapter": chapter, "progress": prog, "total": total,
            "title": display_title(chapter), "subject": db.session.get(Subject, chapter.subject_id)}
