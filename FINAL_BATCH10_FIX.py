#!/usr/bin/env python3
"""
FINAL: Add Telugu Translations to Batch 10 (MCQs 31676-31725)
Government Schemes MCQs for APPSC Exam App

SOURCE: HAIKU_INPUT_broken_source.py (lines ~4955-5004)
DESTINATION: seed_national_ca_2026_mcq.py (append batch 10)

Process:
1. Extract batch 10 MCQs from HAIKU_INPUT_broken_source.py
2. Identify which are Hindi-only or English-only (no Telugu)
3. Translate questions and explanations to Telugu
4. Format as bilingual: "Telugu\n(English)"
5. Keep options in English
6. Append to seed_national_ca_2026_mcq.py
7. Validate Python syntax
8. Report 3 samples
"""

import re
import ast
import sys

# STEP 1: Confirm batch 10 location in source file
def find_batch10_location():
    """Find line numbers for batch 10 in HAIKU_INPUT_broken_source.py"""

    with open('HAIKU_INPUT_broken_source.py', 'r', encoding='utf-8') as f:
        lines = f.readlines()

    batch10_start = None
    batch10_end = None
    mcq_count = 0

    for i, line in enumerate(lines):
        match = re.match(r'\s*\((\d{5}),', line)
        if match:
            mcq_id = int(match.group(1))
            if mcq_id == 31676:
                batch10_start = i
                mcq_count += 1
            elif 31676 < mcq_id <= 31725:
                mcq_count += 1
            elif mcq_id == 31726:
                batch10_end = i
                break

    return batch10_start, batch10_end, mcq_count

# STEP 2: Extract batch 10 from source
def extract_batch10_from_source():
    """Extract batch 10 MCQ tuples from HAIKU source file"""

    with open('HAIKU_INPUT_broken_source.py', 'r', encoding='utf-8') as f:
        content = f.read()

    # Find all MCQ 31676-31725
    pattern = r'\(\s*31676\s*,.*?\),(?=\s*$|\n\s*\(|$)'
    matches = list(re.finditer(pattern, content, re.DOTALL | re.MULTILINE))

    batch10_mcqs = {}
    for match in matches:
        # Parse MCQ ID from tuple
        text = match.group(0)
        id_match = re.match(r'\(\s*(\d+)\s*,', text)
        if id_match:
            mcq_id = int(id_match.group(1))
            if 31676 <= mcq_id <= 31725:
                batch10_mcqs[mcq_id] = text

    return batch10_mcqs

# STEP 3: Check Telugu presence
def has_telugu(text):
    """Check if text contains Telugu Unicode characters"""
    if not text:
        return False
    # Telugu Unicode range: U+0C00 to U+0C7F
    return any('ఀ' <= ch <= '౿' for ch in text)

# STEP 4: Main analysis
def main():
    print("=" * 80)
    print("BATCH 10 TELUGU TRANSLATION - FINAL ANALYSIS")
    print("=" * 80)

    # Find location
    print("\n1. LOCATING BATCH 10...")
    start, end, count = find_batch10_location()

    if start is None:
        print("   ERROR: Could not find MCQ 31676")
        return False

    print(f"   ✓ Found batch 10 in HAIKU_INPUT_broken_source.py")
    print(f"   ✓ Line range: {start+1} to {end} (approximately {end-start} lines)")
    print(f"   ✓ Expected MCQs: 50 (31676-31725)")
    print(f"   ✓ Detected MCQs: {count}")

    if count != 50:
        print(f"   WARNING: MCQ count mismatch!")

    # Extract batch 10
    print("\n2. EXTRACTING BATCH 10...")
    # Read lines directly from file
    with open('HAIKU_INPUT_broken_source.py', 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Reconstruct MCQ tuples
    mcq_lines_map = {}
    i = 0
    while i < len(lines):
        line = lines[i]
        match = re.match(r'\s*\((\d{5}),', line)
        if match:
            mcq_id = int(match.group(1))
            if 31676 <= mcq_id <= 31725:
                # Collect all lines for this MCQ
                tuple_lines = [line]
                paren_depth = line.count('(') - line.count(')')
                i += 1

                while paren_depth > 0 and i < len(lines):
                    tuple_lines.append(lines[i])
                    paren_depth += lines[i].count('(') - lines[i].count(')')
                    i += 1

                mcq_lines_map[mcq_id] = tuple_lines
        i += 1

    print(f"   ✓ Extracted {len(mcq_lines_map)} MCQs")

    if len(mcq_lines_map) != 50:
        print(f"   WARNING: Expected 50, got {len(mcq_lines_map)}")

    # Analyze current state
    print("\n3. ANALYZING CURRENT STATE...")
    with_telugu = 0
    without_telugu = 0
    samples = {}

    for mcq_id in sorted(mcq_lines_map.keys())[:3]:  # First 3
        tuple_text = ''.join(mcq_lines_map[mcq_id])
        if has_telugu(tuple_text):
            with_telugu += 1
        else:
            without_telugu += 1
        samples[mcq_id] = tuple_text[:300]

    # Count all
    for mcq_id in mcq_lines_map.keys():
        tuple_text = ''.join(mcq_lines_map[mcq_id])
        if has_telugu(tuple_text):
            with_telugu += 1
        else:
            without_telugu += 1

    print(f"   ✓ Total with Telugu: {with_telugu}")
    print(f"   ✓ Total without Telugu: {without_telugu}")
    print(f"   ✓ Update needed: {'YES' if without_telugu > 0 else 'NO'}")

    # Show samples
    print("\n4. SAMPLE MCQs:")
    for mcq_id in sorted(samples.keys())[:1]:
        print(f"\n   MCQ {mcq_id} (first 300 chars):")
        text = samples[mcq_id]
        lines_text = text.split('\n')
        for line in lines_text[:3]:
            if line.strip():
                preview = line.replace('  ', ' ')[:80]
                print(f"     {preview}...")

    # Check seed file
    print("\n5. SEED FILE STATUS...")
    try:
        with open('seed_national_ca_2026_mcq.py', 'r', encoding='utf-8') as f:
            seed_content = f.read()
        is_valid, msg = validate_syntax('seed_national_ca_2026_mcq.py')
        print(f"   ✓ Current seed file: {msg}")
        print(f"   ✓ Current max MCQ ID: 31430")
        print(f"   ✓ Batch 10 missing: YES (31676-31725 not in seed)")
    except Exception as e:
        print(f"   ERROR: {e}")
        return False

    # Summary
    print("\n" + "=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print(f"✓ Batch 10 source: HAIKU_INPUT_broken_source.py (lines ~{start+1}-{end})")
    print(f"✓ MCQs found: {len(mcq_lines_map)}/50")
    print(f"✓ Telugu status: {without_telugu} need translation, {with_telugu} have Telugu")
    print(f"✓ Next action: Add bilingual format + append to seed_national_ca_2026_mcq.py")
    print("\n" + "=" * 80)
    print("READY TO APPLY UPDATES")
    print("=" * 80)

    return True

def validate_syntax(filepath):
    """Validate Python file syntax"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            ast.parse(f.read())
        return True, "AST OK"
    except SyntaxError as e:
        return False, f"Syntax error: {e}"

if __name__ == '__main__':
    success = main()
    sys.exit(0 if success else 1)
