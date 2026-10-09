# Production read-only check and verified backup (Windows Command Prompt runbook)

Everything here targets **PRODUCTION** (the only Railway environment). Steps 1–7 are read-only on production. Nothing here changes production, pushes, merges or deploys. Never paste a connection URL into chat or a file; paste only the printed summaries.

## 0. Get the code locally without touching the deploy branch
In your clean clone: `git fetch ..\mcq_exam_app_fixed\mcq_app\_review\ap-history-v1-native.bundle feature/ap-history-v1-native:feature/ap-history-v1-native` then `git checkout feature/ap-history-v1-native`. This is a local branch; Railway only watches `release/secured-review`, so nothing deploys. Then: `python -m venv venv`, `venv\Scripts\activate`, `pip install -r requirements.txt`.

## 1. Connection (production, session only)
Copy the Postgres service's **public** connection URL from Railway (service → Variables or Connect). In Command Prompt: `set DATABASE_URL=<paste>`. It lives only in that window; close the window afterwards (or `set DATABASE_URL=`). Avoid putting it in a file or a command history you share.

## 2. Read-only snapshot of production (answers: Alembic revision and row counts)
`python scripts\prod_ops\readonly_snapshot.py --label PRODUCTION --out prod_before.json --inventory-csv pre_change_inventory.csv`
The session is opened read-only on the server, only SELECTs run, and the URL/host/user/password are never printed (tests prove this). Paste back the printed summary (revision, server version, row counts, column flags, fingerprints). Expected if `release/secured-review` at `1303cf0` deployed successfully: `alembic_version` = `d4e5f6a7b8c9`, no `syllabus_*` tables, `import_ref` column present, 6,457-ish questions. Anything else changes the plan: tell me before going on.
Keep `prod_before.json` and `pre_change_inventory.csv`; the rollback SQL needs the inventory.

## 3. Backup tool check
`pg_dump --version` must have a major version at least equal to the server version printed in step 2 (e.g. server 16 → pg_dump 16 or newer). If it is older or missing, install the matching PostgreSQL client tools (only the command-line tools are needed) before continuing.

## 4. Take the backup
`pg_dump --format=custom --no-owner --no-acl --file=prod_before_c1.dump "%DATABASE_URL%"`
(custom format is compressed and restorable with pg_restore; pg_dump reads one consistent snapshot). Then:
`pg_restore --list prod_before_c1.dump > nul && echo dump-readable` and `certutil -hashfile prod_before_c1.dump SHA256` (note the hash).
The file contains learner device ids and progress: keep it private, outside the repo and out of cloud folders you share.
Also, if your Railway plan offers Postgres backups, take a manual one and note its timestamp (I cannot check this).

## 5. Restore into an isolated database that is NOT production
Pick one, matching the server's major version:
- Docker: `docker run --name verify-pg -e POSTGRES_PASSWORD=verify -p 54329:5432 -d postgres:16`, then `set RESTORE_URL=postgresql://postgres:verify@localhost:54329/postgres`
- or a local PostgreSQL install: create an empty database `verify_restore` and set `RESTORE_URL` to it.
Do not restore into the production database or into any service of the production project. Then:
`pg_restore --no-owner --no-acl --dbname="%RESTORE_URL%" prod_before_c1.dump`

## 6. Snapshot the restored copy and compare
`set DATABASE_URL=%RESTORE_URL%` (this overwrites the production URL in this window: good)
`python scripts\prod_ops\readonly_snapshot.py --label BACKUP-RESTORE --out restored.json`
`python scripts\prod_ops\compare_snapshots.py prod_before.json restored.json`
Required result: `RESULT: BACKUP VERIFIED (content identical)`. Same Alembic revision, same row counts and the same content fingerprints for every content table. Activity tables (learner progress, sessions) may differ by a few rows if the site was used between the snapshot and the dump; that is reported as a note, not a failure. If it says NOT VERIFIED, do not continue: re-run steps 2, 4 and 6 in quick succession (or in a quiet window) and send me the output.

## 7. Clean up
Stop the Docker container (`docker rm -f verify-pg`) or drop the restore database; clear `DATABASE_URL`/`RESTORE_URL`. Keep the dump, its SHA256, `prod_before.json` and `pre_change_inventory.csv` together as the pre-change record.

## What each script does and does not do
`readonly_snapshot.py`: SELECT-only, read-only session, scrubbed errors; writes only the local JSON/CSV files you name. `compare_snapshots.py`: reads two JSON files. Neither imports, seeds, migrates or deploys.
