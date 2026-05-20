#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Apply bilingual Telugu+English format to MCQs 31601-31625 in seed file
"""

import re
import ast

# Read both files
print("Reading seed file...")
with open('seed_national_ca_2026_mcq.py', 'r', encoding='utf-8') as f:
    seed_content = f.read()

print("Reading bilingual output...")
with open('MCQ_31601_31640_BILINGUAL_OUTPUT.py', 'r', encoding='utf-8') as f:
    bilingual_content = f.read()

# Extract the bilingual MCQs list
print("\nParsing bilingual MCQs...")
exec_globals = {}
exec(bilingual_content, exec_globals)
bilingual_mcqs = exec_globals.get('BILINGUAL_MCQS_31601_31640', [])

print(f"Found {len(bilingual_mcqs)} bilingual MCQs")

if len(bilingual_mcqs) > 0:
    # Create a mapping of ID to bilingual MCQ
    bilingual_map = {}
    for i, mcq in enumerate(bilingual_mcqs):
        # The bilingual MCQs are in order, starting from 31601
        mcq_id = 31601 + i
        bilingual_map[mcq_id] = mcq
        if i < 3 or i >= len(bilingual_mcqs) - 3:
            print(f"  MCQ {mcq_id}: difficulty={mcq[0]}, points={mcq[1]}")

    print(f"\nCreated mapping for {len(bilingual_map)} MCQs")

    # Now parse the seed file to find MCQs 31601-31625
    print("\nParsing seed file MCQs...")
    exec_globals_seed = {}
    exec(seed_content, exec_globals_seed)
    all_mcqs = exec_globals_seed.get('NATIONAL_CA_MCQS', [])

    print(f"Found {len(all_mcqs)} total MCQs in seed file")

    # Find the indices of MCQs 31601-31625
    target_indices = []
    for i, mcq in enumerate(all_mcqs):
        if len(mcq) > 5 and 31601 <= mcq[5] <= 31625:
            target_indices.append((i, mcq[5]))

    print(f"Found {len(target_indices)} MCQs in range 31601-31625")

    for idx, mcq_id in target_indices[:3]:
        print(f"  Index {idx}: MCQ ID {mcq_id}")

    # Replace the MCQs in the list
    updated_mcqs = all_mcqs.copy()
    replaced_count = 0

    for target_idx, mcq_id in target_indices:
        if mcq_id in bilingual_map:
            updated_mcqs[target_idx] = bilingual_map[mcq_id]
            replaced_count += 1
            if replaced_count <= 3:
                print(f"Replaced MCQ {mcq_id} at index {target_idx}")

    print(f"\nSuccessfully replaced {replaced_count} MCQs")

    # Now write back the seed file
    print("\nWriting updated seed file...")

    # Create new content with replaced MCQs
    # We need to carefully reconstruct the file

    # Extract the prefix (everything before the questions list)
    questions_start = seed_content.find('questions = [')
    if questions_start == -1:
        questions_start = seed_content.find('NATIONAL_CA_MCQS = [')

    if questions_start > -1:
        prefix = seed_content[:questions_start]

        # Find where the list ends
        # This is a bit tricky because we need to preserve the structure

        # Generate the new questions list Python code
        new_content = prefix + 'questions = [\n'

        for i, mcq in enumerate(updated_mcqs):
            new_content += '        ' + repr(mcq) + ',\n'

        new_content += '    ]\n'

        # Find the rest of the file (after the questions list closes)
        questions_end = seed_content.rfind('questions = [')
        if questions_end > -1:
            # Find the closing bracket
            bracket_count = 0
            in_string = False
            escape = False
            for j in range(questions_end + len('questions = ['), len(seed_content)):
                char = seed_content[j]
                if escape:
                    escape = False
                    continue
                if char == '\\':
                    escape = True
                    continue
                if char in ('"', "'"):
                    in_string = not in_string
                    continue
                if not in_string:
                    if char == '[':
                        bracket_count += 1
                    elif char == ']':
                        bracket_count -= 1
                        if bracket_count == 0:
                            questions_end = j + 1
                            break

        if questions_end > 0:
            rest_of_file = seed_content[questions_end:]
            new_content += rest_of_file
        else:
            new_content += '\ndef seed():\n'
            new_content += seed_content[seed_content.find('def seed():'):]

        # Write the new content
        with open('seed_national_ca_2026_mcq.py', 'w', encoding='utf-8') as f:
            f.write(new_content)

        print("✓ Updated seed file written")

        # Validate AST
        print("\nValidating Python AST...")
        try:
            ast.parse(new_content)
            print("✓ AST validation passed")
        except SyntaxError as e:
            print(f"✗ AST validation failed: {e}")

    else:
        print("Could not find questions list in seed file")

else:
    print("No bilingual MCQs found in output file")
