# Lesson 31 — MCQ NEW REVISE (Opus)

Inputs: review.md; FINAL/lesson_31_rebuilt.md; mcq/FINAL/lesson31_questions.json. Backups of the pre-revision files: q_new.pre_rev.py, qlib.pre_rev.py, build.pre_rev.py, new_questions.pre_rev.json. Source is q_new.py; outputs are new_questions.json (49 questions) and coverage.md.
Result: `python3 build.py` gives **BUILD CLEAN** (0 errors, 0 length flags; the remaining warnings are only Latin acronyms in TE options and one stem-token note on Q10). `check_mcq_giveaways.py new_questions.json` gives **0 problems**. Every question was solved again after the rebuild.

## 1. Tooling
- **OVERLAP check ported** from L29/mcq/NEW/build.py, verbatim, for single-answer kinds: (a) every part of the key also appears in some distractor; (b) the key is the strict centroid of shared parts. It passes on all 49.
- **New code set for 3-statement items** (qlib `STC`): "How many of the statements given above are correct?" with Exactly one / Exactly two / All three / None of them (TE: సరిగ్గా ఒకటి / సరిగ్గా రెండు / మూడూ సరైనవి / ఏదీ సరైనది కాదు). Knowing a single false statement no longer forces the key. Option explanations are generated: each one says the true count and whether the option counts too many (it lists the false statements) or too few (it lists the true ones). The labels avoid "only", so the checker's absolute-word rule passes.
- build.py: count-format keys go into their own bucket and must vary; the old "3-statement keys A/B/C" rule now applies only to the old set, which is no longer used. New rule: A ≥ 9, and A must still be the least frequent key.
- KEY-TEXT (`ok=`) check unchanged. Every new or rewritten S() call has `ok=`.

