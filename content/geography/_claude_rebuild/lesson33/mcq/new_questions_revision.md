# L33 MCQ NEW revision (review.md items)

Result: 77 questions (021 dropped; the number stays as a gap). `build.py` BUILD CLEAN (0 errors, 0 length flags, every fact covered, every section has a why/how item). `check_mcq_giveaways.py new_questions.json`: 0 problems. Keys: A 17, B 20, C 19, D 21 (A is the least frequent new key and above 20%). Combined with the linked set: A 53, B 61, C 47, D 57. A/R keys 1:2, 2:2, 3:3, 4:1. 3-statement keys use A, B and C. Matching key positions 4, 3, 1, 2.

How it was done: `q_new.py.bak` is the reviewed source. `rev_blocks.py` holds the replaced questions and `rev_apply.py` holds the other edits. It rebuilds `q_new.py` from the .bak; each string edit must match exactly once.

## Fact check and lesson edit (072)
- WebSearch: Haryana's cabinet brought in SC sub-classification in October 2024 by executive decision, with no Act (Drishti IAS, 24 Oct 2024: "Haryana becomes first state to clear Dalit sub-quotas"). Telangana's Act took effect on 14 Apr 2025. So "Telangana was the first state to implement it" was wrong as written.
- Lesson `S/L33/FINAL/lesson_33_rebuilt.md`: two lines changed and ids kept. The X31 bullet now says Telangana was "first by an Act" and that Haryana acted earlier by cabinet decision in October 2024. Fact F147 now says "first by an Act, Telangana (14 Apr 2025); first by cabinet decision, Haryana (Oct 2024)". `facts.txt` F147 and X31 were updated to match. Ran `python3 S/build_html.py 33`: no tag errors, no broken links.
- 072: the reason for statement 1 and the explanation now give Haryana (cabinet decision, Oct 2024) and Telangana (by Act, 14 Apr 2025). The SUB table now reads "first state by an Act". The key is unchanged (B).

## Must-fix items
- 016: the Telugu statement 1 now matches the English ("జనగణన 2027 లో అన్ని కులాల గణన 1951 జనగణన తర్వాత మొదటిసారి"). It is false and the key B stands. F023 was added to its facts.
- 015: rebuilt as an A/R that uses the lesson's hedge. A gives the Dec 2026 to Jan 2027 count in the four states. R gives the snow-bound September count and its weather reason. Both are true, but R does not explain A (key B). The explanation says "news reports say" the advance was tied to the March–May 2027 assembly terms and that the opposition criticised it. Reference dates are no longer named, so it does not leak 014.
- 033: now uses 1921–31 (11.00), 2001–11 (17.70), 1951–61 (21.64) and 1961–71 (24.80) from the lesson's Census table. The smallest gap is 3.2 points and the stem says "Using Census figures". Key 1, 4, 2, 3 (C).
- 051: statement 3 is now a plain swapped-years claim ("rose from 13.6% in 2001 to 15.9% in 2011"), which is false. TE "Census 2011" changed to "జనగణన 2011".
- 012: the stem now says "for most of the country" (EN and TE).

## Giveaways and weak distractors
- 042: options are now <12 per 1,000 live births>, <70 per lakh live births> (key), <25 per 1,000 live births> and <7 per 1,000 women>. The key shares its unit with no distractor and its number with none. The explanations use only the lesson (scale and denominator).
- 049: new data (26 / 64 / 9 lakh). All four options are decimals: 35.4, 40.6, 54.7 (key) and 182.9.
- 077: no option names the Gulf. The stem carries "(Gulf countries)". The key was shortened so it is not the longest. The UN DESA "half in the Gulf" line was removed from the explanation (it was unverified and leaked 064).
- 076 (TE): all four options now end in a verbal noun (…తగ్గడం / …రావడం / …కావడం). The 2005–06 to 2055–56 window was removed from the explanation (it leaked 050).
- 020: the distractors are real sources that did not first show the crossover: SWOP 2025, SRS Statistical Report 2024, and UN DESA Migrant Stock 2024. The stem asks which source "first" showed it. TE report names are in Telugu.
- 018: Census 2021 and "Census 2027 provisional" were replaced by Census 2001 (102.87 crore) and the Census 2027 houselisting phase. The SRS figure changed to 141 crore so it does not echo 020. 142.86 was removed from the explanation.
- 022: Mexico, Germany and the Philippines were replaced by Indonesia (about 24 crore, 2010), Russia (about 14.3) and Japan (about 12.8). Pakistan was not used: it is too close to 20 crore and would make the question ambiguous.
- 034: statement 2 no longer uses "only" ("Kerala's population fell in 2001–11", false).
- 063: B is now "about 1.4 crore", the lesson's figure for all who left home on both sides. C is now "about 7.3 lakh" (ten times too small). The explanation tells 1.4 crore apart from the 1951 count of 73 lakh, and the unclear "use the names West/East Pakistan" sentence was removed.
- 061: B is now 27.3% (dividing by total plus migrants), with an explanation of the slip. "3 in 8" was removed.

