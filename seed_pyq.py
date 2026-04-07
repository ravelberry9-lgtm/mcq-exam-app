"""
Seed script to load APHC Previous Year Questions into the database.
Run: python seed_pyq.py
"""
import json
import os
import sqlite3

DB_PATH = os.path.join(os.path.dirname(__file__), 'database.db')
SEED_FILE = os.path.join(os.path.dirname(__file__), 'pyq_seed_data.json')


def seed():
    if not os.path.exists(SEED_FILE):
        print(f"Error: {SEED_FILE} not found")
        return

    with open(SEED_FILE, 'r', encoding='utf-8') as f:
        questions = json.load(f)

    conn = sqlite3.connect(DB_PATH)
    conn.execute('''CREATE TABLE IF NOT EXISTS pyq_questions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        topic TEXT NOT NULL,
        year TEXT NOT NULL,
        paper TEXT NOT NULL,
        question_number INTEGER DEFAULT 0,
        question_text TEXT NOT NULL,
        option_a TEXT NOT NULL,
        option_b TEXT NOT NULL,
        option_c TEXT NOT NULL,
        option_d TEXT NOT NULL,
        correct_answer TEXT DEFAULT '',
        language TEXT DEFAULT 'English',
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )''')

    # Clear existing PYQ data
    conn.execute('DELETE FROM pyq_questions')
    conn.commit()

    # Insert all questions
    inserted = 0
    for q in questions:
        conn.execute('''INSERT INTO pyq_questions
            (topic, year, paper, question_number, question_text,
             option_a, option_b, option_c, option_d, correct_answer, language)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
            (q['topic'], q['year'], q['paper'], q['question_number'],
             q['question_text'], q['option_a'], q['option_b'],
             q['option_c'], q['option_d'], q['correct_answer'], q['language']))
        inserted += 1

    conn.commit()
    print(f"Successfully loaded {inserted} PYQ questions into database!")

    # Show summary
    cur = conn.execute('SELECT topic, COUNT(*) as c FROM pyq_questions GROUP BY topic ORDER BY c DESC')
    print("\nBy topic:")
    for row in cur.fetchall():
        print(f"  {row[0]}: {row[1]}")

    cur = conn.execute('SELECT year, COUNT(*) as c FROM pyq_questions GROUP BY year ORDER BY year')
    print("\nBy year:")
    for row in cur.fetchall():
        print(f"  {row[0]}: {row[1]}")

    conn.close()


if __name__ == '__main__':
    seed()
