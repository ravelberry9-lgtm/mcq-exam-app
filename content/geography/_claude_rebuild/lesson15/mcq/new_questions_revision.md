# Lesson 15 — MCQ NEW REVISE

Result: build.py BUILD CLEAN (0 length flags, 0 errors); check_mcq_giveaways.py on new_questions.json: 0 problems (checker.txt). 57 questions, ids GEO-NEW-15-001…057 unchanged. **No key changed**: answer letters compared with `pipe/L15/mcq/NEW_prerev_bak/new_questions.json` match for all 57. Spread A15 B13 C15 D14. The backup of the sources from before this revision is in NEW_prerev_bak/.

## 1. Giveaways
| Q | Change |
|---|---|
| 003 | "(Somali)" / "(సోమాలియా)" removed from both stems. |
| 011 | The TE key now carries "Positive IOD" like the three distractors, so it no longer stands out as the only pure-Telugu option. In the EN key, "Indian Ocean" became "western half of the ocean" (this also clears the stem-token warning). |
| 016 | All four TE options are in Telugu script now (చురు, ముంగేష్‌పూర్, అల్వార్). |
| 024 | ITCZ taken out of the TE and EN key ("monsoon cloud band / clouds"). Option D replaced with "islands are cooler than Kerala, so the wind turns to them first", with a lesson-based reason. This removes the half-true latitude explanation. |
| 052 | TE stem bracket "(Muggy heat)" replaced by "(Coastal towns)". |
| Matching 004, 007, 020, 039, 046 | Distractors still come from L11/L12 `qlib._pick_wrong`, which was already in place (identical code). The key's A pair, its D pair and at least 3 of its 4 pairs appear in some distractor, and the key is never the strict centre option. Every matching question now passes a `why` dict, so each wrong pair is explained with one clause (for example Q20 "B–3 does not fit; Bardoli chheerha … helps tea, not coffee"). The five keys were kept, so three of them still start with A–2. |
| Sequence 013, 018, 025 | New distractor sets chosen so that the key shares fewer positions than at least one distractor (it is not the centre option). Each set has one distractor with no correct position, one with one correct position, and the key's first item also appears first in a distractor. 013: 1342 / 3241 / 4231. 018: 1243 / 2431 / 4231. 025: 1324 / 3124 / 4312. Each has a new reason line. build.py now also rejects a sequence key that shares as many positions as any distractor. |
| 004 | The 15°N item that leaked Q5's answer is gone: List II item 3 is now "Upper wind blowing east to west over south India". |
| 019 | The stem now asks about Mumbai against Delhi only. The explanation and options no longer give the Chennai figure or the Chennai date, so Q18's order and Q25's dates are not leaked. |
| 038 | Options C and D are now Shillong and Mumbai. Agumbe, Mahabaleshwar and the "Cherrapunji of the South" leak to Q26 are removed. |

## 2. Fact fixes
- 046: List I item C is now "Rashtriya Barh Ayog (National Flood Commission) report", paired with 1980. The explanation and the C clause say the commission was set up in 1976 and reported in 1980. TE: "జాతీయ వరద కమిషన్ (Rashtriya Barh Ayog)", matching the lesson.
- 015 (A): "In the NCERT division, October–November (to December in the south) is the retreating monsoon season". This follows the lesson table. The A note adds that the IMD calls October–December the northeast (post-monsoon) season. Key A is unchanged.
- 013: the explanation gives NCERT winter as December–February and the retreating season as October–November (to December in the south).
- 027 (A note) and 039 (List II item 1): "driest plains region" in place of "driest region of India", because Leh is drier.
- 005: the 30°N westerly-jet material (lesson 8) is removed from the option A explanation and from the EXP. Option C now gives the real reason.
- 014 D: "No source in the lesson…". 034 C: "15 °C is far above the 10 °C pre-condition". 050: the bullock-worship clause is removed. 047 B: the Himalayan-snowmelt explanation is reworded.

## 3. Duplicates and leaks with the existing set: rewritten
| Q | Old | New (key letter unchanged) |
|---|---|---|
| 022 | Onset date over Keralam (= GAP-054) | Reasoning: why Kerala is the first mainland area to get the monsoon (southern tip facing the SW wind, Western Ghats lift). The name-change note is kept in the EXP; no 1 June date appears. Key D. |
| 037 | India mean 116 cm (= GAP-062) | Which region is in the under-50 cm class: Kachchh (against Konkan, the Assam valley and eastern UP). Facts F074 and F073. F071 stays covered by GAP-062. Key D. |
| 043 | Subdivision boundaries vs districts (= ORIG-18-010/015/020) | A–R. A: a below-normal year has a negative deviation (F086). R: 36 subdivisions (F083). Both are true and R does not explain A. Key B. |
| 055 | AP SW share 60% vs 75% (= GAP-073, ORIG-18-003) | A–R "why". A: Nellore and Tirupati get a large share of their rain in October–December. R: north-easterly winds and Bay depressions strike the south coast. R explains A. Facts F115 and F117. Key A. The how_to_answer flag is dropped. F112 stays covered by Q54. |
| 009 | Statement 1 repeated GAP-026 (Walker found the SO) | Statement 1 is now about the Walker circulation (air rises over the western Pacific and sinks in the east; F024). Truth pattern T/T/F, key A. |
| 020 | 3 of 4 items = GAP-006 | Aandhi is replaced by Loo. This is still a controlled overlap of 3 items (Blossom, Mango, Bardoli/nor'westers). |

## 4. Telugu terms (lesson forms)
001 "వార్షిక ఉష్ణోగ్రత వ్యత్యాసం (Annual temperature range)". 020 "కాఫీ జల్లులు (Blossom showers)", "బర్దోలి ఛీర్హా", "లూ (Loo)". 029 "Monsoon break (వర్షాభావ విరామం)". 040 Isotherms "సమోష్ణ రేఖలు" (as in the glossary); Isochrones "ఐసోక్రోన్ రేఖలు", because the lesson has no Telugu term and this follows the book's "ఐసో హైప్స్" style. 046 "జాతీయ వరద కమిషన్". 022 TE option: "వాతావరణ శాఖ" in place of IMD.

## 5. Weak distractors replaced
031: the western-disturbance option (a repeat of 036) became "NE winds bring hot Thar air". 041 A: "most rain in winter from the Bay of Bengal". 047: the betting option became "most farmland under canals / dam releases". 056: A is now "longer shoreline, sea breezes", and D is now "Godavari evaporation".

## Not changed (reviewer optional or out of scope)
- 021, 048, 053, 029 are kept as controlled repeats (each has a new angle). Q48's R was reworded so it explains the letter clash.
- 008: the key was shortened slightly but is still the longest option (under 1.3 times, warning only).
- 018 (Nungambakkam note): not added.
- Existing set: ORIG-16-008's key contradicts the lesson ("rain falls over the main belt when the trough shifts"). It lives in FINAL/lesson15_questions.json and is not in this step's sources. It must be fixed there.
