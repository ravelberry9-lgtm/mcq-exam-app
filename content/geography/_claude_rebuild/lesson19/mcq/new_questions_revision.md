# Lesson 19 NEW MCQ revision (applies review.md)

Source edited: q_a.py (backup q_a.py.bak_pre_revise). Rebuilt with build.py: BUILD CLEAN. check_mcq_giveaways.py on new_questions.json: 0 problems. All 39 ids kept. No key changed (all 39 keys identical to before; spread still A10 B10 C10 D9).

## Changes

| Q | Change |
|---|---|
| 003 | Telugu explanation fixed: "190 లో 200" became "200 లో 190" (95%). |
| 010 | Recast to a different fact (no longer repeats Q009 / leaks Tehri-highest, Bhakra-highest-gravity). A: "Tehri Dam is a concrete gravity dam" (false, rock-and-earth fill); R: "Tehri stands on the Bhagirathi" (true). Key D kept. Fact F022. |
| 011 | Statement 3 changed from Idukki arch dam (leaked Q009 D-3) to check dam definition (true, F020). Pattern and key B kept. Facts now F020, F023, F024. |
| 012 | Stem no longer states the canal starts at Harike (removes leak to FINAL IA07-014). Key now "start below the Sutlej-Beas confluence" (Harike appears only in the post-answer explanation). Invented-geography distractors replaced with true facts used wrongly: Gobind Sagar of Bhakra (Bhakra canals), Ropar headworks (Sirhind), Madhopur headworks on the Ravi (Upper Bari Doab). Key no longer strictly longest. Key D kept. |
| 016 | Explanation no longer gives Gujarat 9 MAF / Rajasthan 0.5 MAF (leaked Q015). |
| 017 | Distractors C and D replaced: "to share water with Bangladesh under the Ganga Waters Treaty" (treaty came 1996, caused by the diversion) and "to control Kosi floods in north Bihar" (Kosi Barrage does that). Key B kept. |
| 024 | Repeated-35,000 tell removed: distractors now 25,000 / 50,000 / 40,000 cusecs (11,574 from Q018 dropped). Explanation adds as-of note: 30-year term ends December 2026, watch for renewal. Key D kept. |
| 025 | Retargeted (no longer duplicates Q024 or IA07-089): 1. 30-year term ends Dec 2026 (T); 2. Joint Rivers Commission set up under the 1996 treaty (F, it is 1972); 3. 54 common rivers (T). Key C (1 and 3) kept. Facts F053, F054. |
| 033 | Replaced: A-R on KC Canal (A: built 1863-70 by the Madras Irrigation and Canal Company for navigation and irrigation; R: starts at Sunkesula anicut on the Tungabhadra; both true, R does not explain A). Key B kept. Fact F080. No longer leaks Q032. |
| 034 | False statement 2 no longer depends on Section 85 (Q023 leak): now "Polavaram is being built by the GRMB" (false; Polavaram Project Authority under Section 90). Explanations updated. Key C kept. |
| 039 | R no longer states "19th gate" and "stop-log" (Q038 statements 2, 3): now "one of the dam's crest gates failed and a large volume of water had to be released". Key A kept. |

## Skipped (would need key changes) or left as is

- Statement-question pattern (all 11 have two true statements; "1, 2 and 3" never the key) and key-rebalance by type: need key changes, skipped.
- Q003 leak from Q002 (90-100% = Critical): inherent to the pair; cannot fix without a key change or drop. Keep Q002 and Q003 in separate tests.
- Q009 unchanged; after the Q010 and Q011 edits nothing else in the set leaks its answer.
- Q015/Q016: Q016 explanation leak removed; Q015 itself unchanged.
- Remaining FINAL overlaps (partial, not verbatim), noted only: Q019 (IA07-006, IA07-025), Q026 (IA07-026, IA07-087), Q032 (IA07-059, IA07-STRICT-B01-059), Q033 KC Canal touches IA07-056 (length/storage there, not builder/head), Q035 (IA07-STRICT-B01-072), Q036 (IA07-045). Q025's statement 3 (54 rivers) overlaps IA07-090; JRC year is tested differently.
- Not in the brief, not done: STYLE rewording of Q001/Q004/Q021 stems, Q002 matching-explanation run-ons and list II Telugu wording, Q005 Telugu nit, Q037 option order/value doubt.
- build.py warnings remain of the pre-existing kind (Latin proper nouns in TE options, missing English brackets).
