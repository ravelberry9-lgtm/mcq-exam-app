# MCQ App — Rebuild Plan v1

**Date:** 26 May 2026
**Goal:** Rebuild the APPSC / AP High Court exam prep app from scratch with effective storage, a simple unified design, and a maintainable codebase. Preserve all existing content via clean migration.

---

## 1. Why a rebuild (the diagnosis)

The current app is functional but has accumulated structural debt that makes every bug expensive and every new feature risky.

**Code rot.** `app.py` is a single 7,890-line file containing ~150 Flask routes. Of those, roughly 100 are one-off `/api/mcq/seed_chN` and `/api/notes/seed_chN` endpoints with chapter content hardcoded as Python literals. The repo folder has 459 files — most are one-off migration scripts (`ADD_BATCH11_*.py`, `HAIKU_OUTPUT_*.py`, dozens of `apply_*` and `convert_*` scripts) that have served their purpose and should be archived.

**Data fragmentation.** There are **three separate question tables**, each with a different schema:
- `questions` (3,495 rows) — English-only, used for AP_HC / GK / Mental_Ability / National_CA
- `chapter_mcqs` (3,682 rows) — Telugu-only (`q_te`, `explanation_te`), linked to `study_notes`
- `pyq_questions` (661 rows) — previous-year questions with a `language` column

This means "show me a bilingual question with explanation" is impossible to answer with a single query. Bugs in the exam/practice flow trace back to this — code has to branch on which table the question came from.

**Brittle dual-backend adapter.** `db_exec()` hand-rewrites SQL between SQLite and Postgres (`?` → `%s`, `INSERT OR IGNORE` → `INSERT ... ON CONFLICT DO NOTHING`). It works for the routes that exist, but every new query is a chance to break it. This is the root cause of several reported runtime errors.

**Slow.** Single gunicorn worker, no DB indexes on `folder`/`topic`/`study_note_id`/`device_id`, queries that fetch full question rows just to count them, JSON blobs (`sections_json`) that get parsed on every notes page load. Railway cold starts compound this.

**Hard to add content.** Adding a chapter today means: write a Python function with the notes content as a literal, register a new `/api/notes/seed_chN_xx` route, deploy, hit the endpoint once. There's no admin UI for content creation that actually works end-to-end.

---

## 2. What we keep

- All ~7,800 MCQs across the three current tables → merged into one `questions` table.
- All 42 study notes chapters → migrated into a normalized `notes` + `sections` schema.
- All 661 PYQs → folded into the same `questions` table with `source_type = 'pyq'`.
- Exam history (7 `exam_sessions` rows) → migrated as-is so your wrong-answers history survives.
- Bilingual Telugu + English everywhere (this is non-negotiable per your answer).
- Railway deployment URL stays the same so bookmarks keep working.

## 3. What we drop

- All `/api/mcq/seed_chN_*` and `/api/notes/seed_chN_*` endpoints. Content moves to data files, not code.
- All `/api/.../force-reseed` and `/api/.../archive-and-delete` one-off routes.
- The `__pycache__` and 400+ migration scripts at the repo root — archived to a separate folder.
- The dual-backend SQL adapter (replaced — see §4).
- Three-table question model — collapsed to one.

---

## 4. New architecture

### 4.1 Stack

| Layer | Choice | Why |
|---|---|---|
| Web framework | **Flask** (kept) | Already works, you know it, no migration tax |
| ORM | **SQLAlchemy 2.x** | Kills the hand-rolled SQL adapter; one model definition works on SQLite and Postgres |
| Migrations | **Alembic** | Schema changes become reviewable diffs instead of seed routes |
| Templates | **Jinja2** (kept) + **HTMX** for interactivity | No React build step; HTMX gives snappy partial updates for quiz flow |
| CSS | **Single `app.css` file** with CSS variables for theming | No Tailwind build, no framework — just clean utility classes you control |
| Storage (prod) | **Postgres on Railway** (same URL) | Keeps your deployment; SQLAlchemy makes it transparent |
| Storage (dev) | **SQLite** file | Identical model code |
| Hosting | **Railway** (same project) | No bookmark churn |
| Server | **Gunicorn** with 2 workers + `--preload` | Faster cold starts, handles concurrent practice sessions |

### 4.2 New database schema (unified)

Six tables instead of seven, with proper indexes and a single source of truth for MCQs.

