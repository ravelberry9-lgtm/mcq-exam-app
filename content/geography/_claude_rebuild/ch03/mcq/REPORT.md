# Chapter 3 MCQ check — REPORT

Validator: **PASS**. 538 questions (531 original + 7 historical), ids/order/keys/option counts unchanged, no empty strings,
0 answer changes. Original bank SHA-256 `3ed337ecafd9d0886f8b861923347bacaf913799f1b6deb5622f99b33607c9b7` unchanged.

## Totals
- links: 538 (537 linked, 1 null: GEO-BOOK-P009-F008 ATLAS). Every link target exists in the lesson.
- fix entries: 521 questions, 6,056 leaf field writes. 17 questions untouched.
- Fix ids: all 521 exist in the bank (the earlier 4-digit-id mistake is no longer present in any batch file).

| Flag | Questions |
|---|---|
| TRANSLATION | 504 |
| EXPLANATION-WEAK | 147 |
| GIVEAWAY | 56 |
| DUPLICATE | 31 |
| EXPLANATION-WRONG | 4 (SOLAR-PRACTICE-046, P006-F012, P010-F009, P022-F004) |
| OUTDATED-FACT | 3 (SOLAR-PRACTICE-050, -054, P004-M018: tilt values aligned to lesson 23.44°/66.56°) |
| AMBIGUOUS | 3 (SOLAR-PRACTICE-096, P003-F002, P003-F022) |
| DISTRACTOR | 2 (P006-F008, P006-F012) |
| WRONG-KEY | 0 |

## Merge fixes
- Key normalisation: whole arrays applied first, indexed keys on top; b3/b8 whole `matching_lists` dicts split into left/right.
- **Bug caught:** b1 wrote whole `en.options` / `en.option_explanations` arrays with `null` for unchanged items (11 questions,
  SOLAR-PRACTICE-013…050). Treated as "keep bank value"; without this the patch would have blanked 41 English strings.
- Leftovers done: P007-F021, P008-F007, P008-F015 option explanations rewritten to match the new options (en+te);
  P005-M001/M002 long generated pair-by-pair explanations trimmed to one line each; P005-M001 English list had "Dwarf planet"
  on both sides (giveaway) -> "Definition of a dwarf planet" / "The category name 'dwarf planet'" (matches Telugu).
- P008-M007 link check: `inner-motion` is correct (Axial tilt section; Mercury 0.03° stated there). No batch touched it: its
  Telugu lists still use Telugu planet names and option explanations are thin ("use the same angular convention") — editor item.

## Historical (PYQ) questions
All 7: stem, options, matching lists and key unchanged (validator-enforced). Only explanations changed.
- APPSC-EXT-0159: option 1 explanation now says "Dr Allen Sundes" may be a misprint of Allan Sandage (American astronomer known
  for Hubble-constant work), who did not propose the steady-state theory. Option text untouched.
- APPSC-G1-122023-P2-GEO-063 (WESAT): key 1 kept. Explanation adds that "first" is how the college and news reports described
  it and the key accepts it; it already notes ISRO treats WESAT as a POEM-3 payload (PSLV-C58, 1 Jan 2024).

## Facts not in the lesson — checked with WebSearch (all kept; none wrong)
STEREO 360° two-sided Sun imaging (2011); main belt ~2.2–3.2 AU; belt total mass < Moon; aphelion ~152 million km;
Pluto inclination ~17°; Hydra > Virgo > Ursa Major (3rd); Charon = Pluto's moon; Ganymede/Titan larger than Mercury;
gravitational contraction (Kelvin–Helmholtz) as 19th-c. Sun-energy idea; light-year 9.461×10¹² km; Earth diameter ≈ 7,900 mi
(12,742/1.609 ≈ 7,918); supermoon up to ~14% bigger / ~30% brighter than a micromoon (NASA); Hartshorne 1939 *The Nature of
Geography* / 1959 *Perspective…*; Lunokhod 2 (1973), Chang'e 5 (2020 sample return), Apollo 15 first LRV (1971); totality
longest on the centre line; WESAT built by LBS Institute of Technology for Women, flown on PSLV-C58 POEM-3; DART impact
23:14 UTC 26 Sep 2022; Eris images 21 Oct 2003 / found 5 Jan 2005; NEA perihelion < 1.3 AU (CNEOS).

