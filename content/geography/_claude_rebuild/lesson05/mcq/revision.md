# Revision of the 87 new Lesson 5 MCQs (after the cold review)

Backup of the pre-revision folder: `mcq05/NEW_backup_prerev/`. Sources edited: `q_a.py`, `q_b.py`, `q_c.py`, `qlib.py`, `build.py`. `new_questions.json` and `coverage.md` were rebuilt.

Final checks: `build.py` gives 0 length flags, 0 errors, 0 warnings, BUILD CLEAN. `check_mcq_giveaways.py` gives 0 problems. 87 questions; answer spread A 23, B 23, C 20, D 21. 53 questions changed (some changes are only in shared confusables tables).

## Key changes (all rechecked by hand)

| Q | Old key | New key | Why |
|---|---|---|---|
| 46 | 4 (1, 2, 3) | 3 (1 and 3 only) | Statement 2 now false: it says Bhuj 2001 struck on Independence Day (it was Republic Day). This stops the checker flag "only in distractors only" when all statements are true. |
| 58 | 3 (both) | 2 (only 2) | Statement 1 now false: it says the Richter scale ends at 9. |
| 83 | 3 (both) | 1 (only 1) | Statement 2 now false: it says bauxite is a copper ore. |
| 35, 54, 67 | same letter | key strings changed | List II reordered: Q35 is now A–1; B–3; C–4; D–2, Q54 is now A–4; B–1; C–3; D–2, Q67 is now A–2; B–1; C–4; D–3. All 7 match keys are now different. |

## Fact items
- **Q46 st. 3:** now says "Among earthquakes with the epicentre on the Indian landmass, the 1950 Assam earthquake (8.6) is the largest recorded". The explanations say Sumatra–Andaman 2004 (Mw 9.1) was larger, but its epicentre was offshore. The EQ table and Q60 now use the same "Indian landmass" wording.
- **Q79:** stem now reads "According to National Geographic … active volcanoes". The options are 75 / 50 / 90 / 25 (90 is the earthquake trap). It is a how-to-answer item: older Telugu books say "half". The new option-2 explanation no longer reads as "pick the other one".
- **Q35:** B is now Scandinavian Mountains, not Vindhya. The how-to note says Telugu books call the Vindhya Caledonian, but Vindhyan rocks are Proterozoic. The Q38 explanation and the MTN table now say the same.
- **Q47 / Q49:** the 2002 merger of Zone I is no longer said to happen "after Latur". Q49 A is now "In its 2002 revision BIS merged Zone I into Zone II". The explanations say Latur came first but is not the official reason. ZONES table row fixed.
- **Q48** (a second Zone VI item on a changing fact) is replaced by a stable A–R item: tectonic quakes are the most numerous and strongest (A), with elastic rebound as R (F086, F083). The key is still 1.
- **Q50:** now has the as-of date (November 2026).
- **Q75:** was not in the lesson (it relied on coarse grains). It now asks why the Bhongir batholith is seen at the surface, which the lesson covers (cover rock eroded). It has four new distractors on vent, fissure/dyke and earthquake.
- **Q26 R:** now says "is believed to have passed over" the Réunion hotspot.
- **Q62:** options are now VI / V / VII / VIII, and the stem names USGS, so the key is VI. The explanation no longer says "pick VIII if offered"; it now says "USGS means VI; by the Telugu textbook, VIII".

## Ambiguities
Q40: the stem now says "by the present geological classification", and all four options have the same shape (the EN and TE Andes options match). Q46 and Q79 are covered above.

## Giveaways
- **Q1:** all four options are now transliterated terms (ఓరోజెని, ఎపిరోజెని, డినుడేషన్, ఆగ్రడేషన్). The echo of "కదలిక" between stem and options is gone.
- **Q3:** the bracket is removed, the distractors are in a plain register, and TE now says "పది కోట్ల".
- **Q8:** all options now share the same "…, so …" / "…తేలుతుంది" form, and "కాబట్టి" is removed.
- **Q17:** now asks "which of these is a minor plate?" without giving the thresholds. The options are Indian / South American / Antarctic / African.
- **Q30:** "(Graben)" removed from the stem. The salt and caldera options are replaced by a fold-crest option and a crater-lake option.
- **Q38:** the key no longer repeats "block".
- **Q40:** covered under Ambiguities above.
- **Q53:** the options are now a clean 2x2 of wider/smaller area and stronger/weaker shaking.
- **Q63:** all options are acronyms with a city: INCOIS, IMD, NIO, ISRO.
- **Q81:** the key no longer says "layers", and the absolute word in a distractor is removed.

**Matching (all 7):** new distractors are built so that the key never shares the most pairs with the other options. Each set has one 0-correct rotation, one with a single correct pair and one with two. `build.py` now fails the build on a centroid key or a duplicate key string. `qlib.M` takes a `why` argument, and every wrong option's explanation now says why each wrong pair fails.

## Weak distractors
- Q7: Lystrosaurus "only in Africa".
- Q13: four real ridges.
- Q22: the absolute wording is removed.
- Q45: 6.3 / 5.6 / 7.0 / 7.7.
- Q55: plausible wrong methods.
- Q61: "10 levels, I to X" is now the Rossi–Forel trap.
- Q68: 5 lakh / 15 lakh / 2 lakh / 50,000.
- Q80: options on hotspots and ridges.
- Q82: Hydration.
- Q16 / Q15: the Q16 stem no longer gives away 7.

## Telugu
- Glossary terms: అస్తినోస్ఫియర్ (Q22), మౌనా కీ (Q34).
- Coined terms replaced: Q25 uses దగ్గరకు వచ్చే / దూరం జరిగే. Q43 uses ఎలాస్టిక్ రీబౌండ్ సిద్ధాంతం.
- Q28 and Q67 TE lists now carry the English terms. Q67 now has ఆఆ లావా (Aa).
- Q69: "ఈ పాఠంలోని వర్గీకరణ" removed.
- Q76: "దాన్ని" fixed.
- Q65: only one city name is used now.
- NCERT is now జాతీయ విద్యా పరిశోధన శిక్షణ మండలి (Q71, Q84). GSI as భూగర్భ is no longer used.

## Duplicate clusters
- 47–50: Q48 replaced, and Q49 now tests the 2002 revision versus Latur's location.
- 52 / 63: they no longer share any distractor institution.
- 15 / 16: separated.
- Q36: the list order is changed, so its key (3, 1, 4, 2) no longer equals Q18's.

## Not done / for the lesson owner
- Q29: TE bracketed English could not be added, because `build.py` forbids brackets in TE options. It is left as is (rated low by the reviewer).
- The lesson (lesson_05_rebuilt.md, row 1950 near line 1018) still says "భారత ప్రాంతంలో నమోదైన అతి పెద్దది". It should be aligned to "భారత భూభాగంపై అధికేంద్రం ఉన్నవాటిలో". The lesson was not edited.