```sql
-- One row per study area. Replaces ad-hoc folder/topic strings.
CREATE TABLE subjects (
  id          SERIAL PRIMARY KEY,
  slug        TEXT UNIQUE NOT NULL,      -- 'indian_polity', 'ap_current_affairs'
  name_en     TEXT NOT NULL,
  name_te     TEXT NOT NULL,
  exam_scope  TEXT NOT NULL,             -- 'APPSC' | 'AP_HC' | 'BOTH'
  sort_order  INTEGER DEFAULT 0
);

-- Optional grouping inside a subject (e.g. "Ancient History" chapter).
CREATE TABLE chapters (
  id          SERIAL PRIMARY KEY,
  subject_id  INTEGER NOT NULL REFERENCES subjects(id) ON DELETE CASCADE,
  chapter_num INTEGER NOT NULL,
  title_en    TEXT NOT NULL,
  title_te    TEXT NOT NULL,
  UNIQUE(subject_id, chapter_num)
);

-- THE ONE QUESTIONS TABLE. Replaces questions + chapter_mcqs + pyq_questions.
CREATE TABLE questions (
  id              SERIAL PRIMARY KEY,
  subject_id      INTEGER NOT NULL REFERENCES subjects(id),
  chapter_id      INTEGER REFERENCES chapters(id),       -- NULL for non-chapter MCQs
  source_type     TEXT NOT NULL,                          -- 'practice' | 'chapter' | 'pyq'
  pyq_year        TEXT,                                   -- only for source_type='pyq'
  pyq_paper       TEXT,
  difficulty      TEXT DEFAULT 'M',                       -- E/M/H
  question_en     TEXT,
  question_te     TEXT,
  options_en      JSONB,                                  -- {"a":"...", "b":"...", ...}
  options_te      JSONB,
  correct_answer  CHAR(1) NOT NULL,                       -- 'a'..'e' lowercase
  explanation_en  TEXT,
  explanation_te  TEXT,
  passage_id      INTEGER REFERENCES passages(id),        -- for reading-comp groups
  created_at      TIMESTAMP DEFAULT now(),
  updated_at      TIMESTAMP DEFAULT now()
);
CREATE INDEX ix_q_subject ON questions(subject_id);
CREATE INDEX ix_q_chapter ON questions(chapter_id);
CREATE INDEX ix_q_source ON questions(source_type);

-- Reading-comp / case-study shared passages.
CREATE TABLE passages (
  id        SERIAL PRIMARY KEY,
  text_en   TEXT,
  text_te   TEXT
);

-- Notes as proper sections instead of JSON blob.
CREATE TABLE notes (
  id          SERIAL PRIMARY KEY,
  chapter_id  INTEGER NOT NULL REFERENCES chapters(id) ON DELETE CASCADE,
  section_num INTEGER NOT NULL,
  heading_en  TEXT,
  heading_te  TEXT,
  body_en     TEXT,           -- markdown
  body_te     TEXT,           -- markdown
  UNIQUE(chapter_id, section_num)
);

-- Per-device state. Single table for seen + wrong + flagged.
CREATE TABLE user_question_state (
  device_id    TEXT NOT NULL,
  question_id  INTEGER NOT NULL REFERENCES questions(id) ON DELETE CASCADE,
  seen_count   INTEGER DEFAULT 0,
  wrong_count  INTEGER DEFAULT 0,
  flagged      BOOLEAN DEFAULT false,
  last_seen_at TIMESTAMP,
  PRIMARY KEY (device_id, question_id)
);
CREATE INDEX ix_uqs_device ON user_question_state(device_id);
CREATE INDEX ix_uqs_flagged ON user_question_state(device_id) WHERE flagged = true;

-- Exam attempts.
CREATE TABLE exam_sessions (
  id            UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  device_id     TEXT NOT NULL,
  config        JSONB NOT NULL,   -- subjects, count, mode, lang, time_limit
  question_ids  JSONB NOT NULL,   -- ordered list
  answers       JSONB DEFAULT '{}',
  started_at    TIMESTAMP DEFAULT now(),
  submitted_at  TIMESTAMP,
  score         INTEGER,
  total         INTEGER
);
CREATE INDEX ix_es_device ON exam_sessions(device_id, started_at DESC);
```

