# Chapter 3 new MCQs: revision after two blind reviews

Inputs: review_part1.md (N001–N082) and review_part2.md (N083–N163 plus GEO-BOOK-P004-M007).
Backup taken before any edit: `mcq03/NEW_backup_prerev/`.

## How the edits were made

- The sources are still `q_a.py` … `q_j.py`. Every change is written as a short function in `rev/b01.py` … `rev/b14.py`, one function per question.
- `revise.py` copies the sources back from the backup and then applies `rev/b*.py` in order, so a rerun gives the same result. `srctool.py` loads and rewrites the n-th `Q(...)` call.
- After that, `build.py` and then `finalize.py` were run. `new_questions.json`, `coverage_table.md` and `coverage.md` were regenerated.
- 125 questions were touched; the 185 edit functions include several follow-up passes on some of them.
- M007 is edited directly in `m007_fix.json`.

## Final validator state (build.py)

- 0 errors, 0 warnings, 0 length flags.
- Answer spread: A 41, B 41, C 41, D 40.
- Assertion–reason keys: A 1, B 1, C 2, D 1.
- Match keys: 13 distinct keys over 31 questions, none used more than 4 times. No key is in list order or reverse list order.
- Coverage: unexplained facts 0.

New checks added to build.py:
- **Key breaks option template** (single-answer questions only). This is a warning when the three distractors agree on a feature and the key does not. The features are:
  - TE ending word, such as కాబట్టి or వల్ల
  - EN opening word
  - a semicolon
  - digits
  - brackets
  - a hedge word (ఉండవచ్చు, may, might, probably)

  On its first run it found about 20 more questions beyond the 17 the reviewer named, and all were fixed.
- **Reverse-order keys** are now errors: a match key of A–4, B–3, C–2, D–1, or a sequence key of 4, 3, 2, 1.

## Must-fix items

| Item | What was done |
|---|---|
| **N042 wrong key** | Statement 3 now says "మన Galaxy (Milky Way) లోనే జరిగి కంటికి కనిపించిన చివరి Supernova SN 1054" (EN "in our own galaxy, the Milky Way"). The key is now 1 ("1, 2 మాత్రమే"). The explanation and all four option explanations agree: the last one in our galaxy was SN 1604 (Kepler), and SN 1987A was naked-eye but in the LMC. |
| **N136 Tide Tables** | Checked on the web. The sources found do not settle who publishes the Indian Tide Tables today: Survey of India's Geodetic & Research Branch has a long tide-prediction history, and the NHO lists tides among its functions. The lesson itself names both (lines 8660 and 8675). Because this could not be confirmed, statement 3 was replaced with a safe lesson fact: "తీరం ఆకారం, సముద్రం లోతు వల్ల ఒక్కో చోట పోటు ఎత్తు మారుతుంది." The key stays 2. F728 is now untested, with a note in existing_map.skip. **Lesson lines 8675 and 10253 should be checked or softened.** |
| **"Key breaks template" pattern** | All 17 reviewer IDs were fixed, plus the further ones the new check found (023, 030, 035, 041, 049, 054, 057, 061, 066, 071, 075, 086, 106, 108, 119, 126, 150, 156, 157, 158, 159, 161). All four options now share the same ending and shape. Where a distractor carried an absolute word, it was removed or the wording was hedged like the key (096, 110, 116, 123, 150, 151, 158, 163, 053, 106, 119, 126). |
| **N137 reverse-order key** | List II was reordered. The new key is A–2, B–4, C–3, D–1, and the answer is still option 3. |
| **N095 and N109 solvable without knowledge** | N095 (the years were in order) is now a single question: "about 76 years; 2061", with the old dates kept in the explanation. In N109, List I is now "Kepler first, second and third law, Astronomia Nova (1609)", so no words match between the lists. |
| **"పాఠం ప్రకారం" and quoted-question stems** | Direct stems now in 021, 022, 057, 064, 090, 102, 103, 118, 147, 157, 161. All "పాఠం చెప్పే … / the lesson says" option explanations were rewritten with a real reason (004, 049, 051, 053, 087, 088, 091, 108, 119, 125, 127, 138, 158, 160). N075's explanation no longer says "పాఠంలోని జాబితా". |
| **Statement option explanations** | Every statement question now says why the false statement is false in each wrong option. That is 37 statement questions, including 10 that the reviews did not list: 004, 085, 089, 100, 121, 130, 131, 141, 149, 153. |
| **Statement-key variety** | All-true answers dropped from 6 to 2 (N060, N087). N003, N032, N125 and N138 were made mixed by changing one statement to false. Keys were also moved in N028 (now 2), N072 (now 2), N045 and N069 (now "ప్రకటన 2 మాత్రమే"), and N076 (now "రెండూ సరైనవి"). Three-statement keys are now 1×11, 2×9, 3×7, 4×2, and two-statement keys 1×1, 2×3, 3×4. |
| **M007** | List II gains a fifth value, 38.8 AU, which is the Titius–Bode prediction for Neptune. Options 2 (D–5) and 3 (C–1, D–5) are now sorted-order traps, so sorting the numbers leaves three candidates and the student must know that Neptune is about 30 AU. The key is unchanged (option 1, A–2; B–3; C–4; D–1). The explanation was cut from 9 sentences to 4. The learning table is trimmed to 7 rows, including a Titius–Bode row. Note: 38.8 AU is the standard Titius–Bode value; the lesson gives the law but not this number. |

