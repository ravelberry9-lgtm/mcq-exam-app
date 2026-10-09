"""Data access for the design-system journey: Learn -> Section -> Topic -> Notes -> Practice.

Terminology: the prototype's "topic" is a ``Chapter`` row; a "section" is an ``ExamSection``
(a block of an exam paper such as "Indian History, 30 marks") that groups subjects.
Nothing here writes to the database except the small progress helpers at the bottom.
"""
import re
from datetime import datetime

import bleach
from sqlalchemy import case, func, or_

from ..db import db
from ..models import (
    Chapter, ChapterProgress, Exam, ExamPaper, ExamSection, ExamSyllabusItem,
    ExpandedNote, ExpandedNoteAppMap, Note, Question, Subject, SyllabusChapter,
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
    from .note_images import rewrite_images
    return rewrite_images(clean_note_html(strip_blocks(html), keep_class))


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


# ── question banks ──────────────────────────────────────────────────
# Every question is reachable from exactly one place in Learn:
#   * chapter bank  - source_type 'chapter' with a chapter: the topic's Practice;
#   * PYQ bank      - source_type 'pyq' (any chapter or none): the subject's Previous papers;
#   * practice bank - everything else (practice questions, and chapter-type rows with no chapter): the subject's Practice.
# The counts shown on hub, section and subject pages are built from these same three groups, so a number on a page is the
# number of questions that page can actually reach.
BANKS = ("practice", "pyq")


def bank_counts(subject_ids=None):
    """{subject_id: {'practice': n, 'pyq': n, 'chapter': n}}"""
    no_chapter = case((Question.chapter_id.is_(None), 1), else_=0)
    q = db.session.query(Question.subject_id, Question.source_type, no_chapter, func.count(Question.id)).group_by(
        Question.subject_id, Question.source_type, no_chapter)
    if subject_ids is not None:
        ids = list(subject_ids)
        if not ids:
            return {}
        q = q.filter(Question.subject_id.in_(ids))
    out = {}
    for sid, st, nochap, n in q.all():
        d = out.setdefault(sid, {"practice": 0, "pyq": 0, "chapter": 0})
        if st == "pyq":
            d["pyq"] += n
        elif st == "chapter" and not nochap:
            d["chapter"] += n
        else:
            d["practice"] += n
    return out


def bank_questions(subject_id, bank):
    q = Question.query.filter(Question.subject_id == subject_id)
    if bank == "pyq":
        q = q.filter(Question.source_type == "pyq")
    elif bank == "practice":
        q = q.filter(Question.source_type != "pyq", or_(Question.source_type != "chapter", Question.chapter_id.is_(None)))
    else:
        raise ValueError(bank)
    return q.order_by(Question.id).all()


def _empty_banks():
    return {"practice": 0, "pyq": 0, "chapter": 0}


def subject_entries():
    """All subjects that have chapters or questions, with the counts of what Learn can reach for each."""
    ch = dict(db.session.query(Chapter.subject_id, func.count(Chapter.id)).group_by(Chapter.subject_id).all())
    banks = bank_counts()
    out = []
    for s in Subject.query.order_by(Subject.sort_order, Subject.id).all():
        b = banks.get(s.id, _empty_banks())
        total = b["practice"] + b["pyq"] + b["chapter"]
        out.append({"subject": s, "chapter_count": ch.get(s.id, 0), "question_count": total, "banks": b,
                    "available": ch.get(s.id, 0) > 0 or total > 0})
    return out


def hub(exam=None):
    """Return {'exam': Exam|None, 'papers': [...], 'subjects': [...]}; ``flat`` is the subject list when no exam is seeded."""
    entries = subject_entries()
    exam = exam or get_exam()
    if exam is None:
        return {"exam": None, "papers": [], "flat": entries, "subjects": entries}

    banks = bank_counts()
    papers = []
    for paper in ExamPaper.query.filter_by(exam_id=exam.id).order_by(ExamPaper.paper_num).all():
        sections = []
        for sec in ExamSection.query.filter_by(paper_id=paper.id).order_by(ExamSection.sort_order).all():
            chapters = (db.session.query(Chapter.id, Chapter.subject_id)
                        .join(ExamSyllabusItem, ExamSyllabusItem.chapter_id == Chapter.id)
                        .filter(ExamSyllabusItem.section_id == sec.id).distinct().all())
            ids = [c[0] for c in chapters]
            subject_ids = {c[1] for c in chapters}
            chapter_q = (db.session.query(func.count(Question.id))
                         .filter(Question.chapter_id.in_(ids), Question.source_type == "chapter", Question.subject_id.in_(subject_ids)).scalar()
                         if ids else 0)
            bank_q = sum(banks.get(i, _empty_banks())["practice"] + banks.get(i, _empty_banks())["pyq"] for i in subject_ids)
            sections.append({"section": sec, "chapter_count": len(ids), "question_count": chapter_q + bank_q,
                             "available": len(ids) > 0 or bank_q > 0})
        # Mains rules (duration, negative marking, question format) are NOT published here: the seeded
        # values are unverified. They stay hidden until a paper is explicitly marked verified.
        papers.append({"paper": paper, "sections": sections, "is_prelims": paper.paper_num == 0})
    return {"exam": exam, "papers": papers, "flat": [], "subjects": entries}


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
    # a topic's count is what its Practice page serves: chapter-type questions only (see ``chapter_questions``)
    q_n = dict(db.session.query(Question.chapter_id, func.count(Question.id))
               .filter(Question.chapter_id.in_(ids), Question.source_type == "chapter").group_by(Question.chapter_id).all())
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


def with_banks(groups, subjects=()):
    """Attach each group's question-bank counts. A subject with questions but no chapters gets a group of its own so it
    is still reachable (``subjects`` are the subjects the page is about)."""
    present = {g["subject"].id for g in groups if g.get("subject")}
    for sub in subjects:
        if sub.id not in present:
            groups.append({"subject": sub, "topics": []})
    counts = bank_counts([g["subject"].id for g in groups if g.get("subject")])
    keep = []
    for g in groups:
        g["banks"] = counts.get(g["subject"].id, _empty_banks())
        if g["topics"] or g["banks"]["practice"] or g["banks"]["pyq"]:
            keep.append(g)
    return keep


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


def note_link_for(q, cache=None):
    """Where "Read this in notes" should point for a question, or None when there is nothing honest to link to.

    * exact: the question names a note section (``note_section_num``) and that section exists in the question's chapter;
    * chapter: no exact section (or it no longer exists), but the chapter has notes: a chapter-level link, which the
      templates label as such (never presented as the exact passage);
    * None: the question has no chapter, or its chapter has no notes. An unrelated note is never substituted.
    ``cache`` is an optional dict that holds each chapter's section numbers across a page's questions."""
    from flask import url_for
    cache = cache if cache is not None else {}
    trace = q.source_trace if isinstance(q.source_trace, dict) else {}
    anchors = ((trace.get("expanded_note") or {}).get("anchor_ids")) or []
    if q.syllabus_chapter_id and anchors:
        return _expanded_link(q, anchors, cache)
    cid = q.chapter_id
    if not cid:
        return None
    if cid not in cache:
        cache[cid] = {n for (n,) in db.session.query(Note.section_num).filter(Note.chapter_id == cid).all()}
    sections = cache[cid]
    if not sections:
        return None
    num = q.note_section_num
    if num is not None and num in sections:
        return {"url": url_for("learn.notes", chapter_id=cid, section=num), "exact": True}
    return {"url": url_for("learn.notes", chapter_id=cid), "exact": False}


def _expanded_link(q, anchors, cache):
    """Link for a question whose package names expanded-note anchors. Exact = the named anchors exist and are linked;
    otherwise a chapter-level link to the expanded-notes index (labelled as such), or None when there are no expanded notes."""
    from flask import url_for
    ck = ("x", q.subject_id, q.syllabus_chapter_id)
    if ck not in cache:
        ch = db.session.get(SyllabusChapter, q.syllabus_chapter_id)
        rows = ExpandedNote.query.filter_by(subject_id=q.subject_id, syllabus_chapter_id=q.syllabus_chapter_id).all()
        cache[ck] = (ch.slug if ch else None, {r.anchor_id: r for r in rows})
    slug, by_anchor = cache[ck]
    if not slug or not by_anchor:
        return None
    found = [by_anchor[a] for a in anchors if a in by_anchor]
    if not found:
        return {"url": url_for("learn.expanded_index", slug=slug), "exact": False}
    first, more = found[0], found[1:]
    def one(n):
        return {"url": url_for("learn.expanded_note", slug=slug, anchor_id=n.anchor_id) + "#" + n.anchor_id,
                "title_en": n.heading_en, "title_te": n.heading_te or n.heading_en, "kind": n.kind, "section": n.package_section}
    link = one(first)
    return {"url": link["url"], "exact": True, "expanded": True, "title_en": link["title_en"], "title_te": link["title_te"],
            "section": link["section"], "more": [one(n) for n in more]}


def native_meta(q):
    """Learner-facing facts for a question imported through ap-history-import-v1: its source links, the four-level difficulty and
    the honest review label. Internal provenance (source ids, H, candidate ids, import refs) is never returned."""
    from urllib.parse import urlparse
    t = q.source_trace if isinstance(q.source_trace, dict) else {}
    if not q.syllabus_chapter_id or not t.get("format_version"):
        return {"native": False, "sources": [], "author_reviewed": False, "diff4": None}
    sources = []
    for s in t.get("sources") or []:
        u = (s.get("url") or "").strip()
        if u.startswith(("http://", "https://")):
            host = urlparse(u).netloc.lower()
            sources.append({"url": u, "host": host[4:] if host.startswith("www.") else host, "locator": (s.get("locator") or "").strip()})
    d4 = t.get("difficulty_original")
    return {"native": True, "sources": sources, "diff4": d4 if d4 in ("easy", "medium", "tough", "toughest") else None,
            "author_reviewed": bool(t.get("content_approval_note")) and q.review_status != "fact_verified"}


def question_view(q):
    """Everything the template needs for one question, with display-only clean-up applied."""
    link = note_link_for(q)
    keys = sorted({k for k in list((q.options_en or {}).keys()) + list((q.options_te or {}).keys())
                   if (q.options_en or {}).get(k) or (q.options_te or {}).get(k)})
    options = [{
        "key": k,
        "en": strip_option_prefix((q.options_en or {}).get(k)),
        "te": strip_option_prefix((q.options_te or {}).get(k)),
    } for k in keys]
    return {
        "id": q.id, "difficulty": q.difficulty, "options": options, "source_type": q.source_type,
        # provenance comes from the row itself; an exam name is not stored, so PYQs are never attributed to one
        "is_pyq": q.source_type == "pyq" or bool((q.pyq_year or "").strip() or (q.pyq_paper or "").strip()),
        "pyq_year": (q.pyq_year or "").strip(), "pyq_paper": (q.pyq_paper or "").strip(),
        "q_en": (q.question_en or "").strip(), "q_te": (q.question_te or "").strip(),
        "x_en": (q.explanation_en or "").strip(), "x_te": (q.explanation_te or "").strip(),
        "note_url": link["url"] if link else None, "note_exact": bool(link and link["exact"]),
        "note_title_en": link.get("title_en") if link else None, "note_title_te": link.get("title_te") if link else None,
        "note_more": (link or {}).get("more") or [], "note_expanded": bool(link and link.get("expanded")),
        **{"meta": native_meta(q)},
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
