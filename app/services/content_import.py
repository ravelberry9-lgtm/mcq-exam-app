"""Safe content import: preview, then a scoped, transactional, backed-up apply.

Replaces the old loader behaviour that deleted every note of every subject before
re-inserting from ``content.db``. Rules this module enforces:

* **Nothing is deleted or overwritten by default.** The default apply only *adds* what is missing.
* Notes that exist in the live database but differ from the source (for example edited by hand in the
  admin editor) are reported as "differs" and **kept**, unless the caller explicitly asks to replace them.
* Replacing or removing notes is opt-in per call, limited to the subjects chosen, and every note it touches is
  first copied into ``note_backups`` in the same transaction, so ``restore_batch`` can undo it.
* Notes of subjects that were not selected, and notes in chapters the source does not mention, are never touched.
* Everything happens in one database transaction: any error rolls the whole import back.
* ``apply_import`` refuses if the live data changed since the preview (fingerprint mismatch).
"""
import gzip
import hashlib
import json
import os
import shutil
import sqlite3
import tempfile
import uuid
from datetime import datetime
from pathlib import Path

from ..db import db
from ..models import Chapter, Note, NoteBackup, Question, Subject

ROOT = Path(__file__).resolve().parent.parent.parent
DEFAULT_SOURCE = ROOT / "data" / "content.db"
SAMPLE_LIMIT = 5


class ContentImportError(Exception):
    """A refusal or failure with a message that is safe to show to the admin."""


# ── source ─────────────────────────────────────────────────────────
def _sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def open_source(path=None):
    """Open the source SQLite read-only. A missing ``content.db`` is unpacked from ``content.db.gz`` into a
    temporary file (never into the repository). Returns ``(connection, sha256_of_file)``."""
    path = Path(path) if path else DEFAULT_SOURCE
    if not path.exists():
        gz = Path(str(path) + ".gz")
        if not gz.exists():
            raise ContentImportError(f"Source database not found: {path.name}")
        tmp = Path(tempfile.mkdtemp(prefix="content_src_")) / path.name
        with gzip.open(gz, "rb") as fin, open(tmp, "wb") as fout:
            shutil.copyfileobj(fin, fout)
        path = tmp
    conn = sqlite3.connect(f"file:{path}?mode=ro", uri=True)
    conn.row_factory = sqlite3.Row
    return conn, _sha256(path)


def _j(val):
    """JSON columns arrive as TEXT in the source; store real objects, not a JSON string of a string."""
    if val is None or val == "":
        return {}
    if isinstance(val, (dict, list)):
        return val
    try:
        return json.loads(val)
    except Exception:
        return {}


def _qhash(src_type, q_en, q_te):
    text = (q_en or q_te or "")[:120]
    return hashlib.md5(f"{src_type}:{text}".encode("utf-8", "replace")).hexdigest()


def _note_fields(r):
    return {k: (r[k] or "") for k in ("heading_en", "heading_te", "body_en", "body_te")}


def _same(note, fields):
    return all((getattr(note, k) or "") == fields[k] for k in fields)


