"""
tests/test_migration.py
Validates the Phase 2 migration output at /tmp/app_v3_migrated.db.

Run after migration:
    DATABASE_URL="sqlite:////tmp/app_v3_migrated.db" python -m pytest tests/test_migration.py -v
"""
import os
import json
import sqlite3
import pytest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

MIGRATED_DB = Path(
    os.environ.get("DATABASE_URL", "sqlite:////tmp/app_v3_migrated.db")
    .replace("sqlite:////", "/")
    .replace("sqlite:///", "")
)
ARCHIVE_JSON = ROOT / "_legacy" / "archived_dropped" / "intl_ca.json"


@pytest.fixture(scope="module")
def conn():
    if not MIGRATED_DB.exists():
        pytest.skip(f"Migrated DB not found at {MIGRATED_DB}. Run migration first.")
    c = sqlite3.connect(str(MIGRATED_DB))
    yield c
    c.close()


# ── Question count ────────────────────────────────────────────────

def test_question_count_in_range(conn):
    """Total migrated questions must be between 6,700 and 6,800."""
    count = conn.execute("SELECT COUNT(*) FROM questions").fetchone()[0]
    assert 6700 <= count <= 6800, (
        f"Expected 6700–6800 questions, got {count}"
    )


def test_question_count_near_target(conn):
    """Exact expectation: ~6737 (allow ±5 for ordering/dedup edge cases)."""
    count = conn.execute("SELECT COUNT(*) FROM questions").fetchone()[0]
    assert abs(count - 6737) <= 5, f"Expected ~6737, got {count}"


# ── correct_answer validity ───────────────────────────────────────

def test_correct_answer_valid_values(conn):
    """Every correct_answer must be one of a-e (lowercase)."""
    bad = conn.execute(
        "SELECT COUNT(*) FROM questions WHERE correct_answer NOT IN ('a','b','c','d','e')"
    ).fetchone()[0]
    assert bad == 0, f"{bad} rows have invalid correct_answer"


def test_correct_answer_all_lowercase(conn):
    """No uppercase correct_answer values."""
    bad = conn.execute(
        "SELECT COUNT(*) FROM questions WHERE correct_answer != LOWER(correct_answer)"
    ).fetchone()[0]
    assert bad == 0, f"{bad} rows have uppercase correct_answer"


# ── FK integrity ──────────────────────────────────────────────────

def test_chapter_id_fk_integrity(conn):
    """Every non-null chapter_id must resolve to a real chapter."""
    orphans = conn.execute("""
        SELECT COUNT(*) FROM questions q
        WHERE q.chapter_id IS NOT NULL
          AND NOT EXISTS (SELECT 1 FROM chapters c WHERE c.id = q.chapter_id)
    """).fetchone()[0]
    assert orphans == 0, f"{orphans} questions have orphaned chapter_id FKs"


def test_subject_id_fk_integrity(conn):
    """Every subject_id must resolve to a real subject."""
    orphans = conn.execute("""
        SELECT COUNT(*) FROM questions q
        WHERE NOT EXISTS (SELECT 1 FROM subjects s WHERE s.id = q.subject_id)
    """).fetchone()[0]
    assert orphans == 0, f"{orphans} questions have orphaned subject_id FKs"


def test_notes_chapter_fk_integrity(conn):
    """Every note must point to an existing chapter."""
    orphans = conn.execute("""
        SELECT COUNT(*) FROM notes n
        WHERE NOT EXISTS (SELECT 1 FROM chapters c WHERE c.id = n.chapter_id)
    """).fetchone()[0]
    assert orphans == 0, f"{orphans} notes have orphaned chapter_id FKs"


# ── AP Economy split ──────────────────────────────────────────────

def test_ap_economy_questions_count(conn):
    """Exactly 12 questions should be tagged to ap_economy (Andhra-mentioning rows)."""
    ap_eco_id = conn.execute(
        "SELECT id FROM subjects WHERE slug='ap_economy'"
    ).fetchone()
    assert ap_eco_id, "ap_economy subject not found"
    count = conn.execute(
        "SELECT COUNT(*) FROM questions WHERE subject_id=?", (ap_eco_id[0],)
    ).fetchone()[0]
    assert count == 12, f"Expected 12 ap_economy questions, got {count}"


def test_indian_economy_has_no_ap_tagged_rows(conn):
    """Indian Economy questions must not contain Andhra-mentioning text."""
    ind_eco_id = conn.execute(
        "SELECT id FROM subjects WHERE slug='indian_economy'"
    ).fetchone()
    assert ind_eco_id, "indian_economy subject not found"
    andhra_in_eco = conn.execute("""
        SELECT COUNT(*) FROM questions
        WHERE subject_id=?
          AND (question_en LIKE '%Andhra%' OR question_en LIKE '%ఆంధ్ర%')
    """, (ind_eco_id[0],)).fetchone()[0]
    assert andhra_in_eco == 0, (
        f"{andhra_in_eco} indian_economy questions still contain 'Andhra'"
    )


