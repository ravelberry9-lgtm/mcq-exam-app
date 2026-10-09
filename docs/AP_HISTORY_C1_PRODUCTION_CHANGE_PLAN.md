# AP History fresh collection (Chapter 1): production change plan
**NOTHING IN THIS FILE HAS BEEN RUN ON PRODUCTION.** Railway has one environment, **production**, and it is live. Confirmed settings: repository `ravelberry9-lgtm/mcq-exam-app`, connected branch `release/secured-review`, **auto-deploy on**, **Pre-deploy command `python -m alembic upgrade head`**. Direction: `AP_HISTORY_FRESH_BUILD_DECISION_20261009.txt` (fresh collection; legacy banks are not merged; no wipe or progress reset implied) and `docs/AP_HISTORY_FRESH_COLLECTION_DESIGN.md`.

## A. Verified production baseline (2026-10-09, read-only; nothing changed)
Sources: `PRODUCTION_READONLY_FINDINGS_20261009.txt` and `PRODUCTION_BACKUP_VERIFIED_20261009.txt`.
| Fact | Value |
|---|---|
| Live deployment | `eb98f16c-963d-4af0-9669-129ac66f8af3`, branch `release/secured-review`, 2026-10-09 04:57 IST |
| **Live commit** | `709b0fc82ae0a8178bb1c41365c68c3f4b5b1ace` "Fix AP History canonical navigation and chapter practice membership" (its parent is `842a696`, the commit my branch was built on) |
| Alembic revision | `a7b8c9d0e1f2` (the live commit adds no migration) |
| Server / tools | PostgreSQL 18.6 |
| Rows | questions 7,778 (AP History 1,701); notes 980; chapters 194; subjects 11 |
| Canonical taxonomy | already populated: 5 units, 35 chapters, 187 subtopics, 317 microtopics; Chapter 1 slugs match the package |
| Older Chapter 1 set | 64 rows, all legacy `chapter_id = 107`, **zero** canonical `syllabus_chapter_id` |
| Fresh batch / expanded notes | none (`source_qid` rows 0, `expanded_notes` table absent) |
| **Backup** | **BACKUP VERIFIED (all public table content identical)**: custom-format dump, 3,366,893 bytes, SHA256 `c3cf2b3f2d0e88db95ec12898fb103844e23902abef295710c591719761405b7`, in a private folder outside any Git repository (`...\AP_History_Private_Backups\c1_20261009_133151`). `pg_restore` into a freshly initialised loopback-only local cluster; 22 public tables compared by full-row fingerprints, schema metadata and canonical inventories equal; revision equal. Limits stated by the checker: not independently compared are sequence values, roles, extensions and Railway platform settings; the original runbook scripts were not used (a different but equivalent method). The dump contains learner data and must never be committed or published. |

## B. Integration with the live commit (done locally; nothing pushed)
`gh/release/secured-review` (`709b0fc`) was fetched from the public repository and merged into `feature/ap-history-v1-native`. The merge conflicts and decisions:
* `syllabus_view.py` and `syllabus_chapter.html`: merged by hand. The live commit's `chapter_questions()` (legacy canonical practice membership by `note_target_slug` prefix) now also filters `collection_id IS NULL`; without that, fresh questions (whose slugs share the prefix) would have appeared in the **live** legacy practice.
* Practice URL: the live route `/learn/ap-history/<slug>/practice` (`ap_history_practice`) is kept and is now the single practice URL per chapter. It serves the legacy canonical bank by default (unchanged for learners) and the fresh collection only when the chapter's learner setting is switched (or `?collection=fresh` for an administrator).
* Two tests of the live commit were stale (`test_seeding_changes_no_existing_content_and_learn_pages_are_identical` fails on `709b0fc` itself, because the live commit made `/learn/subject/ap_history` redirect and changed the `/learn/` tile). Updated to assert the intended behaviour; no app behaviour changed for it.
* Result: the merge commit is a **descendant of `709b0fc`, so pushing it to `release/secured-review` is a fast-forward** (checked with `git merge-base --is-ancestor`). Diff against the live commit: 38 files, additive, plus the two migrations.
* **Page-for-page check against the live code** (same populated local database at `a7b8c9d0e1f2`, with 84 canonical-tagged legacy rows): rendered 17 learner URLs with the live commit, ran `alembic upgrade head`, rendered them again with the merged code. 16 identical; the chapter page differs only by whitespace and the CSRF token. Questions, notes and syllabus rows hash identically before and after the migration.

