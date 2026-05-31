#!/usr/bin/env python3
"""
scripts/load_content.py
=======================
Idempotent bulk-loader: reads data/content.db (the pre-built migrated SQLite)
and inserts everything into the live PostgreSQL database via SQLAlchemy.

Tables populated (in order):
  subjects → chapters → notes → questions → pages

Run:
    python scripts/load_content.py          # reads DATABASE_URL from env
    python scripts/load_content.py --dry    # count rows, no writes

Safety:
  • INSERT … ON CONFLICT DO NOTHING / INSERT OR IGNORE everywhere
  • Does NOT delete or overwrite existing rows
  • Can be re-run safely multiple times
"""

import sys, os, json, sqlite3
from pathlib import Path
from datetime import datetime

DRY = "--dry" in sys.argv

ROOT      = Path(__file__).resolve().parent.parent
DATA_DB   = ROOT / "data" / "content.db"

sys.path.insert(0, str(ROOT))

# ── Bootstrap Flask app context so we can use SQLAlchemy ─────────
os.environ.setdefault("FLASK_ENV", "production")
from app import create_app
from app.db import db
from app.models import Subject, Chapter, Note, Question

app = create_app()

# ── Helpers ───────────────────────────────────────────────────────
def _j(val):
    """Return val as-is if already a dict/list, else parse JSON string."""
    if val is None:
        return {}
    if isinstance(val, (dict, list)):
        return val
    try:
        return json.loads(val)
    except Exception:
        return {}


def _now():
    return datetime.utcnow()


