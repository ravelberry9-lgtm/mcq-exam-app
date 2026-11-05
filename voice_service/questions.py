"""Pick the next question for a device, adaptively, from the app's own question bank."""
import json
import random
from sqlalchemy import text

ORDER = ["E", "M", "H"]


def recent_accuracy(conn, device_id, subject_id=None, window=10):
    rows = conn.execute(text("""SELECT seen_count, wrong_count FROM user_question_state
        WHERE device_id=:d ORDER BY last_seen_at DESC LIMIT :w"""), {"d": device_id, "w": window}).fetchall()
    seen = sum(r[0] or 0 for r in rows)
    wrong = sum(r[1] or 0 for r in rows)
    return None if seen == 0 else 1 - wrong / seen


def target_difficulty(acc):
    if acc is None: return "M"
    if acc >= 0.8: return "H"
    if acc >= 0.5: return "M"
    return "E"


def next_question(conn, device_id, subject_id, chapter_id=None, difficulty=None, rng=random):
    """Priority: previously wrong > never seen > least recently seen; difficulty-matched where possible."""
    want = difficulty or target_difficulty(recent_accuracy(conn, device_id))
    sql = """SELECT q.id, q.difficulty, q.question_en, q.question_te, q.options_en, q.options_te,
                    q.correct_answer, q.explanation_en, q.explanation_te, q.chapter_id,
                    COALESCE(u.seen_count,0) AS seen, COALESCE(u.wrong_count,0) AS wrong
             FROM questions q LEFT JOIN user_question_state u ON u.question_id=q.id AND u.device_id=:d
             WHERE q.subject_id=:s AND q.correct_answer IS NOT NULL AND q.correct_answer<>''
               AND COALESCE(q.question_te, q.question_en, '')<>''"""
    p = {"d": device_id, "s": subject_id}
    if chapter_id:
        sql += " AND q.chapter_id=:c"; p["c"] = chapter_id
    rows = [dict(r._mapping) for r in conn.execute(text(sql), p)]
    if not rows:
        return None
    def bucket(r): return 0 if r["wrong"] > 0 else (1 if r["seen"] == 0 else 2)
    def dist(r): return abs(ORDER.index(r["difficulty"] if r["difficulty"] in ORDER else "M") - ORDER.index(want))
    rng.shuffle(rows)
    rows.sort(key=lambda r: (bucket(r), dist(r), r["seen"]))
    q = rows[0]
    for k in ("options_en", "options_te"):
        if isinstance(q[k], str):
            try: q[k] = json.loads(q[k])
            except Exception: q[k] = {}
    for k in ("options_en", "options_te"):
        o = q[k]
        if isinstance(o, list):
            o = {"abcde"[i]: v for i, v in enumerate(o) if i < 5}
        q[k] = {str(a).lower(): v for a, v in (o or {}).items()}
    q["correct_answer"] = str(q["correct_answer"]).strip().lower()
    return q


def record_answer(conn, device_id, question_id, correct: bool):
    """Table key is (device_id, question_id). Update first, insert if no row was touched."""
    p = {"d": device_id, "q": question_id, "w": 0 if correct else 1}
    n = conn.execute(text("""UPDATE user_question_state SET seen_count=COALESCE(seen_count,0)+1,
        wrong_count=COALESCE(wrong_count,0)+:w, last_seen_at=CURRENT_TIMESTAMP
        WHERE device_id=:d AND question_id=:q"""), p).rowcount
    if not n:
        conn.execute(text("""INSERT INTO user_question_state(device_id,question_id,seen_count,wrong_count,flagged,saved,last_seen_at)
            VALUES(:d,:q,1,:w,false,false,CURRENT_TIMESTAMP)"""), p)