# ── plan (read-only) ───────────────────────────────────────────────
def build_plan(src, src_sha):
    """Describe what an import would do, per source subject, without writing anything."""
    live_subjects = {s.slug: s for s in Subject.query.all()}
    live_chapters = {(c.subject_id, c.chapter_num): c for c in Chapter.query.all()}
    live_notes = {}
    for n in Note.query.all():
        live_notes.setdefault(n.chapter_id, {})[n.section_num] = n
    existing_hashes = {_qhash(t, en, te) for t, en, te in db.session.execute(
        db.select(Question.source_type, Question.question_en, Question.question_te)).all()}

    src_subj = {r["id"]: r for r in src.execute("SELECT * FROM subjects ORDER BY sort_order, id")}
    src_ch = {r["id"]: r for r in src.execute("SELECT * FROM chapters")}
    plans, digest = [], hashlib.sha256()
    for sid, s in src_subj.items():
        live_s = live_subjects.get(s["slug"])
        p = {"slug": s["slug"], "name_en": s["name_en"], "name_te": s["name_te"], "exists": live_s is not None,
             "chapters": {"source": 0, "new": 0},
             "notes": {"source": 0, "add": 0, "same": 0, "differ": 0, "extra_live": 0},
             "questions": {"source": 0, "add": 0, "duplicate": 0}, "samples": []}
        seen = {}                                     # live chapter id -> source section numbers
        for c in (c for c in src_ch.values() if c["subject_id"] == sid):
            p["chapters"]["source"] += 1
            live_c = live_chapters.get((live_s.id, c["chapter_num"])) if live_s else None
            if live_c is None:
                p["chapters"]["new"] += 1
            for r in src.execute("SELECT * FROM notes WHERE chapter_id=? ORDER BY section_num", (c["id"],)):
                p["notes"]["source"] += 1
                cur = live_notes.get(live_c.id, {}).get(r["section_num"]) if live_c else None
                if live_c:
                    seen.setdefault(live_c.id, set()).add(r["section_num"])
                if cur is None:
                    p["notes"]["add"] += 1
                elif _same(cur, _note_fields(r)):
                    p["notes"]["same"] += 1
                else:
                    p["notes"]["differ"] += 1
                    if len(p["samples"]) < SAMPLE_LIMIT:
                        p["samples"].append({"chapter_num": c["chapter_num"], "section_num": r["section_num"],
                                             "live_heading": cur.heading_en or cur.heading_te or "",
                                             "source_heading": r["heading_en"] or r["heading_te"] or ""})
                    digest.update(f"{cur.id}:{hashlib.md5(((cur.body_en or '') + (cur.body_te or '') + (cur.heading_en or '') + (cur.heading_te or '')).encode()).hexdigest()}".encode())
        for live_id, sections in seen.items():        # only chapters the source mentions
            p["notes"]["extra_live"] += sum(1 for sec in live_notes.get(live_id, {}) if sec not in sections)
        for r in src.execute("SELECT source_type, question_en, question_te FROM questions WHERE subject_id=?", (sid,)):
            p["questions"]["source"] += 1
            if _qhash(r["source_type"], r["question_en"], r["question_te"]) in existing_hashes:
                p["questions"]["duplicate"] += 1
            else:
                p["questions"]["add"] += 1
        plans.append(p)
    digest.update(json.dumps(plans, sort_keys=True, default=str).encode())
    digest.update(src_sha.encode())
    return {"subjects": plans, "source_sha256": src_sha, "fingerprint": digest.hexdigest()}


# ── apply (one transaction) ────────────────────────────────────────
def _backup(batch_id, note, reason):
    db.session.add(NoteBackup(batch_id=batch_id, reason=reason, chapter_id=note.chapter_id,
                              section_num=note.section_num, heading_en=note.heading_en, heading_te=note.heading_te,
                              body_en=note.body_en, body_te=note.body_te, created_at=datetime.utcnow()))


