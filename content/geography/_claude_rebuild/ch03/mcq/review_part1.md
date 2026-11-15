# Review part 1: GEO-NEW-03-001 to 082 (82 questions)

Method: every question solved independently, arithmetic redone, key compared (answer is 1-indexed: 1=A). Option lengths measured with a script; every option_explanations block checked for the "సరైనది" marker sitting on the keyed option. Lesson chapter_excerpts spot-checked against lesson_03_rebuilt.md. No files edited.

## Summary

- WRONG-KEY: 1 (Q042)
- Clean (no flag at all): about 40 of 82
- Flagged: AMBIGUOUS 3, GIVEAWAY 11, WEAK-DISTRACTOR 9, TELUGU 6, WEAK-EXPLANATION 8 (plus a blanket issue for statement-type option_explanations), SYMBOLS 5, NOT-IN-LESSON 0
- Key spread over the 82 is fine: A 21, B 20, C 22, D 19. After fixing Q042 (3 to 1): A 22, B 20, C 21, D 19.
- Option lengths are well balanced overall. A script found no question where the correct option is clearly the longest. I checked this because I first suspected Q030, 049, 057, 066, 071 and 074, and the character counts cleared them.

## WRONG-KEY

**Q042** (statement question on supernovae)
- Statement 1 is true: no hydrogen lines means Type I, with hydrogen means Type II.
- Statement 2 is true: Type Ia are standard candles.
- Statement 3 is false: the last naked-eye Milky Way supernova was SN 1604 (Kepler), not SN 1054.
- The correct option is "1, 2 మాత్రమే", which is option 1. The key says 3 ("1, 3 మాత్రమే").
- The explanation itself says "1, 2 సరైనవి", so the explanation contradicts the key. The EN explanation says the same.
- Fix: set `answer` to 1.
- Also fix option_explanations, which currently put "సరైనది" on option 3:
  - Option 1: "సరైనది. ప్రకటన 1, 2 సరైనవి; ప్రకటన 3 తప్పు, కంటికి కనిపించిన చివరి Supernova SN 1604."
  - Option 2: "తప్పు. ప్రకటన 2 సరైనదే కానీ ప్రకటన 1 కూడా సరైనది, ప్రకటన 3 తప్పు."
  - Option 3: "తప్పు. ప్రకటన 3 తప్పు (SN 1604, SN 1054 కాదు); ప్రకటన 2 సరైనది."
  - Option 4: "తప్పు. ప్రకటన 3 తప్పు."
  - Mirror the same in EN.

## Per-question findings