**Key wins of this schema.** Single `questions` table means one query path for every MCQ feature — exam, practice, PYQ, chapter MCQs, wrong-answer review. Bilingual fields are first-class (`*_en` and `*_te` side-by-side, not split across tables). Per-device state collapses three old concerns (seen / wrong / flagged) into one row. JSONB option storage means adding a 5th option (`e`) is data, not a schema change.

### 4.3 Repo layout

```
mcq_app/
├── app/
│   ├── __init__.py          # create_app() factory
│   ├── models.py            # SQLAlchemy models (one file, ~200 lines)
│   ├── db.py                # engine, session, helpers
│   ├── config.py            # env-driven config
│   ├── routes/
│   │   ├── home.py          # landing, dashboard
│   │   ├── exam.py          # start / take / submit exam
│   │   ├── practice.py      # subject practice mode
│   │   ├── notes.py         # browse notes
│   │   ├── review.py        # wrong answers, flagged, history
│   │   ├── admin.py         # content CRUD (PIN-gated)
│   │   └── api.py           # JSON endpoints for HTMX
│   ├── services/
│   │   ├── question_picker.py   # exam composition logic
│   │   ├── scoring.py
│   │   └── importer.py          # YAML/JSON → DB
│   └── templates/
│       ├── base.html
│       ├── _macros.html         # shared question card, option, etc.
│       ├── home.html
│       ├── exam.html
│       ├── practice.html
│       ├── notes/...
│       └── admin/...
├── static/
│   ├── app.css              # one stylesheet, CSS variables, ~400 lines
│   ├── app.js               # HTMX helpers + ~100 lines vanilla
│   └── icons/
├── content/                 # SOURCE OF TRUTH for seed content (YAML)
│   ├── subjects.yml
│   ├── indian_polity/
│   │   ├── ch01_constitution.notes.yml
│   │   └── ch01_constitution.mcqs.yml
│   └── ...
├── migrations/              # Alembic
├── tests/
│   ├── test_models.py
│   ├── test_exam_flow.py
│   └── test_importer.py
├── scripts/
│   ├── migrate_from_old_db.py   # one-time: old → new schema
│   └── import_content.py        # YAML → DB
├── _archive/                # 400+ old one-off scripts moved here
├── requirements.txt
├── Procfile
├── alembic.ini
└── README.md
```

`app.py` shrinks from 7,890 lines to a 5-line entrypoint that calls `create_app()`. Every route file is under 300 lines. Content lives in YAML — adding a chapter is `cp template.yml content/.../chN.mcqs.yml`, edit, then `python scripts/import_content.py`. No more seed routes.

### 4.4 UI redesign

Three guiding principles: **one column**, **one action per screen**, **identical question card everywhere**.

**Layout.** Single column, max-width 720px, centered. Sticky header with: app title, language toggle (TE/EN/Both), and a back arrow. That's it. No sidebar, no nested menus.

**Home screen.** Four big cards stacked vertically:
1. Continue last exam (if any in-progress)
2. Start new exam → wizard
3. Practice by subject → subject grid
4. Review (wrong answers, flagged, history)

Below the cards: a single "Notes" section with subjects as collapsible accordions.

**Question card** (the most-used component, identical in exam / practice / review / PYQ):
- Subject badge + chapter number (top-left)
- Difficulty pill (top-right)
- Question text — Telugu on top, English below (or single language if toggle is set)
- Four/five options as full-width tap targets
- After answer: green/red feedback, explanation in both languages, "Flag" and "Next" buttons

