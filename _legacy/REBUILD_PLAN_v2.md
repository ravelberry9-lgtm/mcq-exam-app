# MCQ App — Rebuild Plan v2

**Date:** 26 May 2026 · supersedes v1
**Changes from v1:** Current-affairs content dropped (–2,000 MCQs); admin becomes a full CMS that controls navigation, home tiles, dropdowns, and styling; 12 issues from v1 review resolved.

---

## 1. Content scope (what survives)

Dropped: `AP_Current_Affairs_2026` (200), `International_Current_Affairs` (1,100), `Indian_Economy` (700). **2,000 MCQs archived, not migrated.**

| Bucket | Source table | Count kept |
|---|---|---|
| AP_HC Everyday Science | `questions` | 500 |
| GK Art & Culture | `questions` | 344 |
| GK General Science | `questions` | 600 |
| Mental Ability (Seating/Puzzles) | `questions` | 50 |
| Indian Polity / History / etc. chapter MCQs | `chapter_mcqs` | 3,682 |
| Previous Year Questions (Art & Culture etc.) | `pyq_questions` | 661 |
| **Total migrated** | | **≈ 5,837** |
| Notes (Polity, Geography, History, AP CA) | `study_notes` + HTML files | 42 DB + ~60 HTML |

The 2,000 dropped MCQs go into `_archive/dropped_current_affairs_2026/` as JSON dumps so nothing is permanently lost.

---

## 2. The big shift: admin-controlled UI ("Full CMS" mode)

Nothing visible in the app is hardcoded. The admin can change every navigation surface and every piece of content without touching code or redeploying.

### 2.1 What admin controls

| Surface | Admin can | Storage |
|---|---|---|
| App title, tagline, accent color, logo | Edit | `app_settings` table |
| Home tiles (the 4–8 big cards on landing) | Add / edit / reorder / hide / icon-pick / link to anywhere | `home_tiles` table |
| Side menu (top-level + nested dropdowns, any depth) | Add / edit / reorder / hide | `menu_items` table |
| Subjects (Indian Polity, AP Geography, etc.) | Add / edit / merge / archive | `subjects` table |
| Chapters within a subject | Add / edit / reorder | `chapters` table |
| Questions (MCQs) | Add / edit / bulk-import (YAML/CSV) / delete / flag-as-bad | `questions` table |
| Notes sections | Rich-text edit (Telugu + English), reorder | `notes` table |
| PYQs | Same as questions, with year + paper metadata | `questions` (filtered) |
| Exam templates ("APPSC Group 2 Mock", "AP HC Full") | Create reusable exam configs | `exam_templates` table |

### 2.2 How admin actually works

A single `/admin` area, PIN-gated (keep `1234` until you change it). Sidebar on the left with sections: **Site** (settings, tiles, menus), **Content** (subjects, chapters, questions, notes), **Tools** (import, audit, archive).

Every list view supports: search, filter, sort, drag-to-reorder where order matters, inline-edit for common fields, "duplicate" button. Every edit form validates both Telugu and English fields are present before saving.

**Home tiles UI.** Drag-and-drop grid showing live preview. Each tile has: title (TE/EN), description, icon (pick from emoji or upload SVG), action (one of: open subject, start exam template, open notes chapter, open custom URL, open built-in route like Review/History).

**Menu builder UI.** Tree editor — drag items in/out to nest, click to edit label or link target. Same action types as tiles. Visibility toggle per item. A `parent_id` self-reference makes arbitrary nesting depth possible; the UI renders dropdowns when an item has children.

**MCQ editor.** Single form with side-by-side Telugu | English columns, four/five options, correct-answer radio, difficulty pill, explanation fields, optional chapter link, optional PYQ year/paper. "Save and add another" button for batch entry.

### 2.3 New schema additions (on top of v1's six tables)