## 2. Dropped (IDs left as gaps)
| Q | Why |
|---|---|
| 6 | Basic-needs cluster: three questions on one fact set, and the six-need list repeats 6-P520-002. Q4 (organisation) and Q5 (A-R welfare vs basic needs) stay. |
| 29 | Sri Lanka/India cluster: its statements were given away by Q19/Q20/Q30. Its facts (MYS/EYS, India's indices) are still taught by Q30's explanation and the INDIA table. |
| 43 | PQLI cluster: Q47's stem gave its key. Q47 stays as the why-question, and its explanation now gives the three indicators (F059 is still covered). |

## 3. Leak clusters broken
- **Q4/5/6**: Q6 dropped. Q4's explanation no longer lists the needs.
- **Q7/8/9**: Q7's explanation no longer gives HPI-2 1998 or the 2010 indices. Q8's options no longer explain the MPI/HPI replacement. Q9 is rebuilt (HDRO computes; HPI-1 is for developing and HPI-2 for OECD countries; "TAI measures a gender gap in tech jobs" is false), with no years that Q7 tests.
- **Q27/29/30**: Q29 dropped. Q27's explanation no longer gives Sri Lanka's 77.5/10.8.
- **Q41/45/46**: no question's key appears as a distractor in another. Q41's 131 became 130 (India's HDI rank). Q45's 131 became 133 (India's recalculated 2022 HDI rank). Q46 is restructured to "rank out of how many countries": 131/145 (key), 131/148 (2025), 129/146 (2024), 129/145. Q41's explanation no longer names WEF 131. Q28's Denmark became Finland, so the "Denmark first on GII" fact sits only in Q41.
- **Q43/47**: Q43 dropped.
- **Q31/33**: Q31's explanation no longer gives India's 0.685/0.475/30.7%.
- **Q32/34**: Q32 option D no longer gives India's 12.6%/group 5.
- Also: Q17's explanation no longer works the 0.168/0.552 geometric mean, and Q21's explanation no longer states "GM below AM whenever the indices differ" (that was Q25's A). Q50's stem and explanation no longer say "undivided", which is Q52's key.

## 4. Per-item changes
| Q | Change |
|---|---|
| 3 | The key no longer echoes "productivity" ("lets each worker produce more in the same time"). Weak A/B became "enlarges the labour force by raising population" and "lowers the wage each worker is paid". |
| 4 | Asks only for the organisation (year in the stem). Options are ILO, UNDP, UNICEF, WHO, each with a fact-based explanation. Key moved C to B (breaks the CCC run). |
| 8 | Self-eliminating PHDI and HDI/IHDI options became "TAI and HPI-2" and "GEM and TAI". The key is not the centroid. Key moved B to A. |
| 9, 24, 39, 51 | Moved to the count format. Keys: Q9 two (B); Q24 all three (C; statement 2 rewritten as true, "fixed cut-off values"); Q39 exactly one (A; statement 2 now false, "UNDP prepares the National MPI"); Q51 two (B). |
| 10 | The invented title "Climate and our shared future" became a neutral "A new HDR 2026 released in 2026". |
| 11 | A/C/D became plausible: "cannot compare across currencies" (PPP solves that), "GDP leaves out income earned abroad" (that is the 2010 GNI reason), "growth had stopped". |
| 20 | Option A's explanation now notes that EYS index is left above 1 (uncapped). |
| 23 | D became "keep each index between 0 and 1" (that comes from normalisation, not from the mean). |
| 30 | Absurd A/D became "income carries more weight" and "lower inequality is added to the HDI" (confusion with the IHDI). |
| 34 | C/D became "women's life expectancy is lower than men's" (false: Indian women live longer) and "gap between 7.5 and 10%" (group 4). |
| 37 | A/D became "H already contains depth" and "A tells how many are poor" (H/A swap). |
| 40 | The non-lesson 13.5 crore and the off-scale 120 crore (TE/EN mismatch) are gone. The options are now all two-decimal crore figures built from lesson numbers: 29.17 and 11.28 (the shares misread as crore) and 17.89 (the percentage-point fall, 29.17 minus 11.28). The explanation warns not to mix the percentages with the count. |
| 44 | Each option explanation now carries its own fact (the lesson records only MP 2016 and AP 2017; HP is a common guess from state HDI; Telangana formed in 2014). |
| 47 | Absurd distractors became "HDI already measured income" (the HDI came in 1990), "income cannot be scaled 0–100", and "literacy already reflects income". All four TE options now end in "కాబట్టి". |
| 50 | It overlapped 6-P527-002 (NHDR not comparable with the UNDP table). It is now an A-R on why AP's NHDR value rose (0.377 to 0.416) while its rank fell (9 to 10): other states moved faster (lesson line 1065). The key stays A. |
| 51 | Statement 3 now reads "computed by UNDP's HDRO" (false; computed by the Global Data Lab), which closes the "HDRO data centre hosts it" argument. The old Bihar statement was replaced by NHDR consumption expenditure (true), so F072 stays covered. Bihar remains in the explanation. |
| 52 | Weak reasoning item became a concept item: which territory the NHDR 2001 "Andhra Pradesh" value covers (key: undivided AP with Telangana; distractors: 13-district AP of 2014, 28-district AP of 2025, coastal Andhra alone). It no longer repeats 6-P527-002 or Q50. |
| 1, 14, 21, 28, 38 | Key moved to A, with the options unchanged, to spread the keys. |

## 5. Keys after the rebuild (all re-solved)
Sequence (Q1..Q52, without 6/29/43): ABCBCDABCBDCADACBDDACBCBBDACDCABBDCAABDCCBDCBCABD
New set: A 10, B 14, C 14, D 11. A is still the rarest. Combined with the linked FINAL set (A12 B13 C11 D12): A 22, B 27, C 25, D 23. AR keys: A 2, B 1, C 1, D 1. Count-format keys: B, C, A, B. 2-statement keys: Q2 B, Q33 A, Q48 B.

## 6. Left as is, with notes
- 2-statement keys are still only "only 1" or "only 2". build.py's house rule (keys A/B) requires that; review note kept for the orchestrator.
- Q10 and Q28 still sit next to FINAL 6-P524-001, whose stem says "HDR 2025 … latest as of November 2026". That is a bank question and was not edited here.
- Q34 C rests on Indian women's life expectancy being higher than men's. This is true in HDR 2025 but not stated in the lesson. It is used only as a distractor reason.
