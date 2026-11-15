# Revision: pipe/L22/mcq/NEW (60 questions), 2026-11-05

Source: `q_new.py`, rebuilt into `new_questions.json` and `coverage.md`. Backups: `q_new.prerev.py`, `new_questions.prerev.json`.
Result: build.py **BUILD CLEAN** (0 errors, 0 length flags); check_mcq_giveaways.py **0 problems**. Every section has at least one why/how item.
Ids, `answer` values and key positions are unchanged for all 60 questions; I checked this against the prerev JSON. Key spread is still A 8, B 17, C 18, D 17. AR keys are still A5 B3 C2 D2.

## Hard duplicates and Q46 rewritten instead of retired (same id, same kind, same key position)

| Q | Was | Now (fact) | Key |
|---|---|---|---|
| 45 | fab vs ATMP AR (dup P392-Q002; R restated A) | AR: BHEL's Bhopal unit is older than BHEL, because HEIL (1956) was absorbed by BHEL (1964) in 1974 (F132). R is a real cause. Soft overlap: P391-Q005 has the same years in its options, but its stem does not give them. | A |
| 46 | Andhra Cotton Mills, Proddatur (not verifiable) | Where is Deccan Sugars? Samalkot (F143). P396-Q005 has Deccan Sugars only as a wrong pair (Guntakal). | C |
| 47 | AP silk centres (dup P399-Q004) | How many of NCERT's 15 industrial districts are in UP? Six (F034, F035). Options are ascending 1, 2, 3, 6 and each distractor is a real count (one-district States, UP's 2 minor regions, MP's 3). Section is now minor-regions, which makes up for Q60 leaving it. | D |
| 51 | craft match (all pairs in P400-Q002 stem) | Match the centre to its present district: Venkatagiri-Tirupati, Uppada-Kakinada, Dharmavaram-Sri Sathya Sai, Madanapalle-Annamayya (F156, F155, F141). No linked stem gives the districts. The new key A–4;B–1;C–2;D–3 is unique in the set, and the build confirms it is not the centroid. | C |
| 54 | Gandrajupalle (third copy) | APIIC Palakollu cluster: coir (F162). The explanation separates this from the Narsapur–Palakollu lace craft. No linked question covers it. | B |
| 58 | UADNL partners (dup P404-Q002 stem) | Where is the GI Registry? Chennai (F154). The distractors are the other lesson headquarters: Bengaluru (Silk Board), Guntur (Tobacco Board), Hyderabad (IDPL). I removed "registry at Chennai" from Q50's explanations so Q50 no longer leaks it. | D |
| 60 | Adilabad–Nizamabad AR (dup P375-Q002; R restated A) | AR: AP's large industries cluster on the coast, because the coast offers ports, water, transport and markets (F138). Section is now ap-industries. | A |

The facts these items used to test are still covered by the linked set: F134 (P392-Q002), F141 (P399-Q004), F161 (P402-Q006, P403-Q002), F170 (P404-Q002), F029/F035 (P375-Q002). F140 (the Proddatur mill) is no longer tested by any new item.

## Other fixes
- **Leaks.** Q3: the explanation no longer states Q5's key. Q5: the jute-land distractor is replaced by "mills moved to Kanpur", so Q5 and Q8 no longer share facts. Q8: the strike and Sterlite distractors are replaced by Hugli-topic traps (Damodar coal "went to East Pakistan"; jute mills "scattered with electricity"). Q17 and Q39: the sugar, cement and aluminium distractors are replaced by same-topic reversed or false reasons (cotton "loses weight", cloth "spoils"; clinker "gains weight", limestone "spoils"). This breaks the 17/25/35/39 triad, and the key no longer has a unique word overlap with the stem. Q41/Q43: Q43 now tests a different fact (Tejas vs Marut), so it no longer gives Q41's answer.
- **Weak A-R items (keys kept).** Q9: R is now a true fact about the same region (Saharanpur–Yamunanagar paper mills) that is not the cause. Q21: R is now sericulture stages; it mentions mulberry, so it looks like a reason but is not one. Q43: rewritten as above. The invented "built at Cochin because it is largest" cause is gone. Q59: A is now an outcome (Isuzu, Daikin, Mondelez and Alstom set up there) and R, the location near Chennai, is its real cause. I left Q2 and Q35 as they were: in both, R is a genuine cause of A (ore and coal location; the power demand of electrolysis).
- **Distractors.** Q6: Rishra/Bhatpara and Kankinara/Titagarh are inner centres of the same belt; F013 added. Q13: the SEZ option is replaced by "part of the Chotanagpur major region". Q30: the alumina-refinery and machine-tool options are replaced by the shore-based and ore-based integrated plant types; F096 added.
- **Numbers.** Q31 options are now in descending order (400, 300, 164.9, 149.4) so the key stays in position B. The filler 200 is replaced by the filler 400. Q55 options are now ascending (2008, 2017, 2018, 2019). The new 2017 is a lesson fact (Etikoppaka GI), replacing 2025.
- **Rajasthan wool.** I dropped "about 47%" from Q18's option explanation, from its explanation (TE/EN) and from the FIB table row.
- **Telugu.** I removed the decorative stem brackets from Q5, Q8, Q11, Q17, Q28, Q37 and Q39 (Q46 was rewritten without one). Q15: "రాష్ట్రంలోని" changed to "...లోని". Q37: the Telugu options are now Latin Cracking, Tanning, Smelting, Reeling, matching the lesson. These produce build warnings only.
- **Low-priority items.** Q32: A now reads "stands inland beside its iron ore", so it is false regardless of how the plant is classified. Q34: "closed for good" is now "closed by the Tamil Nadu government in 2018".
- **Tables.** APX: the Andhra Cotton Mills row is replaced by Deccan/KCP Sugars. CLU: a Palakollu coir row is added. SEMI: a BHEL row is added.

## Not done (soft items, left for the orchestrator)
- I did not swap the soft-duplicate statements in Q19, Q24, Q27, Q40 and Q49. They are still valid. Their overlap is one or two statements or pairs with the linked set, and none of them is readable from a linked stem.
- I did not re-shape the matching distractors to break the "second-highest overlap" pattern. The build's centroid check still passes.
- Q57 still depends on IA08-P403-Q006 being kept unchanged.
