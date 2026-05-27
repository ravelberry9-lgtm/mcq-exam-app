#!/usr/bin/env python3
"""
Extract MCQs 31676-31725 from database to understand current structure
"""

import sqlite3
import json

# Try different database files
db_files = ['database.db', 'questions.db', 'mcq_app.db', 'app.db', 'mcq.db']

for db_file in db_files:
    try:
        conn = sqlite3.connect(db_file)
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()

        # Check if questions table exists
        cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tables = [row[0] for row in cur.fetchall()]
        print(f"\n{db_file}: Tables: {tables}")

        if 'questions' in tables:
            # Try to get MCQs in our range
            cur.execute("""
                SELECT id, question, option_a, option_b, option_c, option_d, answer, explanation
                FROM questions
                WHERE id >= 31676 AND id <= 31725
                ORDER BY id
            """)

            mcqs = cur.fetchall()
            print(f"  Found {len(mcqs)} MCQs in range 31676-31725")

            if mcqs:
                # Show first 3
                for i, mcq in enumerate(mcqs[:3]):
                    print(f"\n  === MCQ {mcq['id']} ===")
                    print(f"  Question: {mcq['question'][:100]}...")
                    print(f"  OptA: {mcq['option_a'][:50]}...")
                    print(f"  Answer: {mcq['answer']}")
                    print(f"  Explanation: {mcq['explanation'][:100]}...")

                # Save first 3 to file for manual inspection
                with open('batch10_samples.txt', 'w', encoding='utf-8') as f:
                    for mcq in mcqs[:3]:
                        f.write(f"MCQ {mcq['id']}\n")
                        f.write(f"Q: {mcq['question']}\n")
                        f.write(f"A: {mcq['option_a']}\n")
                        f.write(f"B: {mcq['option_b']}\n")
                        f.write(f"C: {mcq['option_c']}\n")
                        f.write(f"D: {mcq['option_d']}\n")
                        f.write(f"Ans: {mcq['answer']}\n")
                        f.write(f"Exp: {mcq['explanation']}\n")
                        f.write("\n" + "="*80 + "\n\n")

                print("\n  Saved samples to batch10_samples.txt")

        conn.close()
        break  # If we found data, stop

    except Exception as e:
        print(f"\n{db_file}: Error - {e}")
        continue
