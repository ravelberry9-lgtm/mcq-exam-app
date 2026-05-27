#!/usr/bin/env python3
"""
Parse MCQs 31676-31725 from seed_national_ca_2026_mcq.py and show their current state
"""

import sys
import os

# Read the file
with open('seed_national_ca_2026_mcq.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract the questions list portion
import_section_end = content.find('def seed():')
questions_start = content.find('questions = [', import_section_end)
questions_end = content.find(']', questions_start)

questions_section = content[questions_start:questions_end+1]

# Count how many MCQs start with 316/317
import re
mcq_matches = list(re.finditer(r'\(\s*(\d{5}),', questions_section))

print(f"Total MCQ tuples found in file: {len(mcq_matches)}")

# Check specific range
target_mcqs = []
for match in mcq_matches:
    mcq_id = int(match.group(1))
    if 31676 <= mcq_id <= 31725:
        target_mcqs.append(mcq_id)

target_mcqs.sort()
print(f"\nMCQs in range 31676-31725: {len(target_mcqs)}")
if target_mcqs:
    print(f"  IDs: {min(target_mcqs)} to {max(target_mcqs)}")
    print(f"  Sequential check: {target_mcqs[:5]}...")

# Try to actually import and execute the seed function partially
print("\nAttempting to parse MCQ structure...")

# Find one MCQ tuple to analyze
match = re.search(
    r'\(\s*31676,\s*"([^"]*)",\s*"([^"]*)",\s*"([^"]*)",\s*"([^"]*)",\s*"([^"]*)",\s*"([^"]*)",\s*"([^"]*)",\s*"([^"]*)",\s*"([^"]*)"\)',
    questions_section,
    re.DOTALL
)

if match:
    print("\nSuccessfully parsed MCQ 31676 structure!")
    print(f"  Question (first 100 chars): {match.group(1)[:100]}")
    print(f"  Option A (first 50 chars): {match.group(2)[:50]}")
    print(f"  Answer: {match.group(6)}")
    print(f"  Folder: {match.group(8)}")
    print(f"  Topic: {match.group(9)}")
else:
    print("\nCould not parse MCQ 31676 with regex (likely due to escaped characters)")
    # Try a different approach - get raw lines
    lines_in_section = questions_section.split('\n')
    for i, line in enumerate(lines_in_section):
        if '31676,' in line:
            print(f"\nFound line with 31676 at index {i}:")
            print(f"  {line[:150]}...")
            break
