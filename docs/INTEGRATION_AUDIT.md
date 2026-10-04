# Design-system integration: audit and progress

## Approach
Incremental. Existing routes, admin, DB and tests are untouched. The new journey lives under `/learn`
(blueprint `app/routes/learn.py`, service `app/services/learn.py`, templates `app/templates/ds/`,
assets `static/ds.css`, `static/ds.js`, `static/fonts/`). Old pages are replaced only after the new journey passes tests (stage 8).

## Mapping prototype -> data model
- Topic = Chapter; Section = ExamSection (groups subjects via ExamSyllabusItem); notes = Note rows (`section_num`).
- Questions link to chapters only (no question -> note-section link).
- Language: `lang` cookie (te/en/both) drives `html[data-lang]`; missing language falls back to the other (never blank).

## Provenance and unverified data
- PYQ metadata present: `pyq_year`, `pyq_paper` (date + optional shift). No exam name stored -> display "Source not verified".
- No metadata is invented. Exam rules (duration, negative marking, Mains format) are NOT shown: the seed sets duration 150 on all papers, which is unverified. They will be configurable with a `rules_verified` flag and stay disabled until confirmed from the official notification.

## Data-quality items to review
- 6 chapters with "recovered" titles (shown as "Chapter N").
- 146 chapters have no questions.
- Chapter MCQs are Telugu-only; practice/PYQ are English-only.
- 134 notes contain unsafe markup (sanitised at render; source rows unchanged).
- Telugu UI strings in `app/services/ui_text.py` are drafts and need human review.
- Pre-existing failing test: `tests/test_notes.py::test_reader_empty_chapter_shows_message` (not caused by this work).

## Stage log
1. Shell, tokens, fonts, nav, language setting: done.
2. Learn -> Section/Subject -> Topic -> Notes -> Practice -> Explanation: done (`tests/test_learn_journey.py`).
3. Bookmarks, mistakes, progress: next.
4. PYQ filtering. 5. Timed tests/results/review. 6. Current affairs, infographics. 7. Offline/Android tests. 8. Replace old pages.

## Dev setup
Copy `data/content.db` to a dev DB, set `DATABASE_URL`, run `python seed_exam_group2.py` if exam tables are empty, then `python -m pytest -q`.
