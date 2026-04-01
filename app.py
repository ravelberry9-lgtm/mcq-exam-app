"""
MCQ Exam App - Main Application
Local:   python app.py  →  http://localhost:5000
Railway: set DATABASE_URL env var → auto-uses PostgreSQL
"""

from flask import Flask, render_template, request, jsonify, redirect, url_for, session
import os, json, random, uuid
from datetime import datetime

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'mcq_secret_key_2024')
QUESTIONS_BANK = os.path.join(os.path.dirname(__file__), 'questions_bank')

# ─────────────────────────────────────────────
# DATABASE — SQLite locally, PostgreSQL on Railway
# ─────────────────────────────────────────────
DATABASE_URL = os.environ.get('DATABASE_URL', '')
if DATABASE_URL.startswith('postgres://'):
    DATABASE_URL = DATABASE_URL.replace('postgres://', 'postgresql://', 1)
USE_POSTGRES = bool(DATABASE_URL)

if USE_POSTGRES:
    import psycopg2
    import psycopg2.extras
else:
    import sqlite3
    DB_PATH = os.path.join(os.path.dirname(__file__), 'database.db')


def get_db():
    if USE_POSTGRES:
        return psycopg2.connect(DATABASE_URL)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def db_exec(conn, sql, params=()):
    """Execute SQL on either backend. Returns cursor."""
    if USE_POSTGRES:
        sql = sql.replace('?', '%s')
        sql = sql.replace('INSERT OR IGNORE', 'INSERT')
        if 'ON CONFLICT DO NOTHING' not in sql and 'INSERT INTO seen_questions' in sql:
            sql = sql + ' ON CONFLICT DO NOTHING'
        cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    else:
        cur = conn.cursor()
    cur.execute(sql, params)
    return cur


def row_to_dict(row):
    if row is None:
        return None
    return dict(row)


