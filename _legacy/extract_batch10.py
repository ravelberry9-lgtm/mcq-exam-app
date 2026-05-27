#!/usr/bin/env python3
import re

# Read the seed file
with open('seed_national_ca_2026_mcq.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract all MCQ tuples (they're in format: (id, question, opt_a, opt_b, opt_c, opt_d, answer, explanation, folder, topic))
# Pattern to match MCQ entries
pattern = r"\(\s*(\d+),\s*\"([^\"]*)\",\s*\"([^\"]*)\",\s*\"([^\"]*)\",\s*\"([^\"]*)\",\s*\"([^\"]*)\",\s*\"([^\"]*)\",\s*\"([^\"]*)\",\s*\"([^\"]*)\",\s*\"([^\"]*)\"\)"

matches = re.finditer(pattern, content, re.DOTALL)

mcqs = []
for match in matches:
    mcq_id = int(match.group(1))
    if 31676 <= mcq_id <= 31725:
        mcqs.append({
            'id': mcq_id,
            'question': match.group(2),
            'opt_a': match.group(3),
            'opt_b': match.group(4),
            'opt_c': match.group(5),
            'opt_d': match.group(6),
            'answer': match.group(7),
            'explanation': match.group(8),
            'folder': match.group(9),
            'topic': match.group(10),
        })

print(f"Found {len(mcqs)} MCQs in range 31676-31725")
for mcq in mcqs[:3]:
    print(f"\n\n=== MCQ {mcq['id']} ===")
    print(f"Question: {mcq['question'][:100]}")
    print(f"Folder: {mcq['folder']}, Topic: {mcq['topic']}")
