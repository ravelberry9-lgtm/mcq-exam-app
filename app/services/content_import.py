"""Safe content import: preview, then a scoped, transactional, backed-up apply.

Used by every admin/CLI path that loads notes or questions from an external source (``data/content.db`` and the
AP History HTML chapter files). Rules this module enforces:

* **Nothing is deleted or overwritten by default.** The default apply only *adds* what is missing. Chapters are never deleted.
* Notes that exist live but differ from the source (e.g. edited by hand) are reported as "differ" and **kept**, unless the
  caller explicitly asks to replace them.
* Replacing or removing notes is opt-in per call, limited to the chosen subjects, and every note it touches is first copied
  into ``note_backups`` in the same transaction, so ``restore_batch`` can undo it.
* Subjects that were not chosen, and notes in chapters the source does not mention, are never touched.
* One database transaction. The tables involved are locked first, then the preview fingerprint of each chosen subject is
  recomputed *under the lock*; a mismatch (live data or source changed since the preview) refuses the import. A concurrent
  edit therefore either lands before the check (and is detected) or waits until the import has committed.
* Question identity is the full content (subject, type, text, options, answer, PYQ year/paper), never a text prefix, so
  distinct questions that share a stem are all kept; only exact duplicates are skipped.
"""
import gzip
import hashlib
import json
import shutil
import sqlite3
import tempfile
import uuid
from datetime import datetime
from pathlib import Path

from sqlalchemy import text

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


class Source:
    """A read-only SQLite source (subjects/chapters/notes/questions) plus its content hash.
    Use as a context manager: closing releases the connection and removes any temporary files."""

    def __init__(self, conn, sha, tmpdir=None, warnings=()):
        self.conn, self.sha, self._tmpdir, self.warnings = conn, sha, tmpdir, list(warnings)

    def execute(self, *a):
        return self.conn.execute(*a)

    def close(self):
        try:
            self.conn.close()
        finally:
            if self._tmpdir:
                shutil.rmtree(self._tmpdir, ignore_errors=True)
                self._tmpdir = None

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        self.close()


def open_source(path=None):
    """Open ``content.db`` read-only. A missing file is unpacked from ``content.db.gz`` into a temporary directory
    (never into the repository) that is removed on ``close()``."""
    path = Path(path) if path else DEFAULT_SOURCE
    tmpdir = None
    if not path.exists():
        gz = Path(str(path) + ".gz")
        if not gz.exists():
            raise ContentImportError(f"Source database not found: {path.name}")
        tmpdir = tempfile.mkdtemp(prefix="content_src_")
        path = Path(tmpdir) / path.name
        with gzip.open(gz, "rb") as fin, open(path, "wb") as fout:
            shutil.copyfileobj(fin, fout)
    try:
        conn = sqlite3.connect(f"file:{path.as_posix()}?mode=ro", uri=True)
        conn.row_factory = sqlite3.Row
        return Source(conn, _sha256(path), tmpdir)
    except Exception:
        if tmpdir:
            shutil.rmtree(tmpdir, ignore_errors=True)
        raise


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


def _canon(val):
    return json.dumps(_j(val), sort_keys=True, ensure_ascii=False)


def _qkey(slug, source_type, q_en, q_te, o_en, o_te, answer, year, paper):
    """Full-content identity of a question (an md5 of canonical JSON). Whitespace at the ends is ignored."""
    payload = json.dumps([slug, source_type or "practice", (q_en or "").strip(), (q_te or "").strip(),
                          _canon(o_en), _canon(o_te), (answer or "a").strip(),
                          str(year) if year else "", str(paper) if paper else ""], ensure_ascii=False)
    return hashlib.md5(payload.encode("utf-8", "replace")).hexdigest()


def _src_qkey(slug, r):
    return _qkey(slug, r["source_type"], r["question_en"], r["question_te"], r["options_en"], r["options_te"],
                 r["correct_answer"], r["pyq_year"], r["pyq_paper"])


