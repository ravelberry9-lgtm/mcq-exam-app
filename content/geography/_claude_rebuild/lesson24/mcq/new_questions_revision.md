# Lesson 24 NEW questions: revision (MCQ NEW REVISE)

Backups: `q_new.prerev.py`, `new_questions.prerev.json`; lesson `FINAL/lesson_24_rebuilt.pre_namo.md`.
Result: build.py CLEAN (0 errors, 0 length flags), check_mcq_giveaways.py 0 problems. 69 questions; no key or key position changed (verified by diff of `answer` against prerev). Changed: #3, 10, 15, 17, 18, 23, 24, 27, 31, 33, 35, 36, 43, 57, 62.

## Lesson fixes (done before the MCQ revise)
- Line ~1068 trap: Namo Bharat now "(RRTS; డిజైన్ వేగం 180, నడిచే వేగం 160 km/h)"; agrees with the narrative and selfcheck 22.
- Gatimaan vs Vande Bharat: sources differ in wording (Gatimaan 2016 = "India's first semi-high-speed train", e.g. Byju's, Testbook, The Quint, railway.supply; Vande Bharat 2019 = "first indigenous semi-high-speed train", Wikipedia/PIB usage). Added a note to the Gatimaan bullet and a new `::: exam` block after the Gatimaan fact ("read the word: first → Gatimaan; first indigenous → Vande Bharat"). Copied to `lesson_24.md`; build_html.py 24 clean.

## Per item
| # | Review flag | Fix |
|---|---|---|
| 3 | leak with #2 | New A (road: last-mile, flexibility, F004) and R (air: urgent high-value cargo, F006); key B kept. |
| 10 | leak with #15; even/odd repeat | Statement 1 now "odd numbers increase from south to north" (false); even/odd assignment no longer restated. |
| 15 | weak A; even/odd repeat | A "NH-27 runs north–south" (false); R "NH-27 links Porbandar with Silchar" (true); rule not restated; key D kept. |
| 17 | weak R; overclaim | R is now the cause (ROBs / RUBs replace railway gates, lesson line 607); explanation "fall sharply" instead of "no accidents". Key A kept. |
| 18 | PMGSY re-test with #16 | Statement 2 now "PMGSY-III launched in 2016" (false, 2019). |
| 23 | leak with #22 EPC definition | R now "contractor is paid for construction; no toll or operating rights" (lesson table). Key A kept. |
| 24 | weak distractors, TE/EN key length | Plausible distractors (Indian merchants' goods, villages to schools/hospitals, princely states' rail); key shortened in TE and EN. |
| 27 | leak with #26 (T-50) | Statement 1 now the USBRL expansion (true); explanation updated. |
| 31 | off-region distractors | Three west-coast / Deccan mix-ups. |
| 33 | "only" beyond lesson | "first". |
| 35 | ambiguous | Stem now names 2016, New Delhi–Agra, 160 km/h; Vande Bharat option note and explanation give the "indigenous" rule. |
| 36 | leak with #32 | Statement 1 now "DFCCIL set up in 2016" (false, 2006). |
| 43 | explanation beyond lesson | Replaced with the lesson's reason (ships cheap per tonne-km for heavy cargo). |
| 57 | nonsense distractor | "Lies inland, reaches sea by canal" (literal misreading of "landlocked"). |
| 62 | duplicate of IA10-BOOK-030 | New angle: A "NH-16 is part of the Golden Quadrilateral", R "NH-16 was NH-5 under the old numbering" (true, not the reason); key B kept. Avoids 1,024 km so #12's distractor stays live. |

## Not done (with reason)
- AR key skew (5 of 9 keyed A) and "flip #17/#33/#61 to B/C/D": would change keys, which this revise must not do. #17 and #23 R are now real causes, so the A keys are earned.
- #5, #46 TE key length (ratios 1.29, 1.15) and #24 EN key 51 vs 50: below the 1.3 limit; checker 0.
- #51/#56 Mundra and #66 UDAN: low; left as is.
