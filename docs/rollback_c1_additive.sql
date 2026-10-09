-- Surgical rollback of the Chapter 1 closure import (batch aph-u1-c01-closure-20261009), revision metadata-r1.
-- NOT EXECUTED anywhere except on local test copies. Destructive: needs its own explicit approval, a verified and
-- isolated-restore-tested backup, and a count check first.
--
-- It removes ONLY what the change added:
--   * questions of this batch (legacy rows have source_qid NULL and are never matched),
--   * expanded notes of this batch,
--   * canonical rows whose slug is NOT in the pre-change inventory (so canonical rows that already existed in production
--     before the seed are never removed, even though they also appear in the seed).
-- BEFORE any seed, capture the inventory from the real production baseline and keep it with the backup:
--   \copy (select 'unit', slug from syllabus_units union all select 'chapter', slug from syllabus_chapters union all
--          select 'subtopic', slug from syllabus_subtopics union all select 'microtopic', slug from syllabus_microtopics)
--          to 'pre_change_inventory.csv' csv
-- Then run this file with psql from the folder holding pre_change_inventory.csv. Every guard must print the expected number
-- before the last line is changed from ROLLBACK to COMMIT.
BEGIN;
CREATE TEMP TABLE pre_slugs(kind text, slug text);
\copy pre_slugs from 'pre_change_inventory.csv' csv

DELETE FROM questions WHERE batch_id = 'aph-u1-c01-closure-20261009' AND source = 'codex_generated' AND source_qid LIKE 'APH-U1-C1-B20261009%';
DELETE FROM expanded_note_app_map WHERE expanded_note_id IN (SELECT id FROM expanded_notes WHERE package_batch_id = 'aph-u1-c01-closure-20261009');
DELETE FROM expanded_notes WHERE package_batch_id = 'aph-u1-c01-closure-20261009';
-- children first; a row is removed only when it was absent from the pre-change inventory
DELETE FROM syllabus_microtopics WHERE slug NOT IN (SELECT slug FROM pre_slugs WHERE kind = 'microtopic');
DELETE FROM syllabus_subtopics   WHERE slug NOT IN (SELECT slug FROM pre_slugs WHERE kind = 'subtopic');
DELETE FROM syllabus_chapters    WHERE slug NOT IN (SELECT slug FROM pre_slugs WHERE kind = 'chapter');
DELETE FROM syllabus_units       WHERE slug NOT IN (SELECT slug FROM pre_slugs WHERE kind = 'unit');

-- guards (compare with the pre-change record): batch rows left must be 0; the canonical counts must equal the inventory counts
SELECT (SELECT count(*) FROM questions WHERE source_qid IS NOT NULL AND batch_id = 'aph-u1-c01-closure-20261009') AS batch_questions_left,
       (SELECT count(*) FROM expanded_notes) AS expanded_left,
       (SELECT count(*) FROM syllabus_units) AS units, (SELECT count(*) FROM syllabus_chapters) AS chapters,
       (SELECT count(*) FROM syllabus_subtopics) AS subtopics, (SELECT count(*) FROM syllabus_microtopics) AS microtopics,
       (SELECT count(*) FROM pre_slugs) AS inventory_rows,
       (SELECT count(*) FROM questions) AS questions_total, (SELECT count(*) FROM notes) AS notes_total;
ROLLBACK;   -- change to COMMIT only after the numbers match
