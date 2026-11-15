# L28 NEW MCQ revision (Opus), 5 Nov 2026

Result: 49 questions (52 − 6 dropped + 3 new). `build.py` BUILD CLEAN (0 errors, 0 length flags); `check_mcq_giveaways.py` 0 problems. New keys A4 B15 C14 D16 (A rarest; combined with linked set A92 B32 C26 D32). Every question re-solved after the rebuild; all 49 keys agree with the content.
Backups of the pre-revision state: `*.pre_rev.py`, `new_questions.pre_rev.json`.

## 1. WRONG-KEY root cause (Q10, 14, 17, 20, 26, 33, 34, 42, 47, 48, 51)

`qlib.S()` assumed that `opts[0]` is the correct option and moved it to position `pos`. In these 11 calls the author had already put the correct option at position `pos` in the list. S took the distractor in `opts[0]`, inserted it at `pos`, and gave it the "Correct."/"సరైనది." prefix. The true option moved down to `pos − 1`. That is why the shift was always one place. build.py could not catch it because the key and the marker came from the same object, so they always agreed with each other.

Fix at the source:
- `qlib.S()` now needs `ok=<EN text of the correct option>`. It finds that tuple anywhere in `opts` and places it at `pos`, so the list order no longer matters. It raises an error if `ok` is missing or does not match exactly one option. All 29 S calls in `q_new.py` now carry `ok=`. For the 11 defective calls, `ok` is the option the author put at `pos`.
- Every builder records the intended correct text separately from the position, as `_ok = (te, en)`: S uses `ok`, M and SEQ use `key`, STX uses the statement set computed from the truth values, and ARX uses the A-R option computed from at/rt/explains.
- New `build.py` check KEY-TEXT. It FAILS when `options_te/en[answer-1]` is not the declared correct text, when that text is not present exactly once, or when it is missing. Negative test: with the old opts[0] behaviour put back (in a scratch copy), the check fails the build on the defective items.

## 2. Drops and replacements

Dropped as duplicates of linked FINAL items: Q8 (44B-009/010/015/020), Q14 (P489-006), Q26 (P491-001), Q40 (P494-001/002), Q47 (P495-003, P496-003), Q52 (P494-005). `existing_map.py` now maps X19 → P494-001, P494-002 and X21 → P495-003, so no fact is left without a question.
New questions, so that every section still has a why/how item:
- N14 (colour-revolutions, A-R, key A). Colour names other than the four fixed pairs vary by book because no law or official list fixes them (how-to-answer).
- N26 (livestock-basics, reasoning, key C). The state with the most cattle need not lead in milk, because of stock vs flow and yield (how-to-answer).
- N47 (fisheries, reasoning, key D). Why FFDA was set up at the district level in 1973–74 (village ponds were not farmed scientifically).

## 3. Q37

The current fact is kept: Uttar Pradesh is first in milk, with 15.66% (BAHS 2025). The how-to line is now "as of November 2026", plus a note that Gujarat leads in AMUL procurement but not in output. The exam-gossip line about the 2016 paper is removed. The linked item AVS-AH-2016-P493-02 is retired, so the two no longer conflict.

## 4. Giveaways (longest key, stem labels)

The keyed option was shortened or reworded in Q3, 5, 17 (TE), 20, 33, 34, 42, 47 and 51. Labels were removed from stems: Q10 "(Diminishing returns)" became "(Fertiliser use)", and in Q51 "(Aquaculture hub)" and "being first" were removed. Q42 and Q47 keys now follow the "Because…/To…" template of their distractors. Q42 "always" was removed, and so was Q51 "all".
Weak distractors were replaced in Q2 (fish → godown storage), Q3 (tall stems → low-fertiliser yield), Q5 (pests → black soils/rain-fed), Q10 (ban → wheat-to-cotton shift), Q32 (58 → 224), Q36 (116/17 → 230.58 (2022–23) / 221.06 (2021–22)) and Q42 (export/more-milk → fat content / AI ease).

## 5. Leak pairs fixed

- Q1 confusables → Q2: the "Ship to mouth" table row no longer states the answer.
- Q9 st.3 → Q10: statement 3 is now about groundwater over-pumping (F028), not diminishing returns.
- Q13 → Q14, Q21/Q24 → Q26, Q27/28/33 → Q52, Q47 → Q50: the target questions were dropped.
- Q45 explanation (CIFE Mumbai) → Q46 st.3: the CIFE sentence was removed from Q45.
- Q51 stem (AP first) → Q50 st.1: the stem now asks about the growth of pond farming and does not give the rank.

## 6. Telugu and facts

- Kerala: "కేరళ (Keralam)" / "Kerala (Keralam)" in Q16 and Q27 (stem, lists, explanations), plus an exam line in Q16 saying they are the same state, renamed in August 2026.
- Cattle: in count contexts, "ఆవులు" became "ఆవు జాతి పశువులు" (the lesson's ఆవు జాతి term), in Q21–Q24 and in the CEN/TOP tables. Note: the lesson's own 2019 tables (lines 893, 909) still read "ఆవులు (Cattle)".
- Telugu List I items: Q11 (NAIP, BGREI; also Lab-to-Land, HYVP), Q39 (NLM, NADCP, AHIDF) and Q45 (all four institutes) now have Telugu names in the TE stem and in matching_lists_te.
- Q2 and Q51: "AP" in TE options replaced with ఆంధ్ర / ఆంధ్రప్రదేశ్.
- Q49: "seventh in milk" is now tied to 2023–24 (NDDB).

## 7. Other lessons (not edited)

L25, L26, L27 and L29 `qlib.py` have a byte-identical `S()` (the same opts[0] code path), and none of their q_new.py calls declare `ok`. The KEY-TEXT check therefore cannot apply to them as built: their only "declared" text is opts[0], which is the defect itself. Instead, every single-answer question was re-solved (L25 42, L26 39, L27 46, L29 29: keyed option against its "Correct." explanation and the stem). Mismatches: 0 in all four lessons. To guard them for real, port the new S/_ok/KEY-TEXT code and add `ok=` to each S call.
