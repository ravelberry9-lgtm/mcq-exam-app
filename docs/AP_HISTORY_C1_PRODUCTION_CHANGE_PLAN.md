# Chapter 1 closure import: production change plan (NOTHING IN THIS FILE HAS BEEN RUN ON PRODUCTION)

Railway has one environment, **production**, and it is live. Confirmed settings: repository `ravelberry9-lgtm/mcq-exam-app`, connected branch `release/secured-review`, **auto-deploy on**, **Pre-deploy command `python -m alembic upgrade head`**. Every command below that uses `DATABASE_URL` for Railway touches production. Terms "staging" in earlier documents were wrong and have been corrected.

## A. Where the earlier "scratch copy" came from
It was a local PostgreSQL database inside the cloud sandbox (`tdb`, created 2026-10-04, all 6,457 question rows written within one second, alembic revision `c3d4e5f6a7b8`). It was **not** copied from Railway: this session has never had Railway credentials or network access. I called it a "mirror of staging" without being able to show it matched anything on Railway; I cannot reconstruct the exact load command from the history I retain. Treat it only as a realistic local test database (same schema chain, about the same size, 380 AP History questions, 17 notes in app chapter 2). It says nothing about production's data or revision.

## B. What was validated (local databases only)
- Full chain from empty: `c68decc8a6c3` → … → `b8c9d0e1f2a3` (8 migrations), `alembic check` reports no drift; downgrade/upgrade of the four newest revisions works on empty tables.
- Step-by-step upgrade of a copy of `tdb` from `c3d4e5f6a7b8` through each revision to head: row counts and checksums of all 6,457 existing questions and 980 notes identical after every step.
- Canonical seed (5 units, 31 core + 4 supplementary chapters, 187 subtopics, 317 microtopics), 74 notes, 129 questions; repeat runs change nothing; legacy checksums identical; 80 learner pages return 200.
- Backup/restore rehearsal: `pg_dump -Fc` of the pre-change copy restored into a fresh database gave identical counts, checksums and alembic revision. Surgical rollback SQL (`docs/rollback_c1_additive.sql`) applied to a post-import copy restored the exact pre-change checksums, after which `alembic downgrade c3d4e5f6a7b8` ran cleanly.
- A defect found and fixed during this preparation: the 129 questions would have appeared in the generic subject Practice bank and the old `/practice/<subject>` route. They are now excluded there and reachable only on the canonical chapter pages (with their labels and sources). Test added.
- Test suites on this branch: see the handoff message for final numbers.

