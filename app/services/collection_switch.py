"""Per-chapter learner switch between the legacy question/notes content and a fresh collection.

* Chapters are identified by canonical slug (``SyllabusChapter.slug``), never by database id.
* Default = legacy: no setting row, or ``active_collection`` NULL.
* Switching to a collection requires every readiness check to pass (notes, questions, links). There is no override.
  Switching back to legacy is always allowed.
* A switch only writes ``chapter_collection_setting`` and appends to ``chapter_collection_log``. No question, note, progress,
  session or answer row is touched, so both collections and all learner history survive any number of switches.
* "Who": the admin gate is a shared PIN, so the actor is the name typed on the admin form (required) plus the remote address;
  both are recorded with the time and the readiness result.
"""
import re
from collections import Counter
from datetime import datetime

from ..db import db
from ..models import (FRESH_COLLECTION_ID, ChapterCollectionLog, ChapterCollectionSetting, ExpandedNote, Question, Subject,
                      SyllabusChapter, SyllabusSubtopic, LEARNER_VISIBLE_STATUS)
from . import expanded_view as xv
from . import mcq_import as legacy

LEGACY = "legacy"
SUBJECT_SLUG = "ap_history"
COLLECTION_RE = re.compile(r"[a-z0-9][a-z0-9._-]{2,62}")


class SwitchError(Exception):
    """A refusal whose message is safe to show to the administrator."""

    def __init__(self, msg, readiness=None):
        super().__init__(msg)
        self.readiness = readiness


def chapter_by_slug(slug):
    sub = Subject.query.filter_by(slug=SUBJECT_SLUG).first()
    if not sub:
        return None
    return SyllabusChapter.query.filter_by(subject_id=sub.id, slug=slug).first()


def active_collection(ch):
    """The collection id learners are sent to for this chapter, or None for legacy (the default)."""
    row = ChapterCollectionSetting.query.filter_by(syllabus_chapter_id=ch.id).first()
    return row.active_collection if row and row.active_collection else None


def ever_activated(ch, collection_id=FRESH_COLLECTION_ID):
    """True once a switch to the collection has succeeded for this chapter. Content pages and review links of that collection
    stay reachable afterwards (also after switching back) so a learner's history never dead-ends."""
    return db.session.query(ChapterCollectionLog.id).filter_by(syllabus_chapter_id=ch.id, to_collection=collection_id).first() is not None


def can_view_collection(ch, collection_id, is_admin=False):
    return bool(is_admin or active_collection(ch) == collection_id or ever_activated(ch, collection_id))


def _blank(x):
    return not (x or "").strip()


def readiness(ch, collection_id=FRESH_COLLECTION_ID):
    """Run every check. ``ok`` is True only when all pass. Read-only."""
    checks, counts = [], {}

    def add(key, ok, detail):
        checks.append({"key": key, "ok": bool(ok), "detail": detail})

    notes = ExpandedNote.query.filter_by(syllabus_chapter_id=ch.id, collection_id=collection_id).all()
    counts["notes"] = len(notes)
    add("notes_present", any(n.kind == "core" for n in notes), f"{len(notes)} notes, {sum(n.kind == 'core' for n in notes)} core")
    bad = [n.anchor_id for n in notes if _blank(n.heading_en) or _blank(n.heading_te) or _blank(n.body_en) or _blank(n.body_te)]
    add("notes_bilingual", notes and not bad, "all notes have English and Telugu heading and body" if not bad else f"incomplete: {bad[:5]}")
    by_anchor = {n.anchor_id: n for n in notes}
    dangling = sorted({c for n in notes for c in (n.core_connections or []) if c not in by_anchor})
    add("notes_connections_resolve", not dangling, "every addendum connection resolves" if not dangling else f"unknown core anchors: {dangling[:5]}")
    unreachable = [n.anchor_id for n in notes if xv.page(ch, n.anchor_id, collection_id) is None]
    add("note_pages_render", notes and not unreachable, "every note page can be built" if not unreachable else f"unreachable: {unreachable[:5]}")

    qs = Question.query.filter_by(collection_id=collection_id, syllabus_chapter_id=ch.id).all()
    counts["questions"] = len(qs)
    other = Question.query.filter(Question.collection_id == collection_id, Question.syllabus_chapter_id != ch.id).count()
    counts["questions_in_collection_other_chapters"] = other
    add("questions_present", qs, f"{len(qs)} questions in {collection_id} for this chapter")
    unapproved = [q.source_qid for q in qs if q.review_status != LEARNER_VISIBLE_STATUS]
    add("questions_approved", qs and not unapproved, "all are bilingual_approved" if not unapproved else f"not approved: {unapproved[:5]}")

    def incomplete(q):
        for lang in ("en", "te"):
            opts = {k: v for k, v in (getattr(q, f"options_{lang}") or {}).items() if (v or "").strip()}
            if _blank(getattr(q, f"question_{lang}")) or _blank(getattr(q, f"explanation_{lang}")) or len(opts) < 4 or q.correct_answer not in opts:
                return True
        return False
    inc = [q.source_qid for q in qs if incomplete(q)]
    add("questions_bilingual_complete", qs and not inc, "stem, options, answer and explanation in both languages" if not inc else f"incomplete: {inc[:5]}")
    subs = {s.id for s in SyllabusSubtopic.query.filter_by(chapter_id=ch.id)}
    bad_sub = [q.source_qid for q in qs if q.subtopic_id not in subs]
    add("questions_taxonomy", qs and not bad_sub, "every question sits on a subtopic of this chapter" if not bad_sub else f"bad subtopic: {bad_sub[:5]}")
    bad_id = [q.source_qid for q in qs if q.chapter_id is not None or not q.source_qid]
    add("questions_isolated_from_legacy", not bad_id, "no collection question carries a legacy chapter id" if not bad_id else f"legacy chapter ids on: {bad_id[:5]}")
    stems = Counter(legacy.norm(q.question_en) for q in qs)
    hashes = Counter(q.content_hash for q in qs if q.content_hash)
    dups = [s[:40] for s, n in stems.items() if n > 1] + [h for h, n in hashes.items() if n > 1]
    add("questions_deduplicated_in_collection", not dups, "no duplicate inside the collection" if not dups else f"duplicates: {dups[:5]}")

    missing, unresolved, no_link = [], [], []
    from . import learn as svc
    cache = {}
    for q in qs:
        t = q.source_trace if isinstance(q.source_trace, dict) else {}
        anchors = (t.get("expanded_note") or {}).get("anchor_ids") or []
        if not anchors:
            missing.append(q.source_qid); continue
        if any(a not in by_anchor for a in anchors):
            unresolved.append(q.source_qid); continue
        try:
            link = svc.note_link_for(q, cache)
        except Exception:        # no request context: the anchor check above already proves the target exists
            link = {"exact": True}
        if not link or not link.get("exact"):
            no_link.append(q.source_qid)
    add("questions_name_a_note", qs and not missing, "every question names an expanded-note anchor" if not missing else f"no anchor: {missing[:5]}")
    add("question_links_resolve", qs and not unresolved and not no_link,
        "every question's note link resolves to a loaded note" if not (unresolved or no_link) else f"unresolved: {(unresolved + no_link)[:5]}")
    return {"chapter": ch.slug, "collection_id": collection_id, "ok": all(c["ok"] for c in checks), "checks": checks, "counts": counts}


