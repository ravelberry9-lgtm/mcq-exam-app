# Lesson 29 — MCQ NEW REVISE (Opus)

Inputs: review.md; FINAL/lesson_29_rebuilt.md; mcq/FINAL/lesson29_questions.json. Started again from the *.pre_rev.* copies. The current files matched them byte for byte, so the interrupted run had made no edits. Source: q_new.py; output: new_questions.json (51 questions), coverage.md.
Result: `python3 build.py` gives BUILD CLEAN (0 errors, 0 length flags). `check_mcq_giveaways.py` reports 0 problems. Every question was solved again after the rebuild; the keys are in section 4.

## 1. Tooling (ported from L28 plus one new check)
- qlib.S() now needs `ok=<correct EN option text>`. The correct tuple is found by its text, not by its place in the list. M/SEQ/STX/ARX also record `_ok`.
- build.py KEY-TEXT check: the build fails when the keyed option (TE or EN) is not the declared correct text, or when that text does not appear exactly once. A negative test (key forced to A on Q2) failed the build as it should.
- All 31 S() calls carry `ok=`.
- New OVERLAP check in build.py, for single-answer kinds. It fails the build when (a) every part of the key (split on commas, "and", dashes and similar) also appears in some distractor, or (b) the key shares strictly more parts with the other options than any distractor does. Before the rewrites it caught Q5, Q11, Q23, Q41, Q48 and Q52; it now passes.

## 2. Fact check: Q19 and the lesson
- Prasar Bharati Act, 1990: in force from 15 Sep 1997; the corporation was established on 23 Nov 1997 (Wikipedia, indiacode). The lesson already says this (line 561) and its other lines say only "formed 23 Nov 1997", so **the lesson needed no edit and build_html was not re-run**.
- In Q19, R is now "established on 23 Nov 1997 under the 1990 Act" (true). Its note gives both dates; the key stays D. The RADIO confusable row is corrected ("అమలు 15 సెప్టెంబర్ 1997; సంస్థ 23 నవంబర్ 1997").

## 3. Per-item changes
| Q | Change |
|---|---|
| 2 | The Velankar distractor is now Lord Clive (1766), so the Velankar/PIN leak to Q5 is gone. |
| 4 | Telecom date (26 Jun 2024) removed from the explanation (Q9 leak). |
| 5 | Person-only question: the date is in the stem, and the options are four independent names (Velankar, Pitroda, Sarabhai, J.C. Bose). The overlap and the Riddell leak are gone. |
| 6 | Statement 2 is now "nine zones, first digit shows the zone"; the Army fact moved out (Q7 leak). |
| 7 | The region distractor that the stem ruled out is replaced by "registered and insured articles"; all four options are now service types. |
| 8 | Option B explanation now explains Bombay/1881. |
| 10 | Weak distractors A and D replaced ("billed in urban circles", "counts calls"). |
| 11 | Asks only whom Basu spoke to. Options: Sukh Ram, Paswan, Mahajan, Narasimha Rao. VSNL removed from the explanation. |
| 12 | Bug fix: the SEQA item lists were in date order, not item-number order, which garbled the option explanations. They are now in item order (1 VSNL, 2 Simla, 3 5G, 4 telegraph). |
| 14 | Option is now "About 4.8 crore" (wireline), matching its explanation. |
| 17 | Retired (bank duplicate of P503-007). The ID now holds a new question: DD Free Dish's first name, DD Direct Plus (F043). Q21's explanation no longer names DD Direct Plus. |
| 18 | Statement 2 is now IBC 1936 (false; 1927). The Vividh Bharati leak to Q21 and the extra TE "key 1957" sentence are gone. |
| 19 | See section 2. |
| 22 | Option D explanation: "22 is not an AIR figure" (removed the Eighth Schedule reference, which is not in the lesson). |
| 23 | First-winner question only: Devika Rani vs Prithviraj Kapoor, Satyajit Ray, Raj Kapoor. B.N. Reddy removed (Q24 leak). |
| 26 | PRGI statement removed (RNI/PRGI cluster). New statements: Hindi first (T), Maharashtra first among states (F; UP), 1,51,474 total (T). Key: 1 and 3. |
| 27 | TE "భారతీయుడు" changed to "నివాసి" (also in the TFLOW table). |
| 28 | "(Leakage)" removed from the TE stem. The three absurd distractors are replaced by tourism-term distractors (arrivals counting, overnight/tourist label, carrying capacity). Option lengths now 60–69 characters. |
| 29 | Ooty sentence removed from the explanation (now tested in Q31). |
| 30 | Distractors are "rejected 2024", "inscribed then removed" and "private body". The explanations no longer give Ramappa 2021 (Q31) or Adarsh Smarak (Q39). |
| 31 | Statement 2 is now Ooty in the Palani Hills (F), replacing Horsley/Eastern Ghats (Q29 leak). |
| 33 | Item 1 is plain "e-Visa", so the stem no longer hints at the order. |
| 36 | Retired (e-Visa cluster with Q33). |
| 37 | New distractors with no overlap. "57 destinations" moved to the explanation. |
| 38 | Swadesh Darshan statements removed. Now PRASHAD only: Srisailam and Simhachalam (T), Tirupati and Ahobilam (F). |
| 39 | Town distractors replaced with AP temple, shrine and nature sets. The explanation no longer names anchor hubs or PRASHAD (Q38 and Q50 leaks). |
| 40 | Retired as a bank duplicate (P503-004/005). The ID now holds a fact question: Buddhist circuits in six NE states (Feb 2026); "Eight" is the trap. |
| 41 | Asks only the first-placed state (UP). AP removed (Q52 leak). |
| 42 | TE stem: "అనుబంధ ఖాతా". Option D is "5.80%"; no jobs-figure leak. F102 added to its fact ids. |
| 43 | Retired (TSA cluster: Q42 and Q45 kept). |
| 45 | Absurd and satellite-pun distractors replaced with real accounting misconceptions. The key no longer breaks the option pattern or stands out by length. |
| 46 | Four feature pairs with no shared half (Belum, Lepakshi, Amaravati, Gandikota). The Tentative List mention and the district (Q47 leak) were removed. |
| 48 | Year-only question (1976 vs 1956, 2015, 1983). Vijayawada no longer appears in the options (Q16 leak). |
| 49 | Retired as a duplicate (bank P504-004). The ID now asks where PNS Ghazi sank (Visakhapatnam vs Karachi, Chennai, Andamans). |
| 51 | R is a different, false fact: G.O. dated 2019 (actually 10 Dec 2024). Key C. The unsupported phrase "as of 2026 in force" was removed. |
| 52 | Asks the figure only, with four independent numbers (29.03, 25.47, 2.06 and 428.55 crore). The rank overlap is gone. |
| 53 | The absurd CBFC/TRAI/abolished distractors are replaced by plausible RNI/PRGI misconceptions. This is now the only RNI/PRGI item. |

Leaks listed in review section 3: all 15 pairs were broken by the changes above. Not changed: Q34 (List II is the "type" list, so the heading is right) and the bank-overlap items the review accepted (Q1, Q3, Q9, Q21, Q27, Q44).

## 4. Keys
- 51 questions; 36 and 43 retired (ID gaps).
- New keys: A 11, B 13, C 13, D 14. A is rarest, as required. Combined with the bank: A 34, B 38, C 36, D 33.
- AR keys: 1, 4, 2, 3. 2-statement keys: A 4, B 2. 3-statement keys: A, B, C. Matching keys are all different.
- Re-solve: my own answer matched the stored key on all 51.
