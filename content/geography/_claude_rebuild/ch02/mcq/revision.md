# Revision of Chapter 2 new MCQs (GEO-NEW-02-001 to 066)

- The pre-revision copy is in `mcq02/NEW_backup_prerev/`.
- I edited the sources `q_part1.py`, `q_part2.py`, `q_part3.py` and `qlib.py` with the one-off script `mcq02/rev_patch.py`. Every replacement was an exact match, checked for a single occurrence.
- I then rebuilt `new_questions.json` with `build.py`.
- IDs and section links did not change.

## Build result

| Check | Result |
|---|---|
| Length flags | 0 |
| Errors | 0 |
| Arithmetic asserts | all pass. New asserts cover the Q021 slip (3.18 × 15 = 47.7), the Q014 city gaps (19 and 40 min) and the Q023 distractor (5 × 15 = 75) |
| Answer spread | A 16, B 17, C 17, D 16 (was 18/16/16/16) |
| Assertion–Reason keys | 1 ×3 (012, 027, 059), 2 ×2 (037, 050), 3 ×1 (004). Was key 1 in 5 of 6 |
| Meaning-carrying symbols (× ÷ ≈ = + ± −) in TE/EN explanations and option explanations | 0 left (scanned the built JSON) |
| Remaining warnings | 7, all harmless: a stem word that appears in one distractor (011, 023, 031, 033, 041, 052), and "every year" in a true statement (058) |

## Changes by question

**Ambiguities**
- **037:** The tides Reason contradicted the lesson, which says tides are caused by Moon and Sun gravity. It is now "the Earth takes about 365¼ days to go round the Sun". The key stays 2. The explanation now separates rotation (the apparent daily motion) from revolution (the year, and with tilt the seasons). Fact F083 was replaced by F050, and a "year means revolution" row was added to the confusables.
- **043:** Item D is now "Foucault pendulum at the North Pole". Item 3 is now "swing plane turns once in about 24 hours", which is in the lesson. The 67 m wire and 28 kg bob moved into the explanation.
  - Item 4 is now "French engineer who described this deflection in 1835". I did not use the reviewer's wording, "the engineer after whom the Coriolis effect is named", because the name match would give B away.
  - The matching lists, the option-4 explanation and the confusables were updated. The key stays A–2, B–4, C–1, D–3.

**Giveaways**
- **030:** List II was reordered. The key is now A–3, B–1, C–2, D–4, still at position D. This is not Q001's key. The distractors follow the review, and their explanations and matching lists were updated.
- **049:** List II was reordered. The key is now A–3, B–4, C–1, D–2, still at position A. The distractors follow the review.
- **007:** Statement 2 is now "Prime Meridian crosses 8 countries, one of which is Antarctica", a lesson trap. Statement 1 was trimmed to a similar length. Fact F027 was replaced by F019, and the explanation lists the 8 countries.
- **048:** The options are now three parallel "11 minutes shorter / 11 hours longer / 11 minutes longer" items, plus "uneven months". The key stays 3.
- **052:** The stem no longer says "equinox". Option 3 is now "Lent had to be shortened again and again". I softened the review's "every century" because the validator flags absolute words in distractors.
- **023:** The stem is now "ముఖ్య కారణం". All four options end in "కాబట్టి". Option 3 is now the false numeric "exactly 5 times 15°", since 82.5 is 5.5 times 15. Option 4 is "exactly 11 times 7.5°".
- **004:** R is now false: "a great circle does not pass through the centre". The key moved from 1 to 3, and the explanation states why R is false. This also helps the AR balance.
- **011:** This is now a why-question using the reviewer's cos-latitude idea. I replaced the reviewer's distractor "1° latitude distance grows northward" with "parallels spread apart northward". The reviewer's version is slightly true for the oblate Earth, and it would make N–S longer, so it was a risky distractor.
- **032:** Option 4 is now "30 December, 10:00".
- **012:** Kept as the review advised. The AR balance was fixed through 004 and 050 instead.

**Assertion–Reason rebalance**
- **050:** R is now the true but unrelated "July is named after Julius Caesar". The key moved from 1 to 2. The explanation and all option explanations were rewritten.
- **Shared AR option A:** In English it is now "Both A and R are true; R rightly explains A". It has 43 characters, the same as option B, so neither key position is the strictly longest option. This affects every AR item's option A text.

**Weak distractors**
- **021:** Option 4 is now 47°42′W, the "3.18 hours × 15" slip, and its explanation says so.
- **024:** The options are now about 58 min (2 min per degree), 2 h 57 min (carry error), 1 h 57 min (key) and 29 min. All four options start with "about"/"సుమారు", so the English key is not a length tell.
- **031:** The distractors are now the UTC±12 zone edges, avoiding Antarctica, and "Greenwich not opposite 180°", with matching explanations.
- **062:** Option 3 is now "refraction stronger near the poles".
- **064:** Option 3 is now "axis points straight at the Sun". Option 4 is now "refraction holds the Sun above the horizon".
- **066:** Option 1 is now "air too thick for particles". Option 2 is now "no magnetic field above the Equator". Option 3 stays as the review advised.
  - I did not use the reviewer's "Equator farthest from the Sun, gets no solar wind", because it would duplicate option 3.

**Not in lesson**
- **014:** Rebuilt on the lesson figures: Hyderabad 78.5°E, Visakhapatnam 83.3°E, Kolkata 88.4°E, with gaps of 19 and 40 min. The distractors are now coast, time zone and "closer to the Sun". The confusables were rebuilt.

**Telugu**
- **063:** "ఉషస్సు" was removed.
- **065:** The stray "పై" was fixed, using the reviewer's sentence.
- **023** and **043:** Fixed as above.

**Weak explanations**
- **002:** "బయలుదేరిన ఊరి (Greenwich)" became "Greenwich సమయం". Option 3 is now "Date Line corrects the date, not longitude".
- **035:** The working now goes through UTC (UTC+9 gives Sunday 17:00 UTC, then UTC−6 gives Sunday 11:00), and the 225° route is kept as a second method. The option-4 explanation says that going east across the Date Line also subtracts a day. The confusing parenthesis was removed.
- **037:** Fixed as above.

**Read-aloud symbol pass (TE and EN)**
- Rewritten in words: 002, 006, 016, 017, 018, 019, 020, 021, 022, 023, 024, 026, 028, 029, 030, 032, 033, 034, 035, 039, 041, 046, 048, 051, 052, 059, 061.
- 006 and 016 were not on the reviewer's list but carried = − + signs. The scan found them, so they were fixed too.
- Degree and minute marks in options, the "UTC + 14" offsets in stems and options, and symbols inside confusable tables were left as they are. The read-aloud rule covers explanations.

## Declined or deferred, with reasons
- **Q038 (swap Ptolemy/Copernicus for Hipparchus/Eratosthenes):** Not done. This was a lower-priority note about overlap with Q001. Both items are correct and unambiguous.
- **Q036 (CSIR-NPL recallable from 025/026):** Accepted as is, as the reviewer allowed.
- **Q066 (giveaway from Q065's explanation):** Accepted as is, since the two only interact across the set.
- **Q053 ("Orbital normal" option):** Kept. It is a lesson term, and the review rated it mild.
- **Q010/Q012 overlap:** No trim was requested, so both are kept.
