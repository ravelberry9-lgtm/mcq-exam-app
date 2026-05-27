# Handoff prompt — continue APPSC v3 rebuild from end of Phase 1

Copy everything below the `---` line into your new Sonnet task as the first message.

---

You are continuing a rebuild of an APPSC + AP High Court exam-prep web app. The previous Sonnet session completed Phase 0 (scaffold) and Phase 1 (core read flow + side drawer + practice flow + Group 2 syllabus seed). The user (Ravelberry) is away for ~1 hour and wants you to push as far through the phases as possible autonomously. You can plan, review, write code, run migrations, commit to git, and use Chrome browser tools if needed. Be decisive — when a small judgement call has two reasonable answers, pick one and document it; don't ask the user.

## Where to start: read these files in order, then think

1. `C:\Users\AashrithaNagababu\Downloads\mcq_exam_app_fixed\mcq_app\REBUILD_PLAN_v3.md` — the architecture spec. Sections 4, 5, 6, 7 are the most important.
2. `app/models.py` — the 15 SQLAlchemy models that define the schema.
3. `scripts/seed_dev.py` and `scripts/seed_exam_group2.py` — the upsert pattern to follow for any new seed/migration code.
4. `app/routes/public.py` — every route that exists today.
5. Run `ls _legacy/` and `ls _legacy/static/notes/` to see what migration sources are available.

Don't skip this reading step. The plan locks ~30 design decisions you'd otherwise rediscover the hard way.

## Project paths

- Working dir on Windows (what the user sees): `C:\Users\AashrithaNagababu\Downloads\mcq_exam_app_fixed\mcq_app`
- Same dir mounted in the Linux sandbox: `/sessions/<your-session>/mnt/mcq_app/` — get the exact prefix from the `<env>` / Shell access section in your system prompt
- Migration source (do **not** modify): `_legacy/`
  - `_legacy/database.db` — SQLite with ~7,838 MCQs across old schema (3 tables: `questions`, `chapter_mcqs`, `pyq_questions`)
  - `_legacy/static/notes/<Subject>/Chapters/*.html` — bilingual HTML notes for Indian Geography, AP Geography, Indian Polity, Art Culture, etc.
  - `_legacy/AP_HC_Constitution_Bilingual.html`, `_legacy/medieval_india_telugu.html`, `_legacy/modern_india_telugu.html`, `_legacy/ap_geo_ch1-5_notes.html` — orphan HTML files from old repo root

## Current state at end of Phase 1

- App boots on localhost (`python wsgi.py`)
- 15 tables created via Alembic baseline
- 11 subjects, 13 chapters, 5 hand-seeded bilingual questions, 17 nav items (after `seed_exam_group2.py`)
- APPSC Group 2 exam seeded: 1 exam, 3 papers, 9 sections, 13 syllabus items
- Routes live: `/`, `/subjects`, `/subject/<slug>`, `/practice/<slug>`, `/exam/<slug>`, `/settings`, `/api/answer`, `/healthz`
- 10/10 tests passing (`python -m pytest tests/ -p no:cacheprovider`)
- Git: tagged `pre-rebuild-snapshot` before the wipe. Phase 0 and Phase 1 work is **uncommitted** — your first git task is to commit it.
- Railway: existing legacy app still running at `https://web-production-ac9f2.up.railway.app/` on project `80d016ab-a223-4bf3-9a41-f7fde6ebc39b`. **Do not push to this service.** New app gets a second service later.

## Your priority order (most important first — drop the bottom items if you run out of time)

### 1. Commit the uncommitted Phase 0 + 1 work
```
git add app/ static/ tests/ scripts/ migrations/ requirements.txt wsgi.py Procfile alembic.ini README.md .env.example .gitignore HANDOFF_PROMPT.md
git commit -m "feat(v3): phase 0 scaffold + phase 1 core read flow + group 2 syllabus seed"
git tag phase-1-complete
```

### 2. Phase 2 — migration from `_legacy/` to new schema  (~25 min)

Write `scripts/migrate_from_legacy.py` that:

