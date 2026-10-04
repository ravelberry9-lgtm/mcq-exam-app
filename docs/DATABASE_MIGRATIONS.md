# Database migrations

Alembic is the **only** thing that changes the database schema. The application never creates
tables or alters columns at startup (`create_all()` and `_patch_schema()` were removed; a test enforces it).

## Deploy / upgrade

    python -m alembic upgrade head          # idempotent; safe to run on every deploy
    python -m alembic current               # which revision a database is on
    python -m alembic check                 # must print "No new upgrade operations detected"

On Railway set the upgrade as the **Pre-deploy command**, so new code never starts against an old schema.
Take a database backup before the first run against any existing database.

## Revisions

| Revision | What it does |
|---|---|
| `c68decc8a6c3` baseline | Creates the 15 tables. **Idempotent**: tables and indexes that already exist are left untouched, so a database created before Alembic is *adopted*, not overwritten. |
| `a1b2c3d4e5f6` | Adds `questions.subject_id` if missing (replaces `_patch_schema`). Chapter questions inherit their chapter's subject. **Never guesses**: if any question still has no subject the upgrade stops with a message (see below). |
| `b2c3d4e5f6a7` | Converges legacy schemas onto the models: keeps `questions.q_hash` (md5 fingerprint, now declared on the model), rebuilds legacy SQLite tables in place (NOT NULL keys, `ON DELETE CASCADE`, `passage_id` FK, declared types; rows copied verbatim), renames legacy `idx_q_*` indexes to `ix_questions_*`. No-op on a correct schema. |

## Decisions worth knowing

* **Downgrade never deletes data.** The baseline cannot tell tables it created from tables you already had, so
  `downgrade` below the baseline *refuses* to drop any table that contains rows (it lists them and changes nothing).
  Empty databases downgrade normally. To really remove populated tables, restore a backup or drop them by hand.
* **`questions.subject_id` is required (NOT NULL).** A legacy database that lacks the column and holds questions with
  no chapter cannot be adopted automatically. The upgrade stops with the count; assign them yourself, e.g.
  `UPDATE questions SET subject_id = (SELECT id FROM subjects WHERE slug='...') WHERE subject_id IS NULL;`
  then re-run. PostgreSQL rolls the failed attempt back; SQLite keeps only the harmless nullable column.
* **`q_hash` is kept**, not dropped: it holds 6,737 fingerprints in the real content database.
* **SQLite type affinity** (VARCHAR vs TEXT, JSON/DateTime/Boolean vs TEXT/INTEGER) is ignored by `alembic check`
  on SQLite only; PostgreSQL comparison is strict.

## Verified (2026-10-04)

| Check | SQLite | PostgreSQL 16 |
|---|---|---|
| Fresh upgrade, 2nd upgrade no-op, `alembic check` clean | yes | yes |
| Legacy (pre-Alembic) database adopted, **`alembic check` clean afterwards** | yes (real `content.db` copy and test fixtures) | yes (older-release shape: no `subject_id`/`q_hash`, no `alembic_version`) |
| Every row identical before/after legacy upgrade | yes (all 6 legacy tables of the real copy; `foreign_key_check` and `integrity_check` clean) | yes (row counts, `subject_id` backfilled, NOT NULL applied) |
| Downgrade refuses to drop populated tables | yes | yes |
| Orphan questions stop the upgrade, then succeed once assigned | yes | (same code path) |

Run the PostgreSQL checks yourself against an **empty scratch database**:
`TEST_PG_URL=postgresql+psycopg2://user:pw@host/scratch python -m pytest tests/test_alembic.py`
(the test wipes the `public` schema of that database first).

**Not covered:** a PostgreSQL database whose tables were hand-created with the old SQLite column types
(TEXT instead of VARCHAR, no cascades). It upgrades without losing data but `alembic check` will still list
those type/constraint differences. And the live Railway database itself has not been touched: run
`python -m alembic current` and `check` there after a backup.

`ALEMBIC_DATABASE_URL` overrides the database for one command (used by tests); otherwise `DATABASE_URL` is used.
