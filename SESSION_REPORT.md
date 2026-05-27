# Session Report — APPSC v3 Rebuild (Phase 2 + 3)

**Date:** 2026-05-27  
**Agent:** Claude Sonnet 4.6 (Cowork session)  
**Handoff from:** Phase 1 complete  
**Budget:** ~1 hour autonomous run

---

## Phases Completed

| Phase | Status | Tag |
|---|---|---|
| 0 — Scaffold | ✅ Complete | `phase-1-complete` |
| 1 — Core read flow + Group 2 seed | ✅ Complete | `phase-1-complete` |
| 2 — Migration from `_legacy/` | ✅ Complete | `phase-3-complete` |
| 3 — Admin CMS paste-HTML editor | ✅ Complete | `phase-3-complete` |

---

## Git State

- **Commits:** 2 new commits on `main`
  - `3cbedfd` — Phase 0+1 scaffold + core read flow + Group 2 syllabus seed
  - `aa02b50` — Phase 2 migration + Phase 3 admin CMS
- **Tags:** `phase-1-complete`, `phase-3-complete`
- **Push status:** ❌ Could not push (no credentials in sandbox). Run manually:
  ```
  git push origin main --tags
  ```

---

## Migration Counts (Phase 2)

| Metric | Value |
|---|---|
| Questions migrated | **6,737** (target ~6,737 ✓) |
| Chapters created | 196 |
| Notes created | 6,257 |
| Exam sessions migrated | 7 |
| Migration errors | **0** |

---

## Phase 5 + 4.5 Addition (Session 3 — 2026-05-27)

### Test totals: 67/67 passing
| Suite | Tests |
|---|---|
| test_smoke | 6 |
| test_phase1 | 9 |
| test_admin | 8 |
| test_notes | 17 |
| test_exam_session | 16 |
| test_study_plan | 11 |

---

## Session 4 — Railway Go-Live + Schema Fix (2026-05-27)

### What happened
All Phase 5 + 4.5 files pushed to GitHub via CM6 API. Railway auto-deployed each commit.

### Schema fix
`_patch_schema()` added to `app/__init__.py`: adds `questions.subject_id` via
`ALTER TABLE … ADD COLUMN IF NOT EXISTS` when missing, then calls `db.create_all()`.

### Smoke tests (live at `mcq-exam-app-production.up.railway.app`)

| Route | Result |
|---|---|
| `GET /healthz` | `{"phase":"1","status":"ok"}` ✅ |
| `GET /` | 200 ✅ |
| `GET /subjects` | 200 (empty, needs seeding) ✅ |
| `GET /plan/new` | 200 ✅ |
| `GET /plan/` | 302 → `/plan/new` ✅ |
| `GET /admin/` | 302 → `/admin/login` ✅ |

### Items still needed before going live

1. **Seed the database** via Railway CLI:
   ```bash
   railway run python scripts/seed_exam_group2.py
   railway run python scripts/migrate_from_legacy.py
   ```

2. **Change ADMIN_PIN** in Railway Variables from `1234` to a secure value.

3. **Sync local git** from Windows terminal:
   ```
   git fetch origin && git reset --hard origin/main && git push --tags
   ```
