#!/usr/bin/env python3
"""
Extract batch 10 MCQs from HAIKU_INPUT_broken_source.py
"""

import re

# Read the source file
with open('HAIKU_INPUT_broken_source.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Find MCQs 31676-31725
print("Extracting batch 10 MCQs (31676-31725)...")

# Find positions
positions = {}
for match in re.finditer(r'\((\d{5}),', content):
    mcq_id = int(match.group(1))
    if 31676 <= mcq_id <= 31725:
        positions[mcq_id] = match.start()

print(f"Found {len(positions)} MCQs in range")

if positions:
    sorted_ids = sorted(positions.keys())
    print(f"ID range: {sorted_ids[0]} to {sorted_ids[-1]}")

    # Extract and show first 3 MCQs
    print("\n=== SAMPLE MCQs ===")

    for sample_id in [sorted_ids[0], sorted_ids[len(sorted_ids)//2], sorted_ids[-1]]:
        start_pos = positions[sample_id]
        # Find the end of this MCQ (closing paren)
        paren_depth = 0
        end_pos = start_pos
        in_string = False
        escape_next = False

        for i in range(start_pos, min(start_pos + 10000, len(content))):
            ch = content[i]

            if escape_next:
                escape_next = False
                continue

            if ch == '\\':
                escape_next = True
                continue

            if ch == '"':
                in_string = not in_string
            elif not in_string:
                if ch == '(':
                    paren_depth += 1
                elif ch == ')':
                    paren_depth -= 1
                    if paren_depth == 0:
                        end_pos = i + 1
                        break

        mcq_text = content[start_pos:end_pos]

        # Show first 500 chars
        print(f"\nMCQ {sample_id} (excerpt):")
        preview = mcq_text[:500]
        # Show readable version
        lines = preview.split('\n')
        for line in lines[:5]:
            if line.strip():
                print(f"  {line[:100]}")
        if len(mcq_text) > 500:
            print(f"  ... [{len(mcq_text)} chars total]")

    # Write MCQs to separate file for processing
    print("\n\nExtracting full batch 10 to file...")

    # Create a new questions list with just batch 10
    batch10_mcqs = []

    for mcq_id in sorted(positions.keys()):
        start_pos = positions[mcq_id]
        # Find end
        paren_depth = 0
        end_pos = start_pos
        in_string = False
        escape_next = False

        for i in range(start_pos, min(start_pos + 10000, len(content))):
            ch = content[i]

            if escape_next:
                escape_next = False
                continue

            if ch == '\\':
                escape_next = True
                continue

            if ch == '"':
                in_string = not in_string
            elif not in_string:
                if ch == '(':
                    paren_depth += 1
                elif ch == ')':
                    paren_depth -= 1
                    if paren_depth == 0:
                        end_pos = i + 1
                        break

        mcq_text = content[start_pos:end_pos].strip()
        if mcq_text.endswith(','):
            mcq_text = mcq_text[:-1].strip()

        batch10_mcqs.append(mcq_text)

    # Write to file
    with open('batch10_extracted.txt', 'w', encoding='utf-8') as f:
        f.write("# BATCH 10 MCQs (31676-31725)\n")
        f.write("# Extracted from HAIKU_INPUT_broken_source.py\n")
        f.write(f"# Total: {len(batch10_mcqs)} MCQs\n\n")

        for mcq_text in batch10_mcqs:
            f.write(mcq_text)
            f.write(",\n\n")

    print(f"Extracted {len(batch10_mcqs)} MCQs to batch10_extracted.txt")

    # Show status
    print("\n=== STATUS ===")
    print(f"✓ Found batch 10 MCQs in HAIKU_INPUT_broken_source.py")
    print(f"✓ MCQ IDs: 31676-31725 ({len(batch10_mcqs)} total)")
    print(f"✓ Check if these have Telugu translations...")

    # Analyze Telugu presence
    with_telugu = 0
    for mcq_text in batch10_mcqs[:5]:  # Check first 5
        if any(ch >= 'ఀ' and ch <= '౿' for ch in mcq_text):
            with_telugu += 1

    print(f"✓ First 5 MCQs Telugu analysis: {with_telugu}/5 with Telugu")
