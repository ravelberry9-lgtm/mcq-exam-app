#!/usr/bin/env python3
"""
Batch 10 Telugu Translator for Government Schemes MCQs (31676-31725)
Extracts, translates, and updates MCQs with bilingual format
"""

import re
import sys

def extract_mcqs_from_file():
    """Extract MCQs 31676-31725 from seed file using AST parsing"""
    with open('seed_national_ca_2026_mcq.py', 'r', encoding='utf-8') as f:
        full_content = f.read()

    # Find the questions list
    questions_start = full_content.find('questions = [')
    if questions_start == -1:
        print("ERROR: Could not find 'questions = [' in seed file")
        return None

    # Extract just the question tuples section
    questions_section = full_content[questions_start+12:]

    # Find all MCQ IDs and their content
    mcqs = {}

    # Pattern to match MCQ tuples - looking for (id, "question",...
    # We'll use a simpler approach: split by lines and parse
    lines = full_content.split('\n')

    i = 0
    while i < len(lines):
        line = lines[i]
        # Look for line starting with (31676 through 31725
        match = re.match(r'\s*\((\d+),', line)
        if match:
            mcq_id = int(match.group(1))
            if 31676 <= mcq_id <= 31725:
                # This is one of our MCQs, extract the full tuple
                tuple_lines = [line]
                i += 1

                # Keep collecting lines until we find the closing paren at depth 0
                paren_depth = line.count('(') - line.count(')')
                while paren_depth > 0 and i < len(lines):
                    tuple_lines.append(lines[i])
                    paren_depth += lines[i].count('(') - lines[i].count(')')
                    i += 1

                # Join and parse
                tuple_str = '\n'.join(tuple_lines)
                mcqs[mcq_id] = {
                    'raw': tuple_str,
                    'line_count': len(tuple_lines),
                    'start_line': i - len(tuple_lines) + 1
                }
        i += 1

    return mcqs, full_content, lines

def show_sample_mcq(mcqs_dict, mcq_id):
    """Show a sample MCQ for review"""
    if mcq_id not in mcqs_dict:
        print(f"MCQ {mcq_id} not found")
        return

    mcq = mcqs_dict[mcq_id]
    print(f"\n=== Sample MCQ {mcq_id} ===")
    print(f"Spans {mcq['line_count']} lines")
    # Print first 500 chars
    raw = mcq['raw']
    if len(raw) > 500:
        print(raw[:500] + "...")
    else:
        print(raw)

if __name__ == '__main__':
    print("Extracting Batch 10 MCQs (31676-31725)...")
    result = extract_mcqs_from_file()

    if result is None:
        sys.exit(1)

    mcqs_dict, full_content, lines = result

    print(f"Found {len(mcqs_dict)} MCQs in range 31676-31725")

    if mcqs_dict:
        # Show samples
        sorted_ids = sorted(mcqs_dict.keys())
        show_sample_mcq(mcqs_dict, sorted_ids[0])  # First
        show_sample_mcq(mcqs_dict, sorted_ids[len(sorted_ids)//2])  # Middle
        show_sample_mcq(mcqs_dict, sorted_ids[-1])  # Last
