# Revision: Chapter 1 new MCQs (review.md → new_questions.json)

Edits were made in q_part1.py, q_part2.py and q_part3.py and rebuilt with build.py. The patch scripts are in `scratchpad/tools/edits1-4.py`, and each one asserts that every replaced string matches exactly once. The pre-revision copy is in `mcq01/NEW_backup_prerev/`.

All 53 ids, answer keys and section ids are unchanged (checked against the backup). 33 questions changed.

## Validation after rebuild
- `errors []`: every question has 4 options and 4 option explanations in TE and EN. Exactly one explanation is marked correct, and it is the keyed one. Each has 3–8 confusables rows of the right width, a valid section id and an answer in the range 1–4.
- **New length check (build.py):** it flags any question where the correct option is 30% or more longer (in characters) than the average distractor, in TE and in EN separately.
  - Before the revision it flagged 39 TE/EN variants across 21 questions.
  - After the revision it flags **0**.
  - The 5 assertion–reason items are exempt. They use the fixed APPSC A–R option set, so option length tells the student nothing. Before the exemption, Q007 and Q019 were flagged only because of that fixed set.
- I also scanned for these, and none were found:
  - a stem year that appears in exactly one option;
  - absolute words in the stems of false statements (the only hits are the true statements in Q007 and Q019);
  - EN explanations that refer to "the lesson".
- Key spread is unchanged: A/B/C/D = 12/14/15/12.

## Fixed (by review item)

| Area | Items | What changed |
|---|---|---|
| Ambiguity | Q018, Q029, Q047 | Q018 now says "as of 2026 (IMD), officially accepted". Q029 now asks who "is credited with" first proposing the idea. Q047 item A now reads "highest value in the centre" / "లోపలికి వెళ్లే కొద్దీ ఎత్తు పెరిగే". |
| Fact doubt | Q032 | Statement 3 now reads "a baseline is measured carefully… the remaining distances are calculated from measured angles". The explanation adds that the GTS's *first* baseline was at St Thomas Mount. |
| Giveaway: stem/year | Q018 | Removed "(standing since 2016)". 2016 now appears in two options. |
| Giveaway: absolute words | Q001, Q031, Q037, Q042 | Each false statement is now hedged the same way as the true ones: "mainly describes…", "land measurement began with Rennell", "GAGAN is India's second independent system", "declination is small and about the same everywhere". |
| Giveaway: length | Q008, Q009, Q010, Q014, Q015, Q016, Q018, Q021, Q024, Q025, Q028, Q034, Q036, Q038, Q039, Q041, Q049, Q051, Q053 | Covers the 12 the reviewer listed plus 7 more that the new check caught. The correct option was shortened, or each distractor was given a clause of the same shape. For Q034 and Q049 the four options now share one template and differ only in the tested fact. |
| Weak distractors | Q009, Q010, Q018, Q025, Q028, Q036, Q038, Q044, Q049, Q051, Q053 | Each was replaced with a confusion the lesson teaches, as listed below. |
| Telugu | Q005, Q011, Q024, Q028, Q047 | Rewrote these as natural Telugu sentences: "ఎవరు? ఏ గ్రంథంలో చెప్పాడు?", "వెళ్లడం", "కారణం ఏమిటి? … ఏ projection సరిపోతుంది?", "RF లో కింది సంఖ్య చిన్నగా ఉండే", "దూరం దూరంగా ఉన్న గీతలు". Q018 has a new Telugu option explanation for Mungeshpur. |
| Weak explanations | Q001 B, Q003 C, Q015 C, Q018 C, Q031 A, Q035 D, Q046 | Each explanation now states the idea itself. The cryptic Q046 line is replaced with the km→cm conversion. Explanations for new distractors were also rewritten so they teach. |
| Not in lesson | Q040, Q041 | Q040: dropped the monsoon mnemonic, which is not in the lesson. Q041: replaced "12°–19° N" with "about 12.7° N to 19.1° N (Vijayawada about 16.5° N)". |

The new distractors for the weak-distractor items:
- **Q009:** a 1/72 misreading.
- **Q010:** Tropic of Capricorn, an Equator/solstice mix-up, and a height misconception.
- **Q018:** Alwar paired with Phalodi's figure.
- **Q025:** Polyconic → Mercator.
- **Q028:** a large RF number, large scale read as large area, and contours belonging to topo sheets.
- **Q036:** equal red/NIR reflectance, which gives NDVI ≈ 0.
- **Q038:** a spare satellite, and GIS info.
- **Q044:** statement 2 now tests which Tropic has the overhead Sun at each solstice, a swap the lesson flags.
- **Q049:** desert/plains/plateau, plus the SoI convention.
- **Q051:** a three-item mix with Title.
- **Q053:** flattening at the Poles as the cause, a bulge at the Poles, and bending at the Equator.

Total: all 46 review items were fixed (3 ambiguity + 1 fact doubt + 17 giveaway + 11 weak distractor + 5 Telugu + 7 weak explanation + 2 not in lesson). On top of those, 7 more length giveaways found by the new check were fixed.

## Verification (WebSearch)
- **AP latitude:** "between 12°41' and 19.07°N" (Wikipedia, Geography of Andhra Pradesh). Rounded to 12.7°–19.1° N.
- **Churu 2019:** sources disagree. Some report 50.8 °C on 1 June 2019 (DNA, LatestLY). Many others report 50.5 °C for a later season. The figure is not in the lesson and IMD's own figure was not confirmed, so **Churu was dropped**. Its slot is now "Alwar — 51.0 °C (2016)", which uses lesson values only.

## Declined or partly declined (with reason)
- **Q044, "make statement 2 false":** declined as specified, because it would change the answer key, and the brief says to keep keys unless one is wrong. The set is still made non-trivial: statement 2 now carries a real Tropic/solstice swap trap, but it is true, so the key stays D.
- **Q032, Q040: edits to the lesson file** ("ఒక Baseline చాలు; ఖచ్చితత్వం కోసం ఇంకొన్ని…", and a monsoon line): not made. The brief scoped this work to the MCQs. Both questions now match the lesson as it stands. If the lesson owner wants it, they can add one lesson line about the extra GTS check baselines.
- **Q038, reviewer's suggested "two for position, one for time, one for altitude":** not used. Lat/long/alt/time really are the four unknowns, so that option would be close to correct. Backup and GIS distractors are used instead.
- **Q051, reviewer's "Scale, Direction, Symbol":** not used. NCERT's "distance" component is shown by scale, so that option would be ambiguous. "Title, Direction, Symbol" is used instead.

Count: 4 declined or partly declined. Each of the four underlying problems was still addressed another way.
