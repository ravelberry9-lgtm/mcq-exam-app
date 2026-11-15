# L26 NEW MCQ revision (Opus)

Result: 64 questions (dropped 024, 032; 008, 063, 065, 066 rewritten as new why/how items with the same ids). build.py CLEAN (0 errors, 0 length flags; every section still has a why/how item; no fact left without a question). check_mcq_giveaways.py: 0 problems. Keys: A6 B22 C19 D17 (A is still the least-used new key, as build.py requires).

## Lesson edits (S/L26/FINAL/lesson_26_rebuilt.md, ids kept; build_html.py 26 is clean)
- X21 (changing): e-NAM 1,389 -> **1,656 mandis, 23 states + 4 UTs (Lok Sabha written reply, 19 Mar 2026; latest as of Nov 2026)**. The old 1,389 (PIB factsheet, Feb 2024) is kept as the earlier count. The sources line is updated too. Checked by web search: Lok Sabha reply of 19 Mar 2026 (MoS Bhagirath Choudhary) and the PIB 10-year e-NAM note of Apr 2026 both give 1,656.
- Cereals: కాయధాన్యాలు (which means pulses) -> **ధాన్యాలు (Cereals)** in the glossary line, the section text, the table, F061 and F062. The glossary TSV has only పప్పు ధాన్యాలు = Pulses, with no cereal entry. Millets are now **చిరుధాన్యాలు**. The section adds a note that the book writes "కాయధాన్యాలు" and that "తృణధాన్యాలు" is used for both cereals and millets, so students should go by the English term in brackets. I avoided తృణధాన్యాలు for cereals because it collides with millets.

## Must-fix items
- 042: new stem "as per the Lok Sabha reply of 19 Mar 2026". Key 1,656. Distractors: 1,389 (Feb 2024 PIB, an older-count trap), 585 (phase-1 target), 1,522. No round numbers. The explanation has a how-to on picking the figure for the date in the question. MKT table updated.
- 023: term fixed. Statement 3 now gives the rule "every millet is a coarse cereal, not every coarse cereal is a millet", which replaces the garbled list item and cuts the overlap with IA12-P461-Q005. The key is still B.
- 008 (duplicate of O45-030): replaced with a new why item. Production rises, so why can the value of output fall? Because of price (F021). Distractors are area, yield alone, and financial year.
- 029, 039, 041, 062: all self-eliminating distractors replaced with near-misses. 029: "brings new water like a canal", "lifts groundwater like a tube well", "tank, like sprinkler". 039: "drop chemicals fully for bio-agents", "spray at first sight", "resistant varieties as the single step". 041: "repealed Nov 2022", "withdrawn by Ordinance Nov 2021", "repealed Dec 2020". 062: "NSA counted twice", "current fallow added to GCA", "inverted NSA/GCA ratio". 066: see below.
- 063: replaced. New A-R: A "Barley is a coarse cereal" (true); R "Barley is a millet, and millets form part of the coarse cereals" (false, so key C). R is now plainly false. It no longer repeats Q023's maize statement.
- 035: R is now unarguably false: "Hybrid seed is the grain an open-pollinated single variety sets in the field."
- 049: the 9% explanation now reads: 9% is the bank lending rate; the 2% subvention brings it to 7%; prompt repayment takes off 3% more, giving 4%. The main explanation says the same.

## Duplicates and overlaps
- Dropped: 024 (same test as IA12-P462-Q001) and 032 (same as IA12-P462-Q005 / P463-Q001). existing_map.py now maps F098 to P462-Q005 and P463-Q001.
- 065 (food loss vs waste, which duplicates O48-009/010/015/020): replaced with a new why item, "how does e-NAM get a better price?" (more buyers bid on one lot). Distractors are MSP procurement, one national price, and warehouse-receipt loans.
- 066 (overlapped 054/055): replaced with a new why item, "why is a Godavari Zone variety not recommended for the Scarce Rainfall Zone?" The 057 explanation sentence that gave this away was removed.
- 054: option notes no longer name 126/NARP or 20/NBSS&LUP, so they don't leak 055. The explanation also drops those counts. 055: the awkward note is reworded.
- 052: the 1800-180-1551 number is removed, so it no longer leaks IA12-P480-Q002. 060: R changed from Western disturbances (a duplicate) to "the NE monsoon of Oct–Dec gives south coastal AP and Rayalaseema a good part of their rain" (true). The key is still D. Partial duplicates I kept: 005, 022, 028, 031, 045, 046, 064 (each tests a new angle).
- Leaks: 001 (option D replaced; it no longer gives 45%), 005 (option note no longer gives 45%), so 006 is clean. 058: the 157% option is replaced by 141%. 020: the PM-KISAN note no longer gives Rs 6,000. 021: the Ceiling Act 1973 mention is removed.

## Other flags fixed
- 001: weak B/D replaced with "most workers left farming" (about 46% still work in farming) and "farm exports fell".
- 012: B is now fragmentation, a real confusable.
- 021: options are 11 months, 12 months, 3 years and 6 months; every option now has its own explanation.
- 026: the Telugu option now includes "100 తో గుణించిన".
- 027: 200 cm replaced with 100 cm, with a note on why NCERT's 75 cm holds.
- 038: statements swapped (key A), because statement keys were over-concentrated after the drops.
- 057: D is now "single soil type such as black soil".

## Left as is (reviewed, low risk)
016 (soft Green Revolution remark), 018, 019, 025, 034 (pure recall of the place name), 036, 064 (key is the longest option; the content is sound). build.py warnings that remain: 005/041 have a stem number repeated in one distractor (by design); 023 statement 3 uses "every" in a true statement.