def _note_fields(r):
    return {k: (r[k] or "") for k in ("heading_en", "heading_te", "body_en", "body_te")}


def _same(note, fields):
    return all((getattr(note, k) or "") == fields[k] for k in fields)


def _nhash(n):
    return hashlib.md5("\x1f".join((getattr(n, k) or "") for k in
                                   ("heading_en", "heading_te", "body_en", "body_te")).encode("utf-8", "replace")).hexdigest()


# ── plan (read-only) ───────────────────────────────────────────────
def _live_questions():
    """live question keys grouped by subject slug."""
    out = {}
    q = db.select(Subject.slug, Question.source_type, Question.question_en, Question.question_te, Question.options_en,
                  Question.options_te, Question.correct_answer, Question.pyq_year, Question.pyq_paper
                  ).join(Subject, Subject.id == Question.subject_id)
    for slug, *rest in db.session.execute(q).all():
        out.setdefault(slug, set()).add(_qkey(slug, *rest))
    return out


def build_plan(src):
    """Describe what an import would do, per source subject, without writing anything. Each subject carries a
    fingerprint of everything its apply depends on: the source, the live subject/chapters, **every** live note in those
    chapters (including ones the source does not mention) and the live question keys."""
    live_subjects = {s.slug: s for s in Subject.query.all()}
    live_chapters = {}
    for c in Chapter.query.all():
        live_chapters.setdefault(c.subject_id, {})[c.chapter_num] = c
    live_notes = {}
    for n in Note.query.all():
        live_notes.setdefault(n.chapter_id, {})[n.section_num] = n
    live_q = _live_questions()

    src_subj = {r["id"]: r for r in src.execute("SELECT * FROM subjects ORDER BY sort_order, id")}
    src_ch = {r["id"]: r for r in src.execute("SELECT * FROM chapters")}
    plans, fps = [], {}
    for sid, s in src_subj.items():
        slug = s["slug"]
        live_s = live_subjects.get(slug)
        chs = live_chapters.get(live_s.id, {}) if live_s else {}
        p = {"slug": slug, "name_en": s["name_en"], "name_te": s["name_te"], "exists": live_s is not None,
             "chapters": {"source": 0, "new": 0},
             "notes": {"source": 0, "add": 0, "same": 0, "differ": 0, "extra_live": 0},
             "questions": {"source": 0, "add": 0, "duplicate": 0}, "samples": []}
        seen = {}
        for c in (c for c in src_ch.values() if c["subject_id"] == sid):
            p["chapters"]["source"] += 1
            live_c = chs.get(c["chapter_num"])
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
        for live_id, sections in seen.items():
            p["notes"]["extra_live"] += sum(1 for sec in live_notes.get(live_id, {}) if sec not in sections)
        have = set(live_q.get(slug, ()))
        for r in src.execute("SELECT * FROM questions WHERE subject_id=?", (sid,)):
            p["questions"]["source"] += 1
            k = _src_qkey(slug, r)
            if k in have:
                p["questions"]["duplicate"] += 1
            else:
                p["questions"]["add"] += 1
                have.add(k)
        # fingerprint: source + all live state this subject's apply reads
        h = hashlib.sha256()
        h.update(src.sha.encode())
        h.update(json.dumps(p, sort_keys=True, default=str).encode())
        h.update(json.dumps([live_s.id, live_s.name_en, live_s.name_te] if live_s else None).encode())
        for num, c in sorted(chs.items()):
            h.update(f"c{c.id}:{num}".encode())
            for sec, n in sorted(live_notes.get(c.id, {}).items()):
                h.update(f"n{n.id}:{sec}:{_nhash(n)}".encode())
        h.update(json.dumps(sorted(live_q.get(slug, ()))).encode())
        fps[slug] = h.hexdigest()
        p["fingerprint"] = fps[slug]
        plans.append(p)
    return {"subjects": plans, "source_sha256": src.sha, "fingerprints": fps, "warnings": list(src.warnings)}


