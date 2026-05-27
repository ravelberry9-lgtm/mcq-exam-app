# -*- coding: utf-8 -*-
# Polity MCQs - Auto-generated from tuple format
# Total: 1 questions

import os
import sqlite3
import psycopg2
import psycopg2.extras

DATABASE_URL = os.environ.get("DATABASE_URL", "")
if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)
USE_POSTGRES = bool(DATABASE_URL)

POLITY_MCQS = [
    {
        "id": 32111,
        "question_text": 'In what year did India consolidate its labour laws into the Labour Codes?\\nతెలుగు: భారతదేశం చట్టపరమైన చట్టాలను కోడ్\u200cలుగా ఏ సంవత్సరంలో సమీకరించింది?',
        "option_a": '2018 / 2018',
        "option_b": '2020 / 2020',
        "option_c": '2022 / 2022',
        "option_d": '2024 / 2024',
        "correct_answer": "B",
        "explanation": 'India consolidated 44 labour laws into 4 Labour Codes in 2020: Code on Wages 2019, Industrial Relations Code 2020, Occupational Safety Code 2020, and Social Security Code 2020.',
        "topic": "Labour_Rights_&_Social_Security",
        "folder": "National_CA"
    },

]

def seed():
    """Seed 1 MCQs to database"""
    if USE_POSTGRES:
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

    cur.execute(delete_sql, (32111, 32111))

    for q in POLITY_MCQS:
        cur.execute(insert_sql, (
            q["id"], q["question_text"],
            q["option_a"], q["option_b"], q["option_c"], q["option_d"],
            q["correct_answer"], q["explanation"],
            q["topic"], q["folder"], "M"
        ))

    conn.commit()
    conn.close()
    print(f"[<stdin>] {len(POLITY_MCQS)} MCQs seeded (IDs 32111-{start_id + len(POLITY_MCQS) - 1}).")


if __name__ == "__main__":
    seed()
