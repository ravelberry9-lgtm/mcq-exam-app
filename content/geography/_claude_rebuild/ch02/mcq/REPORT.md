# Chapter 2 MCQ check — merge report (2026-11-04)

Bank `chapter02_bilingual.json` (242 questions, read only; SHA-256 81ab2024… unchanged). Lesson: `ch02/FINAL/lesson_02_rebuilt.md`.

## Totals
- Linked 235/242. Unlinked (null): GEO-BOOK-P018-F011 (map projections), GEO-BOOK-P019-F013 (semidiurnal tide), GEO-ORIG-02-053 (lunar day), GEO-ATOM-02-006 (fathoms), GEO-ATOM-02-013 (tide interval), GEO-ATOM-02-018 (Romulus calendar), GEO-ATOM-02-025 (UN M49 Kiribati).
- Fix entries: 238 questions (b1 34, b2 25, b3 36, b4 36, b5 42, merge pass +65); 1,813 leaf field writes (te 1,753, en 60).
- Answer keys changed: 0. WRONG-KEY: 0 (batches recomputed every time/longitude sum and checked every match key).

| Flag | Questions |
|---|---|
| TRANSLATION | 237 |
| EXPLANATION-WEAK | 30 |
| DUPLICATE | 18 |
| AMBIGUOUS | 1 (P016-F003; stem tightened, key kept) |
| EXPLANATION-WRONG | 1 (P016-F020; explanation cited a table the item does not show) |
| OUTDATED-FACT | 1 (ORIG-02-058; 23.4° → 23.44°) |
| WRONG-KEY | 0 |

