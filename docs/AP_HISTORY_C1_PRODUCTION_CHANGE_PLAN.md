# AP History fresh collection (Chapter 1): production change plan
**NOTHING IN THIS FILE HAS BEEN RUN ON PRODUCTION.** Railway has one environment, **production**, and it is live. Confirmed settings: repository `ravelberry9-lgtm/mcq-exam-app`, connected branch `release/secured-review`, **auto-deploy on**, **Pre-deploy command `python -m alembic upgrade head`**. Direction: `AP_HISTORY_FRESH_BUILD_DECISION_20261009.txt` (fresh collection; legacy banks are not merged; no wipe or progress reset implied) and `docs/AP_HISTORY_FRESH_COLLECTION_DESIGN.md`.

## A. What is known about production (user-supplied, 2026-10-09)
Source: `PRODUCTION_READONLY_FINDINGS_20261009.txt`, read through the Railway database UI (SELECTs only). **These are UI checks, not the runbook's full snapshot, and not a verified backup.** The fingerprints in that file use a different SQL method and are not comparable with `compare_snapshots.py` output.

| Fact | Value |
|---|---|
| Alembic revision | `a7b8c9d0e1f2` (canonical syllabus and microtopic migrations are already applied) |
| Server | PostgreSQL 18.6 |
| Rows | questions 7,778 (AP History 1,701); notes 980; chapters 194 |
| Canonical taxonomy | already populated: 5 units, 35 chapters, 187 subtopics, 317 microtopics; Chapter 1 slug and its six subtopic slugs match the package |
| `expanded_notes` table | absent |
| Fresh batch | no `source_qid` rows at all; closure batch rows 0 |
| Older Chapter 1 set | **present**: 64 rows (`import_ref`/`source_qid` like `aph-u1c01-…`); the Q026 and Q099 older refs each exist once |
| Backups | Railway backups/PITR need Pro; none created, listed or restored. A separately verified logical dump is the available route |

What this changes from my earlier assumptions (corrected, no longer in the plan): production is **not** at `d4e5f6a7b8c9`, it does **not** hold 6,457 questions, the taxonomy is **not** to be seeded, and the older 64 are **not** hypothetical.

## B. Pending schema (against `a7b8c9d0e1f2`)
Two additive migrations on my branch, applied in order by the Pre-deploy command when the commit is merged: `b8c9d0e1f2a3` (expanded notes tables) then `c9d0e1f2a3b4` (nullable `collection_id` on `questions` and `expanded_notes`, plus `chapter_collection_setting` and `chapter_collection_log`). No existing row changes. The nullable column adds are metadata-only on PostgreSQL; the two new indexes are built on 7,778 rows and the notes table (a brief lock). Verified locally: full chain from empty; upgrade from `a7b8c9d0e1f2` on a populated copy; downgrade of both refuses while they hold data and runs cleanly once empty. **Not yet verified: that the deployed commit is what I think it is** (see I.1).

## C. What the confirmed Railway settings mean
1. A push or merge to `release/secured-review` is a production deploy **and** migration in one automatic step (`alembic upgrade head` of the deployed commit, not pinned). Single head of my branch: `c9d0e1f2a3b4` (check with `python -m alembic heads` before any merge). Pushing `feature/ap-history-v1-native` does not deploy.
2. **Code rollback is not "redeploy the old commit"**: with the DB at `c9d0e1f2a3b4` the old code's pre-deploy fails with "Can't locate revision". Safe route: (a) if the collection was loaded, the surgical data rollback below; then `alembic downgrade a7b8c9d0e1f2` from the feature checkout; then redeploy the old commit; or (b) temporarily clear the Pre-deploy command (its own approval).
3. The additive schema is safe for the **old** code to keep running against (it ignores the new columns and tables). Old code does not know about `collection_id`, so the collection's questions must be loaded **only after the new code is live**; otherwise the old generic Practice bank would list them.
4. The learner switch defaults to **legacy**, so merging the code changes nothing a learner sees. Loading the collection also changes nothing a learner sees until a chapter is switched.
5. Seed and import commands run from your machine against the production URL; auto-deploy does not run them.

## D. The older 64 and the 129 (decision applied)
Legacy stays exactly as it is, **including the older 64**: they carry `collection_id` NULL, are never edited, hidden, merged or deleted by any step here, and keep their ids and learner history. The fresh collection is a separate set (`collection_id = ap-history-fresh-v1`) deduplicated only against itself (`--overlap-scope collection`; the guard is not disabled). Overlaps with legacy rows are listed, not acted on. Local rehearsal with the older 64 present (Chapter 1 chapter id and `source='codex_generated'` deliberately set on them, the worst case for the old marker): scope `all` reports 36 overlap entries and refuses; scope `collection` imports 129, reports the same 36 as informational, and the 64 older rows are byte-identical afterwards and still served by the legacy chapter practice. The 36 entries are **30 distinct fresh questions against 30 distinct older rows**: 2 same-stem (Q026, Q099) and 34 where the package lists an older ref as related. They are overlapping *facts*, not 36 duplicate rows. Why the explicit `collection_id` matters: the older rows may or may not carry a canonical chapter id in production (to be read, I.2); learner filtering, duplicate scoping and the switch use only `collection_id`.