## C. What the confirmed Railway settings mean
1. **A push or merge to `release/secured-review` is a production deploy AND a production migration**, in one automatic step: Railway runs `alembic upgrade head` of the *deployed commit* before the new code starts. `head` is not pinned: it is whatever the commit contains. For this branch it is exactly `b8c9d0e1f2a3` (single head; check with `python -m alembic heads` before any merge).
2. Pushing `feature/ap-history-v1-native` (a branch Railway is not connected to) does not deploy. Nothing in this plan pushes or merges to `release/secured-review` until you approve step 4 below.
3. **Code rollback is not "just redeploy the old commit".** Verified locally: after the database is at `b8c9d0e1f2a3`, the old code (`1303cf0`) fails its pre-deploy with `Can't locate revision identified by 'b8c9d0e1f2a3'`, so a Railway redeploy or rollback to the old commit would not start (reports exist that rollbacks also run the pre-deploy command). Two safe ways, both rehearsed or checkable locally: (a) remove the added rows with the rollback SQL, run `alembic downgrade d4e5f6a7b8c9` against production from the feature checkout, then redeploy the old commit (old code's `upgrade head` was a clean no-op afterwards); or (b) temporarily clear the Pre-deploy command in Railway, redeploy the old commit, restore the command. Option (a) is preferred; (b) is a settings change that needs its own approval.
4. The additive schema is safe for the **old** code to keep running against: the old code served its main pages (home, subjects, practice banks) normally on a database already at `b8c9d0e1f2a3`. So a failed or interrupted deploy leaves the live site working.
5. **Order matters for data**: the old code does not exclude the new questions from the generic subject Practice bank (the fix is in the new code). Therefore the 129 questions are imported only **after** the new code is live, never before.
6. Seed and import commands run from your machine against the production database URL. Auto-deploy does not run them.

## D. Production Alembic revision and row counts (read-only; PRODUCTION)
Run `docs/PRODUCTION_READONLY_CHECK_AND_BACKUP.md` steps 0–2. It prints the revision, server version, row counts, the `questions` column flags and content fingerprints, and writes the canonical-slug inventory the rollback SQL needs. SELECT-only, read-only session, no connection details printed (tested). Expected, if `1303cf0` deployed successfully: `d4e5f6a7b8c9`. Then the migrations that will run are `f6a7b8c9d0e1`, `a7b8c9d0e1f2`, `b8c9d0e1f2a3` (all additive; verified locally from `c3d4e5f6a7b8` step by step with no change to existing rows). If production shows a different revision, stop and tell me.

## E. Backup (before any approval request)
Runbook steps 3–7 of the same file: `pg_dump --format=custom`, readable-dump check and SHA256, restore into an isolated non-production database, snapshot that copy and run `compare_snapshots.py`. Required result: `BACKUP VERIFIED (content identical)`. The approval request for production changes is made only after you report that line (plus the dump hash) back. If your Railway plan has Postgres backups, also take one manually (not verifiable from here).
Rehearsed locally: dump of a pre-change copy restored elsewhere gave identical revision, counts and fingerprints; the compare tool flags a changed row, missing rows or a wrong revision (unit-tested).

## F. Restore / rollback, from least to most destructive
1. Stop at any unexpected preview or snapshot; previews and snapshots write nothing.
2. **Surgical data rollback** (`docs/rollback_c1_additive.sql`, after backup verification and your explicit approval): deletes only this batch's questions and expanded notes and only canonical rows absent from the pre-change inventory. Rehearsed with canonical rows pre-existing (they survive) and with none (all removed).
3. **Schema rollback** (only if wanted): `python -m alembic downgrade d4e5f6a7b8c9` (refuses while the new tables hold rows, so step 2 must come first). Then redeploy old code per C.3(a).
4. **Full restore (last resort)**: restore the verified dump into a NEW Railway Postgres service, point the app's `DATABASE_URL` at it. Never restore over the live database. Accept the loss of writes since the backup (learner progress, sessions, admin note edits).

## G. Exact production changes needing your approval (separately, in order)
| # | Change | How | Effect on production |
|---|---|---|---|
| 0 | Read-only snapshot (D) | runbook steps 0–2 | none (SELECT only) |
| 1 | Backup taken and **verified by isolated restore** (E) | runbook steps 3–7 | none |
| 2 | Push `feature/ap-history-v1-native` to GitHub (not the deploy branch) | `git push origin feature/ap-history-v1-native` | none (Railway ignores it); needs your OK only because it publishes code |
| 3 | Pre-merge gate | `python -m alembic heads` must print only `b8c9d0e1f2a3 (head)`; full test suite green; the exact commit hash to merge recorded | none |
| 4 | **Merge that exact commit into `release/secured-review` and push** (= deploy + migration to `b8c9d0e1f2a3`) | by you, in a low-traffic window, watching Railway's deploy log | adds columns/tables, no row changes; new learner pages go live; Railway runs `upgrade head`. Optional safer variant: first pin the Pre-deploy command to `python -m alembic upgrade b8c9d0e1f2a3` (a settings change, own approval), restore `head` afterwards |
| 5 | Post-deploy checks | `/healthz`, `/learn/`, subject pages, `readonly_snapshot` again (revision must be `b8c9d0e1f2a3`, content fingerprints of questions/notes unchanged except the added columns) | none |
| 6 | Seed canonical structure | preview `python scripts\seed_ap_canonical.py`, apply `... --apply --with-subtopics` | 5 units, 35 chapters, 187 subtopics, 317 microtopics |
| 7 | Load package notes | `python scripts\import_ap_v1.py notes <pkg>` then `... --apply --approval-ref "<ref>"` | 74 `expanded_notes` rows |
| 8 | Import Chapter 1 questions | `python scripts\import_ap_v1.py questions <pkg>` then `... --apply --approval-ref "<ref>"` | 129 `questions` rows (only after step 4) |
| 9 | Final checks | learner pages, counts, legacy fingerprints | none |
Approval references are audit labels; each row above still needs your explicit approval at the time. No legacy question, note or the 17 sections is touched. `main` is untouched.

## H. Revised package metadata-r1 (the package to use; same batch, not additional)
Folder `...\05_claude_import\aph-u1-c01-closure-metadata-r1-20261009`, `questions.jsonl` sha256 `a69d4a50aa1b85a0f682879c3ddac89df588d581f69265a8eee61f8febc2657d` (the original closure hash `1f1ad6fd…` is superseded; the folders are never combined). Same `batch_id` and all 129 `source_qid`s. Preview on isolated local databases: validator importable, 0 errors, 2 warnings (Telugu convention forms, kept as written); notes 74 items, 0 problems, 0 warnings; questions 129 to import, 0 overlaps, 0 unresolved links. A local database that already holds the older 64 questions gives 36 overlap entries (Q026 and Q099 same-stem plus 34 related-reference hits) and apply refuses until you decide. Exact preview commands (write nothing):
`python scripts\import_ap_v1.py notes C:\Users\AashrithaNagababu\Documents\Codex\AP_History_Working\05_claude_import\aph-u1-c01-closure-metadata-r1-20261009`
`python scripts\import_ap_v1.py questions <same path>`

## I. Still open before any approval request
Production revision and counts (D), verified backup (E), Railway auto-deploy timing window, and the decision on pinning the Pre-deploy command for step 4.
