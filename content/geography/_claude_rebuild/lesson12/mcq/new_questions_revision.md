# Lesson 12 — MCQ NEW REVISE

Result: build.py BUILD CLEAN (0 length flags, 0 errors, 6 warnings as before); check_mcq_giveaways.py on new_questions.json: 0 problems (checker.txt). 46 questions, ids GEO-NEW-12-001…046 unchanged. **No key changed** (compared field by field with the pre-revision copy in `pipe/L12/mcq/NEW_prerev_bak/`). Spread A12 B12 C12 D10; A–R keys A6 B3 C6 D2.

## 1. Assertion–reason option explanations (systemic, 17 questions)

- qlib.py: `ARX` replaced with the fixed generator from pipe/L06/mcq/NEW/qlib.py. Each wrong option now gets its own full sentence ("This option needs R to be true, but R is false: …", "This option calls A false, but A is true: …", "A and R are both true, but R does not give the reason for A, so 'R explains A' is wrong."). No more `"R is not false: "` stubs, no lowercase "r", no "Both true, but R correctly explains A" under option B. The generator raises if any A/R note is empty. The matching "Correct:" sentence capitalisation from L06 `M` was ported too; `_pick_wrong` was already L11's version and is kept.
- q_a.py: wrote the A note and R note (TE + EN) for all 17 ARX calls: 001, 003, 006, 007, 012 (both notes), 014, 019, 022, 025, 034, 036 (A note), 017, 027 (R note), 031, 038, 040, 046 (both notes).
- build.py new check (A–R only, EN and TE): rejects option explanations that are empty/under 25 chars, end in a colon, start with the "R/A is not false" / "R/A తప్పు కాదు" stub, contain lowercase " r ", say "correctly explains" under a non-key option B, fail to deny the explanation under option A when the key is B, or call A/R false/true against what the key implies. New check for all kinds: identical option explanations repeated across options (EN or TE).
- The repeat check also caught 035 and 042 (statement questions: two options carried the same "Statement 1 is wrong" line). `STX` now gives each wrong option a different mismatching statement where possible.
- Markdown rule: the old "negative TE not bold" rule (required `**`) is replaced by "no `**` in stems" plus "an EN NOT stem needs a Telugu negative word (కాని/లేని/గీయని…)".

## 2. Other review items

| Q | Change |
|---|---|
| 004 | Explanation and all option explanations give latitudes (Tropic 23.44°N, Ranchi 23.3, Bhopal 23.2 — south, the old text wrongly said north, Agartala 23.8, Kolkata 22.6), per lesson l.167/182. No "according to the book". |
| 005 | Stem now "By total area including water, as in UN and CIA tables" (TE same). |
| 010 | TE explanation: "31 అక్టోబర్ 2019 కి ముందు 7". |
| 013 | TE stem: "Doubly landlocked దేశం (తాను భూపరివేష్టితం, చుట్టూ ఉన్న దేశాలూ భూపరివేష్టితాలే)"; calque removed. |
| 018 | TE `**` removed. Option D "Bengal partition line" (same line as B) replaced by "Line dividing Gurdaspur district" (Radcliffe's Punjab award split Gurdaspur; standard fact, not in the lesson text). |
| 021 | Three identical "does not match the briefing" lines replaced by distinct ones naming nine. Distractors 5/7/12 kept (did not adopt the reviewer's 6/24 Pakistan-claim numbers: not verified, not in lesson). |
| 028 | Explanation adds why 30 km is in the options (trap). |
| 030 | Stem says "natural atolls". Distractors now 20 (administrative atolls), 1,190 (islands), 36 (Lakshadweep islands); key 26 stays at C. |
| 038 | New A/R (overlap with 037 removed): A "first state formed on the basis of language", R "formed from the Telugu-speaking districts of Madras State" (lesson l.1328); key A unchanged. |
| 040 | New A/R (overlap with 039 removed): A "AP is 7th largest by area", R "Bay of Bengal on its east"; both true, R not the reason; key B unchanged. fact_ids now F123, F124 (F125 still covered by 039). |
| 043 | Stem "As of 2026"; TE uses ఛత్తీస్‌గఢ్. |

Not changed: 041/042 overlap (reviewer: acceptable); 026/029 mixed script (as in lesson); 045.
