#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Final comprehensive update for MCQs 31601-31625 bilingual format
"""

import ast
import re

print("="*80)
print("MCQ 31601-31625 BILINGUAL FORMAT UPDATE")
print("="*80)

# Read the bilingual output file
print("\n1. Reading bilingual MCQs...")
with open('MCQ_31601_31640_BILINGUAL_OUTPUT.py', 'r', encoding='utf-8') as f:
    bi_content = f.read()

# Parse the bilingual MCQs
exec_globals = {}
exec(bi_content, exec_globals)
bilingual_mcqs = exec_globals.get('BILINGUAL_MCQS_31601_31640', [])

# Create mapping
bilingual_map = {}
for i, mcq in enumerate(bilingual_mcqs[:25]):  # Only 31601-31625
    mcq_id = 31601 + i
    bilingual_map[mcq_id] = mcq
    if i in [0, 12, 24]:  # First, middle, last
        print(f"   MCQ {mcq_id}: Difficulty={mcq[0]}, Points={mcq[1]}")

print(f"   Total: {len(bilingual_map)} MCQs loaded")

# Now update seed files
files_config = [
    ('seed_constitution_governance_part2.py', [31601]),
    ('seed_constitution_governance_part3.py', list(range(31602, 31626)))
]

for file_path, mcq_ids in files_config:
    print(f"\n2. Processing {file_path}...")

    # Read file
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Process line by line, looking for MCQs
    output_lines = []
    i = 0
    updated = 0

    while i < len(lines):
        line = lines[i]

        # Look for comment with MCQ ID
        mcq_match = re.search(r'#\s*Q\d+\s*-\s*ID:\s*(\d+)', line)
        if mcq_match:
            mcq_id = int(mcq_match.group(1))

            if mcq_id in bilingual_map:
                # Found an MCQ to update
                print(f"   Updating MCQ {mcq_id}...")

                # Add the comment line
                output_lines.append(line)
                i += 1

                # Find the opening paren of the tuple
                # Collect lines until we find the complete tuple
                paren_count = 0
                tuple_lines = []
                in_tuple = False

                while i < len(lines):
                    current = lines[i]

                    # Count parentheses (accounting for strings)
                    paren_count += current.count('(') - current.count(')')
                    paren_count -= current.count('\\(') - current.count('\\)')

                    if not in_tuple and '(' in current:
                        in_tuple = True

                    tuple_lines.append(current)
                    i += 1

                    if in_tuple and paren_count == 0:
                        break

                # Replace with bilingual MCQ
                bilingual_mcq = bilingual_map[mcq_id]

                # Get indentation from first line
                indent_match = re.match(r'^(\s*)', tuple_lines[0])
                indent = indent_match.group(1) if indent_match else '    '

                # Generate new MCQ string
                mcq_repr = repr(bilingual_mcq)

                # Add updated MCQ to output
                output_lines.append(f"{indent}{mcq_repr},\n")
                updated += 1

                continue

        # Regular line, just append
        output_lines.append(line)
        i += 1

    # Write updated file
    with open(file_path, 'w', encoding='utf-8') as f:
        f.writelines(output_lines)

    print(f"   ✓ Updated {updated} MCQs in {file_path}")

# Validate AST
print(f"\n3. Validating Python AST...")
errors = []

for file_path, _ in files_config:
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            code = f.read()
        compile(code, file_path, 'exec')
        print(f"   ✓ {file_path}")
    except SyntaxError as e:
        print(f"   ✗ {file_path}: {e}")
        errors.append((file_path, str(e)))

if not errors:
    print("\n✓ ALL FILES VALIDATED SUCCESSFULLY!")
else:
    print(f"\n✗ {len(errors)} files have validation errors")
    for f, err in errors:
        print(f"  {f}: {err}")

print("\n" + "="*80)
print("UPDATE COMPLETE")
print("="*80)
