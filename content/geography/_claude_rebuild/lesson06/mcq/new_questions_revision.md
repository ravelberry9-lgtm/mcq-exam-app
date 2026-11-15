# Lesson 6 NEW MCQ revision (applies NEW/review.md)

Backups: NEW/prerev/ (q_a.py, q_b.py, qlib.py, new_questions.json). Keys: none changed (51 answers identical to prerev; spread A14 B12 C12 D13). build.py: BUILD CLEAN, 0 errors, 0 length flags. check_mcq_giveaways.py: 0 problems.

## Generator fixes (qlib.py)
- ARX: rewritten option explanations. Every wrong option is now a full sentence saying what that option claims and why it fails ("This option calls R false, but R is true: ..."; "R is true and it does explain A, so 'R does not explain A' is wrong"). ARX now requires a note for both A and R (no empty text after a colon). Fixes 009, 027, 046, 050, 051; 046 A/B and 051 A/B now have distinct reasons.
- M (matching): clauses in the "Correct:" line are capitalised and end with a full stop (010, 018, 028, 047, 049).

## Per question
- 003: statement 3 reason now says "Plains are denser than mountains, so statement 3 is wrong".
- 006 B: "Too few; the Convention lists 8 countries."
- 008: Telugu statement 2 drops "ఐరోపాలో"; EN and TE now both say "Mont Blanc is higher than Elbrus".
- 009: explanation rewritten (R gives only location; Urals are the boundary by convention because they run north to south).
- 011 D: Zurich replaced by "It was named after the Jurassic Coast of England" (real misconception; explanation: the coast is named after the period).
- 012: "భారతదేశం" made "భారత్" to match option C.
- 013 C / 017 B: dangling sentences replaced by sentences with a subject about the statement (Scandinavian Mountains; Great Rift Valley; Drakensberg).
- 024: duplicate of 002 rewritten as a different decision: about 800 m tract with a narrow summit and steep slopes, key Mountain (position A kept). Same facts F036/F037/F034.
- 030 D: "Britannica calls the Altiplano the most extensive high plateau outside Tibet; the lesson says the same."
- 032 D: replaced by "Lava from Vindhya volcanoes piled up at their foot" (plausible, wrong: Vindhyas are not volcanoes; Deccan lava flows).
- 043: stem adds "(Geographical Cycle paper)" in EN and TE to tie the key to 1899.
- 051: assertion A changed to "Soil fertility on flood plains is lost because floods wash away the topsoil" (no absolute giveaway); key D unchanged.

## Not changed (review said keep)
007, 015, 029, 030 rank note, 031, 039, 041, 004/005. Bold ** in 012/025/045 TE stems kept: build.py requires ** in the TE stem of NOT-questions; the app must render ** as bold (owner to confirm).