# ── locking ────────────────────────────────────────────────────────
def lock_for_import():
    """Take a write lock on the tables an import reads and writes, held until commit/rollback. PostgreSQL:
    SHARE ROW EXCLUSIVE (readers continue, other writers wait). SQLite: a write statement takes the database write lock."""
    name = db.session.get_bind().dialect.name
    if name == "postgresql":
        db.session.execute(text("LOCK TABLE subjects, chapters, notes, questions, note_backups IN SHARE ROW EXCLUSIVE MODE"))
    elif name == "sqlite":
        db.session.execute(text("UPDATE note_backups SET id = id WHERE 0"))
    else:
        raise ContentImportError(f"Unsupported database for import: {name}. Nothing was changed.")


# ── apply (one transaction) ────────────────────────────────────────
def _backup(batch_id, note, reason):
    db.session.add(NoteBackup(batch_id=batch_id, reason=reason, chapter_id=note.chapter_id,
                              section_num=note.section_num, heading_en=note.heading_en, heading_te=note.heading_te,
                              body_en=note.body_en, body_te=note.body_te, created_at=datetime.utcnow()))


def apply_import(src, slugs, expected_fingerprints, replace_notes=False, remove_extra=False):
    """Import the chosen subjects. ``expected_fingerprints`` maps slug -> fingerprint from the preview. Returns a result
    dict. Raises ``ContentImportError`` on refusal; any other exception also rolls the transaction back first."""
    slugs = list(dict.fromkeys(slugs or []))
    if not slugs:
        raise ContentImportError("Choose at least one subject. Nothing was changed.")
    batch_id = uuid.uuid4().hex
    res = {"batch_id": batch_id, "subjects": slugs, "replace_notes": replace_notes, "remove_extra": remove_extra,
           "added": {"subjects": 0, "chapters": 0, "notes": 0, "questions": 0},
           "notes_replaced": 0, "notes_removed": 0, "notes_kept_differing": 0}
    try:
        lock_for_import()
        plan = build_plan(src)                       # recomputed under the lock
        unknown = [s for s in slugs if s not in plan["fingerprints"]]
        if unknown:
            raise ContentImportError(f"Unknown subject(s): {', '.join(unknown)}. Nothing was changed.")
        stale = [s for s in slugs if plan["fingerprints"][s] != (expected_fingerprints or {}).get(s)]
        if stale:
            raise ContentImportError("The live data or the source changed since the preview for: "
                                     f"{', '.join(stale)}. Run the preview again. Nothing was changed.")
        src_subj = {r["id"]: r for r in src.execute("SELECT * FROM subjects")}
        live_subjects = {s.slug: s for s in Subject.query.all()}
        for sid, s in src_subj.items():
            if s["slug"] in slugs and s["slug"] not in live_subjects:
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

        have = _live_questions()
        for r in src.execute("SELECT * FROM questions"):
            slug = src_subj[r["subject_id"]]["slug"] if r["subject_id"] in src_subj else None
            if slug not in slugs:
                continue
            k = _src_qkey(slug, r)
            if k in have.setdefault(slug, set()):
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
            have[slug].add(k); res["added"]["questions"] += 1
        db.session.commit()
    except BaseException:
        db.session.rollback()
        raise
    return res


# ── restore ────────────────────────────────────────────────────────
def restore_batch(batch_id):
    """Put back the notes saved by one import. The current versions are saved under a new batch first, so a
    restore can itself be undone. Notes whose chapter no longer exists are skipped and counted."""
    new_batch = uuid.uuid4().hex
    out = {"batch_id": new_batch, "restored": 0, "recreated": 0, "skipped_missing_chapter": 0}
    try:
        lock_for_import()
        rows = NoteBackup.query.filter_by(batch_id=batch_id).all()
        if not rows:
            raise ContentImportError("No saved notes for that batch id.")
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
    except BaseException:
        db.session.rollback()
        raise
    return out
