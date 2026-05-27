# MCQ App — Rebuild Plan v3

**Date:** 26 May 2026 · supersedes v2
**Headline changes from v2:**
1. Multi-exam architecture — subjects are a durable library, exams are curated views over it. Group 2 is the headline exam; Group 1 and AP HC Civil Judge are first-class additional exams.
2. Study-plan + chapter-progress layer added (one plan, multiple subjects, manual mark-complete, on-the-fly test from completed chapters).
3. Drop list revised: only `International_Current_Affairs` (1,100) and `National_CA` (1) are dropped. `AP_Current_Affairs_2026` and `Indian_Economy` are **kept** because Group 2 needs them.
4. Subject taxonomy reorganized to match the Group 2 syllabus structure.
5. Three real content gaps acknowledged: Indian Society (full), Mental Ability + Numeracy (~95% missing), Science & Technology (scope mismatch — needs Space/DRDO/Energy/Ecosystem coverage), and partial India-Geography gap.

---

## 1. Multi-exam architecture

### 1.1 The principle

A **subject** is a permanent knowledge container (Indian Constitution, Indian History, Indian Economy, etc.). Subjects don't belong to exams. Chapters and questions hang off subjects.

An **exam** is a curated mapping: which chapters from the subject library count toward which paper, which section, and how many marks. Adding APPSC Group 1, AP HC Civil Judge, or any future exam means defining a new exam mapping — zero duplication of content.

### 1.2 Schema (replaces v2's flat subjects + chapters)

```sql
-- Durable subject library
CREATE TABLE subjects (
  id          SERIAL PRIMARY KEY,
  slug        TEXT UNIQUE NOT NULL,
  name_en     TEXT NOT NULL,
  name_te     TEXT NOT NULL,
  sort_order  INTEGER DEFAULT 0
);

CREATE TABLE chapters (
  id          SERIAL PRIMARY KEY,
  subject_id  INTEGER NOT NULL REFERENCES subjects(id) ON DELETE CASCADE,
  chapter_num INTEGER NOT NULL,
  title_en    TEXT NOT NULL,
  title_te    TEXT NOT NULL,
  est_read_minutes INTEGER DEFAULT 20,
  UNIQUE(subject_id, chapter_num)
);

-- Notes, questions, passages all reference chapters (same as v2)

-- Exam definitions (multi-exam support)
CREATE TABLE exams (
  id            SERIAL PRIMARY KEY,
  slug          TEXT UNIQUE NOT NULL,    -- 'appsc_group_2', 'appsc_group_1', 'ap_hc_civil_judge'
  name_en       TEXT NOT NULL,
  name_te       TEXT NOT NULL,
  conducting_body TEXT,                  -- 'APPSC', 'AP High Court'
  active        BOOLEAN DEFAULT true
);

CREATE TABLE exam_papers (
  id            SERIAL PRIMARY KEY,
  exam_id       INTEGER NOT NULL REFERENCES exams(id) ON DELETE CASCADE,
  paper_num     INTEGER NOT NULL,        -- 0 = screening, 1 = Paper I, 2 = Paper II
  name_en       TEXT NOT NULL,
  name_te       TEXT NOT NULL,
  total_marks   INTEGER NOT NULL,
  duration_min  INTEGER,
  UNIQUE(exam_id, paper_num)
);

CREATE TABLE exam_sections (
  id            SERIAL PRIMARY KEY,
  paper_id      INTEGER NOT NULL REFERENCES exam_papers(id) ON DELETE CASCADE,
  section_label TEXT,                    -- 'A', 'B', or NULL for single-section papers
  name_en       TEXT NOT NULL,
  name_te       TEXT NOT NULL,
  marks         INTEGER NOT NULL,
  sort_order    INTEGER DEFAULT 0
);

-- The key join table: maps subject chapters into exam sections with weight
CREATE TABLE exam_syllabus_items (
  id            SERIAL PRIMARY KEY,
  section_id    INTEGER NOT NULL REFERENCES exam_sections(id) ON DELETE CASCADE,
  chapter_id    INTEGER NOT NULL REFERENCES chapters(id) ON DELETE CASCADE,
  weight_marks  INTEGER,                 -- estimated marks contribution (NULL if uniform)
  sort_order    INTEGER DEFAULT 0,
  UNIQUE(section_id, chapter_id)
);
```

### 1.3 What you query