def init_db():
    conn = get_db()
    if USE_POSTGRES:
        cur = conn.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS questions (
            id SERIAL PRIMARY KEY,
            folder TEXT NOT NULL,
            topic TEXT NOT NULL,
            source_file TEXT,
            passage TEXT,
            passage_group_id TEXT,
            question_text TEXT NOT NULL,
            option_a TEXT NOT NULL,
            option_b TEXT NOT NULL,
            option_c TEXT NOT NULL,
            option_d TEXT NOT NULL,
            option_e TEXT,
            correct_answer TEXT NOT NULL,
            difficulty TEXT DEFAULT 'M',
            explanation TEXT,
            question_order INTEGER DEFAULT 0,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )''')
        cur.execute('''CREATE TABLE IF NOT EXISTS exam_sessions (
            id TEXT PRIMARY KEY,
            config TEXT NOT NULL,
            questions TEXT NOT NULL,
            answers TEXT DEFAULT '{}',
            started_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            submitted_at TIMESTAMP,
            score INTEGER,
            total INTEGER
        )''')
        cur.execute('''CREATE TABLE IF NOT EXISTS seen_questions (
            device_id TEXT NOT NULL,
            question_id INTEGER NOT NULL,
            seen_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            PRIMARY KEY (device_id, question_id)
        )''')
        conn.commit()
        cur.close()
    else:
        conn.executescript('''
            CREATE TABLE IF NOT EXISTS questions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                folder TEXT NOT NULL, topic TEXT NOT NULL, source_file TEXT,
                passage TEXT, passage_group_id TEXT, question_text TEXT NOT NULL,
                option_a TEXT NOT NULL, option_b TEXT NOT NULL,
                option_c TEXT NOT NULL, option_d TEXT NOT NULL, option_e TEXT,
                correct_answer TEXT NOT NULL, difficulty TEXT DEFAULT 'M',
                explanation TEXT, question_order INTEGER DEFAULT 0,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
            CREATE TABLE IF NOT EXISTS exam_sessions (
                id TEXT PRIMARY KEY, config TEXT NOT NULL, questions TEXT NOT NULL,
                answers TEXT DEFAULT '{}', started_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                submitted_at TIMESTAMP, score INTEGER, total INTEGER
            );
            CREATE TABLE IF NOT EXISTS seen_questions (
                device_id TEXT NOT NULL, question_id INTEGER NOT NULL,
                seen_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                PRIMARY KEY (device_id, question_id)
            );
        ''')
        conn.commit()
    conn.close()


# ─────────────────────────────────────────────
# HELPERS
# ─────────────────────────────────────────────
def get_folder_tree():
    tree = {}
    conn = get_db()
    cur = db_exec(conn, '''
        SELECT folder, topic, COUNT(*) as count
        FROM questions GROUP BY folder, topic ORDER BY folder, topic
    ''')
    rows = [row_to_dict(r) for r in cur.fetchall()]
    conn.close()
    for row in rows:
        folder = row['folder']
        if folder not in tree:
            tree[folder] = {}
        tree[folder][row['topic']] = row['count']
    return tree


def get_folder_totals():
    conn = get_db()
    cur = db_exec(conn, 'SELECT folder, COUNT(*) as count FROM questions GROUP BY folder')
    rows = [row_to_dict(r) for r in cur.fetchall()]
    conn.close()
    return {r['folder']: r['count'] for r in rows}


# ─────────────────────────────────────────────
# ROUTES
# ─────────────────────────────────────────────
@app.route('/')
def index():
    return render_template('index.html', tree=get_folder_tree(), totals=get_folder_totals())

@app.route('/setup')
def setup():
    return render_template('setup.html', tree=get_folder_tree())

@app.route('/api/folder-stats')
def folder_stats():
    return jsonify(get_folder_tree())

@app.route('/api/start-exam', methods=['POST'])
def start_exam():
    data = request.json
    mode      = data.get('mode', 'shuffle')
    duration  = int(data.get('duration', 45))
    selections = data.get('selections', {})
    device_id = data.get('device_id', 'default')

    conn = get_db()
    all_questions = []

    for folder, topics in selections.items():
        for topic, count in topics.items():
            count = int(count)
            if count <= 0:
                continue

            if mode == 'no_repeat':
                cur = db_exec(conn, 'SELECT question_id FROM seen_questions WHERE device_id=?', (device_id,))
                seen_ids = [r['question_id'] for r in cur.fetchall()]

                if seen_ids:
                    ph = ','.join(['?'] * len(seen_ids))
                    cur = db_exec(conn,
                        f'SELECT * FROM questions WHERE folder=? AND topic=? AND id NOT IN ({ph})',
                        [folder, topic] + seen_ids)
                else:
                    cur = db_exec(conn, 'SELECT * FROM questions WHERE folder=? AND topic=?', (folder, topic))
                rows = [row_to_dict(r) for r in cur.fetchall()]

                if len(rows) < count:
                    cur = db_exec(conn, 'SELECT * FROM questions WHERE folder=? AND topic=?', (folder, topic))
                    rows = [row_to_dict(r) for r in cur.fetchall()]
            else:
                cur = db_exec(conn, 'SELECT * FROM questions WHERE folder=? AND topic=?', (folder, topic))
                rows = [row_to_dict(r) for r in cur.fetchall()]

            rows = _pick_questions_smart(rows, count)
            all_questions.extend(rows)

    if not all_questions:
        conn.close()
        return jsonify({'error': 'No questions found for selected topics'}), 400

    if mode == 'shuffle':
        all_questions = _shuffle_keeping_passages(all_questions)

    if mode == 'no_repeat':
        for q in all_questions:
            try:
                if USE_POSTGRES:
                    cur = conn.cursor()
                    cur.execute(
                        'INSERT INTO seen_questions (device_id, question_id) VALUES (%s,%s) ON CONFLICT DO NOTHING',
                        (device_id, q['id'])
                    )
                else:
                    db_exec(conn, 'INSERT OR IGNORE INTO seen_questions (device_id, question_id) VALUES (?,?)',
                            (device_id, q['id']))
            except:
                pass
        conn.commit()

    session_id = str(uuid.uuid4())
    config = {'mode': mode, 'duration': duration, 'selections': selections, 'device_id': device_id}
    q_ids = [q['id'] for q in all_questions]
    db_exec(conn, 'INSERT INTO exam_sessions (id, config, questions) VALUES (?,?,?)',
            (session_id, json.dumps(config), json.dumps(q_ids)))
    conn.commit()
    conn.close()

    client_questions = [{
        'id': q['id'], 'folder': q['folder'], 'topic': q['topic'],
        'passage': q.get('passage'), 'passage_group_id': q.get('passage_group_id'),
        'question_text': q['question_text'],
        'options': _get_options(q), 'difficulty': q.get('difficulty', 'M')
    } for q in all_questions]

    return jsonify({'session_id': session_id, 'questions': client_questions,
                    'duration': duration, 'total': len(client_questions)})


def _get_options(q):
    opts = [{'key': k, 'text': q[f'option_{k.lower()}']} for k in ['A','B','C','D']]
    if q.get('option_e'):
        opts.append({'key': 'E', 'text': q['option_e']})
    return opts

def _pick_questions_smart(rows, count):
    groups, standalone = {}, []
    for r in rows:
        pgid = r.get('passage_group_id')
        if pgid: groups.setdefault(pgid, []).append(r)
        else: standalone.append(r)
    result, remaining = [], count
    group_list = list(groups.values())
    random.shuffle(group_list)
    for group in group_list:
        if remaining <= 0: break
        if len(group) <= remaining:
            result.extend(group); remaining -= len(group)
    random.shuffle(standalone)
    result.extend(standalone[:remaining])
    if len(result) < count:
        rest = [r for r in rows if r not in result]
        random.shuffle(rest)
        result.extend(rest[:count - len(result)])
    return result[:count]

def _shuffle_keeping_passages(questions):
    groups, standalone = {}, []
    for q in questions:
        pgid = q.get('passage_group_id')
        if pgid: groups.setdefault(pgid, []).append(q)
        else: standalone.append(q)
    units = [[q] for q in standalone] + list(groups.values())
    random.shuffle(units)
    result = []
    for unit in units: result.extend(unit)
    return result


@app.route('/exam/<session_id>')
def exam(session_id):
    conn = get_db()
    cur = db_exec(conn, 'SELECT * FROM exam_sessions WHERE id=?', (session_id,))
    sess = row_to_dict(cur.fetchone())
    conn.close()
    if not sess: return redirect('/')
    config = json.loads(sess['config'])
    return render_template('exam.html', session_id=session_id, duration=config['duration'])


@app.route('/api/submit-exam', methods=['POST'])
def submit_exam():
    data = request.json
    session_id = data.get('session_id')
    answers = data.get('answers', {})

    conn = get_db()
    cur = db_exec(conn, 'SELECT * FROM exam_sessions WHERE id=?', (session_id,))
    sess = row_to_dict(cur.fetchone())
    if not sess:
        conn.close(); return jsonify({'error': 'Session not found'}), 404
    if sess['submitted_at']:
        conn.close(); return jsonify({'error': 'Already submitted'}), 400

    q_ids = json.loads(sess['questions'])
    results, score = [], 0
    for qid in q_ids:
        cur = db_exec(conn, 'SELECT * FROM questions WHERE id=?', (qid,))
        q = row_to_dict(cur.fetchone())
        if not q: continue
        user_ans = answers.get(str(qid), answers.get(qid, None))
        correct = q['correct_answer'].strip().upper()
        is_correct = bool(user_ans and user_ans.strip().upper() == correct)
        if is_correct: score += 1
        results.append({
            'id': qid, 'folder': q['folder'], 'topic': q['topic'],
            'passage': q.get('passage'), 'passage_group_id': q.get('passage_group_id'),
            'question_text': q['question_text'], 'options': _get_options(q),
            'correct_answer': correct, 'user_answer': user_ans,
            'is_correct': is_correct, 'explanation': q.get('explanation', ''),
            'difficulty': q.get('difficulty', 'M')
        })

    total = len(results)
    unanswered = sum(1 for r in results if not r['user_answer'])
    db_exec(conn, 'UPDATE exam_sessions SET answers=?, submitted_at=?, score=?, total=? WHERE id=?',
            (json.dumps(answers), datetime.now().isoformat(), score, total, session_id))
    conn.commit(); conn.close()

    return jsonify({'score': score, 'total': total, 'unanswered': unanswered,
                    'percentage': round(score / total * 100, 1) if total else 0, 'results': results})


@app.route('/api/exam-data/<session_id>')
def exam_data(session_id):
    conn = get_db()
    cur = db_exec(conn, 'SELECT * FROM exam_sessions WHERE id=?', (session_id,))
    sess = row_to_dict(cur.fetchone())
    if not sess:
        conn.close(); return jsonify({'error': 'Not found'}), 404
    config = json.loads(sess['config'])
    q_ids = json.loads(sess['questions'])
    questions = []
    for qid in q_ids:
        cur = db_exec(conn, 'SELECT * FROM questions WHERE id=?', (qid,))
        q = row_to_dict(cur.fetchone())
        if q:
            questions.append({'id': q['id'], 'folder': q['folder'], 'topic': q['topic'],
                               'passage': q.get('passage'), 'passage_group_id': q.get('passage_group_id'),
                               'question_text': q['question_text'], 'options': _get_options(q),
                               'difficulty': q.get('difficulty', 'M')})
    conn.close()
    return jsonify({'questions': questions, 'duration': config['duration'], 'total': len(questions)})


# ─────────────────────────────────────────────
# ADMIN / IMPORT ROUTES
# ─────────────────────────────────────────────
@app.route('/admin')
def admin():
    tree = get_folder_tree()
    totals = get_folder_totals()
    conn = get_db()
    cur = db_exec(conn, 'SELECT COUNT(*) as c FROM questions')
    total_q = row_to_dict(cur.fetchone())['c']
    conn.close()
    return render_template('admin.html', tree=tree, totals=totals, total_q=total_q)


def _insert_questions(conn, questions, filename):
    count = 0
    for q in questions:
        db_exec(conn, '''
            INSERT INTO questions
            (folder, topic, source_file, passage, passage_group_id, question_text,
             option_a, option_b, option_c, option_d, option_e,
             correct_answer, difficulty, explanation, question_order)
            VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
        ''', (
            q['folder'], q['topic'], q.get('source_file', filename),
            q.get('passage'), q.get('passage_group_id'), q['question_text'],
            q['option_a'], q['option_b'], q['option_c'], q['option_d'], q.get('option_e'),
            q['correct_answer'], q.get('difficulty', 'M'),
            q.get('explanation', ''), q.get('question_order', 0)
        ))
        count += 1
    return count


@app.route('/api/import-html', methods=['POST'])
def import_html():
    from parser.html_parser import parse_html_file
    file = request.files.get('file')
    folder = request.form.get('folder', 'GK')
    topic  = request.form.get('topic', 'General')
    if not file: return jsonify({'error': 'No file'}), 400
    content   = file.read().decode('utf-8', errors='ignore')
    questions = parse_html_file(content, folder, topic)
    conn = get_db()
    count = _insert_questions(conn, questions, file.filename)
    conn.commit(); conn.close()
    return jsonify({'imported': count, 'folder': folder, 'topic': topic})


@app.route('/api/import-pdf', methods=['POST'])
def import_pdf():
    from parser.pdf_parser import parse_pdf_file
    file = request.files.get('file')
    folder = request.form.get('folder', 'Mental_Ability')
    topic  = request.form.get('topic', 'Puzzles')
    if not file: return jsonify({'error': 'No file'}), 400
    content   = file.read()
    questions = parse_pdf_file(content, folder, topic)
    conn = get_db()
    count = _insert_questions(conn, questions, file.filename)
    conn.commit(); conn.close()
    return jsonify({'imported': count, 'folder': folder, 'topic': topic})


@app.route('/api/add-question', methods=['POST'])
def add_question():
    d = request.json
    conn = get_db()
    db_exec(conn, '''
        INSERT INTO questions
        (folder, topic, source_file, passage, passage_group_id, question_text,
         option_a, option_b, option_c, option_d, option_e,
         correct_answer, difficulty, explanation)
        VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)
    ''', (
        d.get('folder'), d.get('topic'), d.get('source_file', 'manual'),
        d.get('passage'), d.get('passage_group_id'), d['question_text'],
        d['option_a'], d['option_b'], d['option_c'], d['option_d'], d.get('option_e'),
        d['correct_answer'], d.get('difficulty', 'M'), d.get('explanation', '')
    ))
    conn.commit(); conn.close()
    return jsonify({'success': True})


@app.route('/api/delete-topic', methods=['POST'])
def delete_topic():
    d = request.json
    conn = get_db()
    db_exec(conn, 'DELETE FROM questions WHERE folder=? AND topic=?', (d['folder'], d['topic']))
    conn.commit(); conn.close()
    return jsonify({'success': True})


@app.route('/api/reset-seen', methods=['POST'])
def reset_seen():
    d = request.json
    device_id = d.get('device_id', 'default')
    conn = get_db()
    db_exec(conn, 'DELETE FROM seen_questions WHERE device_id=?', (device_id,))
    conn.commit(); conn.close()
    return jsonify({'success': True})


@app.route('/api/stats')
def stats():
    conn = get_db()
    tree = get_folder_tree()
    total    = row_to_dict(db_exec(conn, 'SELECT COUNT(*) as c FROM questions').fetchone())['c']
    sessions = row_to_dict(db_exec(conn, "SELECT COUNT(*) as c FROM exam_sessions WHERE submitted_at IS NOT NULL").fetchone())['c']
    avg_row  = row_to_dict(db_exec(conn, "SELECT AVG(CAST(score AS FLOAT)/total*100) as a FROM exam_sessions WHERE submitted_at IS NOT NULL AND total>0").fetchone())
    conn.close()
    return jsonify({'total_questions': total, 'total_exams': sessions,
                    'avg_score': round(avg_row['a'], 1) if avg_row['a'] else 0, 'tree': tree})


@app.route('/result/<session_id>')
def result(session_id):
    return render_template('result.html', session_id=session_id)


# ─────────────────────────────────────────────
# STARTUP
# ─────────────────────────────────────────────
init_db()

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    print("\n" + "="*55)
    print("  📚 MCQ EXAM APP — STARTED")
    print(f"  DB: {'PostgreSQL ☁️' if USE_POSTGRES else 'SQLite 💾'}")
    print("="*55)
    if not USE_POSTGRES:
        import socket
        try: local_ip = socket.gethostbyname(socket.gethostname())
        except: local_ip = "127.0.0.1"
        print(f"\n  💻 On this PC:    http://localhost:{port}")
        print(f"  📱 On your phone: http://{local_ip}:{port}")
        print(f"\n  Make sure phone is on same WiFi network!")
    print("="*55 + "\n")
    app.run(host='0.0.0.0', port=port, debug=False)
