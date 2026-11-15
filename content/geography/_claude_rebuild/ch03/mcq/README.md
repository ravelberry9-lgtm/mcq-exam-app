# Chapter 3 (Solar System) MCQ check — FINAL

Bank (read only): `/mnt/user-data/uploads/geography/solar_bilingual.json` — `original` 531 + `historical` 7 = 538.

## fixes.json format
`{question_id: {"flags": [...], "fields": {KEY: VALUE}, "note": "...", "batch": "b1…b9|merge"}}`

Keys are normalised to leaf level (one key per changed string; only strings that differ from the bank):
`te|en.question`, `.explanation`, `.options[i]`, `.option_explanations[i]`, `.matching_lists.left[i]` / `.right[i]`.
Batch whole-array writes (`te.options`, `te.matching_lists.left`, whole `matching_lists` dicts) were applied first and indexed keys
refined them; a `null` inside a b1 whole array means "keep the bank value". No `answer` changes. Entries with flags but no field
change (duplicate notes) have `"fields": {}`.

## Files
- `links.json` — 538 ids -> lesson section id (`null` = not taught: GEO-BOOK-P009-F008 only). All targets exist in `lesson_03_rebuilt.md`.
- `fixes.json` — 521 entries, 6,056 field writes.
- `build_final.py` — merge b1–b9 + manual repairs (`../work/manual.json`) + Telugu consistency pass; writes `../work/pass_diff.txt`
  (every script-changed field, before/after) and `../work/merge_stats.json`. Re-run: `python3 -I FINAL/build_final.py`.
  Uses `../work/merge_lib.py`.
- `validate_and_patch.py` — applies fixes to a copy, checks ids/order/counts/keys, option counts, no empties, historical
  stem/options/matching lists unchanged, original SHA-256 unchanged. `python3 -I FINAL/validate_and_patch.py`.
- `solar_bilingual.patched.json` — patched copy (same top-level keys as the bank).
- `REPORT.md` — totals, verifications, duplicates, retire and lesson-addition suggestions.
