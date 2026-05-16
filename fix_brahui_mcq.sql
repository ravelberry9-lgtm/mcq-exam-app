-- Fix 1: Update the Brahui tribe question if it exists with wrong correct_option
UPDATE chapter_mcqs
SET correct = 'c'
WHERE q_te LIKE '%తెగ%' AND q_te LIKE '%సింధు నాగరికత వారసులు%';

-- Fix 2: Also ensure the question exists (in case chapter_mcqs was seeded from old broken file)
-- Run this only if the above UPDATE affected 0 rows and you want to re-seed

-- Verification:
SELECT id, q_te, opt_a, opt_b, opt_c, opt_d, correct
FROM chapter_mcqs
WHERE q_te LIKE '%తెగ%';
