# Chapter 1 closure import: production change plan (NOTHING IN THIS FILE HAS BEEN RUN ON PRODUCTION)

Railway has one environment, **production**, and it is live. Every command below that uses `DATABASE_URL` for Railway touches production. Terms "staging" in earlier documents were wrong and have been corrected.

## A. Where the earlier "scratch copy" came from
It was a local PostgreSQL database inside the cloud sandbox (`tdb`, created 2026-10-04, all 6,457 question rows written within one second, alembic revision `c3d4e5f6a7b8`). It was **not** copied from Railway: this session has never had Railway credentials or network access. I called it a "mirror of staging" without being able to show it matched anything on Railway; I cannot reconstruct the exact load command from the history I retain. Treat it only as a realistic local test database (same schema chain, about the same size, 380 AP History questions, 17 notes in app chapter 2). It says nothing about production's data or revision.

## B. What was validated (local databases only)
- Full chain from empty: `c68decc8a6c3` → … → `b8c9d0e1f2a3` (8 migrations), `alembic check` reports no drift; downgrade/upgrade of the four newest revisions works on empty tables.
- Step-by-step upgrade of a copy of `tdb` from `c3d4e5f6a7b8` through each revision to head: row counts and checksums of all 6,457 existing questions and 980 notes identical after every step.
- Canonical seed (5 units, 31 core + 4 supplementary chapters, 187 subtopics, 317 microtopics), 74 notes, 129 questions; repeat runs change nothing; legacy checksums identical; 80 learner pages return 200.
- Backup/restore rehearsal: `pg_dump -Fc` of the pre-change copy restored into a fresh database gave identical counts, checksums and alembic revision. Surgical rollback SQL (`docs/rollback_c1_additive.sql`) applied to a post-import copy restored the exact pre-change checksums, after which `alembic downgrade c3d4e5f6a7b8` ran cleanly.
- A defect found and fixed during this preparation: the 129 questions would have appeared in the generic subject Practice bank and the old `/practice/<subject>` route. They are now excluded there and reachable only on the canonical chapter pages (with their labels and sources). Test added.
- Test suites on this branch: see the handoff message for final numbers.

## C. Read-only production check (requested explicitly; PRODUCTION)
Please run against the **production** database, from a clean clone of the branch, and paste back only the output (never the URL):
```
set DATABASE_URL=<PRODUCTION Postgres URL>
python -m alembic current
psql "%DATABASE_URL%" -At -c "select count(*) from questions; select count(*) from notes; select count(*) from chapters; select count(*) from alembic_version; select to_regclass('syllabus_chapters') is not null, to_regclass('expanded_notes') is not null; select exists(select 1 from information_schema.columns where table_name='questions' and column_name='source_qid');"
```
All of these are SELECTs. If `psql` is not installed, send only the `alembic current` output; I will tell you the rest of the checks that matter. Also tell me: which git branch does Railway deploy from, and does a push to it auto-deploy? Pushing to that branch would deploy to production. Also read (do not change) the Railway service setting **Pre-deploy command**: `docs/DATABASE_MIGRATIONS.md` recommends `python -m alembic upgrade head` there, and if it is set, deploying the new code runs the migration automatically, so step 4 would also be step 3. Tell me what it says; the plan then either pins it to `b8c9d0e1f2a3` first (a settings change that needs your approval) or treats deploy and migration as one approved step.

## D. Backup (before any production write)
1. In the Railway dashboard, open the production Postgres service and check whether volume/database backups are enabled on your plan; if available, take a manual backup and note its timestamp. I cannot verify this from here.
2. Independent logical dump from your Windows machine (needs PostgreSQL client tools whose major version is at least the server's; check with `pg_dump --version` and `select version();`):
   `pg_dump --format=custom --no-owner --file=prod_before_c1_YYYYMMDD.dump "%DATABASE_URL%"`
3. Verify the dump before trusting it: `pg_restore --list prod_before_c1_YYYYMMDD.dump` (non-empty), then restore it into a throwaway LOCAL database and compare counts with the production counts from section C (`createdb verify_db`, `pg_restore --no-owner -d verify_db prod_before_c1_YYYYMMDD.dump`).
4. Capture the pre-change canonical inventory (needed by the rollback SQL; see its header) and record the pre-change numbers (questions, notes, chapters, `alembic current`) in a text file next to the dump. Keep both outside the repo (they contain learner data).
5. Because production is live, schedule a low-traffic window; learner progress, sessions and any admin note edits written after the backup would be lost by a full restore.

## E. Restore / rollback procedure (ordered from least to most destructive)
1. **Stop before writing**: every step is separate; if a preview shows anything unexpected, stop. Previews write nothing.
2. **Surgical rollback (preferred)**: all changes are additive, so remove only what was added: `docs/rollback_c1_additive.sql`. It deletes the batch's 129 questions and expanded notes, and only those canonical rows whose slug is **not** in a pre-change inventory that you capture from production BEFORE the seed (command in the file's header); canonical rows already present in production are therefore never removed. Guards print the counts; the file ends in ROLLBACK until you change it to COMMIT after the numbers match. Rehearsed locally with canonical rows pre-existing: they survived, the new ones went, totals returned to baseline. Needs its own approval and a backup. Then, if wanted, `python -m alembic downgrade c3d4e5f6a7b8` (the migrations refuse to downgrade while their tables hold rows). Warning: `d4e5f6a7b8c9` may already be applied on production by an earlier release; only downgrade to the revision production had before this change (from section C).
3. **Full restore (last resort)**: restore the dump into a NEW Railway Postgres service (or a local database to inspect), then repoint the app's `DATABASE_URL`. Do not restore over the live database. Accept the loss of writes since the backup.
4. Code rollback: redeploy the previous commit (`1303cf0`, or whatever production runs now). The added tables and columns are nullable/additive, so the old code runs unchanged against the new schema.

