# Merge report: secured branch + origin/main (fetched 2026-10-04)

* Ours: `design-system-stage-1-2` @ `6516227` (Learn journey, security, Alembic). Theirs: `origin/main` @ `ce2343c` (57 commits ahead of local `main`; 29 of them are new since the 2026-05-30 snapshot ea34696: the AP History notes feature).
* Merge base `2244842`. Done in an independent clone; the original repository, `main`, locks, `static/`, `data/` and Railway were not touched.

## Release blocker: kept out
`origin/main`'s `app/__init__.py` adds `_patch_schema()` (executes `DROP TABLE questions CASCADE` and `DROP TABLE user_question_state CASCADE` at startup when `questions` lacks `subject_id/chapter_id/source_type/options_en`) and `db.create_all()`. Resolution: this file is taken **entirely from the secured branch**. A new test (`test_no_destructive_or_implicit_schema_code_anywhere_in_the_app`) fails if `DROP TABLE`, `drop_all`, `create_all` or `_patch_schema` appears anywhere in `app/` or `wsgi.py`; it flags origin's file.

## The 16 conflicted files

| File | Hunks | Resolution | Why |
|---|---|---|---|
| `app/__init__.py` | 1 (+ auto-merged destructive code) | **ours** (whole file) | origin's only change is the destructive startup patch; ours keeps the blueprint, security headers, note sanitiser, production config check |
| `app/routes/admin.py` | 1 | ours for the import line; origin's new `/parse-ap-history` and `/load-content` changes merged | `hmac`/`time` needed by login throttle; blueprint-wide CSRF covers the new POST routes |
| `app/templates/notes/reader.html` | 1 | **ours** | origin's `{{ body | safe }}` is the stored-XSS bug; ours uses the `note_html` sanitiser. Origin's other fixes (restored `</script>` and `endblock`, `&middot;`) are kept: auto-merged |
| `app/templates/subjects.html` | 2 | ours | origin's copy has double-encoded Telugu (mojibake) |
| `app/templates/admin/parse_ap_history.html` | 5 | ours | origin's copy is mojibake (`â¶`, `â³`) and lacks the CSRF token and header |
| `app/templates/admin/load_content.html` | 2 | ours | identical except CSRF token/header, which origin lacks |
| `app/templates/admin/seed.html` | 2 | **both**: origin's version + CSRF | origin adds fetch error handling; CSRF re-applied |
| `app/templates/exam_session/results.html` | 6 | **theirs** | the branch's Retry was `<a formmethod="post">`: an anchor cannot POST and the start route is POST-only, so it never worked. Origin links to the exam page, where the start form is. Rest is formatting |
| `app/templates/exam_session/take.html` | 11 | ours | origin strips comments and the `aria-checked` updates; behaviour otherwise equal |
| `app/templates/study_plan/dashboard.html` | 3 | ours | origin only strips comments / reflows |
| `app/templates/subject_detail.html` | 2 | ours | formatting and comments only |
| `app/routes/exam_session.py` | 5 | ours | origin only strips comments |
| `app/routes/study_plan.py` | 4 | ours | origin only strips comments |
| `tests/test_exam_session.py` | 12 | ours | origin's fixtures replaced Telugu text with Devanagari (Hindi) script |
| `tests/test_study_plan.py` | 5 | ours | same Devanagari substitution |
| `SESSION_REPORT.md` | 1 | ours; origin's copy kept verbatim as `docs/SESSION_REPORT.origin-main-2026-05-31.md` | nothing lost |

## Merged from origin without conflict (reviewed)
AP History feature: `scripts/load_content.py`, `scripts/fix_notes.py`, `scripts/parse_ap_history_notes.py`, `static/ap_history_notes.css`, 12 AP History chapter HTML files, `data/content.db.gz` (225 AP History sections), `beautifulsoup4` in requirements, `base.html` `head_extra` block, `public.py` duplicate-route removal, `chapter_list.html` entity fix, `app.css`.

## Flagged for your decision (not changed)
1. `/admin/load-content` runs `Note.query.delete()` (all notes) and then reloads from `content.db`; `parse_ap_history_notes.py` deletes the AP History chapters and notes. Notes edited by hand in the admin editor are lost when either runs. Both are PIN + CSRF protected and operator-triggered, not startup. Consider a confirmation step or a "replace only this subject" mode before using them on production.
2. `scripts/scripts/scripts/scripts/load_content.py` is a stray duplicate created by a web upload (kept; delete when convenient).
3. `data/content.db.gz` (3.3 MB binary) is committed on origin.

## Verification (merged tree)
* Full suite: see commit message. Includes security, Alembic and the new guards.
* Real content (copy of `data/content.db`): migrations upgrade to head with `alembic check` clean; 782 requests across all 194 chapters (legacy reader, Learn topic/notes/practice), hub, subjects, settings, healthz, admin login: 0 non-200; 0 reader pages containing script/handler/iframe/style.

## Follow-up: safe content import (replaces the global notes deletion)

