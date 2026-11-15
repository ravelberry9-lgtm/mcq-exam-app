# Chapter 1 MCQ check — merge report (2026-11-04)

Bank `chapter01_bilingual.json` (198 questions, read only; SHA-256 98760eba… unchanged). Lesson: `ch01/FINAL/lesson_01_rebuilt.md`.

## Totals
- Linked 192/198. Unlinked (null): GEO-BOOK-P014-F008 (Cartography, not taught); GEO-ORIG-01-047, 068, 072, 076, 094 (held source-study items).
- Fix entries: 193 questions (b1 46, b2 50, b3 35, b4 38, merge pass +24); 1,631 field writes.
- Answer keys changed: 0. WRONG-KEY: 0 (all 20 match keys checked mechanically by batch writers).

| Flag | Questions |
|---|---|
| TRANSLATION | 182 |
| EXPLANATION-WEAK | 128 |
| DUPLICATE | 28 |
| AMBIGUOUS | 5 |
| OUTDATED-FACT | 3 |
| EXPLANATION-WRONG | 3 |
| WRONG-KEY | 0 |

Merge-pass Telugu work:
- Batch-1 positions 21–35 (GEO-ORIG-01-021…035; 5 match + 10 two-statement): hand rewrite in Tenglish of stem, List I/II, explanation and every option explanation (Indian grouping 1:50,00,000 in Telugu).
- Auto pass on every Telugu field no batch had rewritten: 365 fields in 115 questions. English names/terms in Telugu script → Latin (Challenger Deep, Geoid, Mauna Kea, Chimborazo, Legend, Contour line, Scale, Survey, Equator, Dead Sea, Ptolemy, Al-Idrisi, NOAA… 100+ terms); old generator case-suffix errors fixed (పటంకు→పటానికి, వైశాల్యంకు→వైశాల్యానికి, కృషికు→కృషికి, పటాలుకు→పటాలకు; 43 hits).
- "‘X’కు సరైన వివరణ" stems: none left after the batches (b1/b2 had rewritten all).

## Verification of batch-added facts
| Item | Source | Result |
|---|---|---|
| Mauna Kea 4,207 m a.s.l. | USGS HVO (via Wikipedia, 4,207.3 m) | OK; 4,205 m only in the lesson's trap note |
| Mauna Kea base-to-summit >10,210 m | NOAA Ocean Service | OK; CHANGED GEO-VIS-01-023 "more than 10,200 m" → 10,210 m (en+te) |
| Chimborazo ~2 km farther from centre | NOAA "over 2,072 m" | OK (NOAA says ~1° S; actual 1°28′ S, lesson 1.5° S kept) |
| Equatorial−polar radius ≈21 km | WGS-84 6,378.137−6,356.752 = 21.4 km | OK |
| Eratosthenes 7.2° (1/50) | standard sources | OK |
| Lapland/Peru 1730s | lesson: Peru 1735, Lapland 1736–37 | OK |
| Death Valley (Badwater) −86 m | USGS via Wikipedia | OK |
| Danakil ~125 m below MSL | Wikipedia | OK as "about 125 m" |
| Puerto Rico / South Sandwich / Java trenches | Five Deeps (Bongiovanni 2021): 8,378 / 7,432 / 7,182 m | OK, matches lesson table |
| Lut ~70 °C is surface temp | NASA Earth Observatory: 70.7 °C LST, MODIS 2005 | OK |
| Oymyakon −67.8 °C | Guinness −67.7 °C (1933) | CHANGED → −67.7 °C (4 strings, P014-F006) |
| Dras −62 °C | reported −60 °C (1995) | CHANGED → −60 °C (P014-F006, en+te) |
| Isohyet | AMS Glossary: equal precipitation | OK |
| Al Azizia annulled 2012 | CS Monitor 13 Sep 2012 (WMO overturned; observer/instrument/site errors, ~7 °C high) | OK; lesson wording holds |
| Globe wording | lesson #maps-globe-vs-map | OK |
| Dallol mean 34.4 °C | lesson/textbook only | consistent; no independent figure found |

## Validator (validate_and_patch.py)
Default (pending excluded): PASS — 1,614 writes; ids exist; 0 answer changes; option counts unchanged; te/en counts match; option_explanations = options; matching-list lengths unchanged; no empty strings; original bank hash unchanged. Held change: GEO-ORIG-01-070 unheld.
`--include-pending`: PASS (1,631 writes; F019, M005 also unheld).

## Held questions
| Id | Recommendation |
|---|---|
| GEO-ORIG-01-047 | Retire: Eratosthenes-measured-axial-tilt not taught, weakly sourced |
| GEO-ORIG-01-068 | Retire/keep held: Babylonian map villages/rivers/hills not taught |
| GEO-ORIG-01-072 | Retire/keep held: Ptolemy India-smaller not taught; 085 covers Taprobana |
| GEO-ORIG-01-076 | Retire/keep held: Al-Idrisi Arabia-centre not taught; 073/075 cover Al-Idrisi |
| GEO-ORIG-01-094 | Retire: duplicates 070, layout claim not taught |
| GEO-ORIG-01-070 | Unhold (applied): lesson now teaches Greece/Mediterranean centre |
| GEO-BOOK-P015-F019, P015-M005 | Unhold PENDING page-15 check (lesson reads yellow = Plateaus). Marked status pending-page15; excluded from default patched copy; apply with --include-pending after check |

## Duplicates to keep apart in one test
- GEO-ORIG-01-001…020 vs 021–025 (match) vs 026–035 (statements): 001–004~021/026/027; 005–008~022/028/029; 009–012~023/030/031; 013–016~024/032/033; 017–020~025/034/035.
- P013-M004 ~ P013-F013…F016; P013-M005 ~ P013-F017…F020.
- P014-F001~F002; P015-F004~F005; P015-F008~F009.
- GEO-ORIG-01-040 ~ P015-F022 (keep 040, retire F022).
- GEO-ORIG-01-049 ~ 089 (keep 089 as calculation item).
- 085~071/072; 093~061/062/064; 096~065/090; 094~070.

## Remaining editor items
1. P015-M005 List II item 3 — now "An unclear land category in the printed legend". Proposed "Plateaus" / "Plateaus (పీఠభూములు)" is in fixes.json (pending); confirm against page 15.
2. P015-F019 option 2 "Plateaus" — same page-15 check.
3. Lesson gaps: Cartography definition (P014-F008, P014-M002 D); Huygens with Newton (P013-M002); Sumer = southern Mesopotamia (062, 093).
4. Non-lesson distractor facts in fixes (all verified): Danakil −125 m, Lut 70.7 °C, Oymyakon −67.7 °C, Dras −60 °C, Isohyets — editor may swap for lesson confusables.
5. The auto pass only fixed script/suffixes; template sentence shapes remain in some untouched match explanations (e.g. P014-M004 "X కు సరైనది Y; Z కాదు"). Human read-through recommended.
