# Lesson 9 — MCQ NEW REVISE

Result: build.py BUILD CLEAN (0 length flags, 0 errors, 20 warnings, same mild key-longest set as before); check_mcq_giveaways.py: 0 problems (checker.txt). 49 questions, ids GEO-NEW-09-001…049 unchanged. **No key changed** (checked field by field against `pipe/L09/mcq/NEW_prerev_bak/`). Spread A5 B15 C16 D13 — L09 rule kept (existing bank skews to A, so A must be the rarest new key); review item 4 (move keys to A) therefore not applied.

## 1. Tooling ported from L12

- qlib.py: `M`, `STX`, `ARX` replaced with the L12 versions. ARX raises on any empty A/R note; wrong options get full sentences ("This option calls R false, but R is true: …", "R is true and it does explain A, so 'R does not explain A' is wrong. …"); no "R is not false:" stubs, no lowercase "r", no "Both true, but R correctly explains A" under B.
- ARX extra (L09): the correct option now names the mechanism too: "Correct. A is true: <A note> R is also true and it is the reason for A / but it is not the reason for A: <R note>" (fixes stubs 15A, 46A, 29B).
- STX extra (L09): correct option labels every statement ("Statement 1 is correct: … Statement 2 is wrong: …"); each wrong option names every statement it gets wrong ("Statement k is wrong, yet this option counts it as correct" / "Statement k is also correct, but this option leaves it out") and always names the false statement ("(Statement 3 is wrong; this option rightly leaves it out.)"). STX records `false_statements` (stripped from the JSON output).
- build.py: L12 checks added (A/R stubs, empty/short, colon-ending, lowercase r, contradictions with the key, option A/B denial checks EN+TE; identical option explanations across options; no `**` in stems; EN "NOT" stem needs a TE negative word). New L09 check: every statement-question option text (EN and TE) must contain "Statement N is wrong" / "ప్రకటన N తప్పు" for each false statement. L09 spread rule (A ≤ every other key) kept.

## 2. A/R notes (15, 16, 29, 46)

All four ARX calls have all four notes (TE+EN). 46 R note rewritten to name the mechanism (summer subsidence under the subtropical high keeps the coast dry; winter Westerlies bring cyclonic rain). 15, 16, 29 notes were already specific and are now used in every option text.

## 3. Statement questions (4, 7, 19, 22, 33, 40)

Subjectless reasons rewritten so they read correctly under a statement label: 4 st1 ("Group A is defined by the coldest month, not the warmest…"), 7 st2 ("The west coast south of Goa is not As but Amw…"), 19 st2 ("The statement is reversed: savanna rain falls in summer…"), 22 st1 ("Temperate grasslands lie not along coasts but inland…"). TE same.

## 4. Q13 (Coringa)

Distractors Pulicat, Kolleru, Nelapattu (Nelapattu is in Tirupati district, not Nellore; none taught in the lesson) replaced by lesson-taught AP places: Papikondalu teak forests, Nallamala hill-edge forests (lesson l.423 teak), Anantapur rain-shadow dry lands (l.196/259). "Near Kakinada" (not in lesson) dropped; explanation adds the Krishna-delta mangroves (l.441). Key C unchanged; TE key no longer strictly longest.

Not done (out of the requested scope / key rule): key rebalance toward A, Q2/Q3 and Q7/Q9 overlap merges, weak-distractor swaps, mild key-longest trims, Telugu-script name alignment (Q2, Q3, Q10).