## Duplicates replaced or dropped
- 003 (repeated the provisional/final bank item): replaced by a reasoning item on count versus rate ("most infant deaths does not mean highest IMR"; F013, F014).
- 075 (repeated 933→943 / 927→918): replaced by a reasoning item, "missing women are not women left out of the census" (F088; lesson line on Sen). This also gives sex-ratio its why item.
- 066 (repeated the NPP 2045 bank item): replaced by an A/R. A is NPP 2000's voluntary approach and R is why seats were frozen. Both are true and not linked (key B). This also removes the 017 leak.
- 067 (repeated the national-law caution): now an A/R on the two dates only. A (AP, January 2026) is false and R (Telangana, January 2026 law) is true (key D).
- 070 (repeated 078 and the UP/Punjab bank item): replaced by a concept item on the lowest SC share among states that have an SC list: Mizoram 0.1%, with Meghalaya 0.6%, Goa 1.7% and Punjab 31.9% as distractors. States with no SC list are excluded to avoid ambiguity.
- 021 (one fact with 018/020): dropped. X08 moved to 018.
- 041/074: 074's explanation no longer reuses 041's numbers (18 of 20,000, 90).

## Leak chains broken
- 007: the List I/II items now cover 1872, 1881, 1951 (first of independent India) and 1941 (canvasser method). 1931 and "15th census" are gone, so 007 no longer answers 008, 016 or 010. Facts are now F019, F020, F021 and X03.
- 008: now 2 statements (Census Act 1948 true; run by MoSPI false, it is ORGI under MHA). The 1931 statement was removed. Key A.
- 009: "since 1941" was removed from the stem, so it does not answer 007 D. The TE term now matches the lesson (ఇంటింటి గణకుడి పద్ధతి).
- 010: option "16th; 8th" (Census 2027's numbers, answering 013) became "16th; 6th". The 2027 sentence was removed from the explanation.
- 011 (1872 versus 1881, answered by 006/007): replaced. It now tests the Census 2011 houselisting phase (Apr–Sep 2010; "Feb 2011" is false) and C. Chandramouli (true). Key B.
- 019: statement 1 (the full 2011 total, which answered 018) became "In 2011 India was already more populous than China" (false). Count is two (B). The derived "seven times" claim was removed.
- 031: the explanation no longer cites 1911–21 −0.31% (it answered 035).
- 038/073/036: 038 no longer states 1798 (036 showed it). Its statements were reordered so the key is A (needed to keep the 3-statement spread). 073 now tests population geometric (true) versus food geometric (false), so it does not reveal 038 statement 3.
- 017: R carries "(status as of November 2026)" and the Telugu term పునర్విభజన (Delimitation).

## Telugu and explanations
- Brackets added in stems: 010, 020, 027, 031, 033, 037, 041 (also the book term ప్రసూతి మరణాల రేటు), 042, 056, 059 (Main / Marginal workers), 061, 062, 064 (Remittances, in Telugu), 065, 068, 069, 071, 072, 077.
- "Census 2011" became జనగణన 2011 in the 030, 034 and 051 stems. 008 now uses జనగణన చట్టం (Census Act) and రిజిస్ట్రార్ జనరల్, జనగణన కమిషనర్.
- Names are in Telugu script in the TE options of 036 and 039, with English given once in the explanation.
- 002: all four TE options now end with a "కాబట్టి" clause.
- 030: the root step is now read-aloud safe ("1.1770 to the power one-tenth, then subtract 1"). The RATE table was updated to match.
- 058: the explanation was cut to the point the question asks.

## Re-solve
All 77 keys were solved again after the rebuild. The changed items were each solved and recomputed: 003 A, 007 D, 008 A, 010 D, 011 B, 012 A, 015 B, 016 B, 017 C, 018 C, 019 B, 020 B, 022 D, 033 C, 038 A, 042 B, 049 C (35/64 = 54.7), 051 A, 061 A (45.58/121.09 = 37.6; 45.58/166.67 = 27.3), 063 D, 066 B, 067 D, 070 A, 072 B, 073 C, 075 A, 077 D. The unchanged items match the review's blind solve. No wrong keys.

Remaining build warnings are acronyms (SRS, IMR, MMR, UNFPA, UN DESA) in TE options, 005 "2026" in one distractor (intended: release year), and "first" in 016 statement 1 (the fact itself).