## Telugu consistency pass
Applied only to te fields a batch changed (historical stems/options excluded). 123 fields in 68 questions changed; every one read
in `../work/pass_diff.txt`. Rules: suffix spacing as in the lesson (`Density కు`, `1930 లో`, `5 న`; lesson ~95% spaced);
Telugu-script English -> Latin (మిలియన్/బిలియన్ -> million/billion, ప్లూటో -> Pluto, ఇస్రో/పీఎస్‌ఎల్‌వీ–సీ59 -> ISRO PSLV-C59,
ఎల్2 -> L2); planet canon per lesson: `(బృహస్పతి)` -> `(గురుడు)`, `(అంగారకుడు)` -> `(కుజుడు)`, bare అంగారకుడు/అంగారకుడి -> Mars,
"Mars–గురు గ్రహం" -> "Mars–Jupiter"; "Saturn (శని) కి" -> "Saturn కి" where the gloss already appears in the question.
First-mention double glosses "(కుజుడు, అంగారకుడు)" kept. Post-pass scan of all batch-written te strings: 0 glued
Latin+Telugu joins, 0 Telugu-script English names left (except kept double glosses in PYQ explanations).
Not normalised (lesson also uses both): bare శుక్రుడు/బుధుడు/శని in sentences.

## Duplicate groups — user decision (keep / drop)
| Group | Ids | Suggestion |
|---|---|---|
| Universe/Earth age | SOLAR-PRACTICE-073, P002-F011, P002-F012 | keep F011, F012; retarget 073 to Earth 4.54 billion or drop |
| Mercury–Neptune distances km vs AU | P004-F035–F038 = P004-F027–F030; P004-M007 recap | keep one unit set as main, other as reserve |
| Diameter ranks | P004-F010 vs P004-F015–F022 | drop F010 or keep as reserve |
| Aurora borealis/australis | P007-F005, P007-F006 (+ M002 A/B) | keep one |
| Earth 71% / 29% | P007-F022, P007-F023 (+ M006 B/C) | keep one |
| P003 match recaps | P003-M001…M006 = F001, F005–F008, F009–F012, F013–F016, F017–F020, F021–F024 | keep as review set or drop |
| P008–P010 match recaps | P008-M008, P009-M001…M004, P010-M001…M004 (each = 4 preceding F items) | keep as review set or drop |
| Ceres dwarf planet | P009-F018 vs P009-F004 / P009-M001 | drop F018 or reserve |
| Supermoon/micromoon | P022-F015, P022-F016 (same option set) | keep one |
| Mixed-topic match | P002-M003 (Human geography + ages) | keep; mixed section link |

## Retire suggestions
- **GEO-BOOK-P009-F008** (ATLAS early warning) — not in lesson, link null. Retire, or add the lesson line below. Also used as item D in P009-M002.
- P004-M007 / P004-F035–F038 if the km set is not wanted (pure duplicates).
- P008-M007 if no one will rewrite its thin option explanations.

## Lesson-addition suggestions (one line each)
- #missions-dart: planetary defence = detect (ATLAS surveys) then deflect (DART); DART impact 23:14 UTC 26 Sep 2022.
- #distances-light-year: 1 light-year = 9.461 × 10¹² km (now only in the sources list).
- #moon-phases: supermoon up to ~14% bigger and ~30% brighter than a micromoon.
- #asteroid-belt: main belt ~2.2–3.2 AU; total mass less than the Moon; NEA = perihelion < 1.3 AU.
- #motion-perihelion-aphelion: aphelion ~152 million km (perihelion ~147).
- #kuiper: Pluto orbit tilted ~17°; Charon; Eris imaged 21 Oct 2003, identified 5 Jan 2005.
- #sun-interior or history: 19th-c. gravitational-contraction idea (Kelvin–Helmholtz) before fusion.
- #sky-constellation: Hydra, Virgo, Ursa Major = three largest.
- #missions-sun-international: STEREO (two spacecraft, first full 360° Sun view 2011).
- #eclipse-solar-types: totality longest on the centre line.
- #moon-chandrayaan: Lunokhod 1/2 (1970/1973), Apollo 15 LRV (1971), Chang'e 3 (2013), Chang'e 5 sample return (2020).
- #address-geographers: Humboldt's *Kosmos*; Hartshorne 1939 vs 1959 titles.
- #missions-satellite-payload: plain natural vs artificial satellite definition; WESAT as POEM-3 payload.
- #moon-surface: Oceanus Procellarum; height reference = sphere of mean radius 1,737.4 km.
