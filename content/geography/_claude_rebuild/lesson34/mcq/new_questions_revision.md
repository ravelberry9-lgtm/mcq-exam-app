# L34 MCQ NEW revision (review.md items)

Result: 73 questions, no drops. `build.py` BUILD CLEAN (0 errors, 0 length flags, every fact covered except F051 as before, every section has a why/how item). `check_mcq_giveaways.py new_questions.json`: 0 problems. Keys: A 15, B 19, C 18, D 21 (A is still the least frequent new key and at least 20%). Combined with the linked set: A 60, B 66, C 56, D 54. A/R keys (9 items): A 3, B 3, C 1, D 2. Statement keys are unchanged (2-statement A/B, 3-statement A/B/C). Matching key positions are 4, 2, 3, 3, 4.

How it was done: `q_new.py.bak_review` is the reviewed source. `rev_blocks.py` holds the replaced questions and `rev_apply.py` holds the other edits (each string edit must match exactly once). The script rebuilds `q_new.py`. All 28 questions that changed were solved again blind, and every key matches. The other 45 questions are unchanged, and the reviewer's blind solve of them stands.

## Fixes the brief asked for
- **026**: the stem now says "Andhra Pradesh here means undivided Andhra Pradesh (2011)" (EN and TE). The key is unchanged (C). The build warns that the stem token "Andhra" appears only in the key. This is accepted: the note only defines a term, and it was asked for.
- **Stem-tag leaks**: 019 "(Suburbanisation గురించి)" is now "(Urban growth)". 039 was rewritten (see below). 068 "(Population projection)" is now "(Population figure)".
- **034 script giveaway**: the TE key is now "నాలుగు రకాలు: తడి, పొడి, శానిటరీ, ప్రత్యేక జాగ్రత్త", so all four options are in Telugu.
- **050 Amaravati**: the fragile claim "not a municipal corporation" was removed. The question is now an A/R item. A says "As of 2026, Amaravati is the statutory capital of Andhra Pradesh", which is the lesson's wording and the shared fact (AP Reorganisation (Amendment) Act, 2026, assent April 2026). R says "As of October 2026, AP has 17 municipal corporations". Both are true and R does not explain A, so the key is B. The question is marked how-to-answer, and the explanation tells students to check the date.
- **031 JJM (Urban)**: statement 1 is now "AMRUT 2.0 is the scheme for tap connections in rural homes" (cleanly false). The explanation adds a line: the 2021–22 Budget called the urban plan "Jal Jeevan Mission (Urban)" and it was launched as AMRUT 2.0 (checked with WebSearch, PIB PRID 1759593). The key is unchanged (B).

## Cross-leaks broken
- **005 → 004**: 004 no longer tests the 75% rule. Its statements are now: (1) governed by a gram panchayat (true), (2) a minimum of 10,000 (false), (3) 400 per sq km (true). The key is still C. The gram-panchayat line was removed from 005's explanation.
- **022 / 023**: 022 statement 2 is now the threshold/range swap (false). 023's options no longer define the threshold.
- **033 → 035**: the 033 key is now Nellore (not selected), and the Super Swachh League line was removed from its explanation. 035 is the only question keyed to Vijayawada.
- **011 → 012**: 012 statement 1 is now "Kerala (Keralam) is second in urban share" (false; Mizoram is second). Statement 2 (17.3% to 31.1%) is unchanged and the key is still B.
- **046 → 044**: 046 was replaced (see duplicates), so Sanjan no longer appears in it.
- **053 → 056**: the 053 distractors are Caldwell, Risley and Chatterji. Nishada/Kirata were removed from its explanation. The urban names Geddes and Christaller are gone.
- **039 → 040**: 039 no longer lists the group growth rates.
- Also fixed:
  - 015 no longer gives the 2011 UA ranks, which leaked 016.
  - 068 no longer gives 4,93,86,799 or 4,95,77,103, which leaked the new 066.
  - 014 no longer repeats 008 statement 1.
  - 058 no longer names Gondi, which leaked 056.
  - 013 D no longer says "Technical Group projection", which leaked 068.

## Near-duplicates of linked questions replaced or reframed
- 004 / 005 (ORIG-61-022): 004 was changed as above. 005 now asks why the test uses workers and not the whole population, and "male main workers" stays only in the explanation. The new distractors are "the Census leaves children out of a town's population" and "workers' taxes decide municipality status".
- 008 (A19-P558-001): statement 3 is now "for boundary expansion to add urban population, people must first migrate" (false). The key is still "Exactly two".
- 014 (ORIG-61-019/-023): new A/R. A: the urban share rose faster in 2001–11 than in 1991–2001 (2.1 vs 3.3 points). R: Census Towns nearly tripled. Key A.
- 018 (A19-P557-007): new A/R. A: "UN limit, eight megacities in 2011" (false). R: eight UAs above fifty lakh (true). Key D.
- 021 (A19-P559-002): new A/R, finger shape caused by road strips. Key A. This also removes the naming-vs-cause ambiguity.
- 046 (A19-P563-002): now a Jewish community and coast pair (Bene Israel – Maharashtra coast). Key B. Fact F087.
- 058 (A19-P567-001, ORIG-68-017): now asks why Kuvi and Telugu are in the same South-Central Dravidian group. The distractors are script, region and Eighth Schedule. Key C.
- 059 (A19-P569-003/P570-003): now matches Sindhi–21st (1967), Konkani–71st (1992), Santali–92nd (2003) and Art 350A–primary mother-tongue instruction. Key D. This keeps F118 covered.
- 060 (A19-P569-005): statement 2 is now "more than one in ten Indians returned Telugu" (false, 6.70%). The key is still C.
- 061 (A19-P567-005): new A/R. A: "all 22 Eighth Schedule languages are national languages" (false). R: Art 348, English in the SC/HCs (true). Key D. This keeps F119 covered.
- 066 (A19-P571-001): now a "How many…" application that works out the 13-district figure: 4,95,77,103 minus 1,90,304 = 4,93,86,799. The distractors are an add slip, a borrow slip and a digit slip. Key B. This keeps the ap-population why/how count.
- 069 (A19-P575-002/P574-001): new A/R. A: AP's Christian share (1.38%) is below India's (2.30%). R: the three AP shares add to 99.57%. Key B, which also breaks the "R begins with Because, so the key is A" pattern.

## Weak distractors
- 013: "UN 34%", "provisional 31.16%", "final 31.14%" (key) and "NFHS 2019–21 value". The key's TE ending now matches the others (…కాబట్టి).
- 023: equal range, rivers and hills, overlapping regions; the key is circles leave gaps.
- 039: rewritten as a neutral ratio question ("a group's number grows but its share falls — when?"). The options are faster than, total stops growing, same rate, and slower than the total (key D). The explanation uses neutral numbers.
- 042: Mizoram was replaced by Tamil Nadu. The explanation keeps the "Kerala (Keralam), same state" line. The TE options cannot take brackets, so Keralam stays in the option explanation and the main explanation.
- 048: resident population, advance forecast, and a sum since 2013; the key is repeat visits.
- Non-lesson names used only as plainly wrong distractors: Caldwell and Risley (053), Tamil Nadu (042), West Bengal coast (046), NFHS (013), Kerala as second (012). Kerala's 47.7% is in the lesson table.

## Also
- 067 stem now says "(with the seven transferred mandals)".
- Remaining build warnings are minor: stem token "Kumbh"/"Telugu" in a distractor (048, 058), "Andhra" in 026, and the key being strictly longest by a few characters in 039 TE, 046, 048 TE and 068 EN, all under the 1.3x length flag.