- **All chapters covered by Group 2:**
  `subjects → chapters → exam_syllabus_items → exam_sections → exam_papers WHERE exam.slug = 'appsc_group_2'`
- **Progress for Group 2 Paper II Section A:** filter `chapter_progress` rows joined against the syllabus items for that section.
- **"Test on completed chapters" for a plan:** filter `questions` where `chapter_id` is in the user's completed chapters AND in the plan's exam syllabus.

---

## 2. Study-plan layer (from v6 design)

### 2.1 Schema

```sql
CREATE TABLE study_plans (
  id          SERIAL PRIMARY KEY,
  device_id   TEXT NOT NULL,
  exam_id     INTEGER REFERENCES exams(id),   -- NULL = freestyle plan (no exam binding)
  name        TEXT NOT NULL,
  subject_ids JSONB,                          -- optional subset; NULL = whole exam
  target_date DATE NOT NULL,
  status      TEXT DEFAULT 'active',          -- 'active' | 'paused' | 'completed' | 'archived'
  created_at  TIMESTAMP DEFAULT now()
);

CREATE TABLE chapter_progress (
  device_id          TEXT NOT NULL,
  chapter_id         INTEGER NOT NULL REFERENCES chapters(id),
  status             TEXT NOT NULL,           -- 'not_started' | 'in_progress' | 'completed'
  current_section    INTEGER,
  marked_complete_at TIMESTAMP,
  last_opened_at     TIMESTAMP,
  PRIMARY KEY (device_id, chapter_id)
);
```

### 2.2 Behavior

- One active plan at a time per device (enforce by `UNIQUE(device_id) WHERE status='active'`).
- A plan binds to **one exam** but can include a subset of its subjects.
- "Continue plan" button on home → routes to the most recently-opened in-progress chapter.
- "Mark chapter complete" is a deliberate user action; nothing auto-completes.
- "Test on N completed chapters" pulls random questions only from `questions` whose `chapter_id` is in `(SELECT chapter_id FROM chapter_progress WHERE device_id=? AND status='completed')` AND is part of the active plan's exam syllabus.

### 2.3 Pacing logic

When the home displays "pace looks healthy / behind by N chapters / ahead":
```
expected_done = total_chapters * (days_elapsed / total_days)
actual_done   = COUNT chapter_progress WHERE status='completed' AND in plan
delta         = actual_done - expected_done
  >= 0  → "healthy" or "ahead"
  -1 to -3 → "slightly behind"
  < -3  → "behind by N"
```

---

## 3. Revised drop list

| Bucket | Decision |
|---|---|
| `AP_Current_Affairs_2026` (200) | **KEEP** — Group 2 Screening needs AP CA |
| `International_Current_Affairs` (1,100) | **DROP** — gap covered by news/other sources |
| `National_CA` (1 row) | **DROP** — only 1 row, not material |
| `Indian_Economy` (700) | **KEEP** — Group 2 Main Paper II-A is 75 marks of Economy |
| All `chapter_mcqs` (3,682) | KEEP — chapter content for Polity/History/etc. |
| All `pyq_questions` (661) | KEEP |
| GK Art_Culture (344) + General_Science (600) + Everyday_Science (500) | KEEP |
| Mental_Ability (50) | KEEP, but expand significantly (see §5 gaps) |

**New migration totals:** ~6,737 questions migrated (was 5,837 in v2). Only 1,101 questions dropped (was 2,000 in v2). Archive JSON files for the dropped Intl CA still produced.

---

## 4. Subject taxonomy (final, 11 subjects)

Per user decision (26 May): India-level and AP-level Geography are separate subjects; same for Economy. The exam syllabus mapping (§6) can group them under one paper section if needed, but as study subjects they live independently so the user can drill each at its own pace.

| # | Subject (slug) | Chapters (existing) | Content source |
|---|---|---|---|
| 1 | `indian_history` | 14 | `chapter_mcqs` + study_notes (Ancient/Medieval/Modern) |
| 2 | `indian_constitution` | 12 | existing Polity `chapter_mcqs` + study_notes |
| 3 | `ap_history` | 5 (target) | partial Art_Culture + new content needed (prehistoric → 1956) |
| 4 | `indian_geography` | 11 | `static/notes/Indian_Geography/Chapters/ch01–ch11.html` |
| 5 | `ap_geography` | 15 | `study_notes` (15 AP Geo rows) + 5 `ap_geo_ch*_notes.html` files |
| 6 | `indian_economy` | 10 (target) | un-dropped `Indian_Economy` 688 Q (12 AP-related Q split off below) |
| 7 | `ap_economy` | 3 (target) | 12 AP-tagged Q from old Economy bucket + new content needed |
| 8 | `science_technology` | 11 (target) | partial from General/Everyday Science; needs Space/DRDO/Energy/Ecosystem |
| 9 | `indian_society` | 6 (target) | **fully missing — content gap** |
| 10 | `mental_ability` | 9 (target) | 50 existing Q + ~95% gap (Logical Reasoning, Numeracy, Data Interp) |
| 11 | `current_affairs` | rolling (no fixed chapters) | `AP_Current_Affairs_2026` 200 Q + new monthly additions |