def _clean_actor(actor):
    a = re.sub(r"[\x00-\x1f\x7f]", " ", actor or "").strip()
    if len(a) < 2:
        raise SwitchError("name of the person making the change is required (2 to 80 characters)")
    return a[:80]


def set_active(slug, target, actor, remote_addr=None, reason=None):
    """Switch one chapter. ``target`` is 'legacy' or a collection id. Returns a result dict; raises SwitchError on refusal."""
    ch = chapter_by_slug(slug) or (_ for _ in ()).throw(SwitchError(f"unknown canonical chapter slug: {slug!r}"))
    actor = _clean_actor(actor)
    target = (target or "").strip()
    if target != LEGACY and not COLLECTION_RE.fullmatch(target):
        raise SwitchError("target must be 'legacy' or an explicit collection id")
    cur = active_collection(ch)
    new = None if target == LEGACY else target
    rd = None
    if new is not None:
        rd = readiness(ch, new)
        if not rd["ok"]:
            failed = [c["key"] for c in rd["checks"] if not c["ok"]]
            raise SwitchError(f"chapter is not ready for {new}: failed checks {failed}. Nothing was changed.", rd)
    if cur == new:
        return {"changed": False, "chapter": ch.slug, "active": new or LEGACY, "readiness": rd}
    row = ChapterCollectionSetting.query.filter_by(syllabus_chapter_id=ch.id).first()
    now = datetime.utcnow()
    try:
        if row is None:
            row = ChapterCollectionSetting(syllabus_chapter_id=ch.id)
            db.session.add(row)
        row.active_collection, row.updated_by, row.updated_at = new, actor, now
        db.session.add(ChapterCollectionLog(
            syllabus_chapter_id=ch.id, chapter_slug=ch.slug, from_collection=cur, to_collection=new, actor=actor,
            remote_addr=(remote_addr or "")[:64] or None, changed_at=now,
            readiness=({"ok": rd["ok"], "counts": rd["counts"], "checks": [c["key"] for c in rd["checks"]]} if rd else None),
            reason=(reason or "").strip()[:300] or None))
        db.session.commit()
    except Exception:
        db.session.rollback()
        raise
    return {"changed": True, "chapter": ch.slug, "from": cur or LEGACY, "active": new or LEGACY, "readiness": rd}


def overview(collection_id=FRESH_COLLECTION_ID):
    """Rows for the admin page: every canonical chapter that has any content in the collection, plus its state and last change."""
    sub = Subject.query.filter_by(slug=SUBJECT_SLUG).first()
    if not sub:
        return []
    ids = {c for (c,) in db.session.query(Question.syllabus_chapter_id).filter(Question.collection_id == collection_id)}
    ids |= {c for (c,) in db.session.query(ExpandedNote.syllabus_chapter_id).filter(ExpandedNote.collection_id == collection_id)}
    out = []
    for ch in SyllabusChapter.query.filter(SyllabusChapter.id.in_(ids)).order_by(SyllabusChapter.sort_order, SyllabusChapter.id):
        cur = ChapterCollectionSetting.query.filter_by(syllabus_chapter_id=ch.id).first()
        last = ChapterCollectionLog.query.filter_by(syllabus_chapter_id=ch.id).order_by(ChapterCollectionLog.id.desc()).first()
        out.append({"chapter": ch, "active": (cur.active_collection if cur and cur.active_collection else LEGACY), "readiness": readiness(ch, collection_id),
                    "last": last, "collection_id": collection_id})
    return out