Release blocker found in review: `/admin/load-content` ran `scripts/load_content.py`, which executed `Note.query.delete()` on **every
note of every subject** and re-inserted from `data/content.db`, destroying hand-edited notes and notes outside the source.

What changed:

* `app/services/content_import.py` is the only import code path. `/admin/load-content` (GET page), `/load-content/preview`,
  `/load-content/apply` and `/load-content/restore` are POST + admin login + CSRF. The old streaming-subprocess POST is gone (405).
* **Preview** is read-only and shows, per subject: new chapters, notes to add, notes identical, notes that *differ* (kept), live-only
  notes, questions to add. No subject is preselected.
* **Default apply only adds missing rows.** Existing notes, including hand-edited ones, are kept.
* Replacing differing notes and removing live-only notes are separate opt-in boxes, limited to the ticked subjects and to chapters the
  source mentions, and require typing `REPLACE`. Each touched note is first copied into the new `note_backups` table in the same
  transaction; `/load-content/restore` (type `RESTORE`) puts them back, and a restore is itself undoable.
* One transaction: any error rolls everything back. A fingerprint of the plan, source file and differing live notes must match
  the preview, otherwise the apply is refused.
* Question JSON options are stored as JSON objects, not as a JSON string of a string.
* `scripts/load_content.py` is now a CLI over the same service: default is preview only; `--subjects`/`--all-subjects` to add;
  `--replace-notes`/`--remove-extra` need `--yes`; `--restore BATCH --yes`.
* New migration `c3d4e5f6a7b8` (`note_backups`, no foreign keys so backups outlive their chapters).
* Tests: `tests/test_content_import.py` (21) — preview writes nothing; default apply keeps edited/extra/unrelated notes; unselected and
  non-source subjects untouched; replace/remove are backed up and restorable; injected failure rolls back; stale preview refused;
  auth, CSRF and confirm phrases; idempotence; and a guard that no `Note.query.delete()` / `DELETE FROM notes` exists in `app/` or the loader.

Real-content check (temporary SQLite from migrations): preview wrote nothing; `--all-subjects` added 11 subjects / 194 chapters / 980 notes /
6242 questions; after hand-editing a note, a second run changed nothing and kept the edit. Note: the old page text claimed 6 257 notes and
6 742 questions; the shipped `content.db` contains 980 notes and 6 242 questions. Worth confirming which is intended.

## Follow-up 2: review findings on the import (P1 x2) and the AP History parser

* **Question de-duplication (P1).** Identity was an md5 of `source_type:` plus the first 120 characters of the text, so different
  questions sharing a long stem were silently dropped. Identity is now the full content: subject, type, text (en/te), options (en/te),
  correct answer, PYQ year and paper. Exact duplicates are still skipped (also inside the source). On the shipped `content.db` the old rule
  discarded **215 distinct questions**: a full import now yields 6 457 questions, not 6 242. Known trade-off: a question corrected by
  hand in the live database is no longer recognised as "the same" as the source version and would be added again; the preview shows
  the count before anything is written.
* **Stale-preview protection (P1).** The fingerprint is now per subject and covers the source hash, the live subject, its chapters,
  *every* live note in those chapters (id, section, content, including notes the source does not mention) and all live question keys.
  Changes to another, unselected subject do not block an import. Tests cover added/edited/deleted extra notes, a new chapter, a new
  live question and a changed source file.
* **Check-then-write race.** The import locks the tables first (PostgreSQL `LOCK TABLE ... SHARE ROW EXCLUSIVE`; SQLite write lock),
  recomputes the fingerprints under that lock, and only then writes; the lock is held until commit or rollback and released on every refusal.
  Restore takes the same lock. Tests: a concurrent writer is blocked on SQLite (and on PostgreSQL when `TEST_PG_URL` is set).
* **AP History parser.** `/admin/parse-ap-history`, `scripts/parse_ap_history_notes.py` no longer delete anything. The HTML files are parsed
  by `app/services/ap_history_parse.py` into a temporary source and go through the same preview, scoped add-only apply, opt-in
  replace/remove with backup, and restore. The old POST is gone (405); chapters are never deleted; the old `--sqlite` mode that edited
  `data/content.db` is removed. Missing chapter files are shown as warnings. With the shipped files: 12 chapters, 225 sections,
  216 identical, 9 differ (kept by default), nothing added on top of a full content import.
  Behaviour change: chapter titles/reading times of existing chapters are not updated by the parser any more.
* **Cleanup.** `open_source` returns a `Source` context manager that closes the SQLite connection and removes the temporary directory of a
  decompressed `content.db.gz`; all callers use `with`.

Still open / not changed:

* `scripts/fix_notes.py` rewrites notes inside `data/content.db` (the *source* file) from the legacy database; it never touches the live database.
* `scripts/scripts/scripts/scripts/load_content.py` (stray nested copy of an older additive-only loader) is left in place; remove it in a separate reviewed commit.
* The old page claimed 6 257 notes / 6 742 questions; the shipped file has 980 notes and 6 457 distinct questions. Please confirm which is intended.
* Live Railway database not inspected or backed up.
