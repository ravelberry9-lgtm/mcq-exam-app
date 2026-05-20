"""
fix_national_ca.py — Remove 345 broken MCQs (31431-31760) added by a Haiku session.

Why these are broken:
  1. 31431-31450 (Telugu, 20 MCQs): tuples have only 8 elements — missing the
     `folder` and `topic` fields → seeder fails with "tuple index out of range".
  2. 31451-31760 (Hindi, 310 MCQs): wrong language for a Telugu+English APPSC
     app, and folder='National' instead of 'AP_HC' → wouldn't display anyway.

This script:
  - Removes everything between the broken-block header and the closing ]
  - Restores DELETE range from id <= 31775 back to id <= 31430
  - Restores print message back to the correct total

Run: python fix_national_ca.py
Then: git add seed_national_ca_2026_mcq.py
      git commit -m "Remove 345 malformed MCQs from National CA seed file"
      git push
"""
import os

SEED_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                         'seed_national_ca_2026_mcq.py')

with open(SEED_FILE, 'r', encoding='utf-8') as f:
    content = f.read()

original_size = len(content)
original_lines = content.count('\n') + 1

# 1. Find start of the bad-MCQs block (the "NATIONAL CA EXPANSION 2026" header)
start_marker_partial = "NATIONAL CA EXPANSION 2026 (31431-31460)"
start_idx = content.find(start_marker_partial)
if start_idx == -1:
    print("[!] Couldn't find the broken-block header. Was the file already cleaned?")
    raise SystemExit(0)

# Walk backwards to the opening ════ comment line of that block (which precedes the header)
header_block_start = content.rfind('        # ════', 0, start_idx)
if header_block_start == -1:
    header_block_start = start_idx  # fallback

# 2. Find the closing ] of the questions list (it precedes "    if db_type == 'pg':")
end_marker = "    if db_type == 'pg':"
end_idx = content.find(end_marker, start_idx)
if end_idx == -1:
    print("[!] Couldn't find the questions list closing pattern.")
    raise SystemExit(1)

# The closing "    ]" line is just before end_marker. Find it.
closing_bracket = content.rfind('    ]\n', 0, end_idx)
if closing_bracket == -1:
    print("[!] Couldn't find closing ].")
    raise SystemExit(1)

# 3. Excise: keep everything before header_block_start, then "    ]\n", then rest from end_marker
new_content = (
    content[:header_block_start].rstrip() + '\n' +
    '    ]\n' +
    content[end_idx:]
)

# 4. Fix DELETE ranges back to 31430
new_content = new_content.replace(
    "DELETE FROM questions WHERE id >= 31001 AND id <= 31775",
    "DELETE FROM questions WHERE id >= 31001 AND id <= 31430",
)

# 5. Fix print message
new_content = new_content.replace(
    "EXPANSION COMPLETE: Seeded {len(questions)} National CA 2026 MCQs (IDs 31001-31775). 775 MCQs total (103% of 750 target).",
    "Seeded {len(questions)} National CA 2026 MCQs (IDs 31001-31430).",
)

# Write
with open(SEED_FILE, 'w', encoding='utf-8') as f:
    f.write(new_content)

new_size = len(new_content)
new_lines = new_content.count('\n') + 1

print(f"Done.")
print(f"  Before: {original_lines} lines / {original_size} bytes")
print(f"  After:  {new_lines} lines / {new_size} bytes")
print(f"  Removed: {original_lines - new_lines} lines")
print()
print("Verify with:")
print(f"  python -c \"import ast; ast.parse(open('{SEED_FILE}', encoding='utf-8').read()); print('AST OK')\"")
print()
print("Then:")
print("  git add seed_national_ca_2026_mcq.py")
print("  git commit -m \"Remove 345 malformed MCQs from National CA seed file\"")
print("  git push")
