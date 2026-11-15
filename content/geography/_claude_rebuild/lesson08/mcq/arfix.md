# Lesson 08 — A–R / option-explanation fix

Port from pipe/L12/mcq/NEW (see its revision.md). Backup of the pre-fix folder: `NEW_bak_arfix/`.

- qlib.py: `STX` replaced with the L12 version (each wrong option gets a different mismatching statement where possible, so no two options repeat the same line); "Correct:" sentence capitalisation in `M` ported.
- build.py: ported the L12 checks: A–R option explanations (empty/short, ends in colon, "not false" stub, lowercase r, option B saying R explains A, option A not denying explanation when key is B, A/R called false/true against the key) and, for all kinds, identical option explanations repeated across options. "Negative TE not bold" replaced by "no `**` in stems" + "EN NOT stem needs a Telugu negative word".
- Verified against the backup build (script compares field by field): same ids in the same order, same answer positions, same key texts EN and TE.
- `ARX` was already the fixed generator in L08 (all 5 calls have notes); not changed.
- L08 STX rule kept: the wrong option's line prefers a false statement the option wrongly includes (ported STX sorts mismatches that way).
- Lesson rules kept: key-spread rule, `te_opt` / TE_TERMS book Telugu terms for options, ST2 option wording.
- 065: new stem check caught `**తప్పు**`; TE stem now "… (Temperate cyclones) సరైనది కాని ప్రకటన ఏది?" (no asterisks, has negative word).

Changed: 13 questions. Statements (option explanations): 002 004 009 013 021 025 033 042 044 050 059 064. 065: TE stem only.

Result: BUILD CLEAN (0 length flags, 0 errors, 7 warnings as before); check_mcq_giveaways.py 0 problems.