Each subject is bilingual (`name_en`, `name_te`) per the always-both rule. The `current_affairs` subject is special — no fixed chapters, content groups by month/year. Migration script tags the 12 AP-mentioning Economy Q (IDs 8242–8253 etc.) into `ap_economy` instead of `indian_economy` based on keyword match on "Andhra" / "ఆంధ్ర".

---

## 5. Content gap inventory (honest, post-split)

| Gap | Severity | Affects Group 2 marks | Plan |
|---|---|---|---|
| **Indian Society** | Full — nothing exists | 30M Screening | Phase 8 content build (admin UI batch entry + AI-assisted draft) |
| **Mental Ability + Reasoning + Numeracy** | ~95% missing | 30M Screening | Phase 8 content build — most can be templated (number series, coding) |
| **Science & Technology** | Scope mismatch — have biology/physics, need Space/DRDO/Energy/Ecosystem | 75M Main II-B | Phase 8 content build, re-tag existing where possible |
| **AP Economy** | Only 12 Q exist (AP-mentioning rows from old Indian Economy bucket); no chapters yet | shared section (Main II-A 75M with Indian Economy) | Phase 8 content build — 3 chapters: AP GSDP, AP sectoral, AP budget |
| **AP History prehistoric→1956** | Partial — Art_Culture overlaps but doesn't cover dynasties/movements | ~50M of 75M Main I-A | Phase 8 content build |

**Indian Geography is no longer a gap** — `static/notes/Indian_Geography/Chapters/` has 11 HTML chapters that get imported in the notes-importer step (Phase 4). They were invisible in v2/v3 because the audit only looked at the `study_notes` DB table.

**Phase 8 is new:** "Content gap fill." It runs in parallel with admin UI being live (Phase 3) so you can add content as soon as the editor works. Doesn't block migration or cutover. Realistically a multi-week effort spread across actual study — not blocking the app launch.

---

## 6. Group 2 syllabus mapping (the seed data)

This is the data that populates `exams + exam_papers + exam_sections + exam_syllabus_items` for APPSC Group 2 in a one-time seed script:

```
exam: appsc_group_2
  ├─ paper 0 · Screening · 150M · 150 min
  │   ├─ Indian History (30M)        → indian_history ch 1-14
  │   ├─ Geography (30M)             → indian_geography ch 1-11 AND ap_geography ch 1-15
  │   ├─ Indian Society (30M)        → indian_society ch 1-6
  │   ├─ Current Affairs (30M)       → current_affairs (rolling)
  │   └─ Mental Ability (30M)        → mental_ability ch 1-9
  ├─ paper 1 · Main Paper I · 150M · 150 min
  │   ├─ Section A · AP Social & Cultural History (75M)  → ap_history ch 1-5
  │   └─ Section B · Indian Constitution (75M)           → indian_constitution ch 1-12
  └─ paper 2 · Main Paper II · 150M · 150 min
      ├─ Section A · Indian & AP Economy (75M)           → indian_economy ch 1-10 AND ap_economy ch 1-3
      └─ Section B · Science & Technology (75M)          → science_technology ch 1-11
```

The split lets the user study `indian_geography` alone, `ap_geography` alone, or both via the Group 2 syllabus view. Same for Economy. `exam_syllabus_items` rows simply reference chapters from both subjects under the same `exam_sections` row, so progress aggregates correctly.

### 6.1 Future exams (placeholders, populated later via admin)

- **APPSC Group 1** — slug `appsc_group_1`. Mostly overlapping subject library (Constitution, History, Economy, Geography, S&T) plus essay paper, plus an optional subject. Marks are higher. Map when syllabus is in hand.
- **AP HC Civil Judge** — slug `ap_hc_civil_judge`. Mainly Law subjects (Indian Constitution, Code of Civil Procedure, Code of Criminal Procedure, Evidence Act, Contract Act, Specific Relief Act, etc.) — most are new to the subject library. English language + General Knowledge are partial overlap.

