# Lesson 10 new MCQs: revision after review.md

The sources (q_a.py, q_b.py, qlib.py) were edited and new_questions.json was rebuilt. build.py: CLEAN (0 length flags, 0 errors). check_mcq_giveaways.py: 0 problems (checker.txt). There are still 74 questions, ids GEO-NEW-10-001 to 074. I checked every id, key position and key text against a rebuild of the old sources: none changed. Answer spread is unchanged (A 18, B 19, C 20, D 17). 19 questions differ from the old build.

## Matching-key pattern (Q4, 10, 14, 21, 56)
I rewrote `qlib._pick_wrong`. The key's A pair and D pair each now appear in at least one distractor, and so do at least 3 of its 4 pairs. The key must still not be the centre option. The choice is seeded per key, so the five questions have different shapes. A different single pair is left unique to the key in each question: C in Q4 and Q56, B in Q10, Q14 and Q21. Knowing the first pair no longer solves any of the five. A cut where every pair is shared is impossible without making the key the centre option, which build.py rejects.

## Fact and wording fixes
- Q16 Chagos: the treaty was signed on 22 May 2025 and is still not in force as of November 2026 (UK implementing legislation is pending). This is in the explanation and the option note. The statement keeps "by early 2026" and stays false. The key is unchanged.
- Q27: I deleted the book-error sentence about Lake Van 330‰ and the unverified "APPSC Group-2 (2024)" claim, in both languages and in the option note.
- Q33: the stem now says "According to standard textbooks" and uses the term లాగూన్. The Vembanad distractor (arguable) was replaced by Loktak (a freshwater lake in Manipur).
- Q43: the Telugu key is now "ఆయనాంత వేలా తరంగాలు", which matches the other options. The explanation says "the book calls these solstitial tides".
- Q64: the stem no longer names the Huang He. It now reads "a river of northern China ... settles as mud".
- Q67: the stem now lists the options it compares (terrigenous, biogenous, hydrogenous, red clay). The unsourced 45% / 2% figures were softened to "up to about half" and "a few percent".
- Q73: the Kavaratti OTEC plant is described as "still being developed in 2026 news, no commissioning date". The 40‰ salinity distractor was replaced by a current-speed distractor.
- Q25 statement 3: changed from 3.5 PSU (a unit-pedantry trap) to "mean salinity about 53‰" (still false).
- Q65 statement 3: the CCD depth was changed from 500–1,000 m to 1,000–2,000 m (still false, but closer and more testing).

## Distractor and Telugu upgrades
- Q30: replaced the mirror-image distractor D with "currents from the Arctic warm the northern seas".
- Q47: replaced Upwelling and Seiche with Counter current and Undercurrent.
- Q71: replaced the Mid-Atlantic Ridge crest and Zhemchug Canyon with the Peru Basin and the North American Basin plain.
- Q3: the Telugu option B is now తీర లాగూన్.
- Q40: the Telugu option is now ప్రయాణించే తరంగాలు.

## Not done, and why
- The review asked to sort the numeric options in Q20, Q58 and Q72 and re-key them. It also asked for one statement key of "1, 2 and 3" and one of "Both", and for a different A-R key spread. Each of these changes a key, which this revision forbids. They are left for a pass where keys may change.
- Lower-priority items were left as they are: weak distractors in Q2, 6, 7, 8, 12, 15, 22, 39, 42, 44, 49, 54, 57, 63, 66 and 69; the trivial A-R questions 29 and 31; the duplicate clusters 17-18, 40-42, 56-57 and 61-63; and the Gulf/సింధుశాఖ Telugu convention (Q14, Q68).
