# L27 NEW MCQ revision (Opus), responding to review.md

Result: 77 questions (ids kept, N057 and N061 replaced in place). build.py BUILD CLEAN, check_mcq_giveaways.py 0 problems. New-key spread A 12 / B 25 / C 22 / D 18 (A is the rarest). Matching keys are unchanged, none is 2-4-1-3. 2-statement keys are A/B only. No fact is left uncovered.

## Giveaways
- N063: the distractors are now J&K places (Sopore, the apple town; Gulmarg; Bhaderwah, known for lavender).
- N077: the CCRI expansion is gone from the stem. Option explanations no longer name Tocklai, Jorhat, RRII or IISR.
- N058: four parallel climate + rain + soil options (cool hill / 100 cm / red; hot dry / <75 cm / black; mild / 150 cm / alluvial). The stem says కేరళ (Keralam).
- N076: options are now in one format (Spices, Sugarcane and sugar, Millets, Oilseeds). The Lucknow sugarcane trap is kept. No CCRI/RRII leak.
- N070: all options are three districts joined by "and". "Parvathipuram Manyam" is used in EN and TE, with a note on the ASR "Manyam" confusion. Distractor C changed so it does not cue N057 (West Godavari).

## Weak distractors
- N005: wells changed to borewells (బోర్ల). New distractors: dry-sown on soil moisture, farm-pond rainwater, deep-water floodplain rice.
- N012: the stem now says bread/biscuit flour (no chapati "rise"). The key is shortened. Distractors no longer reverse three facts.
- N025: canal water for a second crop, south-west monsoon, borewell groundwater.
- N026: Niger and Safflower replaced by Castor and Sunflower. Castor is an industrial crop that is still among the nine, which makes it a real competitor.
- N028: the options cross "industrial / Gujarat", so each distractor is half right.
- N038: now a top-three order question (WB, Bihar, Assam vs. permutations and Odisha). The old version was a length giveaway with absurd states.
- N041: the ranges are now 6–8, 8–10 and 18–24.
- N044: D is now cigar/cheroot leaf (N. tabacum).
- N045: black water-holding soil, more sun, no frost.
- N051: new distractors are Arabica's high hills, no shade trees, and higher price. The "70%" line was removed from the explanation (it answered N050).
- N053: now asks where Brodie grew coffee (Pamuleru vs. the Araku trap, Horsley Hills, Papi Hills), so it no longer recycles lesson names.

## Leaks / overlaps (no question now answers another)
- N049: the events are neutral (no Brodie, Pamuleru, Robert Bruce or Thattekkad), so it no longer gives away N053 or N055.
- N019: statement 2 is now the 2018 national year vs. the 2023 UN year (F047/F048). The Rajasthan/Karnataka millet line is gone, so N020 stands alone.
- N001: the rice statement is replaced by sugarcane (false, Brazil) and banana (true). Rice is removed from the explanation. N003 alone tests rice in 2024–25.
- N060: statement 2 is now Karnataka/onion. The AP rank list is removed from the explanation. AP ranks live only in N068.
- Board HQs: N046 now tests the first GI (Assam vs. Darjeeling, false) and the Tea Act 1953 (true), key B. HQ lines were removed from N055 and N064. Only N052 names board HQs. N064 now uses the Jagtial and Karimnagar traps instead of Kozhikode (the IISR leak).
- N076 and N077 no longer name each other's institutes or N074's Tocklai/Jorhat. The N076 millets explanation no longer names IIMR (N075).

## Partial overlaps with linked questions
- N016: the sorghum and finger-millet rows (linked P467/P468) are replaced by rice (Oryza sativa, F008, previously untested) and maize (Zea mays).
- N061 (cocoa shade) duplicated IA12-P472-Q002, so it was dropped. F148 is now mapped to P472-Q002 in existing_map.py. N061 is now an apple chilling-requirement "why" item (F146), which keeps a why-question in horticulture-spices.
- Kept as distinct angles: N012 (gluten), N014 (largest use), N036, N051 (yield/hardiness, not altitude), N070 (district names), N074, and N075 (the Ludhiana maize-IIMR trap).

## Telugu
- Nitrogen fixation is now స్థిరీకరించు in N021 (statement and explanation). N061 is gone. The same term was fixed in the lesson F055 fact line (L27/FINAL/lesson_27_rebuilt.md, now "స్థిరీకరించినా (Nitrogen fixation)") and in facts.txt.
- కేరళ (Keralam) is used in the N004, N055 and N058 stems and explanations. N004's explanation carries the exam line "Kerala and Keralam are the same state". The lesson's first Kerala mention (rice/Kuttanad paragraph) now reads "కేరళ (Keralam; 2026 నుంచి అధికారిక పేరు, రెండూ ఒకే రాష్ట్రం)". build_html.py 27 ran clean (no tag, id or link errors).
- Other fixes: N012 విసిరితే changed to మిల్లింగ్; N017 stem uses "కోడో మిల్లెట్ (Kodo millet)"; N062 List II has the English term with the Telugu in brackets (Berry, Stigma, Capsule).
- Not changed: N053 Telugu options are still transliterated, because build forbids Latin words in TE options. The stems and explanations use the Latin names, as the lesson does.

## Ambiguous A-R
- N032: R now says groundnut needs warmth and moderate rain at sowing and flowering, both only in the SW monsoon season. It is a clear cause, key A.
- N071: A is now framed as "counted under Eluru rather than West Godavari". R (the 2022 upland/delta split) directly explains it, key A.

## Thin explanations
- N059: the 2005–06 option is now explained as the National Horticulture Mission, merged into MIDH in 2014–15. 2019–20 is explained as already five years in.
- N072: the options are 1.72/8 (old book), 2.27 (July 2024 figure), and 3.49/28 (28 is the total AP districts). Each has a real reason.
- Several explanations now carry the trap line (N017, N028, N044, N045, N055, N063).

## N057 replaced
- The vulcanisation-year item (low value, its dates were cues) is replaced by an AP rice-district group question for 2025–26 (F164, previously untested, how_to_answer). Key: West Godavari, East Godavari and Kakinada. Distractors are Rayalaseema, south Rayalaseema and north Andhra groups.
