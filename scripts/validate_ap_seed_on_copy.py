"""Validate the canonical hierarchy seed on a DISPOSABLE copy of the bundled content database.

    python scripts/validate_ap_seed_on_copy.py [--report docs/ap_history_seed_validation_report.md]

Decompresses data/content.db.gz into a temporary directory (never a user path, never staging or production), runs the Alembic
migrations on the copy, seeds units/chapters/supplementary chapters and the ap-history-taxonomy-v1 subtopics + microtopics, and checks
counts, idempotence and that every pre-existing table and column is byte-for-byte unchanged. The copy is deleted afterwards.
"""
import argparse
import gzip
import hashlib
import os
import shutil
import sqlite3
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

LEGACY_COLS = {
    "subjects": "id,slug,name_en,name_te,sort_order",
    "chapters": "id,subject_id,chapter_num,title_en,title_te,est_read_minutes",
    "notes": "id,chapter_id,section_num,heading_en,heading_te,body_en,body_te",
    "questions": "id,subject_id,chapter_id,source_type,q_hash,pyq_year,pyq_paper,difficulty,question_en,question_te,options_en,options_te,"
                 "correct_answer,explanation_en,explanation_te,passage_id",
}


def snapshot(db):
    con = sqlite3.connect(db)
    try:
        hashes = {t: hashlib.md5(repr(con.execute(f"SELECT {c} FROM {t} ORDER BY id").fetchall()).encode()).hexdigest() for t, c in LEGACY_COLS.items()}
        counts = {t: con.execute(f"SELECT COUNT(*) FROM {t}").fetchone()[0] for t in LEGACY_COLS}
        ap = con.execute("SELECT COUNT(*) FROM questions q JOIN subjects s ON s.id=q.subject_id WHERE s.slug='ap_history'").fetchone()[0]
        return hashes, counts, ap
    finally:
        con.close()


def run():
    tmpdir = Path(tempfile.mkdtemp(prefix="ap_seed_validation_"))
    db = tmpdir / "content_copy.db"
    try:
        with gzip.open(ROOT / "data" / "content.db.gz", "rb") as src, open(db, "wb") as dst:
            shutil.copyfileobj(src, dst)
        before = snapshot(db)
        os.environ["ALEMBIC_DATABASE_URL"] = f"sqlite:///{db}"
        from alembic import command
        from alembic.config import Config as AlembicConfig
        cfg = AlembicConfig(str(ROOT / "alembic.ini")); cfg.set_main_option("script_location", str(ROOT / "migrations"))
        command.upgrade(cfg, "head")
        command.check(cfg)
        from app import create_app
        from app.config import Config as AppConfig

        class Disposable(AppConfig):
            SQLALCHEMY_DATABASE_URI = f"sqlite:///{db}"
        app = create_app(Disposable)
        with app.app_context():
            from app.services import ap_canonical as k
            first = k.seed()
            tax_first = k.seed_taxonomy()
            second = k.seed()
            tax_second = k.seed_taxonomy()
        after = snapshot(db)
        con = sqlite3.connect(db)
        q = lambda sql: con.execute(sql).fetchone()[0]  # noqa: E731
        res = {
            "before": before, "after": after, "seed_first": first, "taxonomy_first": tax_first, "seed_second": second, "taxonomy_second": tax_second,
            "units": q("SELECT COUNT(*) FROM syllabus_units"),
            "core_chapters": q("SELECT COUNT(*) FROM syllabus_chapters WHERE classification<>'supplementary'"),
            "supplementary_chapters": q("SELECT COUNT(*) FROM syllabus_chapters WHERE classification='supplementary'"),
            "subtopics": q("SELECT COUNT(*) FROM syllabus_subtopics"), "microtopics": q("SELECT COUNT(*) FROM syllabus_microtopics"),
            "subtopics_on_supplementary": q("SELECT COUNT(*) FROM syllabus_subtopics s JOIN syllabus_chapters c ON c.id=s.chapter_id WHERE c.classification='supplementary'"),
            "questions_with_provenance": q("SELECT COUNT(*) FROM questions WHERE source IS NOT NULL OR syllabus_chapter_id IS NOT NULL OR subtopic_id IS NOT NULL"),
            "source_map_rows": q("SELECT COUNT(*) FROM chapter_source_map"),
            "taxonomy_versions": [r[0] for r in con.execute("SELECT DISTINCT taxonomy_version FROM syllabus_subtopics")],
            "legacy_identical": before == after,
        }
        con.close()
        ok = (res["legacy_identical"] and res["units"] == 5 and res["core_chapters"] == 31 and res["supplementary_chapters"] == 4
              and res["subtopics"] == 187 and res["microtopics"] == 317 and res["subtopics_on_supplementary"] == 0
              and res["questions_with_provenance"] == 0 and res["source_map_rows"] == 0
              and sum(res["seed_second"][k] for k in ("units_added", "chapters_added", "supplementary_added")) == 0
              and tax_second["subtopics_added"] == 0 and tax_second["microtopics_added"] == 0)
        res["ok"] = ok
        return res
    finally:
        shutil.rmtree(tmpdir, ignore_errors=True)


def render(r):
    b, a = r["before"], r["after"]
    return "\n".join([
        "# AP History seed validation on a disposable copy", "",
        "Run by `scripts/validate_ap_seed_on_copy.py`. The copy is decompressed from `data/content.db.gz` into a temporary directory and deleted afterwards. "
        "Nothing was seeded into staging, production or any real database.", "",
        f"- Result: **{'PASS' if r['ok'] else 'FAIL'}**",
        f"- Units / core chapters / supplementary chapters: {r['units']} / {r['core_chapters']} / {r['supplementary_chapters']}",
        f"- Learner-facing subtopics / microtopics: {r['subtopics']} / {r['microtopics']} (taxonomy version(s): {', '.join(r['taxonomy_versions'])})",
        f"- Subtopics attached to supplementary chapters: {r['subtopics_on_supplementary']}",
        f"- First run added: {r['seed_first']} and {r['taxonomy_first']}",
        f"- Second run added: {r['seed_second']} and {r['taxonomy_second']} (idempotent)",
        f"- Legacy tables before and after (subjects, chapters, notes, questions) identical, column by column: **{r['legacy_identical']}**",
        f"- Row counts before: {b[1]}; after: {a[1]}; AP History questions before/after: {b[2]}/{a[2]}",
        f"- Questions carrying provenance or canonical mapping after seeding: {r['questions_with_provenance']}",
        f"- chapter_source_map rows (mapping is not seeded): {r['source_map_rows']}", ""])


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--report", help="write a markdown report here")
    args = ap.parse_args()
    res = run()
    text = render(res)
    print(text)
    if args.report:
        Path(args.report).write_text(text, encoding="utf-8")
    sys.exit(0 if res["ok"] else 1)
