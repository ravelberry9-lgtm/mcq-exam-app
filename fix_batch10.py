#!/usr/bin/env python3
"""
Fix Batch 10 (31676-31725) - Add Telugu translations to Government Scheme MCQs
"""

import re
import sys

def fix_government_scheme_mcqs():
    """Main function to fix batch 10 MCQs with Telugu translations"""

    # Read the seed file
    with open('seed_national_ca_2026_mcq.py', 'r', encoding='utf-8') as f:
        content = f.read()

    # The task requires:
    # 1. Find MCQs 31676-31725 (50 MCQs)
    # 2. Each MCQ needs:
    #    - Telugu translation of question
    #    - Bilingual format: "Telugu\nEnglish"
    #    - Same for explanation
    #    - Options A-D stay English
    #    - Keep folder='AP_HC', topic='National_Current_Affairs_2026'
    #    - Keep answer unchanged

    # Let's identify the MCQs first by searching patterns
    # Pattern: (31xxx, "question", "optA", "optB", "optC", "optD", "answer", "explanation", "folder", "topic")

    # Find line range containing these MCQs
    lines = content.split('\n')
    start_line_idx = None
    end_line_idx = None
    mcq_counts = {}

    for i, line in enumerate(lines):
        # Look for MCQ ID patterns
        match = re.search(r'\((\d{5}),', line)
        if match:
            mcq_id = int(match.group(1))
            if 31676 <= mcq_id <= 31725:
                if start_line_idx is None:
                    start_line_idx = i
                end_line_idx = i
                mcq_counts[mcq_id] = i

    if start_line_idx is None:
        print("ERROR: Could not find MCQs 31676-31725 in file")
        return False

    print(f"Found {len(mcq_counts)} MCQs in range 31676-31725")
    print(f"Line range: {start_line_idx} to {end_line_idx}")
    print(f"First MCQ ID: {min(mcq_counts.keys())} at line {mcq_counts[min(mcq_counts.keys())]}")
    print(f"Last MCQ ID: {max(mcq_counts.keys())} at line {mcq_counts[max(mcq_counts.keys())]}")

    # Show samples
    print("\nSample MCQ lines:")
    for mcq_id in [31676, 31700, 31725]:
        if mcq_id in mcq_counts:
            idx = mcq_counts[mcq_id]
            print(f"\nMCQ {mcq_id} (line {idx+1}):")
            line = lines[idx]
            # Show first 200 chars
            preview = line[:200].replace('\\n', '\\n\n')
            print(f"  {preview}...")

    return True

if __name__ == '__main__':
    success = fix_government_scheme_mcqs()
    sys.exit(0 if success else 1)