## F. Exact production changes that need your approval (each separately, in this order)
| # | Change | Command (run by you, from the Windows clean clone) | Writes |
|---|---|---|---|
| 0 | Backup verified (section D) | as above | none |
| 1 | Read-only revision/count check (section C) | as above | none |
| 2 | Push branch `feature/ap-history-v1-native` to GitHub, no deploy | `git push origin feature/ap-history-v1-native` (a non-deploy branch; confirm Railway's deploy branch first) | none on production |
| 3 | Schema migration, pinned target (never a moving `head`) | `python -m alembic upgrade b8c9d0e1f2a3` (run after confirming the production chain from section C; only the revisions between production's current one and the target run) | adds columns to `questions` (if missing) and tables `syllabus_*`, `chapter_source_map`, `expanded_notes`, `expanded_note_app_map`; no row changes |
| 4 | Deploy code that contains the learner pages | merge/push to Railway's deploy branch (never `main` without your say-so) | production redeploy |
| 5 | Seed canonical structure | preview: `python scripts/seed_ap_canonical.py`; apply: `... --apply --with-subtopics` | 5 units, 35 chapters, 187 subtopics, 317 microtopics |
| 6 | Load package notes | preview: `python scripts/import_ap_v1.py notes <pkg>`; apply: `... --apply --approval-ref "<ref>"` | 74 rows in `expanded_notes` |
| 7 | Import Chapter 1 questions | preview: `python scripts/import_ap_v1.py questions <pkg>`; apply: `... --apply --approval-ref "<ref>"` | 129 rows in `questions` |
| 8 | Post-checks | learner pages, counts, legacy checksums | none |
Steps 3 and 4 can be ordered either way for correctness; I recommend 3 first so the new code never runs against an old schema. Not included and not proposed: touching legacy questions, notes, the 17 sections, or `main`.

## G. Exact preview command (safe: writes nothing)
`python scripts/import_ap_v1.py questions C:\Users\AashrithaNagababu\Documents\Codex\AP_History_Working\05_claude_import\aph-u1-c01-closure-metadata-r1-20261009`
(and `notes` instead of `questions`). Expected on a seeded database: notes 74 to add; questions 129 to import, 0 overlaps, 0 unresolved links, validator errors 0, warnings 2.

## H. Revised package metadata-r1 (this is the package to use; same batch, not additional)
Folder `...\05_claude_import\aph-u1-c01-closure-metadata-r1-20261009`, `questions.jsonl` sha256 `a69d4a50aa1b85a0f682879c3ddac89df588d581f69265a8eee61f8febc2657d` (the original closure hash `1f1ad6fd…` is superseded; the two folders are never combined). Same `batch_id` and all 129 `source_qid`s, so a later repeat import is idempotent. Differences from the original, verified record by record: only `related_old_package_refs` of Q099 (adds `aph-u1c01-B006`); manifest gained `package_revision` and the new hash; `note_anchors.json` corrected (A05/A07/A10 titles, A04–A12 core connections); core and addendum text byte-identical.
Preview results on isolated local databases (production untouched):
- native validator: importable, 0 errors, 2 warnings (the two Telugu convention forms, kept as written);
- notes preview: 74 items (50 core, 12 addendum, 8 Group 1, 3 Group 1 connection blocks, 1 revision index), 0 problems, **0 warnings** (the earlier 12 anchor-list warnings are gone);
- questions preview with notes loaded: 129 to import (88 easy, 38 medium, 2 tough, 1 toughest; 44 H, 85 blank), 0 overlaps, 0 unresolved links; before the notes are loaded the importer reports 158 unresolved links and apply would refuse;
- a local database that already holds the older 64-question set: 36 overlap entries (2 same-stem: Q026 and Q099; 34 related-ref hits) and apply refuses until a human decides, as required; nothing deleted.

## I. Still open before any approval request
The package-owner decisions (three title discrepancies, nine missing core connections in `note_anchors.json`), the two Telugu spelling-convention warnings, the two overlap decisions (only relevant if the earlier 64-question set is ever present), the production revision from section C, and Railway's deploy branch.
