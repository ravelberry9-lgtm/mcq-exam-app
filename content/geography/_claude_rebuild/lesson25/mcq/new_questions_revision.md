# L25 MCQ NEW: revision (2026-11-05)

Input: review.md (cold review of 76 questions). Output: new_questions.json, now 71 questions. Ids stay fixed through `ID(n)` in q_new.py. Dropped numbers are left as gaps, and one id was added (077). Results: build.py CLEAN (0 errors, 0 length flags), check_mcq_giveaways.py 0 problems.
Backups of the pre-revision files: q_new.pre_rev.py, qlib.pre_rev.py, build.pre_rev.py, new_questions.pre_rev.json, facts.pre_rev.txt, and ../../lesson_25_rebuilt.pre_mcqrev.md.

## Tooling (qlib.py, build.py)
- **Ids:** `ID(n)` sets the id of the next question. build.py fails on a missing id, a duplicate id, or ids out of order. The old positional numbering and the `REORDER` hook are gone.
- **Fragment check (new, it is an error):** `qlib._sent` checks every STX statement reason and every ARX A/R note.
  - English: 5 or more words, a finite verb, no bare pronoun at the start (these/they/it/this), and a full stop at the end.
  - Telugu: 4 or more words, a full stop, the last word is not a number, Latin word or bracket, and no "ఇవి/ఇది…" start or dash list.
  - On the old file it caught 52 fragments, including every fragment the review listed (Q12, 20, 27, 37, 39, 44, 45, 50, 54, 62, 23, plus "they" in Q8).
- **ARX key text now says why.** It has a note for A, a note for R, and the explains / does-not-explain verdict. A key-3 or key-4 item names both sides. build.py fails if an A-R key explanation is under 60 characters.
- **Key-spread checks (new):**
  - 2-statement keys must use both A and B.
  - 3-statement keys must use A, B and C.
  - A-R keys must use all four options.
  - Matching keys must not all sit at one letter.

## Duplicates
- **Dropped** (true duplicates of bank items): 015 (B444-003 option C tests 18/8), 029 (B445-006), 047 (B449-001/B448-003), 050 (O42-012, B453-002), 054 (B454-001), 068 (PMKKKY, now tested inside the new 059), 059 old (B454-002).
- **existing_map.py:** now records these facts as covered by the bank: X09, X17, X29, X32, F106, X33.
- **Replaced:**
  - 059 is a new matching: PMKKKY/NMEDT/KABIL/DGMS with what each does.
  - 012 now tests magnetite resource ranks plus the "hematite 72%" trap. The production statement that overlapped B444-004 is gone.
  - 022 is now an A-R item (tungsten imports, because Degana closed and Balepalyam is unproven). It gives ferro-alloys its why-question.
  - 001: statement 1 now tests cut-off grade, not grade = tonnage (which O42-013/031 already test).
  - 037: Panna removed. It now tests Boula–Nuasahi and the Surat trap only.
  - 039: insulator statement removed. It now tests the muscovite/phlogopite trap.
  - 044: resources statement removed. It now tests anodes and production.
  - 027: the AP statement, a duplicate of 070, is replaced by "Odisha about half" (false, it is 74%).
  - 008: the uranium-fuel statement, a duplicate of 009, is replaced by the precious-metals statement.
  - 009: converted to the trap form ("metal so metallic" is false), key D.
- **Kept after checking the bank item.** In each case the overlap is a different fact:
  - 019: tests 97% share; the bank tests Sukinda centre.
  - 020: tests NMI 2025 and production; the bank tests old textbook shares.
  - 041: tests world's largest deposit.
  - 043: tests "not banned, no new leases since 1986"; B449-003 only says the fibre harms the lungs.
  - 053: OSCOM is not in B453-003.
  - 072: only one of its four pairs is in B456-002.
  - 035 (Kolar): kept so that F067 stays covered.
- Coverage: 0 facts left without a question.

## Review items fixed
- **Ambiguous:**
  - 014 has an as-of date (2024–25).
  - 030 has its sources (NMI 2025; IBM 2021–22).
  - 032 says "IBM 2021–22, tin concentrate".
  - 022 Degana: now "known as the main mine, closed". The lesson fact box F050 is fixed to agree with the body.
  - 061: the stem now gives Section 3(e) as the definition. The village-panchayat option is replaced with "Union Ministry of Mines".
- **036 gold figure:** WebSearch found 400 kg in 2026–27, then about 900 kg (Swarajya) or about 1,000 kg (GKToday), and 2 t after expansion. Commercial production began 24 June 2026. The explanation now says "about a tonne a year (reports vary between 900 and 1,000 kg)". The lesson X36 line says the same. The key is unaffected.
- **Giveaways and weak distractors:**
  - Rewritten: 002, 004 (5 lakh t), 006 ("only" removed), 007 (exports), 010, 021 (zirconium for tungsten), 026, 033, 042 ("sets faster"), 055, 063, 075 (Kadapa/Palnadu/NTR belts), 076.
  - Fixed after build warnings: 002 and 007 key-template breaks, 055 digit only in the key, 018 "Limited".
- **Scripts:**
  - 049: all four options are in Telugu script (ఎల్లో కేక్).
  - 061, 060, 066: all options are in Telugu.
  - 016, 059, 072: జాబితా-I/II.
  - Telugu terms with one English bracket: 001, 004, 005, 006, 023, 039, 044, 048, 052, 058, 062, 065.
  - Brackets that added nothing are removed from 003, 007, 036, 046, 063.
- **066:** the stem no longer defines the answer.
- **Weak explanations:** all statement and A-R reasons are full sentences (enforced by the new check). The single-answer option explanations in every question touched above say why the option is wrong. 003 had a doubled "సరైనది" prefix, now removed.
- **Keys:**
  - All new questions: A 17, B 21, C 17, D 16. Combined with the bank: A 38, B 40, C 39, D 37.
  - A-R: A 3, B 2, C 2, D 3 (was 5/3/1/1).
  - 2-statement: A 4, B 5.
  - 3-statement: A 2, B 2, C 2 (001 and 027 now have key C, 039 key B).
  - Matching keys sit at C, D and A (all were B before).
- **062:** the statement 2 reason and the main explanation now say that four of the 31 minerals went back to major on 20 Feb 2025, and that the 2015 statement is still true as history. The 2023 point is removed.
- **077 (new):** asks which four minerals went back to major in 2025, with gypsum/dolomite and bauxite as traps (fact F118a).

## Lesson (FINAL/lesson_25_rebuilt.md, ids kept; build_html.py 25 OK, lint 101 warnings, the same count as before)
- **Verified:** the gazette notification of 20 Feb 2025 (announced 21 Feb 2025) moved barytes, felspar, mica and quartz from minor to major minerals.
  - Reason: they occur with critical minerals (pegmatite: Li, Be, Nb, Ta, Sn; barytes: Sb, Co, Cu, Pb).
  - Existing leases continue. Mines register with IBM by 30 Jun 2025. Royalty still goes to the states.
  - Sources: Tribune, ThePrint, Millennium Post.
- **Added to #institutions-policy:**
  - a paragraph after the 2015 fact;
  - a new `::: fact` (facts.txt id F118a, so other fact ids do not shift);
  - an exam block covering the as-of year, gypsum and dolomite still being minor, and the reason.
- **Fixed in #industrial-minerals:** the exam bullet said "mica is Minor". It now says "Major now; Minor 2015–2025".
- **Other edits:**
  - Added a source line for the Ministry of Mines notice.
  - Fact F050 (Degana) now says the mine is closed.
  - The Jonnagiri second-year figure now notes that reports vary.
