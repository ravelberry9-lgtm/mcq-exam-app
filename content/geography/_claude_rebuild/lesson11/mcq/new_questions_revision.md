# Lesson 11 new MCQs: revision after review.md

I edited the sources (q_a.py, q_b.py, qlib.py) and rebuilt new_questions.json. build.py: CLEAN (0 length flags, 0 errors). check_mcq_giveaways.py: 0 problems (checker.txt). There are still 74 questions, ids GEO-NEW-11-001 to 074. Every id, key position and key text matches the previous build. Answer spread is unchanged (A 20, B 17, C 20, D 17). 31 questions differ from the old build.

## Matching distractors (Q2, 10, 21, 27, 55, 60, 65)
I replaced `qlib._pick_wrong` with the version revised for L10. The key's A pair and D pair, and at least 3 of its 4 pairs, now also appear in some distractor. The key is still not the centre option, and the choice is seeded per key. Exactly one pair is left unique to the key in each question: Q2 C-3, Q10 B-1, Q21 C-2, Q27 C-3, Q55 C-4, Q60 B-3, Q65 B-4. A cut with no unique pair would make the key the centre option, which build.py rejects. Knowing the first pair no longer solves any of the seven.

## Leaks and duplicates
- Q71: I removed "came from the Amazon" from R (EN and TE) and from the explanation, so Q71 no longer answers Q51. R is now only "spreads fast and harms the water", which matches the invasive definition and keeps key A.
- Q73: R no longer names Wickham, 1876 or Kew ("seeds taken out of the Amazon in the late 19th century"), so it no longer answers Q67. Both questions are kept so that ids do not change.
- Q51 confusables: I dropped "(Amazon నుంచి)".

## Wording and distractors
- Q33: the stem now reads "raised many times above the natural rate" instead of "speeded up" (it echoed the key "Accelerated").
- Q63: I replaced the sea-level, glacier and volcanic-ash distractors with overgrazing, invasive grasses and frequent grass fires.
- Q24: the note on option A now says that red, oxidised iron points to good aeration, not waterlogging.

## Telugu
- Q19: స్థాపించే is now స్థిరీకరించే (the lesson term is నైట్రోజన్ స్థిరీకరణ). The Rhizobium note no longer says సహజీవనం.
- Q66: the stem now reads "ఎంత శాతం కంటే ఎక్కువ Canopy cover ఉండాలి".
- Q25: the key is now స్థానబద్ధం కాని మృత్తిక (the lesson's main term). Two distractors were lengthened to keep the length check clean.
- Q50: the options are now పరస్పర సహకారం and సహభోజిత్వం, as in the lesson.
- Lesson English names replace the coined Telugu terms in these questions:
  - Introduced species (Q52, Q71)
  - Succession, Secondary/Primary succession and Pioneer species (Q54, Q55, Q61)
  - Vivipary (Q60)
  - Accelerated/Geological/Stream-bank/Sheet-wash erosion (Q33)
  - Reforestation, Afforestation and Forest degradation (Q68; Deforestation keeps అడవుల నాశనం)
- Person names are now in English in Q6, Q23, Q46 and Q67, as in Q7, Q45, Q69 and the lesson.
- Q8: అజోనల్ నేల is now అజోనల్ మృత్తిక.

## Not done, and why
- A-R keyed B and a varied run in Q71 to Q73: each changes a key, which this revision forbids. The A-R key pattern stays (A 5, C 2, D 2).
- Q7: left as it is. Both stems keep "In the textbook", and the key follows lesson line 122.
- Q4, Q20, Q61 and Q70 distractors, and the clusters 38/41 and 70/74, are left as they are (the review marks these as acceptable).