1. Reads from `_legacy/database.db` (SQLite, old 3-table question schema documented in v2 plan §5 of the rebuild doc)
2. Re-maps `folder` + `topic` strings into the new 11-subject slug taxonomy. Mapping (per v3 §4):
   - `Indian_Polity` → `indian_constitution`
   - `Indian_History` → `indian_history`
   - `AP_Geography` → `ap_geography`
   - `Art_Culture` → `ap_history` (best fit — overlaps with AP cultural history)
   - `General_Science` → `science_technology`
   - `Everyday_Science` → `science_technology`
   - `Indian_Economy` → `indian_economy`, EXCEPT rows where `question_text` contains 'Andhra' or 'ఆంధ్ర' → `ap_economy` (12 rows expected)
   - `Mental_Ability` → `mental_ability`
   - `AP_Current_Affairs_2026` → `current_affairs` (keep)
   - `International_Current_Affairs` → **archive to `_legacy/archived_dropped/intl_ca.json`, do not migrate**
   - `National_CA` (1 row) → **archive, do not migrate**
3. Normalizes everything: lowercase `correct_answer`, map `chapter_mcqs.difficulty` int 1→'E', 2→'M', 3→'H', source_type='chapter' for `chapter_mcqs` rows, source_type='pyq' for `pyq_questions` rows, source_type='practice' otherwise
4. Dedupes passages: `SELECT DISTINCT passage_group_id, passage FROM old WHERE passage NOT NULL` → insert into new `passages`, FK back-fill
5. Imports `_legacy/study_notes` (42 rows, JSON `sections_json` column) into new `notes` rows
6. Sweeps `_legacy/static/notes/**/*.html` and orphans (`_legacy/*.html`) as new chapters + notes (or into `pages` table if they don't fit a subject). Document the mapping in the script output.
7. Migrates `_legacy/exam_sessions` (7 rows) into new `exam_sessions` with `device_id='legacy'`
8. Prints summary: rows in / out per table, dropped count, archived files

Then write `tests/test_migration.py` that asserts:
- `questions` count is between 6,700 and 6,800 (expected ~6,737)
- `correct_answer` is in `('a','b','c','d','e')` for every row
- Every `chapter_id` resolves to a real chapter (no FKs orphaned)
- The 12 AP-Economy questions are tagged `ap_economy`, not `indian_economy`
- `International_Current_Affairs` archive JSON exists with ~1,100 rows

Run the migration against a fresh DB at `/tmp/app_v3_migrated.db` (sandbox SQLite I/O on the Windows-mounted folder fails — see Gotchas below). Re-run the smoke tests. If the migration script errors on any row, log to `migration_errors.json` and continue — don't abort.

### 3. Phase 3 — minimal admin CMS  (~15 min)

Scope is **paste-HTML + save only**, per locked v3 spec. Skip type-mode and upload-mode (those are Phase 3.5).

- New route file `app/routes/admin.py`, registered in `__init__.py` with blueprint
- Routes: `/admin` (PIN gate `1234`), `/admin/notes`, `/admin/notes/<chapter_id>/edit`
- PIN gate via cookie-set session token; very simple — not production-grade
- Editor template with two `<textarea>` panes (Telugu | English) for the chapter's first section
- POST handler runs the HTML through `bleach.clean()` with the tag allowlist from v3 §2.2, writes to `notes.body_te` / `body_en`
- Add the admin route to seed nav (it's already a placeholder pointing to `/admin`)

### 4. Commit + push the Phase 2 work (and Phase 3 if you got there)

```
git add scripts/migrate_from_legacy.py tests/test_migration.py app/routes/admin.py app/templates/admin/ migrations/versions/
git commit -m "feat(v3): phase 2 migration from _legacy + phase 3 admin paste-HTML editor"
git tag phase-2-complete  # or phase-3-complete if you got there
git push origin main      # if remote is configured; if not, leave a note
```

### 5. Railway second-service setup  (~10 min — only if everything above is done)

Use Chrome tools to navigate to `https://railway.com/project/80d016ab-a223-4bf3-9a41-f7fde6ebc39b/`. Goal: create a new service `mcq-app-v2` with its own Postgres add-on. Do NOT touch the existing `mcq-app` service.

If Railway requires interactive login or OAuth, stop, document the manual steps the user needs to take in a `RAILWAY_NEXT_STEPS.md` file, and skip the rest of this step. Don't enter passwords; SSO is OK only if a session already exists in the browser.

### Out of scope for this 1-hour run

Don't attempt:
- Phase 4.5 (study plans UI)
- Phase 5 (exam taking flow)
- Phase 6 (review state)
- Phase 7 cutover (domain swap to production)
- Phase 8 content gap fill (this is an ongoing AI-draft job, not a single session)
- Modifying any file under `_legacy/` (read only)
- Updates to old Railway service

## Critical gotchas — these will save you 30+ min

1. **Write tool truncates large files on the Windows-mounted folder.** Files >~1.5 KB consistently get cut mid-write when using the `Write` tool. The fix: use bash `cat > file.py << 'EOF' ... EOF` heredocs for any file larger than 1 KB. The `Edit` tool works fine for in-place changes. Always verify with `wc -c file && tail -c 50 file` after writing.

2. **SQLite writes to the project folder fail in the sandbox.** `sqlite3.OperationalError: disk I/O error` on writes to `/sessions/.../mnt/mcq_app/app_v3.db`. Workaround: set `export DATABASE_URL="sqlite:////tmp/app_v3_baseline.db"` for any in-sandbox migration / seed run. The user runs the actual app on Windows where this works fine. Tests use in-memory SQLite (no issue).

3. **Two files at the repo root won't move/delete** (`AP_CurrentAffairs_Telugu_v10_FinalAudit.docx` and `static/`). They're Windows-locked. Don't waste time fighting this — they're harmless. The legitimate copy of `static/notes/` is at `_legacy/static/notes/`.

4. **The user is on Windows.** Use `python -m alembic`, `python -m pytest`, `python wsgi.py` in any instructions you write — not bare `alembic`/`pytest` (PATH may not include their Scripts dir).

5. **pytest emits a benign INTERNALERROR about null bytes** at the top of test output. The actual test results line is what matters. Tests pass even when this error appears.

6. **Telugu encoding.** All strings in code are UTF-8. Don't ASCII-escape Telugu — paste it literally inside Python `"..."` strings. Bash heredocs with `<< 'EOF'` (single quotes) preserve Telugu without interpolation issues.

7. **Idempotency is mandatory** for seeds and migrations. Every insert is an upsert by stable key (`slug` for subjects/exams, `(subject_id, chapter_num)` for chapters, `md5(question_en+question_te)` for questions). Re-running must be a no-op, not a duplicate.

## What to do if something goes wrong

- **Migration row fails** → log to `migration_errors.json`, continue. Don't abort the batch.
- **Test fails** → fix it if it's a real bug; otherwise document the failure and move on (don't block).
- **Chrome browser tools require login** → write `RAILWAY_NEXT_STEPS.md` documenting what the user must do, skip that step.
- **Git push requires creds** → stage the commits locally and leave a note. User can push.
- **You hit token budget** → wrap up with a final summary file before context runs out.

## Workflow expectations

- Use `TaskCreate` for every sub-phase (e.g. "Phase 2.1 — write migration script", "Phase 2.2 — write tests"). Update status as you go. Aim for tasks of 5-15 min each.
- Run `pytest -p no:cacheprovider` after every meaningful code change. Don't accumulate broken state.
- Commit at every phase boundary. Tag at the end of each completed phase.
- Don't ask the user clarifying questions — make a judgement call and document it in the commit message. The user trusts your call.

## Final deliverable

When you're done (or out of time), write `SESSION_REPORT.md` at the repo root with:

- What phases completed
- What's tagged in git
- Migration counts (rows in / out / dropped / archived)
- Any errors that need human attention
- Concrete next steps for the next session (exact commands, file paths, what's blocked)
- Time spent vs budget

Then summarize the same in your final chat message so the user sees it without opening the file. Keep the chat summary under 200 words.

## You have full latitude on

- Sub-task ordering within a phase
- Which orphan HTML files become `pages` vs `notes`
- Whether to attempt Railway in this run (skip if blocked by auth)
- Test coverage depth (one test per migration table at minimum; more if time)
- Any small CSS or UI fix you notice as you work

Start by reading the five files I listed at the top. Then make a `TaskCreate` for "Phase 2.0 — read context + commit phase 1". Then begin.

---

**End of handoff prompt.** Everything above the line is the prompt — copy from "You are continuing…" through "Then begin." into the new Sonnet task.