```sql
-- Key/value app settings: title, accent_color, logo_path, default_lang, etc.
CREATE TABLE app_settings (
  key   TEXT PRIMARY KEY,
  value TEXT
);

-- Home page tiles.
CREATE TABLE home_tiles (
  id          SERIAL PRIMARY KEY,
  title_en    TEXT NOT NULL,
  title_te    TEXT NOT NULL,
  desc_en     TEXT,
  desc_te     TEXT,
  icon        TEXT,             -- emoji char or icon-name
  action_type TEXT NOT NULL,    -- 'subject'|'exam_template'|'chapter'|'route'|'url'
  action_ref  TEXT NOT NULL,    -- id or path depending on action_type
  sort_order  INTEGER DEFAULT 0,
  visible     BOOLEAN DEFAULT true
);

-- Menu items (self-referential for nested dropdowns).
CREATE TABLE menu_items (
  id          SERIAL PRIMARY KEY,
  parent_id   INTEGER REFERENCES menu_items(id) ON DELETE CASCADE,
  label_en    TEXT NOT NULL,
  label_te    TEXT NOT NULL,
  icon        TEXT,
  action_type TEXT,              -- nullable: parent items can be pure containers
  action_ref  TEXT,
  sort_order  INTEGER DEFAULT 0,
  visible     BOOLEAN DEFAULT true
);
CREATE INDEX ix_menu_parent ON menu_items(parent_id);

-- Saved exam configs (so you can put "APPSC Mock #1" on a home tile).
CREATE TABLE exam_templates (
  id          SERIAL PRIMARY KEY,
  name_en     TEXT NOT NULL,
  name_te     TEXT NOT NULL,
  config      JSONB NOT NULL,    -- {subject_ids, count, mode, time_limit, lang}
  created_at  TIMESTAMP DEFAULT now()
);
```

Total new schema = the 6 tables from v1 + these 4 = **10 tables**, all with clear single-purpose roles.

### 2.4 Render path

Page templates ask the database for navigation on every render (cached for 60 s in memory). `base.html` becomes:

```jinja
<header>{{ settings.app_title }}</header>
<nav>{{ render_menu(menu_tree) }}</nav>
<main>{% block content %}{% endblock %}</main>
```

Where `menu_tree` is a list of dicts built from `menu_items`, and `render_menu` is a macro that recurses for nested children. Add a menu item in admin → it appears on the next request. No deploy.

---

## 3. Critical fixes from v1 review (resolved)

| v1 issue | Fix in v2 |
|---|---|
| **#1 Cutover hand-wave** | Stand up a **second** Railway service (`mcq-app-v2`) with its own Postgres add-on. Run new code there, point it at the new DB, test on the temp URL. Cutover = move the custom domain from old service to new service (DNS change, ~5 min). Old service stays running for 7-day rollback window, then deleted. |
| **#2 Passage migration missing** | Migration script Step 5a: `SELECT DISTINCT passage_group_id, passage FROM old_questions WHERE passage IS NOT NULL` → insert into `passages` table; then Step 5b: when copying questions, look up the new `passage_id` by old `passage_group_id`. |
| **#4 Difficulty / correct-answer normalization** | Migration explicitly maps: `chapter_mcqs.difficulty` int 1→'E', 2→'M', 3→'H'; lowercases `chapter_mcqs.correct`; lowercases `questions.correct_answer`. Assertion at end: `SELECT correct_answer FROM new_questions WHERE correct_answer NOT IN ('a','b','c','d','e')` must return zero rows. |
| **#8 Admin UI too late** | Admin moves from Phase 6 → **Phase 3**. Read-flow (Phase 1) and migration (Phase 2) come first so there's data to administer; admin then comes before exam-taking flow so you can curate content as you build. |
| **#11 No per-phase verification** | Every phase row now ends with a "Done when…" cell with a concrete check. |
| **#3 Notes source of truth** | Decision: **DB is the source of truth.** Phase 4 includes a one-time importer that reads the 60+ `.html` notes files and inserts them as `notes` rows (one HTML body per section, sanitized). HTML files then move to `_archive/`. |
| **#5 `app.db` vs `database.db`** | `app.db` (empty, 8 KB) is ignored. Migration source is `database.db`. Stated explicitly in the migration script header. |
| **#6 HTMX dependency** | Removed. Quiz "next question" uses vanilla `fetch()` + `innerHTML` swap (~20 lines of JS). No new library. |
| **#7 Notes body format** | Store as **HTML** (sanitized with `bleach` to a known tag allowlist). Telugu tables and inline formatting survive verbatim. |
| **#9 "6 dev days" framing** | Recast as **8 work sessions**, each is one focused sit-down with me. Calendar time depends on cadence. |
| **#10 Importer idempotency** | Importer uses UPSERT keyed on `(subject_slug, chapter_num, question_hash)` where `question_hash = md5(question_en + question_te)`. Re-running the importer on the same YAML is a no-op. Stated in spec. |
| **#12 Day-1 bilingual gap** | Per-quiz language filter: TE-only / EN-only / Both. Default Both. The "questions missing translation" view in admin lets you prioritize backfill for whichever subject you study most. Mitigates the issue but doesn't pretend it's solved. |

