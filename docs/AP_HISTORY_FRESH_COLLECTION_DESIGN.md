# AP History fresh collection: design, local preview and proposed learner switch

Basis: `AP_HISTORY_FRESH_BUILD_DECISION_20261009.txt` (fresh build; no merge with old banks; no production wipe or progress reset implied).
The old64-versus129 reconciliation task is cancelled. Nothing here touches production.

## 1. What "the new collection" is
A question belongs to the fresh collection when `questions.syllabus_chapter_id IS NOT NULL` (canonical chapter) with `chapter_id IS NULL`, loaded from an `ap-history-import-v1` package (`source_qid`, `batch_id`, `import_ref`). Notes live in the separate `expanded_notes` table. Legacy AP History content (380 questions, 17 sections, `chapter_id` set, `syllabus_chapter_id` NULL) is outside it. The two sets are kept apart in code already: the generic Practice bank and legacy `/practice/<slug>` exclude collection rows, and collection pages read only collection rows. Other subjects are never read or written.

## 2. Importer change (this commit)
`--overlap-scope collection` (API `overlap_scope="collection"`): only questions already in the fresh collection, or earlier in the same batch, can block an apply, so the collection is internally deduplicated. Overlaps with legacy questions are listed as `legacy_overlaps_informational` and nothing legacy is changed. Default stays `all`; the guard is not disabled, `--allow-overlaps` is unchanged. The two checks run separately so a legacy match cannot hide an in-collection duplicate (found and fixed by the new test). Each later chapter package uses the same flag.
Unchanged: add-only, one transaction, idempotent on `(source, source_qid)`, `--approval-ref` required, notes must be loaded first, package checksum and `05_claude_import` folder checks, no ids trusted. No question id is reused and nothing is deleted, so no cascade can reach learner history.

## 3. Local preview (isolated database `ap_fresh_preview`, a local copy of a sandbox database, never production)
Migrated to `b8c9d0e1f2a3`; canonical structure and taxonomy seeded locally (5 units, 35 chapters, 187 subtopics, 317 microtopics; a repeat seed adds nothing); 74 notes; 129 questions from metadata-r1 (`questions.jsonl` sha256 `a69d4a50…`). Re-run imports 0. All 6,457 legacy questions and 980 notes are byte-identical before and after (md5 over content columns), every other subject unchanged.
Learner pages (test client, Telugu present on all): `/learn/ap-history`, chapter page, expanded-notes index, core note `CH01-S02`, addendum `CH01-A01`, practice and `?subtopic=` practice all 200; practice shows the "Author-reviewed" label, no internal ids; note links resolve. The automated suite additionally opens all 129 questions' note anchors and checks correct/wrong/skipped review screens.
Test results are in the delivery message.

## 4. Proposed way to switch learners later (not implemented; needs your approval)
Principle: switch by routing, never by deleting.
1. **Dark launch.** After the additive deploy and the collection load (plan G steps 4–9), the collection is reachable at `/learn/ap-history` while learners still land on legacy. Review in production with your own account.
2. **Per-chapter switch.** One new setting (a settings row or environment variable, decided at approval) lists the chapters whose learner entry points use the fresh collection. The AP History subject page, home tiles and chapter practice for a listed chapter point to `/learn/ap-history/<slug>`; unlisted chapters stay on legacy. Chapter 1 alone is therefore switchable while Chapters 2–31 remain on legacy until their fresh packages are loaded. A single subject-wide switch is only sensible once all chapters are covered.
3. **Legacy is hidden, not removed.** Legacy rows stay in the database with their ids, so `user_question_state`, exam sessions and chapter progress keep working and old results stay readable. Direct legacy URLs can remain for existing study plans.
4. **Learner progress.** Fresh questions start with no history (new ids). Learners keep old history under legacy; no progress is reset or migrated. Whether to show a "new content" notice is your call.
5. **Rollback of the switch** is removing the chapter from the setting: instant, no data change.
6. **Retiring legacy (optional, much later, separate approval).** Before touching any legacy row: list exact affected rows and dependent progress/session rows, export an archive, take and restore-verify a new backup, and prefer a soft "retired" marker over deletion. Nothing in steps 1–5 requires it.

## 5. Open items
Production taxonomy state and Alembic revision (read-only snapshot, runbook steps 0–2); verified backup; whether the switch setting is a table row or an environment variable; Telugu interface strings are drafts; content is author-reviewed only; Telugu convention warnings (Q075, R2-Q004) kept as written.
