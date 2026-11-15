# Lesson 20 NEW MCQ revision (applies review.md)

Keys and ids unchanged (all 64 verified identical to new_questions.prerev.json). build.py: BUILD CLEAN, errors 0. check_mcq_giveaways.py: 0 problems (checker.txt).
Backups: q_new.prerev.py, new_questions.prerev.json, FINAL/lesson_20_rebuilt.premcqrev.md/.html.

## Verified facts (WebSearch/WebFetch)
- INCOIS ITEWC SOP (tsunami.incois.gov.in/TEWS/dsssop.jsp): advisory levels are Warning, Alert, Watch (three). Separate bulletin types: Earthquake Information (~T+20 min), Tsunami Information, Cancellation (withdraws Watch/Alert/Warning), All Clear. "Threat passed" is not a level. The lesson line was wrong.
- Storm surge: IMD's RSMC New Delhi issues the Storm Surge Warnings for cyclones (rsmcnewdelhi.imd.gov.in storm surge warning bulletins); INCOIS runs surge model forecasts as guidance and issues tsunami, ocean state and high-wave warnings.

## Lesson fixes (FINAL/lesson_20_rebuilt.md; build_html.py 20 rerun, lint 0 tag/href errors)
- #tsunami-warning: heading "నాలుగు" -> "మూడు స్థాయిలు"; Threat passed row removed; fact F026 rewritten (Warning/Alert/Watch + Cancellation bulletin); new paragraph on Earthquake Information / Cancellation / All Clear bulletins.
- #early-warning: agency table, fact F087, trap, "సూక్ష్మ విషయం" line and comparison row now say storm-surge warning = IMD (in cyclone bulletin), INCOIS = tsunami, sea state, high waves, surge model guidance.
- "2026 కంటే ముందు" -> "2026 August కంటే ముందు" (exam block, heat-wave trap).
- facts.txt F026, F087 updated to match.

## Question fixes
- N001, N002 + NOTIF table: "before 2026" -> "before August 2026".
- N009 S1: three levels + cancellation bulletin (still true, key unchanged); TSU table updated.
- N010 R: absurd "salt raises waves" -> plausible false "mangroves reflect the wave like a sea wall".
- N011 S3: Rudraprayag (leaked by N013) -> "147 districts, 17 States, 2 UTs" (true, lesson line 531).
- N012 A: invented 250 mm rule -> IMD's real 204.5 mm/day "extremely heavy" class misapplied to cloudburst.
- N016: invented 1958 histories removed; now agency + ministry (CWC/Jal Shakti key; IMD/MoES, INCOIS/MoES, CWC/MoES as real-but-wrong pairs).
- N020 C: invented surge cause -> Cyclone Michaung (real, Dec 2023, wrong event).
- N027 R: name "Damini" removed from R (leaked N008 D-1).
- N030: two absurd distractors -> "wind strongest at coast so wind kills most", "rain flooding kills most".
- N033: List II descriptors no longer echo N062/N064 stems (drainage congestion, flash floods dropped).
- N037: List I now Heat wave / Avalanche / Tsunami, high waves, sea state / Landslides; List II DGRE/IMD/GSI/INCOIS (removes N016/N038 leaks and the storm-surge conflict). Fact ids now F087.
- N038: options and explanations per verified surge fact; TE Latin tell removed (all TE options carry an English term, no brackets); D is now a real misreading (INCOIS = tsunami only).
- N051: anchors replaced (IDNDR 1990, Yokohama 1994, UNISDR 1999, Hyogo 2005) so N054/N063 no longer fix positions; fact ids F106, F110; GLOBAL table adds IDNDR.
- N054: invented secretariats (Tokyo, New York) removed; distractors use Geneva (real UNDRR HQ) and AMCDRR 2016 (real event).
- N058: absurd/zero distractors -> concept confusions (slow vs rapid onset, risk vs hazard, State declaration).
- N059: reworked to a new angle: why the notified list matters (funds) vs warnings / NDRF force / DM Act scope. No 12/14 or heat-wave leak; howto dropped.
- N061: TE "App"/"Mobile network" Telugu-ised; absurd Himalaya distractor -> "seismic waves faster than phone signals".
- N062: absurd distractors -> black cotton soil, mangroves blocking river mouths.
- N063: years removed from stem (leak to N051); armed-forces / Japan-only -> "voluntary to legally binding treaty", "Asia-Pacific to global".
- N064: two absurd distractors -> "least rain in AP" (that is Rayalaseema), "heat wave peaks in monsoon".

## Not changed (accepted)
- N041 C-2 (SDMA-CM) still hints N056; lesson has no other chair pair to swap without leaking N042 (SEC). Basic DM Act fact; N056 tests the CM vs minister trap.
- N006 options state coast totals also seen in N007/N060 stems; they do not give N007's rank key.
- N047/N049 recall-labelled application; key spread unchanged because keys may not change.
- Working drafts lesson_20.md / part_A.md still carry "Threat passed"; FINAL is fixed.
