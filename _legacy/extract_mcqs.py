#!/usr/bin/env python3
import re

# Read the source file
with open('HAIKU_INPUT_broken_source.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Extract MCQs 31701-31750
# Find starting line
start_line = None
end_line = None

for i, line in enumerate(lines):
    if '(31701,' in line:
        start_line = i
    if '(31751,' in line:
        end_line = i
        break

if start_line is None:
    print("MCQ 31701 not found")
    exit(1)

if end_line is None:
    # Find next opening paren
    for i in range(start_line + 10, len(lines)):
        if lines[i].strip().startswith('(31751,'):
            end_line = i
            break
    if end_line is None:
        end_line = min(start_line + 500, len(lines))

print(f"Extracting lines {start_line+1} to {end_line}")
section = ''.join(lines[start_line:end_line])

# Save to file
with open('/tmp/mcq_section.txt', 'w', encoding='utf-8') as f:
    f.write(section)

print(f"Saved {len(section)} characters")
print("\nFirst 1500 chars:")
print(section[:1500])