Schema supports both. Content for them lives in the same `subjects/chapters/questions` tables. Defining the exam = inserting rows into `exams + exam_papers + exam_sections + exam_syllabus_items`.

---

## 7. Updated phase plan (10 sessions)

| Phase | What ships | Done when |
|---|---|---|
| **0. Scaffold** | New repo branch, Flask factory, SQLAlchemy models (all 13 tables), Alembic baseline, `tests/` smoke | `flask run` boots; one smoke test passes |
| **1. Core read flow** | `base.html` rendering nav from `menu_items`, home tiles from `home_tiles`, subject list, practice mode, question card | You can answer practice MCQs (hand-seeded) on the new UI |
| **2. Migration** | `migrate_from_old_db.py` end-to-end: old `database.db` → new Postgres; revised drop list; passage dedupe; difficulty + correct-answer normalization; old folder/topic strings mapped to new `subject_id`s | Test asserts ~6,737 Q in / ~6,737 Q out; 0 invalid `correct_answer`s |
| **3. Admin CMS** | `/admin` PIN gate; CRUD for app_settings + home_tiles + menu_items + subjects + chapters + questions + notes; drag-reorder for tiles & menu; MCQ side-by-side editor; HTML notes importer | You can add a home tile, nest a menu dropdown, and edit an MCQ from the UI |
| **4. Notes display** | Public notes browse: subject → chapter → section render; bleach-sanitized HTML; reader view with "mark complete" button | You can open any chapter and read both languages, then mark it complete |
| **4.5. Study plans** | Plan setup wizard (multi-subject, target date); plan hero on home; subject detail with chapter progress; "test on N completed" launcher | You create a 60-day plan, mark 2 chapters done, see them on home, run Quick 10 from those chapters |
| **5. Exam syllabus + exam flow** | Seed APPSC Group 2 syllabus rows; exam wizard; take exam; submit; score; result; exam_templates launcher | You complete one full timed Group 2 mock end-to-end; score correct |
| **6. Review + state** | Wrong answers, flagged, saved, history, confidence selector + calibration; device_id from localStorage | After an exam, wrong answers show up in Review with stats |
| **7. Cutover + polish** | Dark mode (auto), mobile QA, perf pass (EXPLAIN), Railway second service deploy, domain swap, old service archived | Old URL serves new app; rollback runbook documented |
| **8. Content gap fill** (ongoing, parallel to Phase 3+) | Indian Society 6 ch; Mental Ability 9 ch; S&T scope expansion; India Geography; AP History pre-1956 | Group 2 syllabus 100% covered with at least 30 Q per chapter |

Phase 8 isn't blocking. App launches at end of Phase 7 with content gaps clearly labeled in the UI ("This subject has limited content"). Filling gaps becomes ongoing admin work.

---

## 8. Critical issues resolved from v2 (still hold)

All 12 items from v2 review remain fixed in v3 — cutover via second Railway service + domain swap; passage migration step; difficulty + correct-answer normalization; admin moved to Phase 3; vanilla JS (no HTMX); HTML notes (bleach-sanitized) not markdown; importer idempotent; per-phase verification; etc. v2 §3 review table still applies.

---

## 9. Confirmations needed to start Phase 0

1. **Hosting** — second Railway service + new Postgres + domain swap at end. Yes / pick differently.
2. **Subject taxonomy of 11** as listed in §4 (Indian/AP Geography and Indian/AP Economy split per 26-May decision) — yes / further changes.
3. **Phase 8 content gap fill** — accept that the app launches with labeled content gaps and you fill them ongoing, vs. blocking launch until 100% coverage. Recommend launch-then-fill since the kept content is strong on Constitution / Indian History / Economy / Polity / both Geographies (>60% of Group 2 marks).
4. **Admin PIN** — keep `1234` for Phase 3, change in admin once UI exists.

**Migration source: local content only.** Per 26-May user note, the new app will be built from the local `mcq_app/` folder (`database.db` + `static/notes/**/*.html` + `questions_bank/**/*.json`). The live Railway DB is not pulled or touched during the rebuild — the second-Railway-service approach lets the existing service keep running unchanged until cutover.

Reply "build it" with answers, and Phase 0 starts.