## Keys changed (each rechecked against the lesson)

- **Changed by rewriting a statement:**
  - 003 → 2 (layer order swapped in statement 1)
  - 028 → 2 (statement 1 false, statement 3 now true)
  - 032 → 3 (12 constellations, false)
  - 039 → 3 (R: "Fusion holds a white dwarf up", false)
  - 042 → 1
  - 045 and 069 → 2 (statements swapped)
  - 072 → 2 (statement 1 says Mercury, false; statement 3 "no moons", true)
  - 076 → 3 (Ozone blocks UV, true)
  - 125 → 1 (ChaSTE values swapped)
  - 138 → 1 (La Rance and Sihwa swapped; "as of 2024" added)
- **026:** rebuilt as "Polaris altitude ≈ latitude", answer 3.
- **Match questions relisted to break repeated or patterned keys:** 029, 055, 077, 081, 137.
- **Answer position moved for spread, with options and explanations moved together:** 029, 050, 092, 099, 120 (C→D) and 023, 035, 053, 067 (B→A).

## Other reviewer items (all applied)

**Weak distractors replaced with real confusions:**
- 002, 014, 023, 035, 036, 047 (full 2×2 Schmidt/Chiu × expansion grid), 054, 066, 067, 080, 088
- 093, 104, 106, 110, 115, 118 (Mass vs Density), 119, 122, 126, 127, 129, 132, 134, 150, 151, 154, 156, 158, 159, 160, 162, 163

**Distance or number tells removed:**
- 021: options are names only; Sagittarius Dwarf added; the "debated status" note and "2026 నాటికి" added.
- 102 and 103: names only, so the answer is not the biggest or smallest number.
- 064: now the IAU 2015 B3 value, with the old 5778 K key explained.
- 065: asks only for the place.
- 090: Ceres, Vesta, Pallas, Hygiea.

**Symbols written in words:**
- Arrows in 007, 024, 033, 046, 143.
- Minus signs in 028, 103, 104, 125, 135.
- ¼, ½ and fractions in 105, 106, 118, 119, 128, 134.
- T² and a³ in 109.
- వర్గం in 061.

**Facts and wording:**
- Dated or hedged facts: 008 (H₀ 67–73), 029 and 032 ("2026 నాటికి"), 041, 079 (Olympus Mons "రెండున్నర రెట్లు"), 138, 040 (0.012).
- Telugu fixes: 056 ("కూడా కాని"), 083 (Mass, not బరువు), 107, 108, 139 (all "చెప్పడం ద్వారా"), 112 (Telugu season names; irrelevant last sentence removed).
- 007: "ఎగతాళిగా అన్నాడని చెబుతారు" instead of a flat claim.
- 038: Chandra "1999 లో ప్రయోగించిన".
- 099: "Lonar (Maharashtra)" with the Ramsar clue, so no words match between the lists.
- 140: List II now describes each author instead of naming him.
- 147: anchored on the 1543 De revolutionibus, so the loose "Father of modern astronomy" title is not ambiguous.
- 155: the explanation opens with the answer.

## For the editor

- **Lesson follow-ups:**
  - Indian Tide Tables publisher (lines 8660, 8675, 10253).
  - Olympus Mons "మూడు రెట్లు", if present: the ratio is about 2.5.
- **Overlap left as is:** Saturn density appears in 085 and 159 (102 now asks for Earth); Neptune's prediction in 087 and 160. Neither overlap was dropped, because the coverage table depends on them.
- **N074 and N107** still use "In what sense" / "minus sign" stems. The reviewers called these clean, and the sign is the subject of N107.

Sources checked for N136: https://www.geographyandyou.com/survey-of-india/tidal-predictions-geodetic-and-research-branch-survey-of-india , https://docs.iho.int/mtg_docs/rhc/NIOHC/NIOHC7/NIOHC7_India_National_Report.pdf
