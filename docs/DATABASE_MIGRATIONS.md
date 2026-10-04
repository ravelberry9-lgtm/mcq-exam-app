# Database migrations

Alembic is the **only** thing that changes the database schema. The application never creates
tables or alters columns at startup (`create_all()` and `_patch_schema()` were removed).

## Deploy / upgrade

    python -m alembic upgrade head          # idempotent; safe to run on every deploy

On Railway set this as the **Pre-deploy command**, so the new code never starts against an old schema.
`python -m alembic current` shows the revision a database is on.

## Which databases this handles

| Database | What `upgrade head` does |
|---|---|
| Empty | Creates all 15 tables (baseline `c68decc8a6c3`) |
| Created by Alembic earlier | Applies only the newer revisions |
| Legacy, no `alembic_version` (older app, `create_all`, `content.db`) | Baseline creates only the **missing** tables and indexes and leaves existing ones and all rows alone; `a1b2c3d4e5f6` adds `questions.subject_id` if absent |

`questions.subject_id` when added to a legacy table: chapter questions are backfilled from their chapter;
rows without a chapter stay `NULL` (nothing is guessed) and the column stays nullable until they are assigned.

## Changing the schema later

1. Edit `app/models.py`.
2. `python -m alembic revision --autogenerate -m "what changed"`, read the file, adjust.
3. `python -m alembic upgrade head` locally; `python -m alembic check` must report no drift.
4. `tests/test_alembic.py` runs a fresh upgrade + drift check, a legacy upgrade with data, idempotence and downgrade.

## Verified (2026-10-04)

* SQLite and PostgreSQL 16: fresh upgrade, second upgrade is a no-op, `alembic check` clean.
* Copies of the real content database (6,737 questions, 194 chapters, 980 notes) upgraded on SQLite and
  on PostgreSQL with identical row counts afterwards.
* Not verified: the live Railway database. Run `python -m alembic current` there before the first deploy; if it
  prints nothing the DB is "legacy" and `upgrade head` will adopt it as described above. Take a backup first.

`ALEMBIC_DATABASE_URL` overrides the database for one command (used by tests); otherwise `DATABASE_URL` is used.
