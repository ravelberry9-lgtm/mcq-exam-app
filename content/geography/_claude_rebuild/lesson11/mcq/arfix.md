# Lesson 11 — A–R / option-explanation fix

Port from pipe/L12/mcq/NEW (see its revision.md). Backup of the pre-fix folder: `NEW_bak_arfix/`.

- qlib.py: `STX` replaced with the L12 version (each wrong option gets a different mismatching statement where possible, so no two options repeat the same line); "Correct:" sentence capitalisation in `M` ported.
- build.py: ported the L12 checks: A–R option explanations (empty/short, ends in colon, "not false" stub, lowercase r, option B saying R explains A, option A not denying explanation when key is B, A/R called false/true against the key) and, for all kinds, identical option explanations repeated across options. "Negative TE not bold" replaced by "no `**` in stems" + "EN NOT stem needs a Telugu negative word".
- Verified against the backup build (script compares field by field): same ids in the same order, same answer positions, same key texts EN and TE.
- qlib.py: `ARX` replaced with the fixed L06/L12 generator. Lesson rule kept: brackets stripped from TE options.
- Filled empty A/R notes (TE Tenglish, EN plain; content taken from each question's own explanation, which follows lesson_11_rebuilt.md) in all 9 ARX calls: soil-processes F015 (A), soil-texture F020 (A+R), world-soils F048 (R), soil-water-air F028 (A+R), soil-degradation F063 (A), interactions F095 orchid (R), species-status water hyacinth (A+R), cold-biomes polar bear (A+R), forest-uses Hevea rubber (A+R).

Changed: 16 questions, option explanations only. A–R: 011 016 028 031 037 049 071 072 073. Statements: 005 007 018 036 038 045 048.

Result: BUILD CLEAN (0 length flags, 0 errors, 84 warnings as before); check_mcq_giveaways.py 0 problems.
