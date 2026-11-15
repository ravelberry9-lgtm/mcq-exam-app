# Lesson 8 new MCQs: revision after review.md

Sources edited: qlib.py, q_a.py, q_b.py (backup of the old sources: `../NEW_bak_prerevise/`). new_questions.json rebuilt. build.py: CLEAN (0 length flags, 0 errors). check_mcq_giveaways.py: 0 problems (checker.txt). 68 questions, ids GEO-NEW-08-001 to 068. Every id, key position and key text was checked against a rebuild of the old sources: none changed. Answer spread unchanged (A 3, B 22, C 23, D 20). 26 questions differ from the old build.

## TE_TERMS (qlib.py) replaced with book/glossary terms
- Troposphere / Stratosphere / Mesosphere: ట్రోపో ఆవరణం / స్ట్రాటో ఆవరణం / మీసో ఆవరణం (glossary; was ...స్ఫియర్).
- Pressure gradient force: పీడన ప్రవణ బలం (also in the N029 body text).
- ITCZ: అంతర అయనరేఖా అభిసరణ మండలం (book p76/78).
- Calms of Cancer / Capricorn: కర్కట రేఖ కామ్ బెల్ట్ / మకర రేఖ కామ్ బెల్ట్ (book p70 "బెల్ట్ ఆఫ్ కామ్"; the coined ప్రశాంత మండలం clashed with the book's name for the Stratosphere).
- Roaring Forties / Furious Fifties: గర్జించే నలభైలు / సాహసోపేతమైన యాబైలు (book p71).
- Nor'westers: నార్‌వెస్టర్స్ (glossary). D/F region: డి భాగం / ఎఫ్ భాగం (lesson, book p67). Nimbostratus: నింబో స్ట్రాటస్. Sensible heat: సెన్సిబుల్ హీట్ (coined సంవేద్య ఉష్ణం dropped). WMO left in Latin (glossary).

## Body text fixes
- N010: list now ఎఫ్ భాగం / ఇ భాగం / డి భాగం. N023: D is సమభార రేఖ. N024, N034: హాడ్లీ. N034 List I uses హాడ్లీ సెల్ / ఫెరల్ సెల్ / పోలార్ సెల్; coined "ఉష్ణ పరోక్ష" replaced by "Thermally indirect" (lesson form). N038: కాలబైశాఖి. N039: సిరోకో, హర్మటన్. N046: key హేజ్ (was పొగమబ్బు). N047: ఉష్ణప్రవాహ పొగమంచు (same Advection term as N015). N052: నింబో స్ట్రాటస్, స్ట్రాటో ఆవరణం. N054: key అడియాబాటిక్ శీతలీకరణం (lesson keeps Adiabatic cooling); option C ఉష్ణోగ్రత విలోమం.

## Matching distractors (N010, 015, 023, 034, 039, 051)
`_pick_wrong` replaced by L10's version (key's A and D pairs and at least 3 of its 4 pairs appear in some distractor; key not the centroid; seeded per key). The key is no longer the only option with a different first pair in any of the six.

## Fact and explanation fixes
- N005: stem now "latest (2025)"; explanation and option note give WMO GHG Bulletin No. 22 (27 Oct 2026): 426.8 ppm, about 0.043%. COMP table row updated. Key unchanged (About 0.04%).
- N017: "same average lapse rate" now "NCERT's rounded form of the average lapse rate (6.5 °C/km)".
- N021: label now "TGPSC Group 2 (December 2024 exam)"; coverage.md note too.
- N031: option C explanation now "almost the whole width between the tropics (47°)".
- N034: List II item 2 (Polar cell) is now "Cold air sinks over the pole; surface polar easterlies" instead of the unconfirmed "smallest and weakest"; explanation updated.
- STX: a wrong statement-option is now explained by the false statement it includes (fixes N002, N004, N013, N044 "also correct" wording).

## Not done, and why
- N065 `**తప్పు**`: kept. build.py requires bold in the TE stem when the EN stem has NOT, so the app convention is markdown bold; removing it would fail the build.
- Weak distractors (N003, N007, N014, N016, N028, N043, N052, N053, N068), bare Latin glossary terms in stems, partial duplicates N013/N014 and N059/N064, and N008 Geocorona bracket: left for a later pass (lower priority, no wrong facts).
- ధ్రువ / ధృవ spelling: kept ధ్రువ (lesson majority). Dew point kept తుషార స్థానం to match the lesson.
