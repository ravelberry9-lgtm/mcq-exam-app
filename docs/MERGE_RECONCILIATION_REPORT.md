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

## Follow-up 3: release blockers from the mobile smoke test (F1, F2, F3)

* **F1, options in the language that exists.** `exam_session/take.html`, `results.html` and the legacy `practice.html` read `options_en`
  only, so the 3,402 chapter questions (Telugu options, no English) showed no options. A shared helper (`app/services/qdisplay.py`
  and `templates/_partials/bi.html`) now renders both languages when both exist (the language preference hides one), and a single
  always-visible span when only one exists, for question text, options, answer lines on the results page and explanations. The same
  fallback works the other way round (the practice/PYQ rows have English options only). `static/app.js` no longer binds the practice
  card on pages that have no submit button, which was the exam page's `addEventListener of null` error.
* **F2, exam construction.** A session is never "every eligible question". `app/services/exam_rules.py` holds `VERIFIED_RULES`
  (empty): an *official* test can start only for a paper with a verified entry (question count, duration, source of the numbers;
  negative marking is rejected until scoring supports it). Everything else is an **unofficial practice test**: the user picks a
  question count (5-100, default 20) and minutes (5-180, default = one per question), questions are answerable ones only (options
  exist and the correct answer is among them), spread across the paper's sections, stored with a seed. `mode=official` without verified rules is refused (403). The exam page shows the
  official button disabled with "not verified yet" and no longer prints the seeded "150 marks / 150 min". Take and results pages say
  "Unofficial practice test"; the results page shows the raw count only: no pass mark and no negative marking are assumed (the former 60% pass/fail verdict is gone).
  Sessions already created before this change keep working.
* **F3, counts and banks.** Every question is reachable from exactly one place: chapter questions via their topic, PYQs via the
  subject's *Previous papers* bank, everything else via the subject's *Practice* bank (`/learn/subject/<slug>/practice|pyq`). Hub, section
  and subject counts are computed from those same groups, so each number is what the page can reach. Subjects with questions but no
  chapters (Indian Economy, AP Economy, Mental Ability) appear in an "All subjects" list on the hub and open to their banks. PYQ items keep "Source not verified".
* Tests: `tests/test_exam_and_banks.py` (40) run against slices of the real shipped content imported by the production importer.

Not done in this commit (next priority): restoring the answered state after a practice reload, mobile admin preview overflow and which note
field differs, the "Chapter (recovered, sn_id=14)" title on the legacy exam page, the 980-vs-6,257 notes investigation, and the service worker (Stage 7).
The hub still carries the approved prototype line "Screening test, 150 marks (30 per subject)", which is also unverified.

## Follow-up 4: review round 2 (answer API, marks, topic counts, CSRF, duration, size limits)

Fixed on top of `9dbfd0a`:

* **Answer API.** `/exam-session/<id>/answer` accepts only a question that belongs to the session and an option that exists for that question; everything else is a 400 and nothing is stored, so the score can no longer exceed the session length. Payloads that are not objects, non-string choices, non-numeric / out-of-range / boolean confidence (valid: empty, 0-5) and bad JSON return 400, never 500. The Learn practice endpoint `/api/answer` uses the same validation.
* **Marks.** The seeded "150 marks", "30 marks", "30 M" and "Screening test, 150 marks (30 per subject)" no longer appear on the Learn hub, the section page or the exam list. Nothing about marks is shown until a paper has verified rules.
* **Topic counts.** A topic's count is the number of chapter-type questions its Practice page serves. Non-chapter rows that carry a chapter id are counted in the subject banks, not in the topic.
* **CSRF** on exam start, answer and submit (token in the signed session, shared with the admin; forms carry a hidden field, the page script sends `X-CSRF-Token`). Learn practice `/api/answer` and the other legacy POST forms are not covered yet.
* **Session URLs are deliberate bearer links** (no accounts; random UUID4 ids; resuming on another browser is a feature). Session pages send `Cache-Control: no-store` and `X-Robots-Tag: noindex`; a malformed id is a 404. If you want sessions bound to a device or a login instead, that is a product change.
* **Duration.** A session without a usable `duration_min` gets a labelled practice default (one minute per question, 5-180) with a visible note; the silent 150 is gone.
* **Limits.** `MAX_PRACTICE_QUESTIONS` (100) applies to practice only. A verified official pattern is bounded by separate typo guards (`MAX_OFFICIAL_QUESTIONS`, `MAX_OFFICIAL_MINUTES`) and is refused with 409 if fewer answerable questions exist than the pattern needs.

Still open: answered state after a practice reload, mobile admin preview overflow and "which field differs", the recovered chapter title, the 980-vs-6,257 notes question, service worker (Stage 7), CSRF for the remaining legacy forms, answers are still accepted after the timer expires, the legacy `/exam/<slug>` list still counts all question types per chapter and links to the subject practice page.
