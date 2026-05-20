#!/usr/bin/env python3
"""
Update MCQs 31676-31725 with Telugu translations.
Government Schemes batch focusing on APPSC exam preparation.
"""

import ast
import re

# Government schemes with Telugu names and descriptions
SCHEME_DATA = {
    # Central Sector Schemes
    'Pradhan Mantri Kaushal Vikas Yojana': ('प्रधान मंत्री कौशल विकास योजना', 'PMKVY'),
    'Swachh Bharat Mission': ('स्वच्छ भारत मिशन', 'SBM'),
    'National Health Mission': ('राष्ट्रीय स्वास्थ्य मिशन', 'NHM'),
    'Pradhan Mantri Ujjwala Yojana': ('प्रधान मंत्री उज्ज्वला योजना', 'PMUY'),
    'National Education Policy 2020': ('राष्ट्रीय शिक्षा नीति 2020', 'NEP'),
}

# Read the current seed file
with open('seed_national_ca_2026_mcq.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Parse the file to find MCQ boundaries
mcq_ranges = []
for i, line in enumerate(lines):
    if re.match(r'^\s*\((3167[6-9]|3168[0-9]|3169[0-9]|317[0-2][0-9]|3172[0-5]),', line):
        mcq_id_match = re.search(r'\((\d+),', line)
        if mcq_id_match:
            mcq_id = int(mcq_id_match.group(1))
            if 31676 <= mcq_id <= 31725:
                mcq_ranges.append((mcq_id, i))

print(f"Found {len(mcq_ranges)} MCQs in range 31676-31725")
if mcq_ranges:
    print(f"Line range: {mcq_ranges[0][1]} to {mcq_ranges[-1][1]}")
    print(f"First MCQ: {mcq_ranges[0][0]} at line {mcq_ranges[0][1]}")
    print(f"Last MCQ: {mcq_ranges[-1][0]} at line {mcq_ranges[-1][1]}")

    # Show sample of first MCQ
    print("\n=== Sample MCQ 31676 (lines around index) ===")
    start_idx = mcq_ranges[0][1]
    # Find the end of this tuple (closing paren not inside strings)
    paren_count = 0
    end_idx = start_idx
    in_string = False
    escape_next = False

    for j in range(start_idx, min(start_idx + 50, len(lines))):
        line = lines[j]
        for ch in line:
            if escape_next:
                escape_next = False
                continue
            if ch == '\\':
                escape_next = True
                continue
            if ch == '"' and not escape_next:
                in_string = not in_string
            if not in_string:
                if ch == '(':
                    paren_count += 1
                elif ch == ')':
                    paren_count -= 1
                    if paren_count == 0:
                        end_idx = j
                        break
        if paren_count == 0 and end_idx > start_idx:
            break

    print(f"MCQ tuple spans lines {start_idx+1} to {end_idx+1}")
    print("First few lines of first MCQ:")
    for i in range(start_idx, min(start_idx + 3, len(lines))):
        print(f"  {i+1}: {lines[i][:150]}")
