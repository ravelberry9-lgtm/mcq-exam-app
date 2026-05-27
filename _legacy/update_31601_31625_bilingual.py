#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Update MCQs 31601-31625 in both seed files with proper bilingual Telugu+English format
"""

import re
import os

# First, read the MCQs from the bilingual output to use as reference
print("Reading bilingual output file...")
with open('MCQ_31601_31640_BILINGUAL_OUTPUT.py', 'r', encoding='utf-8') as f:
    bilingual_content = f.read()

# Extract the MCQs from bilingual output
exec_globals = {}
exec(bilingual_content, exec_globals)
bilingual_mcqs = exec_globals.get('BILINGUAL_MCQS_31601_31640', [])

print(f"Found {len(bilingual_mcqs)} bilingual MCQs")

# Create mapping of MCQ ID to bilingual MCQ
bilingual_map = {}
for i, mcq in enumerate(bilingual_mcqs):
    mcq_id = 31601 + i
    bilingual_map[mcq_id] = mcq

print(f"Created mapping for MCQ IDs 31601-{31601 + len(bilingual_mcqs) - 1}")

# Now update seed files
files_to_update = [
    ('seed_constitution_governance_part2.py', [31601]),
    ('seed_constitution_governance_part3.py', list(range(31602, 31626)))
]

updated_count = 0

for file_path, mcq_ids in files_to_update:
    print(f"\n{'='*70}")
    print(f"Processing {file_path}")
    print(f"MCQ IDs to replace: {mcq_ids}")
    print('='*70)

    # Read the seed file
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # For each MCQ ID, find and replace
    for mcq_id in mcq_ids:
        if mcq_id not in bilingual_map:
            print(f"  ✗ MCQ {mcq_id} not found in bilingual map")
            continue

        bilingual_mcq = bilingual_map[mcq_id]

        # Generate the new MCQ tuple representation
        new_mcq_str = repr(bilingual_mcq)

        # Find the old MCQ pattern in the file
        # Look for pattern like:  (difficulty, points, "question...", "opt1...", "opt2...", "opt3...", "opt4...", "answer", "explanation...", "tags")

        # Try to find the MCQ by ID number
        pattern = rf'\(\s*(\d+),\s*(\d+),\n\s*"([^"]*(?:\\.[^"]*)*)",'

        # More specific: look for the comment before the MCQ
        comment_pattern = rf'#\s*Q\d+\s*-\s*ID:\s*{mcq_id}\s*\n\s*\(\s*\d+,\s*\d+,'

        if re.search(comment_pattern, content):
            print(f"  Found MCQ {mcq_id} by comment")

            # Find the full MCQ tuple (this is complex because of nested strings)
            # Use a different approach: find the comment, then find the next closing paren
            match = re.search(comment_pattern, content)
            if match:
                start_pos = match.start()
                # Find opening paren
                paren_start = content.find('(', match.start() + 1)

                # Find matching closing paren (accounting for strings)
                paren_count = 1
                pos = paren_start + 1
                in_string = False
                escape = False
                quote_char = None

                while pos < len(content) and paren_count > 0:
                    char = content[pos]

                    if escape:
                        escape = False
                        pos += 1
                        continue

                    if char == '\\':
                        escape = True
                        pos += 1
                        continue

                    if char in ('"', "'") and not in_string:
                        in_string = True
                        quote_char = char
                    elif char == quote_char and in_string:
                        in_string = False
                        quote_char = None
                    elif not in_string:
                        if char == '(':
                            paren_count += 1
                        elif char == ')':
                            paren_count -= 1

                    pos += 1

                if paren_count == 0:
                    # Extract the old MCQ
                    old_mcq = content[paren_start:pos]
                    # Replace with new MCQ
                    # Preserve indentation
                    indent_match = re.search(r'\n(\s*)\(', content[start_pos:paren_start + 20])
                    if indent_match:
                        indent = indent_match.group(1)
                        new_mcq_str_indented = '\n' + indent + new_mcq_str
                    else:
                        new_mcq_str_indented = new_mcq_str

                    content = content[:paren_start] + new_mcq_str_indented + content[pos:]
                    print(f"  ✓ Replaced MCQ {mcq_id}")
                    updated_count += 1
                else:
                    print(f"  ! Could not find closing paren for MCQ {mcq_id}")
        else:
            print(f"  ! Could not find MCQ {mcq_id} by comment pattern")

    # Write updated content back
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"  Wrote updated {file_path}")

print(f"\n{'='*70}")
print(f"✓ Successfully updated {updated_count} MCQs")
print('='*70)

# Validate AST
print("\nValidating Python AST...")
errors = []

for file_path, _ in files_to_update:
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            code = f.read()
        compile(code, file_path, 'exec')
        print(f"  ✓ {file_path} - AST valid")
    except SyntaxError as e:
        print(f"  ✗ {file_path} - Syntax error: {e}")
        errors.append((file_path, e))

if errors:
    print(f"\n✗ {len(errors)} files have syntax errors!")
else:
    print(f"\n✓ All files pass AST validation!")

print("\nDone!")