def apply_import(src, src_sha, slugs, expected_fingerprint, replace_notes=False, remove_extra=False):
    """Import the chosen subjects. Returns a result dict. Raises ``ContentImportError`` on refusal; any other
    exception also rolls the transaction back before propagating."""
    slugs = [s for s in dict.fromkeys(slugs or [])]
    if not slugs:
        raise ContentImportError("Choose at least one subject. Nothing was changed.")
    plan = build_plan(src, src_sha)
    known = {p["slug"] for p in plan["subjects"]}
    unknown = [s for s in slugs if s not in known]
    if unknown:
        raise ContentImportError(f"Unknown subject(s): {', '.join(unknown)}. Nothing was changed.")
    if plan["fingerprint"] != expected_fingerprint:
        raise ContentImportError("The live data or the source file changed since the preview. "
                                 "Run the preview again. Nothing was changed.")
    batch_id = uuid.uuid4().hex
    res = {"batch_id": batch_id, "subjects": slugs, "replace_notes": replace_notes, "remove_extra": remove_extra,
           "added": {"subjects": 0, "chapters": 0, "notes": 0, "questions": 0},
           "notes_replaced": 0, "notes_removed": 0, "notes_kept_differing": 0}
    try:
        src_subj = {r["id"]: r for r in src.execute("SELECT * FROM subjects")}
        live_subjects = {s.slug: s for s in Subject.query.all()}
        for sid, s in src_subj.items():
            if s["slug"] not in slugs:
                continue
            if s["slug"] not in live_subjects:
                live_subjects[s["slug"]] = Subject(slug=s["slug"], name_en=s["name_en"], name_te=s["name_te"],
                                                   sort_order=s["sort_order"])
                db.session.add(live_subjects[s["slug"]]); res["added"]["subjects"] += 1
        db.session.flush()

        live_chapters = {(c.subject_id, c.chapter_num): c for c in Chapter.query.all()}
        ch_map = {}
        for r in src.execute("SELECT * FROM chapters ORDER BY subject_id, chapter_num"):
            slug = src_subj[r["subject_id"]]["slug"]
            if slug not in slugs:
                continue
            key = (live_subjects[slug].id, r["chapter_num"])
            if key not in live_chapters:
                live_chapters[key] = Chapter(subject_id=key[0], chapter_num=r["chapter_num"], title_en=r["title_en"] or "",
                                             title_te=r["title_te"] or r["title_en"] or "",
                                             est_read_minutes=r["est_read_minutes"] or 20)
                db.session.add(live_chapters[key]); db.session.flush(); res["added"]["chapters"] += 1
            ch_map[r["id"]] = live_chapters[key].id

        live_notes = {}
        for n in Note.query.filter(Note.chapter_id.in_(set(ch_map.values()) or {-1})).all():
            live_notes.setdefault(n.chapter_id, {})[n.section_num] = n
        src_sections = {}
        for r in src.execute("SELECT * FROM notes ORDER BY chapter_id, section_num"):
            live_ch = ch_map.get(r["chapter_id"])
            if live_ch is None:
                continue
            src_sections.setdefault(live_ch, set()).add(r["section_num"])
            fields = _note_fields(r)
            cur = live_notes.get(live_ch, {}).get(r["section_num"])
            if cur is None:
                db.session.add(Note(chapter_id=live_ch, section_num=r["section_num"], **fields)); res["added"]["notes"] += 1
            elif _same(cur, fields):
                continue
            elif replace_notes:
                _backup(batch_id, cur, "replaced")
                for k, v in fields.items():
                    setattr(cur, k, v)
                res["notes_replaced"] += 1
            else:
                res["notes_kept_differing"] += 1
        if remove_extra:
            for live_ch, sections in src_sections.items():
                for sec, n in list(live_notes.get(live_ch, {}).items()):
                    if sec not in sections:
                        _backup(batch_id, n, "removed"); db.session.delete(n); res["notes_removed"] += 1
        db.session.flush()

        existing_hashes = {_qhash(t, en, te) for t, en, te in db.session.execute(
            db.select(Question.source_type, Question.question_en, Question.question_te)).all()}
        for r in src.execute("SELECT * FROM questions"):
            slug = src_subj[r["subject_id"]]["slug"] if r["subject_id"] in src_subj else None
            if slug not in slugs:
                continue
            h = _qhash(r["source_type"], r["question_en"], r["question_te"])
            if h in existing_hashes:
                continue
            db.session.add(Question(
                subject_id=live_subjects[slug].id, chapter_id=ch_map.get(r["chapter_id"]) if r["chapter_id"] else None,
                source_type=r["source_type"] or "practice", difficulty=r["difficulty"] or "M",
                question_en=r["question_en"] or "", question_te=r["question_te"] or "",
                options_en=_j(r["options_en"]), options_te=_j(r["options_te"]),
                correct_answer=r["correct_answer"] or "a",
                explanation_en=r["explanation_en"] or "", explanation_te=r["explanation_te"] or "",
                pyq_year=str(r["pyq_year"]) if r["pyq_year"] else None,
                pyq_paper=str(r["pyq_paper"]) if r["pyq_paper"] else None,
                created_at=datetime.utcnow(), updated_at=datetime.utcnow()))
            existing_hashes.add(h); res["added"]["questions"] += 1
        db.session.commit()
    except Exception:
        db.session.rollback()
        raise
    return res


# ── restore ────────────────────────────────────────────────────────
def restore_batch(batch_id):
    """Put back the notes saved by one import. The current versions are saved under a new batch first, so a
    restore can itself be undone. Notes whose chapter no longer exists are skipped and counted."""
    rows = NoteBackup.query.filter_by(batch_id=batch_id).all()
    if not rows:
        raise ContentImportError("No saved notes for that batch id.")
    new_batch = uuid.uuid4().hex
    out = {"batch_id": new_batch, "restored": 0, "recreated": 0, "skipped_missing_chapter": 0}
    try:
        for b in rows:
            if db.session.get(Chapter, b.chapter_id) is None:
                out["skipped_missing_chapter"] += 1
                continue
            cur = Note.query.filter_by(chapter_id=b.chapter_id, section_num=b.section_num).first()
            vals = dict(heading_en=b.heading_en, heading_te=b.heading_te, body_en=b.body_en, body_te=b.body_te)
            if cur is None:
                db.session.add(Note(chapter_id=b.chapter_id, section_num=b.section_num, **vals)); out["recreated"] += 1
            else:
                _backup(new_batch, cur, "replaced")
                for k, v in vals.items():
                    setattr(cur, k, v)
                out["restored"] += 1
        db.session.commit()
    except Exception:
        db.session.rollback()
        raise
    return out
