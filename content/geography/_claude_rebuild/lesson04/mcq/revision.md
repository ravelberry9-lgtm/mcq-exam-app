# Revision of the 55 new Lesson 4 MCQs (after blind review)

Backup of the pre-revision folder: `mcq04/NEW_backup_prerev/`. Edits were made in q_a.py, q_b.py, q_c.py and build.py, then rebuilt. Question numbers are positions 1–55 (id GEO-NEW-04-0NN).

Final build: 0 errors, 0 warnings, 0 length flags. Answer spread A 12, B 14, C 14, D 15. Every fact F001–F178 now has a question (F034, F035 newly covered; F121 kept by Q32).

## Giveaways (9)
- Q15, Q39, Q42, Q51: removed the "X is not among the options, which should you choose?" stems. They are now plain questions: Q15 "inner-core radius per PREM" (TE వ్యాసార్ధం); Q39 "approximate age of the Earth"; Q42 "Cambrian start according to older textbooks"; Q51 "earliest Homo sapiens evidence according to older textbooks". The rule for the newer value stays in the explanation. Options and keys unchanged.
- Q41: the unit nouns (period/epoch/eon; యుగం/కల్పం/ఈయాన్) are gone from all options. A and B now use other plausible spans (Early Ordovician–Early Carboniferous; Early Oligocene–Late Pleistocene) so that the key is no longer the longest option.
- Q19: all options are two-part, mildly worded wave-behaviour claims (S slows but P unchanged / both slow, S continues / both slow, S stopped / both speed up). Option explanations rewritten.
- Q49: the absolute "single step" statement is replaced by a less obvious false one, the wrong order of separation (Madagascar first). The lesson's order is Africa, then Antarctica–Australia, then Madagascar.
- Q11: the meta stem is gone, and Q11 now tests a different fact (see Duplicates).
- Q50: all four options follow "named after …" / "… పేరు మీద వచ్చింది". The key is short ("the Gond region of India") and the fossil-plant link is in the explanation.
- Q7 (echo): the stem no longer uses సమతుల్యంగా ("…తేలుతూ నిలిచి ఉండే సూత్రం"). Options use the glossary form ఖండచలనం and "భూ డైనమో".

## Ambiguities (2)
- Q11: replaced (see Duplicates), so it no longer reads as having several right answers.
- Q34: the distractor "glacial ice / wind-blown silt" (a real soil parent material) is now "salt and gypsum left by evaporated seawater". "Magma, high pressure" is now "lava and volcanic gases".

## Duplicates
- Q10/Q11: Q10 (top two crustal metals) stays. Q11 now asks what SIAL and SIMA stand for (Suess; F034, F035). Distractors: the two names swapped, SIMA as the outer core, and SIAL as the mantle. Key A.
- Q31/Q32: Q31 (name-origin matching) stays. Q32 now names the rock from its features: orthopyroxene-bearing, granite-like, high grade, first described from St. Thomas Mount (F120, F121). Options: Charnockite / Khondalite / Quartzite / Amphibolite. Key A.

## Weak distractors
- Q1: the "keeps one speed in a straight line" option is now "travel faster in liquid layers than in solid" (a reversed idea). The key moved B→A.
- Q27: the stem no longer gives away "carbonate". Options are Chalk / Limestone / Dolomite / Chert.
- Q35: the key now reads "preserve the raw material the planets formed from, little changed". The absurd B and C are now plausible traps (pieces of Earth's interior blasted off; fragments of Earth's first crust). D (iron meteorite) is kept.
- Q37: D now follows the same "half-life …, so …" pattern as the other options.
- Q40: the "legal ban" and "too little uranium" options are now "too deep for mines/boreholes" and "meteorites hold far more uranium".
- Q54: the obvious "oil in igneous rock" statement is gone (see Key rebalancing).

## Telugu
- Spelling now follows the lesson: కాండ్రైట్ (Q35) and వ్యాసార్ధ (Q15 and others). No ఖాండ్రైట్, ఖాండ్రెట్ or వ్యాసార్థ is left in the JSON.
- Q4: the stem says భూకంప అభికేంద్రం (Epicentre), so కేంద్రం no longer means both epicentre and core.
- Q5: the meta stem is now a plain NCERT question, using అభికేంద్రం.
- Q21: బెల్ట్ is now పట్టీ. The explanation notes that Gudur is now in Tirupati district (since 2022) but books still say "Nellore Mica belt".
- Q23: all options are now natural two-clause Telugu.
- Q36: the key no longer repeats the stem's పేర్చ ("…ఒకే వరుసలో తిప్పి నిలిపింది").
- Q43: the wrong bracket "(యుగాల మధ్య హద్దులు)" is now "భూవైజ్ఞానిక కాల విభాగాల (Geological time units) మధ్య సరిహద్దులను". The wording "ప్రధానంగా" follows the lesson's "చాలా సరిహద్దులు".
- Q50: see Giveaways.

## Weak explanations
- Q6 option C: "It includes the false statement 3 and leaves out the true statement 2" (TE "ఇందులో తప్పు అయిన ప్రకటన 3 ఉంది, సరైన ప్రకటన 2 లేదు"). The same pattern is used for every wrong statement-combination option in Q18 and Q49.
- Q9 option B: the circular reason is replaced with "A is false (crust is thicker under mountains), so 'both true' is wrong".

## Soft doubts
- Q18: statement 1 follows the lesson, "about 100 km, varying from region to region". The explanation adds the lesson's range: thinner under the oceans, up to 200 km under old continents.
- Q43: the stem matches the lesson ("mainly", the fossil-change basis). The fact is unchanged.

## Key rebalancing (all keys rechecked)
- Statement questions: 3-statement keys were A, A, A, C and are now Q6 A ("1 and 2 only"), Q18 C ("1 and 3 only"; statement 2 is the false mesosphere one), Q49 B ("2 and 3 only"; statement 1 is false), Q54 D (all three true; statement 2 now correctly says sedimentary layers since Gondwana times). The 2-statement Q8 stays C.
- Assertion–reason: the keys were A A D C B C A and are now A A D C B C D. Q45's A is now false ("oxygen fell sharply about 2.4 Ga"), R stays true, so the key is D. Counts: A 2, B 1, C 2, D 2.

## build.py
- New check: statement-question keys (2- and 3-statement sets combined) and A–R keys must be varied within the set. No single key may cover more than half of a format, a format with 3 or more questions must use at least 3 different keys, and the 2-statement and 3-statement sets must not each repeat one key. The keys are printed, and the build prints `BUILD CLEAN` or `BUILD FAILED`.
- SIAL, SIMA and NIFE are allowed as acronyms in Telugu options.
- The coverage.md line for the "how to answer" questions is updated (Q11 is no longer one of them; the rule now sits in the explanation, not the stem).

## Not done (outside this folder)
- Glossary additions the review suggested: సమస్థితి (Isostasy) and భూకంప అభికేంద్రం (Epicentre). Also add విచ్ఛిన్నత to the lesson's term line next to అసాతత్య తలం.
