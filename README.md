# APPSC Prep — v3 rebuild

Bilingual (Telugu + English) MCQ app for APPSC and AP High Court exam preparation. Rebuilt from scratch per `REBUILD_PLAN_v3.md` and design spec v6.

## Quick start

```bash
# create virtual env (optional but recommended)
python -m venv .venv && source .venv/bin/activate

# install
pip install -r requirements.txt

# create the DB (sqlite for local dev)
alembic upgrade head

# run tests
pytest

# boot the app
python wsgi.py
# → http://localhost:5000
```

## Structure

```
app/
├── __init__.py        # Flask factory
├── config.py          # env-driven config
├── db.py              # SQLAlchemy instance
├── models.py          # 15 models (subjects, exams, study plans, etc.)
├── routes/
│   └── public.py      # home + healthz (Phase 0)
└── templates/
    ├── base.html      # app shell
    └── home.html      # minimal landing
static/
├── app.css            # single stylesheet, CSS vars for theming
└── app.js             # vanilla JS, no framework
tests/
├── conftest.py        # pytest fixtures (in-memory SQLite)
└── test_smoke.py      # Phase 0 smoke + schema tests
migrations/            # Alembic
_legacy/               # snapshot of pre-rebuild content (migration source)
content/               # YAML seed files (Phase 5+)
scripts/               # one-off migration & seed scripts (Phase 2)
```

## Phases

| Phase | What | Status |
|---|---|---|
| 0 | Scaffold | ← here |
| 1 | Core read flow (nav, home, practice, question card) | next |
| 2 | Migration from `_legacy/` (database.db + HTML notes) | |
| 3 | Admin CMS (minimal: paste-HTML + save) | |
| 4 | Notes display | |
| 4.5 | Study plans + chapter progress | |
| 5 | Exam syllabus seed (APPSC Group 2) + exam taking | |
| 6 | Review + state (wrong / flagged / saved / confidence) | |
| 7 | Cutover + polish | |
| 8 | Content gap fill (parallel, ongoing) | |

## Recovery

```bash
# restore pre-rebuild state
git checkout pre-rebuild-snapshot
```

All migration-source content also lives under `_legacy/` for direct read access during Phase 2.
