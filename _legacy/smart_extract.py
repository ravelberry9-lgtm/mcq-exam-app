#!/usr/bin/env python3
"""Smart extraction using string search"""

with open('seed_national_ca_2026_mcq.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Find position of MCQ 31676
pos_31676 = content.find('(31676,')
pos_31700 = content.find('(31700,')
pos_31725 = content.find('(31725,')

print(f"MCQ 31676 position: {pos_31676}")
print(f"MCQ 31700 position: {pos_31700}")
print(f"MCQ 31725 position: {pos_31725}")

if pos_31676 > 0:
    # Extract around MCQ 31676
    start = pos_31676
    # Find the next MCQ ID
    next_pos = content.find('(31677,', start)
    if next_pos < 0:
        next_pos = content.find('(317', start + 10)

    if next_pos > 0:
        excerpt = content[start:next_pos]
        print("\n=== MCQ 31676 (excerpt) ===")
        # Show first 600 chars
        print(excerpt[:600])
        print(f"\n... [{len(excerpt)} chars total]")

if pos_31700 > 0:
    start = pos_31700
    next_pos = content.find('(31701,', start)
    if next_pos < 0:
        next_pos = content.find('(317', start + 10)

    if next_pos > 0:
        excerpt = content[start:next_pos]
        print("\n=== MCQ 31700 (excerpt) ===")
        print(excerpt[:600])
        print(f"\n... [{len(excerpt)} chars total]")

if pos_31725 > 0:
    start = pos_31725
    # This is the last one, so find where it ends
    next_pos = content.find('\n    ]', start)

    if next_pos > 0:
        excerpt = content[start:min(next_pos, start+1000)]
        print("\n=== MCQ 31725 (excerpt) ===")
        print(excerpt[:600])
        print(f"\n... [{len(excerpt)} chars total]")
