# Chapter 2 MCQ check — FINAL

## fixes.json field-key format

`fixes.json` = `{question_id: {"flags": [...], "fields": {KEY: VALUE}, "note": "...", "batch": "b1…b5|merge"}}`

All keys are normalised to the **leaf** level (one key per changed string); whole-array and whole-dict writes from the batches were expanded, and only strings that differ from the bank are listed.

| KEY | VALUE | Meaning |
|---|---|---|
| `answer` / `held` | int / bool | Allowed; none used (0 answer changes, 0 held changes). |
| `te.question`, `en.question`, `te.explanation`, `en.explanation`, `te.visual_caption` | string | Replace the string. |
| `te.options[i]`, `en.options[i]` | string | Replace option *i* (0-based). |
| `te.option_explanations[i]` / `en.…` | string | Replace one option explanation. |
| `te.matching_lists.left[i]` / `.right[i]` | string | Replace one List I / List II item. The bank key is `matching_lists` (b5 wrote a whole dict with "A." / "1." prefixes; split into items, prefixes stripped to match the bank). |
| `te.learning_table.title`, `.headers[i]`, `.rows[i][j]` | string | Replace one learning-table cell. |

The validator also accepts whole-value keys (`te.options` as a list, same length) for future edits.

## Files
- `links.json` — 242 ids → lesson section id (`null` = not taught; 7 ids).
- `fixes.json` — 238 entries, 1,813 field writes.
- `build_final.py` — merge of b1–b5 + distractor replacements + options swap repair + Telugu consistency pass (re-runnable: `python3 -I FINAL/build_final.py`; reads `work/manual_te.json`; writes `work/pass_diff.txt` with every script-modified field, before/after).
- `validate_and_patch.py` — applies fixes to a copy and checks it (`python3 -I validate_and_patch.py`).
- `chapter02_bilingual.patched.json` — patched copy. The original bank is never written (SHA-256 checked before/after).
- `REPORT.md` — counts, verifications, retire/hold advice, duplicates, editor items.