# ── Main loader ───────────────────────────────────────────────────
def main():
    if not DATA_DB.exists():
        print(f"ERROR: content DB not found at {DATA_DB}")
        sys.exit(1)

    src = sqlite3.connect(str(DATA_DB))
    src.row_factory = sqlite3.Row

    # Totals in source
    src_subjects  = src.execute("SELECT COUNT(*) FROM subjects").fetchone()[0]
    src_chapters  = src.execute("SELECT COUNT(*) FROM chapters").fetchone()[0]
    src_notes     = src.execute("SELECT COUNT(*) FROM notes").fetchone()[0]
    src_questions = src.execute("SELECT COUNT(*) FROM questions").fetchone()[0]
    src_pages     = src.execute("SELECT COUNT(*) FROM pages").fetchone()[0]

    print(f"Source (data/content.db):")
    print(f"  subjects  : {src_subjects}")
    print(f"  chapters  : {src_chapters}")
    print(f"  notes     : {src_notes}")
    print(f"  questions : {src_questions}")
    print(f"  pages     : {src_pages}")
    print()

    if DRY:
        print("DRY RUN — no writes.")
        src.close()
        return

    # ── Run inside Flask app context ──────────────────────────────
    with app.app_context():
        ins = {t: 0 for t in ("subjects","chapters","notes","questions","pages")}
        skipped = {t: 0 for t in ("subjects","chapters","notes","questions","pages")}

        # ── 1. Subjects ──────────────────────────────────────────
        print("Loading subjects …")
        for r in src.execute("SELECT * FROM subjects ORDER BY sort_order"):
            existing = Subject.query.filter_by(slug=r["slug"]).first()
            if existing:
                skipped["subjects"] += 1
                continue
            s = Subject(
                slug       = r["slug"],
                name_en    = r["name_en"],
                name_te    = r["name_te"],
                sort_order = r["sort_order"],
            )
            db.session.add(s)
            ins["subjects"] += 1
        db.session.flush()

        # Build slug → live id map
        slug_to_id = {s.slug: s.id for s in Subject.query.all()}
        print(f"  inserted {ins['subjects']}, skipped {skipped['subjects']}")

        # ── 2. Chapters ──────────────────────────────────────────
        print("Loading chapters …")
        # Build src subject_id → slug map
        src_subj_slug = {
            r["id"]: r["slug"]
            for r in src.execute("SELECT id, slug FROM subjects")
        }
        # Build (live_subject_id, chapter_num) → live chapter id for dedup
        existing_chapters = {
            (c.subject_id, c.chapter_num): c.id
            for c in Chapter.query.all()
        }
        src_ch_to_live_ch = {}  # src chapter id → live chapter id

        for r in src.execute("SELECT * FROM chapters ORDER BY subject_id, chapter_num"):
            slug = src_subj_slug.get(r["subject_id"])
            live_subj_id = slug_to_id.get(slug)
            if not live_subj_id:
                skipped["chapters"] += 1
                continue

            key = (live_subj_id, r["chapter_num"])
            if key in existing_chapters:
                src_ch_to_live_ch[r["id"]] = existing_chapters[key]
                skipped["chapters"] += 1
                continue

            ch = Chapter(
                subject_id      = live_subj_id,
                chapter_num     = r["chapter_num"],
                title_en        = r["title_en"] or "",
                title_te        = r["title_te"] or r["title_en"] or "",
                est_read_minutes= r["est_read_minutes"] or 20,
            )
            db.session.add(ch)
            db.session.flush()
            existing_chapters[key] = ch.id
            src_ch_to_live_ch[r["id"]] = ch.id
            ins["chapters"] += 1

        db.session.flush()
        print(f"  inserted {ins['chapters']}, skipped {skipped['chapters']}")

        # ── 3. Notes — delete-and-replace ────────────────────────
        print("Loading notes (delete-and-replace) …")
        # Wipe ALL existing notes so garbage from previous bad migrations
        # (e.g. double-encoded JSON producing 5 000+ single-char notes) is
        # removed before we insert the clean set from content.db.
        deleted_existing = Note.query.delete()
        db.session.flush()
        print(f"  deleted {deleted_existing} existing notes")

        for r in src.execute("SELECT * FROM notes ORDER BY chapter_id, section_num"):
            live_ch_id = src_ch_to_live_ch.get(r["chapter_id"])
            if not live_ch_id:
                skipped["notes"] += 1
                continue
            n = Note(
                chapter_id  = live_ch_id,
                section_num = r["section_num"],
                heading_en  = r["heading_en"] or "",
                heading_te  = r["heading_te"] or "",
                body_en     = r["body_en"] or "",
                body_te     = r["body_te"] or "",
            )
            db.session.add(n)
            ins["notes"] += 1

            if ins["notes"] % 500 == 0:
                db.session.flush()
                print(f"    … {ins['notes']} notes inserted")

        db.session.flush()
        print(f"  inserted {ins['notes']}, skipped {skipped['notes']}")

        # ── 4. Questions ─────────────────────────────────────────
        import hashlib
        def _qhash(src_type, q_en, q_te):
            text = (q_en or q_te or "")[:120]
            return hashlib.md5(f"{src_type}:{text}".encode("utf-8","replace")).hexdigest()

        print("Loading questions …")
        # Build dedup set from live DB (using Python-side hash of content)
        print("  building dedup index from live DB …")
        existing_hashes = set()
        for q_live in db.session.execute(
            db.select(Question.source_type, Question.question_en, Question.question_te)
        ).all():
            existing_hashes.add(_qhash(q_live[0], q_live[1], q_live[2]))
        print(f"  {len(existing_hashes)} existing questions indexed")

        for r in src.execute("SELECT * FROM questions"):
            qh = _qhash(r["source_type"], r["question_en"], r["question_te"])
            if qh in existing_hashes:
                skipped["questions"] += 1
                continue

            live_ch_id   = src_ch_to_live_ch.get(r["chapter_id"]) if r["chapter_id"] else None
            src_slug     = src_subj_slug.get(r["subject_id"])
            live_subj_id = slug_to_id.get(src_slug)
            if not live_subj_id:
                skipped["questions"] += 1
                continue

            opts_en = r["options_en"] or "{}"
            opts_te = r["options_te"] or "{}"

            q = Question(
                subject_id     = live_subj_id,
                chapter_id     = live_ch_id,
                source_type    = r["source_type"] or "practice",
                difficulty     = r["difficulty"] or "M",
                question_en    = r["question_en"] or "",
                question_te    = r["question_te"] or "",
                options_en     = opts_en,
                options_te     = opts_te,
                correct_answer = r["correct_answer"] or "a",
                explanation_en = r["explanation_en"] or "",
                explanation_te = r["explanation_te"] or "",
                pyq_year       = str(r["pyq_year"]) if r["pyq_year"] else None,
                pyq_paper      = str(r["pyq_paper"]) if r["pyq_paper"] else None,
                created_at     = _now(),
                updated_at     = _now(),
            )
            db.session.add(q)
            existing_hashes.add(qh)
            ins["questions"] += 1

            if ins["questions"] % 500 == 0:
                db.session.flush()
                print(f"    … {ins['questions']} questions flushed")

        db.session.flush()
        print(f"  inserted {ins['questions']}, skipped {skipped['questions']}")

        # ── 5. Commit ─────────────────────────────────────────────
        db.session.commit()
        print()
        print("=== LOAD COMPLETE ===")
        for table, count in ins.items():
            print(f"  {table:10s}  inserted {count:5d}  skipped {skipped[table]:5d}")

        # Final live counts
        print()
        print("Live DB counts after load:")
        print(f"  subjects  : {Subject.query.count()}")
        print(f"  chapters  : {Chapter.query.count()}")
        print(f"  notes     : {Note.query.count()}")
        print(f"  questions : {Question.query.count()}")

    src.close()


if __name__ == "__main__":
    main()
