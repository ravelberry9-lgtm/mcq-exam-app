#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Replace MCQs 31602-31625 in seed_constitution_governance_part3.py with bilingual versions
This script carefully reconstructs the file with updated MCQs
"""

import re

print("Reading MCQ bilingual output...")
with open('MCQ_31601_31640_BILINGUAL_OUTPUT.py', 'r', encoding='utf-8') as f:
    bi_content = f.read()

# Extract just the list definition
exec_globals = {}
exec(bi_content, exec_globals)
BILINGUAL_MCQS = exec_globals['BILINGUAL_MCQS_31601_31640']

# Create map: MCQ ID -> MCQ tuple
mcq_map = {}
for i, mcq in enumerate(BILINGUAL_MCQS):
    mcq_id = 31601 + i
    mcq_map[mcq_id] = mcq
    if i < 1 or i in [12, 24]:
        print(f"  MCQ {mcq_id} loaded")

print(f"\nTotal bilingual MCQs loaded: {len(mcq_map)}")
print(f"MCQ ID range: 31601-{31601 + len(mcq_map) - 1}")

# Read the seed file part 3
print("\nReading seed_constitution_governance_part3.py...")
with open('seed_constitution_governance_part3.py', 'r', encoding='utf-8') as f:
    part3_content = f.read()

# Split by lines for careful processing
lines = part3_content.split('\n')

# Find all MCQ comment lines
mcq_indices = {}
for i, line in enumerate(lines):
    match = re.search(r'#\s*Q\d+\s*-\s*ID:\s*(\d+)', line)
    if match:
        mcq_id = int(match.group(1))
        mcq_indices[mcq_id] = i
        if 31601 < mcq_id <= 31625:
            print(f"  MCQ {mcq_id} at line {i}")

print(f"Total MCQs found: {len(mcq_indices)}")

# Now reconstruct the file with replacements
output_lines = []
i = 0

while i < len(lines):
    current_line = lines[i]

    # Check if this is an MCQ comment line
    match = re.search(r'#\s*Q\d+\s*-\s*ID:\s*(\d+)', current_line)
    if match:
        mcq_id = int(match.group(1))

        # For MCQs 31602-31625 in this file, we need to replace them
        if 31602 <= mcq_id <= 31625 and mcq_id in mcq_map:
            print(f"\n  Replacing MCQ {mcq_id}...")

            # Keep the comment line
            output_lines.append(current_line)
            i += 1

            # Skip the old tuple and collect its indentation
            # Find opening paren
            while i < len(lines) and '(' not in lines[i]:
                i += 1

            if i < len(lines):
                indent_match = re.match(r'^(\s*)', lines[i])
                indent = indent_match.group(1) if indent_match else '    '

                # Skip old tuple lines until we find the closing paren
                paren_depth = 0
                first = True
                while i < len(lines):
                    old_tuple_line = lines[i]

                    # Adjust paren depth (naive, doesn't handle strings perfectly, but works for this format)
                    paren_depth += old_tuple_line.count('(') - old_tuple_line.count(')')

                    if first:
                        first = False
                    i += 1

                    if paren_depth == 0:
                        break

                # Now add the new MCQ tuple
                bilingual_mcq = mcq_map[mcq_id]
                mcq_repr = repr(bilingual_mcq)

                output_lines.append(f"{indent}{mcq_repr},")

            continue

    output_lines.append(current_line)
    i += 1

# Write back
print("\nWriting updated seed_constitution_governance_part3.py...")
new_content = '\n'.join(output_lines)

with open('seed_constitution_governance_part3.py', 'w', encoding='utf-8') as f:
    f.write(new_content)

# Validate
print("\nValidating AST...")
try:
    with open('seed_constitution_governance_part3.py', 'r', encoding='utf-8') as f:
        code = f.read()
    compile(code, 'seed_constitution_governance_part3.py', 'exec')
    print("✓ AST validation PASSED")
except SyntaxError as e:
    print(f"✗ AST validation FAILED: {e}")

print("\nDone!")
