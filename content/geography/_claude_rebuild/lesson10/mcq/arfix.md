# Lesson 10 — A–R / option-explanation fix

Port from pipe/L12/mcq/NEW (see its revision.md). Backup of the pre-fix folder: `NEW_bak_arfix/`.

- qlib.py: `STX` replaced with the L12 version (each wrong option gets a different mismatching statement where possible, so no two options repeat the same line); "Correct:" sentence capitalisation in `M` ported.
- build.py: ported the L12 checks: A–R option explanations (empty/short, ends in colon, "not false" stub, lowercase r, option B saying R explains A, option A not denying explanation when key is B, A/R called false/true against the key) and, for all kinds, identical option explanations repeated across options. "Negative TE not bold" replaced by "no `**` in stems" + "EN NOT stem needs a Telugu negative word".
- Verified against the backup build (script compares field by field): same ids in the same order, same answer positions, same key texts EN and TE.
- qlib.py: `ARX` replaced with the fixed L06/L12 generator. All 7 ARX calls already had A and R notes; none needed filling.

Changed: 16 questions, option explanations only. A–R: 018 023 029 031 037 048 052. Statements: 005 011 016 019 046 050 059 062 070.

Result: BUILD CLEAN (0 length flags, 0 errors, warnings unchanged); check_mcq_giveaways.py 0 problems.
