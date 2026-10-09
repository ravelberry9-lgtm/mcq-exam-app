-- Surgical rollback of the Chapter 1 closure import (batch aph-u1-c01-closure-20261009) and the canonical seed.
-- NOT EXECUTED anywhere except on local test copies. Destructive: needs its own explicit approval, a verified backup, and a
-- count check first. Run inside one transaction; every guard must print the expected number before COMMIT.
BEGIN;
-- 1. questions added by this batch only (legacy rows have source_qid NULL and are never matched)
DELETE FROM questions WHERE batch_id = 'aph-u1-c01-closure-20261009' AND source = 'codex_generated' AND source_qid LIKE 'APH-U1-C1-B20261009%';
-- 2. expanded notes of this batch (the mapping table cascades)
DELETE FROM expanded_note_app_map WHERE expanded_note_id IN (SELECT id FROM expanded_notes WHERE package_batch_id = 'aph-u1-c01-closure-20261009');
DELETE FROM expanded_notes WHERE package_batch_id = 'aph-u1-c01-closure-20261009';
-- 3. canonical structure seeded by scripts/seed_ap_canonical.py (only if it was seeded for this change and nothing else uses it)
DELETE FROM syllabus_microtopics;
DELETE FROM syllabus_subtopics;
DELETE FROM syllabus_chapters;
DELETE FROM syllabus_units;
-- guards: expect 0, 0, 0 and the pre-change counts for questions and notes
SELECT (SELECT count(*) FROM questions WHERE source_qid IS NOT NULL) AS batch_questions_left,
       (SELECT count(*) FROM expanded_notes) AS expanded_left,
       (SELECT count(*) FROM syllabus_chapters) AS syllabus_left,
       (SELECT count(*) FROM questions) AS questions_total,
       (SELECT count(*) FROM notes) AS notes_total;
-- COMMIT;   <- only after the numbers match the pre-change record; otherwise ROLLBACK;
ROLLBACK;