## C. What the confirmed Railway settings mean
1. A push or merge to `release/secured-review` is a production deploy **and** migration in one automatic step (`alembic upgrade head` of the deployed commit, not pinned). Single head of my branch: `c9d0e1f2a3b4` (check with `python -m alembic heads` before any merge). Pushing `feature/ap-history-v1-native` does not deploy.
2. **Code rollback is not "redeploy the old commit"**: with the database at `c9d0e1f2a3b4` the live commit `709b0fc` fails its pre-deploy with "Can't locate revision". The procedure is in G.2.
3. The additive schema is safe for the **old** code to keep running against (it ignores the new columns and tables). Old code does not know about `collection_id`, so the collection's questions must be loaded **only after the new code is live**; otherwise the old generic Practice bank would list them.
4. The learner switch defaults to **legacy**, so merging the code changes nothing a learner sees. Loading the collection also changes nothing a learner sees until a chapter is switched.
5. Seed and import commands run from your machine against the production URL; auto-deploy does not run them.

## D. The older 64 and the 129 (decision applied)
Legacy stays exactly as it is, **including the older 64**: they carry `collection_id` NULL, are never edited, hidden, merged or deleted by any step here, and keep their ids and learner history. The fresh collection is a separate set (`collection_id = ap-history-fresh-v1`) deduplicated only against itself (`--overlap-scope collection`; the guard is not disabled). Overlaps with legacy rows are listed, not acted on. Local rehearsal with the older 64 present (Chapter 1 chapter id and `source='codex_generated'` deliberately set on them, the worst case for the old marker): scope `all` reports 36 overlap entries and refuses; scope `collection` imports 129, reports the same 36 as informational, and the 64 older rows are byte-identical afterwards and still served by the legacy chapter practice. The 36 entries are **30 distinct fresh questions against 30 distinct older rows**: 2 same-stem (Q026, Q099) and 34 where the package lists an older ref as related. They are overlapping *facts*, not 36 duplicate rows. Production check (A): the older 64 are legacy `chapter_id = 107` with no canonical chapter id, so the earlier assumption that they might carry one does not apply; the explicit `collection_id` still keeps learner filtering, duplicate scoping and the switch independent of `source` and `syllabus_chapter_id`.