## Merge-pass work
1. **Key normalisation.** All writes emitted as leaf keys. b5 `te.matching_lists` (056, 057): the bank does have Telugu matching lists under the key `matching_lists`; b5's whole dicts were split into `left[i]`/`right[i]` and the "A." / "1." prefixes removed (bank items carry none). b1 `te.learning_table.rows[i][j]` kept (validator extended).
2. **Bug found in b1:** GEO-ORIG-02-011 and 012 had `te.options` and `te.option_explanations` swapped (options read "సరైనది. …"). Swapped back.
3. **Weak distractors replaced** (key position unchanged; en + te + option explanations):
   - P021-F001 opt 2 → "Full darkness until the Sun's upper edge touches the horizon"; opt 3 → "Direct sunlight from the Sun's disk after it has risen" (lesson #seasons-twilight trap).
   - P021-F010 opt 3 → "angle from the Earth–Sun line"; opt 4 → "angle from the Tropic of Cancer" (avoided "Equator plane": also 23.44°, would make the item ambiguous).
   - VIS-02-016 opt 1 → "The real Date Line runs along the Prime Meridian (0°)"; opt 2 Telugu broken join "Date Lineే భూమధ్యరేఖ" fixed; explanations updated.
4. **Telugu consistency pass** over every final Telugu field (stem, options, explanations, option explanations, List I/II, learning tables): 1,146 fields in 204 questions. Every before/after pair is in `work/pass_diff.txt`; all were read and the engine corrected where it misfired ("ఉత్తర ప్రాంతం" turned into "Northern Territory" outside the Australia table; glosses nested inside brackets; "కర్కట రేఖ (Tropic of Cancer)" duplicated; "Leap calendar"; "అధిక / Low tides").
   - English names/terms in Telugu script → Latin (UTC, Greenwich, Arctic/Antarctic Circle, Gregorian, calendar, Nautical mile, Knot, Fathom, Foucault pendulum, country/state names in the Prime-Meridian and 82°30′E tables, Australian zones…).
   - **Native-term policy (lesson rule):** English term in the sentence, Telugu once in brackets — in the stem and main explanation only ("Latitude (అక్షాంశం)", "Solstice (అయనాంతం)"); options, option explanations, lists and tables carry the English term alone. Terms: Latitude, Longitude, Prime Meridian, Equator, Celestial equator, Tropics, Rotation, Revolution, Equinox, Solstice, Axis, Horizon, Orbit, Orbital plane/normal, Date Line, Time zone, Leap year, Sidereal/Mean solar day, Sidereal year, Solar noon, Lunar day, High/Low tide, twilight stages, Declination. Inflections mapped (అక్షాంశానికి → Latitude కు, అక్షాంశాలు → Latitudes). Natural compounds left in Telugu (అక్షాంశ వృత్తం, కక్ష్యా చలనం; అర్ధగోళం stays Telugu as in the lesson).
   - Suffix spacing follows the lesson's dominant form (411 spaced vs 120 joined): "Equator కు", "90° లో"; digit + suffix left as is ("21న").
   - "Rolas దీవి": the lesson uses this exact form; kept. No Latin + vowel-sign broken joins remain (regex check).
   - Read-through repair: ATOM-02-025 option explanations 3–4 ("Eastern Africa ఆఫ్రికా subregion").

## Verification of batch-added facts (WebSearch)
| Item | Source | Result |
|---|---|---|
| Réunion UTC+04:00, no DST (3 h / 2 h ahead of Paris winter/summer) | timeanddate.com/time/zone/reunion | OK |
| US: 4 contiguous zones; 9 incl. Atlantic, Alaska, Hawaii–Aleutian, Samoa, Chamorro | USNO "U.S. Time Zones"; 15 USC 263 | OK |
| Russia 11 zones from 26 Oct 2014; Moscow UTC+3, no seasonal change | Wikipedia "Moscow Time", "Time in Russia" | OK |
| Satellite longitude zero ≠ historic Greenwich line (P016-F018) | Wikipedia "IERS Reference Meridian" (~102 m east) | OK (bank text gives no number) |
| Lunar day ≈ 24 h 50 min; semidiurnal 12 h 25 min | NOAA Ocean Service tides05_lunarday | OK |
| Foucault: full turn ≈ 1 day at a pole, none at the Equator (P019-F017) | Britannica "Foucault pendulum" (strictly one sidereal day) | OK as "about 24 hours" |
| Indian Ocean ≈ 20°E–147°E (ATOM-02-020) | Britannica / IHO limits (Cape Agulhas 20°E; SE Cape, Tasmania 146°55′E) | OK as "about" |
| USA–Canada border along 49°N (ATOM-02-022) | Wikipedia "49th parallel north" (western section) | OK |
| 0°/0° in the Gulf of Guinea, south of Ghana (ORIG-02-045) | Wikipedia "Null Island" | OK |
| Nadir = straight below the observer, opposite the zenith (P021-F003) | Dictionary.com, Mathwords | OK |

No correction needed; nothing removed.

## Validator (validate_and_patch.py)
PASS — 1,813 writes; 242 ids, all exist; top-level, question and variant keys unchanged; 0 answer changes; 0 held changes; option counts, te/en counts, option_explanations = options, matching-list lengths and learning-table shapes unchanged; no empty strings; original bank hash unchanged. Output: `chapter02_bilingual.patched.json`.

## Retire / hold recommendations (not applied — `held` untouched)
| Id | Recommendation |
|---|---|
| GEO-ATOM-02-025 | **Retire.** UN M49 Kiribati sub-region: not taught, no exam value. |
| GEO-ATOM-02-018 | **Retire** (or hold until the lesson adds it). Romulus 10-month/304-day calendar not taught; lesson starts at the 355-day calendar. |
| GEO-ATOM-02-006 | **Hold.** Fathom (6 ft ≈ 1.83 m) not taught; keep only if a line is added to #latlong-distance. |
| GEO-ORIG-02-053 | **Hold** until Lesson 3 (Tides) is linked; lunar day not taught in Lesson 2. |
| GEO-ATOM-02-013 | **Hold** with 053 (tide arithmetic belongs to Lesson 3). |
| GEO-BOOK-P018-F011 | **Retire from Ch 2** (map projection distortion belongs to the maps chapter) or add a note to #latlong-distance. |
| GEO-BOOK-P019-F013 (also unlinked) | Move to Lesson 3 with 053/013. |

## Duplicate groups (keep one per quiz set, or rotate)
- ORIG-02-001 ~ P016-F001; 002 ~ P016-F002; 003 ~ P016-F011; 004 ~ P016-F018; 005 ~ P016-F013; 006 ~ P016-F014; 007 ~ P016-F015; 008 ~ P016-F016.
- ORIG-02-017 ~ 021 (match vs statements); ORIG-02-031 ~ P016-F006 (1° of longitude at 60°).
- P017-F001 ~ P019-F004 (15° per hour); P019-F002 ~ P019-F003 (23.44° / 66.56°).
- VIS-02-029 ~ P021-F005; VIS-02-023 ~ P021-F006; VIS-02-017 ~ P021-F010; VIS-02-030 ~ P021-F003; VIS-02-021 ~ P021-F007; VIS-02-022 ~ P021-F008.
- Match items (P016-M001…M006, P017-M001…M004, P019-M001…M006, P020-M001…M004, P021-M001/M002) deliberately recombine their page's fact items; not flagged.

## Remaining editor items
1. Lesson gaps (tested, not taught): Nadir (#seasons-overhead-sun defines only Zenith); Réunion offset, US zone names, Moscow UTC+3 (#time-zones); Babylonian 360° (#latlong-why); 1° ≈ 69 statute miles (#latlong-distance).
2. Residual Telugu compounds (కాలమండల పటం, కక్ష్యా స్థానం, జూన్ అయనాంతపు) left on purpose; a read-aloud check of learning tables is still worthwhile.
3. P021-F010 stem quotes the textbook 23.5°/66.5°; the lesson uses 23.44°/66.56° — fine as "about", editor may align.
