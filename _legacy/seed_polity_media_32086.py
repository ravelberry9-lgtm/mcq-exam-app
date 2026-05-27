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
        "id": 32086,
        "question_text": 'Which article of the Indian Constitution protects Press Freedom?\\nతెలుగు: భారత రాజ్యాంగం యొక్క ఏ సూత్రం మీడియా స్వేచ్ఛను రక్షిస్తుంది?',
        "option_a": 'Article 16 / సూత్రం 16',
        "option_b": 'Article 19(1)(a) / సూత్రం 19(1)(a)',
        "option_c": 'Article 25 / సూత్రం 25',
        "option_d": 'Article 32 / సూత్రం 32',
        "correct_answer": "B",
        "explanation": 'Article 19(1)(a) guarantees freedom of speech and expression to all citizens, which forms the foundation of press freedom under Indian Constitution.',
        "topic": "Media_&_Press_Freedom",
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

    cur.execute(delete_sql, (32086, 32086))

    for q in POLITY_MCQS:
        cur.execute(insert_sql, (
            q["id"], q["question_text"],
            q["option_a"], q["option_b"], q["option_c"], q["option_d"],
            q["correct_answer"], q["explanation"],
            q["topic"], q["folder"], "M"
        ))

    conn.commit()
    conn.close()
    print(f"[<stdin>] {len(POLITY_MCQS)} MCQs seeded (IDs 32086-{start_id + len(POLITY_MCQS) - 1}).")


if __name__ == "__main__":
    seed()