**Exam wizard** (replaces today's `setup.html` complexity): three steps.
1. Pick subjects (multi-select chips)
2. Pick count (20 / 50 / 100 / custom) and mode (timed / untimed)
3. Confirm and start

**Admin / content.** A real CRUD UI: list questions for a subject, edit in place, add new with a form that validates both Telugu and English are filled. PIN gate stays. Bulk import: drop a YAML file, see a diff preview, confirm.

**Visual style.**
- System font stack (`-apple-system, ...`) — fast, native feel
- One accent color (e.g. APPSC blue `#1e40af`), one neutral palette
- Dark mode via `prefers-color-scheme`, no toggle
- Generous spacing — Telugu script needs vertical room
- Mobile-first, 16px minimum body text, 18px+ for question text

### 4.5 Speed fixes baked in

- DB indexes on every foreign key and every filter column.
- `EXPLAIN ANALYZE` on the three hottest queries (exam start, practice load, history list) — added to the test suite as regression guards.
- HTMX partial swaps for "next question" instead of full page reloads.
- Static assets cached with hashed filenames.
- Gunicorn `--preload` so the question picker is loaded once at boot, not per worker per request.
- The 200KB+ `app.db` SQLite file removed from the repo (it'll be regenerated from YAML on `flask db upgrade && python scripts/import_content.py`).

---

## 5. Migration plan (old → new)

This is the riskiest step. Strategy: build the new app on a parallel branch, dump the old DB once, write a single migration script, verify counts and spot-check 50 random questions, then cut over.

| Step | Action | Verification |
|---|---|---|
| 1 | Snapshot current production Postgres (`pg_dump` from Railway) | Backup file in `_archive/db_snapshots/` |
| 2 | Snapshot local `database.db` (3,495 + 3,682 + 661 MCQs, 42 notes, 7 sessions) | Already have it |
| 3 | Build new schema in parallel Railway DB (new service) | `alembic upgrade head` clean run |
| 4 | Write `scripts/migrate_from_old_db.py` | Idempotent, prints counts before/after |
| 5 | Map old → new:<br>• `questions` → `questions` (source_type='practice')<br>• `chapter_mcqs` → `questions` (source_type='chapter', linked via `study_note_id`→new chapter_id)<br>• `pyq_questions` → `questions` (source_type='pyq')<br>• `study_notes.sections_json` → unpacked into `notes` rows<br>• `exam_sessions` → `exam_sessions` with new UUID keys<br>• `seen_questions` → `user_question_state.seen_count` | Row count assertions, sampling test |
| 6 | Run a parity test: for 50 random old question IDs, render the question on old app and new app side-by-side | Manual eyeball |
| 7 | Point Railway service env vars at new code, keep old DB readable for 30 days | Same URL, no bookmark break |
| 8 | After 30 days clean: drop old tables | Done |

**Bilingual pairing during migration.** Today, `questions.question_text` (English) and `chapter_mcqs.q_te` (Telugu) are not paired by row. The migration script will:
1. Move each row as-is into the new table with whichever language it has.
2. Flag rows missing the other language in a `questions_needing_translation` view.
3. We then fill the gaps in a second pass (manual or AI-assisted) using the `admin` UI.

This means day-1 of the new app may have some Telugu-only or English-only questions until the translation pass completes. Acceptable trade-off vs. blocking the rebuild.

---

## 6. Phased delivery

| Phase | Scope | Output | Est. effort |
|---|---|---|---|
| **0. Greenfield setup** | Repo scaffold, models, alembic baseline, CI lint | App boots locally, shows "Hello" | 0.5 day |
| **1. Core read flow** | Home, subjects list, practice mode, question card | You can do practice MCQs on new app pointing at OLD db via a read-only adapter | 1 day |
| **2. Migration script** | Old → new schema, full data move into a new Postgres DB | New DB has all 7,800+ questions, parity test passes | 1 day |
| **3. Exam + scoring** | Wizard, exam taking, submit, result, history | Full exam cycle works end-to-end | 1 day |
| **4. Notes** | Subject → chapter → section render, search | Notes browsable, equivalent to today | 0.5 day |
| **5. Review & state** | Wrong answers, flagged, seen tracking | Review tab fully functional | 0.5 day |
| **6. Admin UI** | CRUD for questions/notes, YAML import, PIN gate | You can add a new chapter without touching code | 1 day |
| **7. Polish + cutover** | Dark mode, mobile QA, perf pass, Railway cutover | Same URL serves new app; old code archived | 0.5 day |

**Total: ~6 dev days.** Phases 1–2 are the riskiest; everything after is incremental.

---

## 7. What I need from you to start Phase 0

1. **Hosting choice** — you skipped this earlier. Recommend keeping Railway + Postgres for zero bookmark break. Confirm or pick differently.
2. **Confirm the schema in §4.2** — especially: are 5 options (`e`) ever needed, or always 4? Is reading-comp/passage grouping actually used?
3. **Confirm phased delivery order** — or tell me which phase you'd rather do first (e.g. UI redesign before migration, so you can see it).
4. **Admin PIN** — keep current `1234`, or change?

Once those four are settled, I'll start Phase 0 in a new branch under the same repo. Every phase ends with something you can click on — no big-bang reveal.
