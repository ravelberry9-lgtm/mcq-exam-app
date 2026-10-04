"""Load a slice of the REAL shipped content (data/content.db[.gz]) into the test database.

Used by the regression tests for the exam / practice / Learn-bank fixes so they run against the actual shape of the data
(e.g. chapter questions that have Telugu options only) instead of hand-made rows. The slice is copied into an in-memory
SQLite source and imported with the production importer, so the importer is exercised too.
"""
import sqlite3

from app.db import db
from app.services import content_import as ci

TABLES = ("subjects", "chapters", "notes", "questions")


def real_slice(slugs, chapters_per_subject=3, bank_per_type=40):
    """Import ``slugs`` from the real source: the first chapters (with chapter-type questions when a subject has some),
    their notes and questions, plus up to ``bank_per_type`` practice and PYQ questions per subject."""
    with ci.open_source() as real:
        mem = sqlite3.connect(":memory:")
        mem.row_factory = sqlite3.Row
        for name in TABLES:
            mem.execute(real.execute("SELECT sql FROM sqlite_master WHERE type='table' AND name=?", (name,)).fetchone()[0])

        def copy(table, rows):
            rows = list(rows)
            if rows:
                cols = rows[0].keys()
                mem.executemany(f"INSERT INTO {table} ({','.join(cols)}) VALUES ({','.join('?' * len(cols))})", [tuple(r) for r in rows])

        for slug in slugs:
            s = real.execute("SELECT * FROM subjects WHERE slug=?", (slug,)).fetchone()
            copy("subjects", [s])
            chs = list(real.execute(
                "SELECT c.* FROM chapters c WHERE c.subject_id=? ORDER BY (SELECT COUNT(*) FROM questions q WHERE q.chapter_id=c.id) DESC, c.chapter_num LIMIT ?",
                (s["id"], chapters_per_subject)))
            copy("chapters", chs)
            ids = [c["id"] for c in chs]
            if ids:
                marks = ",".join("?" * len(ids))
                copy("notes", real.execute(f"SELECT * FROM notes WHERE chapter_id IN ({marks})", ids))
                copy("questions", real.execute(f"SELECT * FROM questions WHERE chapter_id IN ({marks}) AND source_type='chapter'", ids))
            for kind in ("pyq", "practice"):
                copy("questions", real.execute(
                    "SELECT * FROM questions WHERE subject_id=? AND chapter_id IS NULL AND source_type=? ORDER BY id LIMIT ?",
                    (s["id"], kind, bank_per_type)))
        mem.commit()
        src = ci.Source(mem, "test-slice")
        try:
            plan = ci.build_plan(src)
            ci.apply_import(src, list(slugs), plan["fingerprints"])
        finally:
            src.close()