### Q002 GIVEAWAY, WEAK-DISTRACTOR, WEAK-EXPLANATION
- The key is right: 360 divided by 7.2 is 50.
- The number 7.2° from the stem appears only in option 1, so the stem word matches one option.
- Options 2, 3 and 4 are absurd (camel days, eclipse shadow 50 times bigger, 50 minutes' difference).
- Fix the options so every option talks about the angle:
  - A: "7.2° అనేది 360° లో యాభైయో వంతు కాబట్టి"
  - B: "7.2° అనేది 360° లో నూరో వంతు కాబట్టి"
  - C: "Alexandria నీడ 7.2 అడుగులు ఉంది, Syene లో 0 కాబట్టి దూరం 7.2 రెట్లు"
  - D: "7.2° అంటే Syene–Alexandria దూరం కిలోమీటర్లలో 7.2 వేలు కాబట్టి"
  - Better, add a plausible wrong-method distractor: "7.2° ను 90° తో భాగించగా 12.5 రెట్లు వస్తుంది."
- The explanation does not say why each wrong option fails. The option_explanations should state the reason.

### Q007 SYMBOLS, WEAK-EXPLANATION
- The key 2 is correct: Lemaître 1927, Hubble 1929, Gamow and Alpher 1948, Hoyle 1949.
- The explanation and option_explanations use "→" (Lemaître (1927) → Hubble (1929) → ...). Replace with "తరువాత". Example: "Lemaître (1927), తరువాత Hubble (1929), తరువాత Gamow, Alpher (1948), చివరగా Hoyle (1949)."
- The explanation says Hoyle used the name "ఎగతాళి చేసే ఉద్దేశంతో" as fact. The lesson only says "ఎగతాళిగా అన్నాడని చెబుతారు". Hoyle denied this. Fix: "ఎగతాళిగా అన్నాడని చెబుతారు".

### Q008 WEAK-EXPLANATION (as-of)
- Key 2 is correct.
- H₀ ≈ 70 is a contested value (Hubble tension, roughly 67 to 73). Add "(ఇంచుమించు 67 నుంచి 73 మధ్య, ప్రస్తుత అంచనాలు)" in the explanation, or state it as an approximate value as of 2026.

### Q014 WEAK-DISTRACTOR
- Key 2 is correct.
- Options 3 and 4 put Normal matter at 68% or 27%, which is absurd.
- Replace option 4 with a plausible near-miss: "Dark energy 68%, Normal matter 27%, Dark matter 5%".
- Replace option 3 with: "Dark matter 68%, Normal matter 27%, Dark energy 5%".

### Q018 GIVEAWAY (mild)
- Key 3 is correct.
- Statement 2 is false and contains "సులభంగా". It also reads as an overclaim, so it is guessable without knowledge.
- Fix: "Parallax పద్ధతితో కొన్ని కోట్ల Light-years దూరంలో ఉన్న Galaxies దూరాలను కొలుస్తారు."
- Also write the option_explanations with the reason rather than "ప్రకటన 2 తప్పు".

### Q021 AMBIGUOUS, GIVEAWAY, TELUGU, WEAK-EXPLANATION
- The key 4 follows the lesson (Canis Major Dwarf). The lesson itself (line 1190) says its status as a separate galaxy is still debated, and the lesson also mentions Sagittarius Dwarf (about 70,000 ly).
- The stem is a meta-question ("ప్రశ్నలో 'ఏ పరిమాణమైనా సరే...' అని అడిగారు...").
  - That is unnatural Telugu and not a real exam form.
  - "ఏ పరిమాణమైనా" points to the "Dwarf" option.
  - A student can also pick the smallest distance without knowing anything.
- Fix the stem: "NASA ప్రకారం, తెలిసిన వాటిలో Milky Way కు అత్యంత దగ్గరి Galaxy (పరిమాణంతో సంబంధం లేకుండా) ఏది?"
- Add the as-of note: "(2026 నాటికి NASA జాబితా)".
- Add Sagittarius Dwarf (సుమారు 70,000 Light-years) as a distractor in place of option 3 (Triangulum, which gives no distance).
- Give all options a distance so the smallest number is not the only tell.
- State in the explanation that its galaxy status is debated.

### Q022 TELUGU (minor)
- Key 3 is correct for "average distance over time" (Physics Today, 2019).
- Remove the "ప్రశ్న:" prefix.
- Option 4 ("సమానం") is a weak distractor.
- Replace option 4 with "Mars (కుజుడు), ఎందుకంటే ఒకసారి మాత్రమే దగ్గరకు వస్తుంది" or similar. Optional.

### Q023 WEAK-DISTRACTOR
- Key 2 is correct.
- Only option 2 contains the technical word "Refraction". Options 1, 3 and 4 are obviously false.
- Replace option 3 with the real common confusion: "నక్షత్రాలకు సొంత వెలుగు ఉండి, గ్రహాలు సూర్యకాంతిని Reflect చేయడం".
- Keep it as a wrong cause. Explain in option_explanations that this is the star-versus-planet difference, not the cause of twinkling.

### Q026 GIVEAWAY
- Key 1 is correct (Polaris altitude about equals latitude, so about 16.5°).
- The stem number "16.5°" appears only in option 1.
- Fix: remove the number from the stem. "ఉత్తర అర్ధగోళంలో ఒక ప్రదేశం నుంచి Polaris ఎత్తు దాదాపు దేనికి సమానం?"
- Options:
  - A: "ఆ ప్రదేశం Latitude"
  - B: "ఆ ప్రదేశం Longitude"
  - C: "90° మైనస్ Latitude"
  - D: "భూమి Axis tilt 23.5°"
- Key becomes A. Move it to another slot to balance the key spread.
- Keep a Vijayawada example in the explanation.

### Q028 SYMBOLS
- Key 1 is correct.
- The explanation uses "−1", "+2" and "+6" signs.
- Fix: "మైనస్ ఒకటి", "ప్లస్ రెండు", "ప్లస్ ఆరు".

### Q029 WEAK-DISTRACTOR / repeated key pattern, AS-OF
- Key 3 is correct.
- The key string A–4, B–2, C–1, D–3 is identical to Q025's. Re-shuffle List II here.
- Also repeated in Q043 and Q081 (A–2, B–4, C–1, D–3).
- "R136a1 అతి బరువైన" is a changing estimate. Add "(2026 నాటికి తెలిసినవాటిలో)".

### Q031 TELUGU, AMBIGUOUS
- Statement 1 says "ఈ రెండు సంఘటనల్లో", but the stem defines no two events. The statement is unanswerable as written.
- Fix: "Opposition అనేది Superior planets కు, Transit అనేది Inferior planets కు మాత్రమే సాధ్యమయ్యే సంఘటనలు."
- Both statements are true, so the key 3 stands.

### Q032 AS-OF
- Key 4 is correct.
- Add "2026 నాటికి" to statement 3 (Ayanamsa about 24°).
- Statements 1, 2 and 3 are all true. See the note on "all-true" questions at the end.

### Q035 WEAK-DISTRACTOR
- Key 2 is correct.
- Options 1, 3 and 4 are absurd (magnetic Iron, Iron lighter than Hydrogen, rotation stops).
- Plausible replacements:
  - "Iron Fusion లో Hydrogen కంటే ఎక్కువ శక్తి ఇవ్వడం వల్ల Core పేలిపోతుంది"
  - "Core లో Hydrogen పూర్తిగా అయిపోవడం వల్ల"
  - "Neutrinos బయటకు పోయి Core చల్లబడటం వల్ల"

### Q036 WEAK-DISTRACTOR, GIVEAWAY (guessable)
- Key 4 is correct.
- Options 1 to 3 are absurd. Option 4 is the only one that explains "looked like a planet", so the stem gives it away.
- Real confusions to use:
  - "గ్రహాలు ఈ మేఘాల నుంచే పుడతాయని Laplace Nebular hypothesis భావించడం వల్ల"
  - "ఇవి ఒక నక్షత్రం చుట్టూ గ్రహంలా తిరుగుతాయి కాబట్టి"

### Q038 WEAK-EXPLANATION (fact)
- Key 1 is correct.
- The explanation says "1999 లో NASA తన X-ray Observatory కి Chandra అని పేరు పెట్టింది". The observatory was launched in 1999 (renamed Chandra in 1998).
- Fix: "1999 లో ప్రయోగించిన NASA X-ray Observatory కి చంద్రశేఖర్ పేరు (Chandra) పెట్టారు."
- Also fix List II item 2: "చంద్రశేఖర్ పేరు పెట్టిన NASA X-ray టెలిస్కోప్, 1999 లో ప్రయోగం".

### Q039 GIVEAWAY, key spread
- Key 1 is correct.
- R restates A (the limit itself), so it is circular and can be guessed from the stem wording.
- Across the three Assertion–Reason questions (Q011 key 4, Q019 key 2, Q039 key 1), no question uses key 3 ("A సరైనది, R తప్పు").
- Fix: keep A, and make R false: "R: White dwarf ను నిలబెట్టేది Fusion శక్తి." Key becomes 3. Update the explanation: "White dwarf లో Fusion ఉండదు, Electron degeneracy pressure నిలబెడుతుంది."

### Q040 WEAK-EXPLANATION (arithmetic)
- Key 3 is correct.
- Option 1 says "13 Jupiter masses, అంటే 0.013 solar masses". 13 divided by 1048 is 0.0124, so the figure is 0.012, not 0.013.
- Fix: "0.012". The wrong option should not carry an arithmetic slip.

### Q041 AS-OF
- Key 4 is correct as of the lesson.
- T CrB is overdue. If it has erupted by the time of use, "చివరిసారి 1946" is wrong.
- Add "2026 నాటికి" to the stem or option 4.

### Q047 WEAK-DISTRACTOR
- Key 2 is correct.
- Options 1 and 4 are absurd (Hubble, Bell, silly expansions).
- Better distractors:
  - "Allan Sandage; Quasi-stellar radio source"
  - "Maarten Schmidt; Quantum stellar radiation source"
- Keep Hong-Yee Chiu as the trap.

### Q048 GIVEAWAY (hedge word)
- Key 4 is correct.
- It is the only option with a hedge ("మొదలుపెట్టి ఉండవచ్చు"), while options 1 to 3 are flat claims. The hedge marks the answer.
- Fix: write option 4 as a flat claim: "మేఘం కుంచింపు వల్ల మధ్యలో సూర్యుడు, చుట్టూ Disk లో గ్రహాలు ఏర్పడ్డాయి".
- Make options 1 to 3 similar flat claims about older theories.

### Q053 GIVEAWAY
- Key 2 is correct.
- "Angular momentum" is in the stem and in option 2 only.
- Fix the stem: "Kant–Laplace Nebular hypothesis కు ప్రధాన అభ్యంతరం ఏమిటి?"
- Let other options also mention Mass or momentum. For example, option 3 could be "సూర్యుడిలో Angular momentum గ్రహాల కంటే ఎక్కువ ఉండటం" as the reversed trap.

### Q054 WEAK-DISTRACTOR
- Key 1 is correct.
- Options 2 to 4 are absurd.
- Option 4 pins a fake observation on a real name ("1932 లో Ross Gunn ... చూసినందువల్ల"). The lesson lists Ross Gunn as a real theorist (lines 2992 and 3091), so this is misleading and can confuse a student.
- Real objections for use:
  - "Angular momentum గ్రహాల దగ్గర ఎక్కువ ఉండటాన్ని వివరించలేకపోవడం"
  - "ఇలా దగ్గరగా వెళ్లే నక్షత్రాలు చాలా అరుదు, కాబట్టి గ్రహాలు చాలా అరుదు అవుతాయి"
  - "గ్రహాల Orbits సూర్యుడి Equator తలంలో లేకపోవడం"

### Q055 GIVEAWAY (list order)
- Key 3 is correct.
- B–1, C–2 and D–3 follow list order, and only A differs. The key is almost A–?, B–1, C–2, D–3.
- Fix: reorder List II so no run of three matches the list order. For example, make Schmidt 2, Safronov 4, Titius–Bode 1, Weizsäcker 3.

### Q056 TELUGU
- Key 1 is correct.
- In the explanation, "గ్రహమూ, Dwarf planet ఊ, Satellite ఊ కాని" has "ఊ" as a stray token.
- Fix: "గ్రహం కూడా కాని, Dwarf planet కూడా కాని, Satellite కూడా కాని".
- Options 2 and 3 carry "ఎందుకంటే" reasons but option 1 does not. Add a short reason to option 1 for uniform form: "Small Solar System Body, ఎందుకంటే అది గ్రహం, Dwarf planet, Satellite కాదు".

### Q061 TELUGU
- Key 3 is correct.
- The explanation says "శక్తి సమానం Mass గుణించు కాంతి వేగం వర్గం". "వర్గం" is a hard maths word for this reader.
- Fix: "కాంతి వేగాన్ని దానితోనే మళ్లీ గుణించగా వచ్చే సంఖ్య (c square)". "సమానం" and "గుణించు" are fine.

### Q064 GIVEAWAY / not testable (meta-question)
- Key 2 is "రెండూ సరైనవే", the balanced "both fine" answer. The other options are absurd (swap of °C and K, Corona versus Sunspots).
- It asks how a student should interpret a key. This is not an exam-style fact.
- Replace with a factual question:
  - Stem: "IAU 2015 Resolution B3 ప్రకారం సూర్యుడి Nominal effective temperature ఎంత?"
  - Options: 5772 K, 5778 K, 5500 K, 6000 K.
  - Say in the explanation: "పాత కీ లలో 5778 K ఉంటే అది పాత విలువ."
- Alternatively keep the PYQ form: "(పాత కీ 5778 K)". Per the spec, a PYQ keeps the official key.

### Q065 GIVEAWAY (half-guessable)
- Key 4 is correct (Janssen, Guntur, 18 Aug 1868, Helium).
- The element half is guessable: "solar eclipse and new yellow line" points to Helium without knowing the place. Neon and Argon are absurd.
- Fix: ask only for the place.
  - Stem: "18 ఆగస్టు 1868 సూర్యగ్రహణాన్ని Pierre Janssen ఆంధ్రప్రదేశ్‌లోని ఏ ఊరి నుంచి పరిశీలించాడు?"
  - Options: మచిలీపట్నం, విశాఖపట్నం, గుంటూరు, రాజమండ్రి.
- Put Helium in the explanation.

### Q066 WEAK-DISTRACTOR
- Key 1 is correct.
- Options 3 and 4 (cloud shadows predicting rain, cracks on the Sun) are absurd.
- Replace option 3 with the real confusion of emission and absorption: "అవి సూర్యుడిలోని మూలకాలు స్వయంగా విడుదల చేసే Emission lines".
- Replace option 4 with: "అవి Doppler shift వల్ల వచ్చే గీతలు; వాటి నుంచి సూర్యుడి వేగం తెలుస్తుంది".

### Q067 WEAK-DISTRACTOR (mild)
- Key 2 is correct.
- Options 3 (Moon's shadow for days) and 4 (deep holes) are absurd.
- Replace option 3 with "అక్కడ Convection ఎక్కువగా జరిగి వేడి త్వరగా అంతరిక్షంలోకి పోవడం వల్ల".

### Q068 AMBIGUOUS
- Key 3 (1 and 3) is correct under the lesson's wording.
- Statement 2 says "Magnetic poles సుమారు 22 ఏళ్లకు ఒకసారి తారుమారవుతాయి".
  - The Sun's poles reverse about every 11 years, and the full Hale cycle (back to the same polarity) is 22 years.
  - A reader can legitimately read "తారుమారు" as the full cycle, so the statement is not clearly false.
- Fix, either:
  - make statement 2 unambiguously false: "సూర్యుడి Magnetic poles ఒక్కసారి తారుమారు కావడానికి సుమారు 22 ఏళ్లు పడుతుంది", or
  - ask about the Hale cycle: "సూర్యుడి పూర్తి అయస్కాంత చక్రం (Hale cycle) సుమారు 11 ఏళ్లు".

### Q078 GIVEAWAY (absolute word)
- Key 2 is correct.
- Statement 1 (false) contains "పూర్తిగా", while statements 2 and 3 (true) are hedged or specific.
- Fix: "Mars ధ్రువాల మంచు టోపీలు ఎక్కువగా Dry ice (గడ్డకట్టిన CO₂) తో తయారయ్యాయి." This is still false, since they are mostly water ice, and it has no absolute word.

### Q079 AMBIGUOUS (low)
- Key 2 is correct.
- Statement 3 says Olympus Mons is "దాదాపు మూడు రెట్లు" Everest. The ratio is about 2.5 (21.9 km versus 8.85 km).
- The lesson itself notes "కొన్ని పుస్తకాల్లో 2.5".
- Fix in the statement and the lesson: "Everest కు సుమారు రెండున్నర రెట్లు".

### Q080 WEAK-DISTRACTOR, TELUGU
- Key 4 is correct.
- Options 1 to 3 are absurd. Option 3 puts Titan's methane seas on Jupiter.
- The stem is awkward: "భూమి మీద దిగినట్టు 'దిగలేదు'".
- Fix the stem: "Jupiter మీద భూమి మీద లాగా ఒక Spacecraft ను Land చేయడం ఎందుకు సాధ్యం కాదు?"
- Better distractors:
  - "Jupiter Gravity భూమి కంటే చాలా తక్కువ కాబట్టి"
  - "అక్కడ ఉష్ణోగ్రత చాలా తక్కువ కాబట్టి ఏ నౌకా పనిచేయదు"

## Cross-question patterns

- **Match keys repeated.** Q025 and Q029 both have A–4, B–2, C–1, D–3. Q043 and Q081 both have A–2, B–4, C–1, D–3. Q073 and Q077 both have A–3, B–4, C–1, D–2. Re-shuffle the List II order of at least Q029, Q081 and Q077.
- **"All of 1, 2, 3" as key.** Q003, Q032 and Q060 all have key 4. Combined with the "both correct" forms (Q004, Q031), the all-true answers are easy to guess. Turn one of Q003, Q032 or Q060 into a mixed question, for example by making Q032 statement 3 false.
- **Key 1 ("1, 2 మాత్రమే") is frequent** at Q020, Q028, Q034, Q072, and will be five times after Q042 is fixed. Vary the true statement sets.
- **Single-statement questions** (Q045, Q069, Q076 all key 1). Vary one to key 2.
- **Statement-type option_explanations are weak.** About 25 of them read only "తప్పు. ప్రకటన 2 తప్పు." (Q018, 020, 027, 028, 034, 042, 045, 059, 068, 069, 072, 076, 078, 079, 082). Per the spec each wrong option needs a reason. Repeat the reason inline, for example "తప్పు. ప్రకటన 2 తప్పు: దూర Galaxies కు Parallax కోణం కొలవలేనంత చిన్నది."

## Verified clean (key and content checked, no change needed)

Q001, 003, 004, 005, 006, 009, 010, 011, 012, 013, 015, 016, 017, 019, 020, 024 (symbol only, below), 025, 027, 033 (symbol only, below), 034, 037, 043, 044, 045, 046, 050 (add "2026 నాటికి" if desired), 051, 052, 057, 058, 059, 060, 062, 063, 069, 070, 071, 072, 073, 074, 075, 076, 077, 081, 082.

Additional SYMBOLS items from this group:
- Q024: "→" in the explanation and option_explanations. Replace with "తరువాత" or "ఆ తరువాత".
- Q033: "→" in the option_explanations. Replace likewise.
- Q046: "→" in the explanation and option_explanations. Replace likewise.

Minor, no action required:
- Q057 and Q074: the correct option is multi-clause, but length is within the normal range.
- Q003 and similar: the wrong-option reasons rely only on option_explanations.

## Not in lesson

None found. Every checked fact appears in the lesson (for example, Ross Gunn, Canis Major Dwarf and the T CrB 1946 date at lesson lines 2992, 1190 and 2432).
