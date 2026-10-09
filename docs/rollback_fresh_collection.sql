-- Surgical rollback of the fresh AP History collection (collection_id 'ap-history-fresh-v1').
-- NOT EXECUTED anywhere except on local test copies. Destructive: needs its own explicit approval and a verified,
-- isolated-restore-tested backup. The canonical taxonomy already exists in production and is NEVER touched here.
--
-- Prefer switching learners back to legacy (admin page): it removes nothing. Use this file only to remove the collection itself.
-- It removes ONLY rows tagged with the collection id (legacy rows have collection_id NULL and are never matched):
--   * the switch audit log and setting rows for chapters that carry the collection,
--   * learner state rows for the collection's questions (user_question_state cascades from questions; counted below so
--     you can see how much learner history on FRESH questions would be lost; history on legacy questions is untouched),
--   * the collection's questions and expanded notes (and their app-section map rows).
-- Run: psql "$URL" -f rollback_fresh_collection.sql   (the last line is ROLLBACK until you change it to COMMIT)
BEGIN;
SELECT (SELECT count(*) FROM questions WHERE collection_id = 'ap-history-fresh-v1')           AS fresh_questions_to_remove,
       (SELECT count(*) FROM expanded_notes WHERE collection_id = 'ap-history-fresh-v1')      AS fresh_notes_to_remove,
       (SELECT count(*) FROM user_question_state WHERE question_id IN
            (SELECT id FROM questions WHERE collection_id = 'ap-history-fresh-v1'))           AS learner_state_rows_on_fresh_questions,
       (SELECT count(*) FROM questions WHERE collection_id IS NULL)                           AS legacy_questions_before;

DELETE FROM chapter_collection_setting WHERE syllabus_chapter_id IN
    (SELECT DISTINCT syllabus_chapter_id FROM questions WHERE collection_id = 'ap-history-fresh-v1'
     UNION SELECT DISTINCT syllabus_chapter_id FROM expanded_notes WHERE collection_id = 'ap-history-fresh-v1');
DELETE FROM chapter_collection_log WHERE to_collection = 'ap-history-fresh-v1' OR from_collection = 'ap-history-fresh-v1';
DELETE FROM user_question_state WHERE question_id IN (SELECT id FROM questions WHERE collection_id = 'ap-history-fresh-v1');
DELETE FROM questions WHERE collection_id = 'ap-history-fresh-v1';
DELETE FROM expanded_note_app_map WHERE expanded_note_id IN (SELECT id FROM expanded_notes WHERE collection_id = 'ap-history-fresh-v1');
DELETE FROM expanded_notes WHERE collection_id = 'ap-history-fresh-v1';

-- guards: all three must be 0; legacy_questions_after must equal legacy_questions_before above
SELECT (SELECT count(*) FROM questions WHERE collection_id IS NOT NULL)      AS collection_questions_left,
       (SELECT count(*) FROM expanded_notes WHERE collection_id IS NOT NULL) AS collection_notes_left,
       (SELECT count(*) FROM chapter_collection_setting)                     AS settings_left,
       (SELECT count(*) FROM questions WHERE collection_id IS NULL)          AS legacy_questions_after;
-- After COMMIT, the additive migrations can be reversed with Alembic (each refuses while it still holds data):
--   python -m alembic downgrade a7b8c9d0e1f2        (c9d0e1f2a3b4 then b8c9d0e1f2a3; production's pre-change revision)
ROLLBACK;
