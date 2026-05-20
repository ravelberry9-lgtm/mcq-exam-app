#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Extract MCQs 31601-31625 from seed file"""

import ast
import re

# Read the seed file
with open('seed_national_ca_2026_mcq.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Find all MCQ entries using regex
pattern = r'\(\d+,\s*([0-9]+),\s*"([^"]*)"'
matches = re.finditer(pattern, content, re.MULTILINE | re.DOTALL)

print("=== EXTRACTING MCQs 31601-31625 ===\n")

# Parse the file to get MCQs
try:
    # Try to safely extract by looking for the questions list
    exec_globals = {}
    exec(content, exec_globals)

    all_mcqs = exec_globals.get('NATIONAL_CA_MCQS', [])

    # Find MCQs in range
    target_mcqs = [mcq for mcq in all_mcqs if len(mcq) > 5 and mcq[5] >= 31601 and mcq[5] <= 31625]

    print(f"Found {len(target_mcqs)} MCQs in range 31601-31625\n")

    if target_mcqs:
        # Show first, middle, and last MCQ
        for idx in [0, len(target_mcqs)//2, len(target_mcqs)-1]:
            if idx < len(target_mcqs):
                mcq = target_mcqs[idx]
                print(f"MCQ {idx}: ID={mcq[5] if len(mcq) > 5 else '?'}")
                print(f"  Difficulty: {mcq[0]}, Points: {mcq[1]}")
                print(f"  Question: {mcq[2][:150]}...")
                print(f"  Explanation: {mcq[7][:150]}...")
                print()

except Exception as e:
    print(f"Error: {e}")
    print("\nTrying alternative extraction...")

    # Find lines with MCQ IDs in range
    lines = content.split('\n')
    for i, line in enumerate(lines):
        if any(f'31{j:02d}' in line for j in range(1, 26)):
            print(f"Line {i}: {line[:100]}...")
