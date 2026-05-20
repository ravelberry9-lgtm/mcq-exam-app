# -*- coding: utf-8 -*-
# Polity MCQs - Regenerated with seed() function
# Total: 61 questions

import os
import sqlite3

DATABASE_URL = os.environ.get("DATABASE_URL", "")
USE_POSTGRES = DATABASE_URL.startswith("postgres")

# Only import psycopg2 if actually needed
if USE_POSTGRES:
    import psycopg2
    import psycopg2.extras

POLITY_MCQS = [
    {
        "id": 32136,
        "question_text": "Which consumer protection law in India defines unfair trade practices?",
        "option_a": "Competition Act, 2002",
        "option_b": "Consumer Protection Act, 2019",
        "option_c": "Indian Penal Code",
        "option_d": "Essential Commodities Act, 1955",
        "correct_answer": "B",
        "explanation": "The Consumer Protection Act, 2019 defines unfair trade practices under Section 2(47) as practices that take undue advantage of consumers, include misleading advertisements, and violate consumer rights.",
        "topic": "Consumer_Protection",
        "folder": "National_CA"
    },
]

def seed():
    """Seed 61 MCQs to database"""
    if USE_POSTGRES:
        import psycopg2
        conn = psycopg2.connect(DATABASE_URL)
        conn.autocommit = False
        cur = conn.cursor()
        delete_sql = "DELETE FROM questions WHERE id >= %s AND id <= %s"
        insert_sql = """INSERT INTO questions
            (id, question_text, option_a, option_b, option_c, option_d,
             correct_answer, explanation, topic, folder, difficulty)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
            ON CONFLICT (id) DO NOTHING"""
    else:
        conn = sqlite3.connect(
            os.path.join(os.path.dirname(__file__), "database.db")
        )
        cur = conn.cursor()
        delete_sql = "DELETE FROM questions WHERE id >= ? AND id <= ?"
        insert_sql = """INSERT OR IGNORE INTO questions
            (id, question_text, option_a, option_b, option_c, option_d,
             correct_answer, explanation, topic, folder, difficulty)
            VALUES (?,?,?,?,?,?,?,?,?,?,?)"""

    cur.execute(delete_sql, (32136, 32196))

    for q in POLITY_MCQS:
        cur.execute(insert_sql, (
            q["id"], q["question_text"],
            q["option_a"], q["option_b"], q["option_c"], q["option_d"],
            q["correct_answer"], q["explanation"],
            q["topic"], q["folder"], "M"
        ))

    conn.commit()
    conn.close()
    print(f"[seed_polity_remaining_categories] {len(POLITY_MCQS)} MCQs seeded (IDs 32136-{32136 + len(POLITY_MCQS) - 1}).")


if __name__ == "__main__":
    seed()
