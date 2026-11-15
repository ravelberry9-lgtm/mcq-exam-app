# Lesson 07 — A–R / option-explanation fix

Port from pipe/L12/mcq/NEW (see its revision.md). Backup of the pre-fix folder: `NEW_bak_arfix/`.

- qlib.py: `STX` replaced with the L12 version (each wrong option gets a different mismatching statement where possible, so no two options repeat the same line); "Correct:" sentence capitalisation in `M` ported.
- build.py: ported the L12 checks: A–R option explanations (empty/short, ends in colon, "not false" stub, lowercase r, option B saying R explains A, option A not denying explanation when key is B, A/R called false/true against the key) and, for all kinds, identical option explanations repeated across options. "Negative TE not bold" replaced by "no `**` in stems" + "EN NOT stem needs a Telugu negative word".
- Verified against the backup build (script compares field by field): same ids in the same order, same answer positions, same key texts EN and TE.
- qlib.py: `ARX` replaced with the fixed L06/L12 generator. All 7 ARX calls already had A and R notes; none needed filling.
- Lesson rules kept: L07 `_pick_wrong` (not replaced), all other checks unchanged.

Changed: 14 questions, option explanations only. A–R: 005 011 015 021 024 029 045. Statements: 003 020 032 037 048. Matching (EN "Correct:" capitalisation): 016 027.

Result: BUILD CLEAN (0 length flags, 0 errors, 2 warnings as before); check_mcq_giveaways.py 0 problems.