## E. Production changes needing your approval (separately, in order)
| # | Change | How | Effect on production |
|---|---|---|---|
| 0 | Runbook steps 0–2: **full read-only snapshot** (the UI findings do not replace it) | `docs/PRODUCTION_READONLY_CHECK_AND_BACKUP.md` | none |
| 1 | **Verified backup** (runbook steps 3–7; required result `BACKUP VERIFIED (content identical)`) | `pg_dump` 18, isolated restore, compare | none |
| 2 | Push `feature/ap-history-v1-native` (non-deploy branch) | `git push origin feature/ap-history-v1-native` | none |
| 3 | Pre-merge gate | `alembic heads` prints only `c9d0e1f2a3b4 (head)`; suites green; exact commit hash recorded; I.1 confirmed | none |
| 4 | **Merge that exact commit into `release/secured-review` and push** (= deploy + two additive migrations) | by you, quiet window, watching the deploy log. Optional: first pin Pre-deploy to `python -m alembic upgrade c9d0e1f2a3b4` (own approval) and restore `head` after | new tables/columns, no row changes; learners see no change (switch defaults to legacy) |
| 5 | Post-deploy checks | `/healthz`, `/learn/`, AP History pages, snapshot again (revision `c9d0e1f2a3b4`; content fingerprints of questions and notes unchanged apart from the added columns) | none |
| 6 | **Canonical taxonomy: verify only.** Step 0's snapshot confirms 5/35/187/317. No seed unless something is shown missing, and then only as its own add-only approval | | none |
| 7 | Load Chapter 1 notes (74) | `python scripts\import_ap_v1.py notes <pkg>` then `... --apply --approval-ref "<ref>"` | 74 `expanded_notes` rows, `collection_id` set |
| 8 | Load the 129 questions | `python scripts\import_ap_v1.py questions <pkg> --overlap-scope collection` then `... --apply --approval-ref "<ref>" --overlap-scope collection` | 129 rows, `collection_id` set; legacy untouched; hidden from learners |
| 9 | Readiness review | admin page `/admin/collections` shows every check; admin preview of the chapter | none |
| 10 | **Switch Chapter 1 learners to the fresh collection** (admin page; logged with name, address, time) | refused automatically unless every readiness check passes; reversible at any time without data change | learners of that chapter see the fresh notes, practice and links |
Approval references are audit labels; each row needs your explicit approval at that time. `main` is untouched. Retiring or archiving any legacy row (including the older 64) is **not** part of this plan and would be a separate plan and approval.

## F. Backup
Runbook steps 3–7 (updated for server 18): `pg_dump --format=custom`, readable-dump check and SHA256, restore into an isolated non-production database, snapshot it, `compare_snapshots.py` must print `BACKUP VERIFIED (content identical)`. Railway's own backup feature needs Pro, so the logical dump is the primary route; I cannot verify anything on Railway. The approval request for any production change comes only after you report that line and the dump hash.

## G. Restore / rollback, least to most destructive
1. Switch learners back to legacy (admin page): no data changes; the fresh pages stay reachable only for review links of that collection.
2. **Surgical data rollback** `docs/rollback_fresh_collection.sql` (own approval, after backup verification): removes only rows with `collection_id = ap-history-fresh-v1`, the switch rows and learner-state rows attached to those fresh questions (it prints how many first). Legacy rows, the taxonomy and all other subjects are never matched. Rehearsed locally (guards 0/0/0, legacy count unchanged).
3. `python -m alembic downgrade a7b8c9d0e1f2` (refuses while the new tables or tagged rows hold data), then redeploy the old commit per C.2.
4. Full restore from the verified dump into a NEW Railway Postgres service (never over the live one); accept loss of writes since the dump.

## H. Local results (isolated databases, not production)
Learner switch: database setting per canonical chapter slug, legacy default; readiness gate (12 checks); admin-only (PIN session + CSRF); each change logged with the name typed, remote address, time and readiness result; switching back preserves both collections and all learner history (row-for-row comparison across four consecutive switches); links, practice and notes follow the setting. Package `aph-u1-c01-closure-metadata-r1-20261009`, `questions.jsonl` sha256 `a69d4a50aa1b85a0f682879c3ddac89df588d581f69265a8eee61f8febc2657d` (the folders are never combined).

## I. Open before any approval request
1. **Which commit is deployed.** Revision `a7b8c9d0e1f2` implies the canonical-schema code is live, but I have not seen the deployed commit. Read it in Railway (Deployments → latest commit hash) and confirm `release/secured-review` contains it, so my merge is a clean fast-forward-like addition and not a surprise.
2. **The older 64 in production:** do they carry `syllabus_chapter_id` or `chapter_id`? The updated `readonly_snapshot.py` prints this (`older C1 rows`).
3. Full snapshot and verified backup (E.0, E.1).
4. Deploy window, and whether to pin Pre-deploy for step 4.
5. Content: Telugu convention warnings (Q075, R2-Q004) kept as written; Telugu interface strings are drafts; content is author-reviewed only. The switch actor is a name typed on the form because the admin gate is a shared PIN.
