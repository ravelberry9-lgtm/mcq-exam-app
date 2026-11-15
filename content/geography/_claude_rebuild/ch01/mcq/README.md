# Chapter 1 MCQ check — FINAL

## fixes.json field-key format

`fixes.json` = `{question_id: {"flags": [...], "fields": {KEY: VALUE}, "note": "...", "batch": "b1|b2|b3|b4|merge", "status"?: "pending-page15", "evidence"?: "..."}}`

KEY forms (both whole-value and indexed keys are valid, and can be mixed in one entry):

| KEY | VALUE | Meaning |
|---|---|---|
| `answer` | int (1-based) | New key. Allowed only with flag `WRONG-KEY` and a non-empty `evidence`. (None used.) |
| `held` | bool | Hold / unhold the question. |
| `te.question`, `en.question` | string | Replace the stem. |
| `te.explanation`, `en.explanation` | string | Replace the main explanation. |
| `te.options`, `en.options` | list of strings | Replace the whole options array (same length). |
| `te.options[i]`, `en.options[i]` | string | Replace option *i* (0-based). |
| `te.option_explanations` / `en.option_explanations` | list | Replace the whole array. |
| `te.option_explanations[i]` / `en.option_explanations[i]` | string | Replace one option explanation (0-based). |
| `te.matching_lists.left` / `.right` (also `en.`) | list | Replace a whole List I / List II. |
| `te.matching_lists.left[i]` / `.right[i]` | string | Replace one list item (0-based). |

Apply order: whole-value keys first, then indexed keys (an index refines a whole-array write).
Entries with `status` are **not** applied unless `--include-pending` is passed.

## Files

- `links.json` — 198 ids → new lesson section id (`null` = not taught; 6 ids).
- `fixes.json` — 193 entries, 1,631 field writes.
- `validate_and_patch.py` — applies fixes to a copy and checks it (`python3 -I validate_and_patch.py [--include-pending]`).
- `chapter01_bilingual.patched.json` — patched copy (pending items excluded). The original bank is never written.
- `build_final.py` + `manual_b1_21_35.py` — how fixes.json was produced from b1–b4 (re-runnable from `mcq01/`).
- `REPORT.md` — counts, verifications, held/retire advice, editor items.