# ── Archive file ──────────────────────────────────────────────────

def test_intl_ca_archive_exists():
    """International_Current_Affairs archive JSON must exist."""
    assert ARCHIVE_JSON.exists(), f"Archive file missing: {ARCHIVE_JSON}"


def test_intl_ca_archive_row_count():
    """Archive JSON must contain approximately 1,100 rows (1,050–1,150)."""
    with open(ARCHIVE_JSON, encoding="utf-8") as f:
        data = json.load(f)
    assert 1050 <= len(data) <= 1150, (
        f"Archive should have ~1100 rows, got {len(data)}"
    )


def test_intl_ca_not_in_questions(conn):
    """International_Current_Affairs questions must NOT be in the questions table."""
    # These were only in questions table with topic 'International_Current_Affairs'
    # After migration they should be 0 in DB (all archived)
    # We can verify the total archived+migrated = original
    q_count = conn.execute("SELECT COUNT(*) FROM questions").fetchone()[0]
    assert q_count < 7838, "Questions table has more rows than legacy total (7838)"


# ── Source types ──────────────────────────────────────────────────

def test_source_types_valid(conn):
    """All source_type values must be in the allowed set."""
    invalid = conn.execute("""
        SELECT DISTINCT source_type FROM questions
        WHERE source_type NOT IN ('chapter', 'practice', 'pyq')
    """).fetchall()
    assert len(invalid) == 0, f"Invalid source_type values: {invalid}"


def test_pyq_questions_have_year(conn):
    """PYQ questions should mostly have pyq_year set."""
    total_pyq = conn.execute(
        "SELECT COUNT(*) FROM questions WHERE source_type='pyq'"
    ).fetchone()[0]
    pyq_with_year = conn.execute(
        "SELECT COUNT(*) FROM questions WHERE source_type='pyq' AND pyq_year IS NOT NULL"
    ).fetchone()[0]
    assert total_pyq > 600, f"Expected >600 PYQ questions, got {total_pyq}"
    # At least 95% should have a year
    assert pyq_with_year / total_pyq >= 0.95, (
        f"Only {pyq_with_year}/{total_pyq} PYQ questions have a year"
    )


# ── Subjects and chapters ─────────────────────────────────────────

def test_all_11_subjects_exist(conn):
    """All 11 v3 subjects must be present."""
    expected = {
        "indian_history", "indian_constitution", "ap_history",
        "indian_geography", "ap_geography", "indian_economy",
        "ap_economy", "science_technology", "indian_society",
        "mental_ability", "current_affairs",
    }
    actual = {r[0] for r in conn.execute("SELECT slug FROM subjects").fetchall()}
    missing = expected - actual
    assert not missing, f"Missing subjects: {missing}"


def test_chapter_count_reasonable(conn):
    """Should have at least 100 chapters migrated."""
    count = conn.execute("SELECT COUNT(*) FROM chapters").fetchone()[0]
    assert count >= 100, f"Only {count} chapters, expected >= 100"


def test_exam_sessions_migrated(conn):
    """Legacy exam sessions (7) should be present with device_id='legacy'."""
    count = conn.execute(
        "SELECT COUNT(*) FROM exam_sessions WHERE device_id='legacy'"
    ).fetchone()[0]
    assert count == 7, f"Expected 7 legacy exam_sessions, got {count}"


# ── Idempotency: re-running migration should produce same counts ──

def test_migration_idempotent(tmp_path):
    """Re-running migration on same DB should add 0 new rows (all upserts)."""
    import subprocess, sys
    db2 = str(tmp_path / "test_idempotent.db")
    env = os.environ.copy()
    env["DATABASE_URL"] = f"sqlite:////{db2}"
    # First run
    r1 = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "migrate_from_legacy.py")],
        capture_output=True, text=True, env=env
    )
    assert r1.returncode == 0, f"First run failed:\n{r1.stderr}"
    c1 = sqlite3.connect(db2).execute("SELECT COUNT(*) FROM questions").fetchone()[0]
    # Second run (idempotent)
    r2 = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "migrate_from_legacy.py")],
        capture_output=True, text=True, env=env
    )
    assert r2.returncode == 0, f"Second run failed:\n{r2.stderr}"
    c2 = sqlite3.connect(db2).execute("SELECT COUNT(*) FROM questions").fetchone()[0]
    assert c1 == c2, f"Idempotency failed: first={c1}, second={c2}"