Three smaller items also addressed: gunicorn workers become env-driven (default 1); old scripts are removed via `git rm` and live only in git history (no `_archive/` clutter at the repo root); accent color is now editable in admin so I don't pick one.

---

## 4. Schema summary (final)

10 tables, all with foreign keys and indexes:

1. `app_settings` — global key/value
2. `home_tiles` — landing page cards
3. `menu_items` — nav tree
4. `subjects` — top-level study areas
5. `chapters` — chapters within a subject
6. `passages` — reading-comp shared text
7. `questions` — the **one** MCQ table (practice + chapter + pyq via `source_type`)
8. `notes` — chapter sections (HTML body)
9. `user_question_state` — per-device seen/wrong/flagged
10. `exam_sessions` — attempt history
11. `exam_templates` — saved exam configs (for tile-launch)

(That's 11; rounded "10" was wrong in §2.3 — fixed.)

---

## 5. Repo layout (final)

```
mcq_app/
├── app/
│   ├── __init__.py              # create_app() factory
│   ├── models.py                # SQLAlchemy models
│   ├── db.py
│   ├── config.py
│   ├── routes/
│   │   ├── public.py            # home, subject, practice, exam, notes, review
│   │   ├── admin.py             # all /admin/* CRUD
│   │   └── api.py               # JSON endpoints (quiz next-question, etc.)
│   ├── services/
│   │   ├── nav.py               # build menu_tree from menu_items (cached)
│   │   ├── question_picker.py
│   │   ├── scoring.py
│   │   ├── importer.py          # YAML/CSV → DB (idempotent)
│   │   └── html_sanitizer.py    # bleach config for notes
│   └── templates/
│       ├── base.html            # renders header + nav from DB
│       ├── _macros.html         # render_menu(), question_card()
│       ├── home.html
│       ├── exam.html
│       ├── practice.html
│       ├── notes_view.html
│       └── admin/               # admin CRUD pages
├── static/
│   ├── app.css                  # one file, CSS vars driven by app_settings
│   └── app.js                   # vanilla, ~150 lines
├── content/                     # YAML seed files for bulk import
├── migrations/                  # Alembic
├── scripts/
│   ├── migrate_from_old_db.py   # one-time data move (database.db → new Postgres)
│   ├── import_html_notes.py     # one-time notes import
│   └── import_content.py        # YAML → DB (re-runnable)
├── tests/
│   ├── test_models.py
│   ├── test_exam_flow.py
│   ├── test_importer.py
│   ├── test_nav_render.py
│   └── test_migration.py        # asserts row counts, normalization
├── requirements.txt
├── Procfile                     # gunicorn 'app:create_app()' --workers $WEB_WORKERS
├── wsgi.py
├── alembic.ini
└── README.md
```

Everything outside this tree from the current repo gets deleted via `git rm` in the cutover commit. Old work is preserved in git history (and the snapshot tag `v1-final-snapshot`).

---

## 6. Phased delivery (8 sessions)

| Phase | What ships | Done when |
|---|---|---|
| **0. Scaffold** | New repo branch, Flask factory, SQLAlchemy models, Alembic baseline, `tests/` smoke, gunicorn config | `flask run` boots locally; `pytest` passes 1 smoke test |
| **1. Core read flow** | `base.html` rendering nav from `menu_items`, home tiles from `home_tiles`, subject list, practice mode, question card macro | You can answer practice MCQs (against a hand-seeded test row) on the new UI |
| **2. Migration** | `migrate_from_old_db.py` runs end-to-end: `database.db` → new Postgres. Passages deduped, difficulty + correct-answer normalized, current-affairs categories archived to JSON. | Test asserts 5,837 questions in / 5,837 out, 0 in `NOT IN ('a','b','c','d','e')`, archive JSON files exist |
| **3. Admin CMS** | `/admin` PIN gate, CRUD for app_settings + home_tiles + menu_items + subjects + chapters + questions + notes; drag-reorder for tiles & menu; MCQ side-by-side editor; HTML notes importer | You can add a home tile, nest a menu dropdown, and edit an MCQ entirely from the UI |
| **4. Notes display** | Public notes browse: subject → chapter → section render; bleach-sanitized HTML; print-friendly CSS | You can open any of the 42 chapters and read both languages |
| **5. Exam flow** | Exam wizard, take exam, submit, score, result page, exam_templates launcher | You complete one full timed exam end-to-end, score is correct |
| **6. Review + state** | Wrong answers list, flagged list, history, device_id assignment in localStorage, per-question state writes | After an exam, wrong answers show up in Review with correct stats |
| **7. Cutover + polish** | Dark mode (auto), mobile QA, perf pass (indexes verified via EXPLAIN), Railway second service deploy, domain swap, old service archived | Old URL serves the new app; rollback runbook documented |

**Each phase = one focused work session with me.** I do the build; you review/test the deliverable at the end of each phase before we move on. Calendar pace is yours.

---

## 7. Migration data flow (concrete)

```
database.db (SQLite, local)
   │
   ├── questions WHERE topic NOT IN (
   │     'AP_Current_Affairs_2026',
   │     'International_Current_Affairs',
   │     'Indian_Economy'
   │   )                                              → new questions (source_type='practice')
   │
   ├── questions WHERE topic IN (...dropped...)       → _archive/dropped_*.json
   │
   ├── chapter_mcqs                                    → new questions (source_type='chapter',
   │                                                       difficulty mapped 1→E/2→M/3→H,
   │                                                       correct lowercased,
   │                                                       chapter_id resolved via study_note_id→chapters)
   │
   ├── pyq_questions                                   → new questions (source_type='pyq',
   │                                                       pyq_year/pyq_paper preserved)
   │
   ├── passages (extracted from old questions.passage) → new passages, FK back-filled
   │
   ├── study_notes (42 rows)                           → new chapters + notes
   │                                                       (sections_json unpacked into notes rows)
   │
   ├── HTML notes files (60+)                          → new notes (sanitized HTML body)
   │
   ├── exam_sessions (7 rows)                          → new exam_sessions (UUIDs regenerated, device_id='legacy')
   │
   └── seen_questions (0 rows)                         → user_question_state (seen_count=1)
```

End-of-migration assertions (in `test_migration.py`):
- `questions` row count ≈ 5,837 (±10 for known duplicates)
- Every question has either `question_en` or `question_te` non-null
- Every question's `correct_answer` is in `('a','b','c','d','e')`
- Every `chapter_id` resolves to a real `chapters.id`
- No orphaned `passage_id`

---

## 8. Risk register

| Risk | Likelihood | Mitigation |
|---|---|---|
| Old DB has malformed rows that block migration | Medium | Migration script logs+skips bad rows to `migration_errors.json` rather than aborting; final report lists them for manual cleanup |
| Telugu HTML in notes breaks `bleach` sanitizer | Low | Whitelist covers common tags (`p, h1-h4, ul, ol, li, table, tr, td, th, strong, em, br, span`); test suite parses every imported note |
| Admin lets you create a broken navigation loop | Low | Server-side validation: `menu_items.parent_id` can't reference self or a descendant |
| Domain swap drops live exam sessions | Low | Cutover scheduled when you're not mid-exam; exam state is in DB not memory so it survives anyway |
| 2,000 archived MCQs are needed later | Low | Stored as JSON in `_archive/`, re-importable via `import_content.py` if you change your mind |

---

## 9. Confirm and I start

Three items I need you to confirm before kicking off Phase 0:

1. **Hosting:** stand up a second Railway service (recommended in §3 #1)? Same Postgres provider, new DB, new URL during build, domain swap at the end. Yes / no.
2. **Drop list:** AP_CA 2026 + Intl CA + Indian Economy. Anything else to drop now while we're cleaning house? (e.g. the lone `National_CA` Consumer_Protection row — drop it?)
3. **Admin PIN:** keep `1234` for now and change in admin after Phase 3 ships?

Reply "go" with answers, and I start Phase 0.