## E. Production changes needing your approval (separately, in order)
| # | Change | How | Effect on production |
|---|---|---|---|
| 0 | Read-only snapshot | **done** (A) | none |
| 1 | Verified backup | **done** (A); refresh it just before step 4 if a long time has passed or learners have been active (a quick read-only re-count against the backup is enough to see the drift) | none |
| 2 | Push `feature/ap-history-v1-native` (non-deploy branch; optional, gives a reviewable PR and a backup of the work) | `git push origin feature/ap-history-v1-native` | none |
| 3 | Pre-merge gate | `alembic heads` prints only `c9d0e1f2a3b4 (head)`; suites green; exact commit hash equals the release candidate in `RELEASE_CANDIDATE.txt` | none |
| 4 | **Fast-forward `release/secured-review` to the release commit and push** (= automatic deploy + two additive migrations) | by you, quiet window, watching the deploy log. **Legacy stays active; no import and no switch happens in this step.** Optional: first pin Pre-deploy to `python -m alembic upgrade c9d0e1f2a3b4` (own approval) and restore `head` after | new tables/columns, no row changes; learners see no change (switch defaults to legacy) |
| 5 | Post-deploy checks | `/healthz`, `/learn/`, AP History pages, snapshot again (revision `c9d0e1f2a3b4`; content fingerprints of questions and notes unchanged apart from the added columns) | none |
| 6 | **Canonical taxonomy: verify only** (already 5/35/187/317 in the verified baseline). No seed | | none |
| 7 | Load Chapter 1 notes (74) | `python scripts\import_ap_v1.py notes <pkg>` then `... --apply --approval-ref "<ref>"` | 74 `expanded_notes` rows, `collection_id` set |
| 8 | Load the 129 questions | `python scripts\import_ap_v1.py questions <pkg> --overlap-scope collection` then `... --apply --approval-ref "<ref>" --overlap-scope collection` | 129 rows, `collection_id` set; legacy untouched; hidden from learners |
| 9 | Readiness review | admin page `/admin/collections` shows every check; admin preview of the chapter | none |
| 10 | **Switch Chapter 1 learners to the fresh collection** (admin page; logged with name, address, time) | refused automatically unless every readiness check passes; reversible at any time without data change | learners of that chapter see the fresh notes, practice and links |
Approval references are audit labels; each row needs your explicit approval at that time. `main` is untouched. Retiring or archiving any legacy row (including the older 64) is **not** part of this plan and would be a separate plan and approval.

## F. Backup
Done and verified (A). Keep the dump private and out of every repository and shared folder. For rollback by restore, restore only into a NEW Railway Postgres service, never over the live one.

## G. Rollback, from least to most destructive
1. **Normal rollback = the learner setting.** After a collection load and switch, setting the chapter back to legacy (admin page, always allowed) restores exactly what learners saw before; it deletes nothing and keeps all learner history and both collections. Before any switch, learners already see only legacy.
2. **If the deploy itself must be undone** (before any collection data exists, the new tables are empty): `python -m alembic downgrade a7b8c9d0e1f2` from the feature checkout against production (both new migrations refuse only while they hold data, so this is clean), then redeploy `709b0fc`. Do not redeploy `709b0fc` first: with the database at `c9d0e1f2a3b4` the old code's pre-deploy fails with "Can't locate revision". Alternative: temporarily clear the Pre-deploy command (own approval). Because the schema change is additive, the live commit also keeps running against the migrated database if the new code has to be abandoned quickly.
3. **Removing the collection itself** (only if the 129 questions or 74 notes must be withdrawn; own approval): `docs/rollback_fresh_collection.sql` removes only rows with `collection_id = ap-history-fresh-v1`, the switch rows and learner state on those fresh questions (it prints the counts first), then the Alembic downgrade above. Not the normal path.
4. **Full restore** from the verified dump into a new service; accept loss of writes since the dump.

## H. Local results (isolated databases, not production)
Learner switch: database setting per canonical chapter slug, legacy default; readiness gate (12 checks); admin-only (PIN session + CSRF); each change logged with the name typed, remote address, time and readiness result; switching back preserves both collections and all learner history (row-for-row comparison across four consecutive switches); links, practice and notes follow the setting. Package `aph-u1-c01-closure-metadata-r1-20261009`, `questions.jsonl` sha256 `a69d4a50aa1b85a0f682879c3ddac89df588d581f69265a8eee61f8febc2657d` (the folders are never combined).

## I. What remains before approval can be given
1. Your approval of step 4 (deploy + migration) with a window, and whether to pin Pre-deploy to `upgrade c9d0e1f2a3b4` first (own approval). My recommendation: no pin, since the only pending migrations are the two additive ones; pin only if you prefer a hard stop.
2. Later, separately: collection load (steps 7–8), readiness review (9) and the switch (10). Not part of the deploy approval.
3. Content: Telugu convention warnings (Q075, R2-Q004) kept as written; Telugu interface strings are drafts; content is author-reviewed only. The switch actor is a name typed on the form because the admin gate is a shared PIN.
