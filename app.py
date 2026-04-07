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
ADMIN_PIN = os.environ.get('ADMIN_PIN', '1234')

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
        cur.execute('''CREATE TABLE IF NOT EXISTS study_notes (
            id SERIAL PRIMARY KEY,
            subject TEXT NOT NULL,
            topic TEXT NOT NULL,
            chapter_num INTEGER NOT NULL,
            chapter_title_te TEXT NOT NULL,
            chapter_title_en TEXT NOT NULL,
            pages_ref TEXT DEFAULT '',
            sections_json TEXT NOT NULL DEFAULT '[]',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )''')
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
        cur.execute('''CREATE TABLE IF NOT EXISTS chapter_mcqs (
            id SERIAL PRIMARY KEY,
            study_note_id INTEGER NOT NULL,
            section_idx INTEGER NOT NULL DEFAULT 0,
            difficulty INTEGER NOT NULL DEFAULT 1,
            exam_type TEXT NOT NULL DEFAULT 'General',
            q_te TEXT NOT NULL,
            opt_a TEXT NOT NULL,
            opt_b TEXT NOT NULL,
            opt_c TEXT NOT NULL,
            opt_d TEXT NOT NULL,
            correct TEXT NOT NULL,
            explanation_te TEXT NOT NULL DEFAULT '',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )''')
        conn.commit()
        cur.close()
    else:
        conn.executescript('''
            CREATE TABLE IF NOT EXISTS study_notes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                subject TEXT NOT NULL,
                topic TEXT NOT NULL,
                chapter_num INTEGER NOT NULL,
                chapter_title_te TEXT NOT NULL,
                chapter_title_en TEXT NOT NULL,
                pages_ref TEXT DEFAULT '',
                sections_json TEXT NOT NULL DEFAULT '[]',
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
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
            CREATE TABLE IF NOT EXISTS chapter_mcqs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                study_note_id INTEGER NOT NULL,
                section_idx INTEGER NOT NULL DEFAULT 0,
                difficulty INTEGER NOT NULL DEFAULT 1,
                exam_type TEXT NOT NULL DEFAULT 'General',
                q_te TEXT NOT NULL,
                opt_a TEXT NOT NULL,
                opt_b TEXT NOT NULL,
                opt_c TEXT NOT NULL,
                opt_d TEXT NOT NULL,
                correct TEXT NOT NULL,
                explanation_te TEXT NOT NULL DEFAULT '',
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        ''')
        conn.commit()

    # ── Migration: add subtopic column if not yet present ──
    ph = '%s' if USE_POSTGRES else '?'
    try:
        if USE_POSTGRES:
            cur2 = conn.cursor()
            cur2.execute("ALTER TABLE study_notes ADD COLUMN IF NOT EXISTS subtopic TEXT DEFAULT ''")
            conn.commit()
            cur2.close()
        else:
            conn.execute("ALTER TABLE study_notes ADD COLUMN subtopic TEXT DEFAULT ''")
            conn.commit()
    except Exception:
        pass   # column already exists — safe to ignore
    # ── Migration: add exam_type column to chapter_mcqs if not yet present ──
    try:
        if USE_POSTGRES:
            cur3 = conn.cursor()
            cur3.execute("ALTER TABLE chapter_mcqs ADD COLUMN IF NOT EXISTS exam_type TEXT NOT NULL DEFAULT 'General'")
            conn.commit()
            cur3.close()
        else:
            conn.execute("ALTER TABLE chapter_mcqs ADD COLUMN exam_type TEXT NOT NULL DEFAULT 'General'")
            conn.commit()
    except Exception:
        pass   # column already exists — safe to ignore
    # ── Auto-seed ancient chapters if missing (safe to run on every startup) ──
    # Each chapter gets its own fresh connection to avoid transaction abort issues.
    # Use subtopic='Ancient' count (not chapter_num) to avoid counting Modern ch1.
    try:
        cur_cnt = db_exec(conn, "SELECT COUNT(*) FROM study_notes WHERE topic='Indian_History' AND subtopic='Ancient'")
        row_cnt = cur_cnt.fetchone()
        ancient_count = list(row_cnt)[0] if row_cnt else 0
        if ancient_count < 9:
            print(f"[startup] Only {ancient_count}/9 ancient chapters found — auto-seeding...")
            conn.close()
            _auto_seed_ancient()
            print("[startup] Auto-seed complete.")
            return  # connection already closed inside _auto_seed_ancient
    except Exception as _ae:
        print(f"[startup] Auto-seed check error: {_ae}")

    # Back-fill: any remaining Indian_History row without a subtopic → 'Ancient'
    try:
        db_exec(conn,
            "UPDATE study_notes SET subtopic='Ancient' WHERE topic='Indian_History' AND (subtopic IS NULL OR subtopic='')")
        conn.commit()
    except Exception:
        pass

    conn.close()


def _auto_seed_ancient():
    """Seed all 9 ancient IH chapters. Each chapter uses its own DB connection."""
    import importlib
    for ch_num, mod_name in [
        (1,'seed_ch1'),(2,'seed_ch2'),(3,'seed_ch3'),(4,'seed_ch4'),(5,'seed_ch5'),
        (6,'seed_ch6'),(7,'seed_ch7'),(8,'seed_ch8'),(9,'seed_ch9'),
    ]:
        # Fresh connection per chapter — avoids Postgres aborted transaction spreading
        c = get_db()
        try:
            mod = importlib.import_module(mod_name)
            notes_fn = getattr(mod, f'_seed_ch{ch_num}_notes_inner')
            mcqs_fn  = getattr(mod, f'_seed_ch{ch_num}_mcqs_inner')
            notes_fn(c, db_exec, row_to_dict, USE_POSTGRES, force=False)
            c.commit()
            mcqs_fn(c, db_exec, row_to_dict, USE_POSTGRES)
            c.commit()
            # Explicitly set subtopic='Ancient' for this chapter
            ph = '%s' if USE_POSTGRES else '?'
            c.execute(f"UPDATE study_notes SET subtopic='Ancient' WHERE topic={ph} AND chapter_num={ph} AND (subtopic IS NULL OR subtopic='')" if not USE_POSTGRES else
                      f"UPDATE study_notes SET subtopic='Ancient' WHERE topic={ph} AND chapter_num={ph} AND (subtopic IS NULL OR subtopic='')",
                      ('Indian_History', ch_num))
            c.commit()
            print(f"[auto-seed] ch{ch_num} done.")
        except Exception as e:
            print(f"[auto-seed] ch{ch_num} error: {e}")
            try: c.rollback()
            except: pass
        finally:
            try: c.close()
            except: pass
    # Final back-fill pass: fix any chapter that was seeded without subtopic
    try:
        fc = get_db()
        fc.execute("UPDATE study_notes SET subtopic='Ancient' WHERE topic='Indian_History' AND (subtopic IS NULL OR subtopic='')" if not USE_POSTGRES else
                   "UPDATE study_notes SET subtopic='Ancient' WHERE topic='Indian_History' AND (subtopic IS NULL OR subtopic='')")
        fc.commit()
        fc.close()
    except Exception as e:
        print(f"[auto-seed] back-fill error: {e}")


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
    mode         = data.get('mode', 'shuffle')
    duration     = int(data.get('duration', 45))
    selections   = data.get('selections', {})
    device_id    = data.get('device_id', 'default')
    student_name = data.get('student_name', 'Student')

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
    config = {'mode': mode, 'duration': duration, 'selections': selections, 'device_id': device_id, 'student_name': student_name}
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
# ─────────────────────────────────────────────
# ADMIN PIN PROTECTION
# ─────────────────────────────────────────────
def admin_required(f):
    from functools import wraps
    @wraps(f)
    def decorated(*args, **kwargs):
        if not session.get('admin_ok'):
            # API routes expect JSON; page routes get a redirect
            if request.path.startswith('/api/'):
                return jsonify({'error': 'Not authenticated. Please log in via /admin-login.'}), 401
            return redirect('/admin-login')
        return f(*args, **kwargs)
    return decorated

@app.route('/admin-login', methods=['GET', 'POST'])
def admin_login():
    error = ''
    if request.method == 'POST':
        if request.form.get('pin') == ADMIN_PIN:
            session['admin_ok'] = True
            return redirect('/admin')
        error = '❌ Wrong PIN. Try again.'
    return render_template('admin_login.html', error=error)

@app.route('/admin-logout')
def admin_logout():
    session.pop('admin_ok', None)
    return redirect('/')

@app.route('/admin')
@admin_required
def admin():
    tree = get_folder_tree()
    totals = get_folder_totals()
    conn = get_db()
    cur = db_exec(conn, 'SELECT COUNT(*) as c FROM questions')
    total_q = row_to_dict(cur.fetchone())['c']
    conn.close()
    return render_template('admin.html', tree=tree, totals=totals, total_q=total_q)


def _insert_questions(conn, questions, filename):
    count, skipped = 0, 0
    for q in questions:
        # Duplicate check — skip if same question_text+folder+topic already exists
        cur = db_exec(conn,
            'SELECT id FROM questions WHERE folder=? AND topic=? AND question_text=?',
            (q['folder'], q['topic'], q['question_text']))
        if cur.fetchone():
            skipped += 1
            continue
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
    return count, skipped


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
    count, skipped = _insert_questions(conn, questions, file.filename)
    conn.commit(); conn.close()
    return jsonify({'imported': count, 'skipped': skipped, 'folder': folder, 'topic': topic})


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
    count, skipped = _insert_questions(conn, questions, file.filename)
    conn.commit(); conn.close()
    return jsonify({'imported': count, 'skipped': skipped, 'folder': folder, 'topic': topic})


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

@app.route('/history')
def history():
    return render_template('history.html')

@app.route('/api/history')
def api_history():
    conn = get_db()
    cur = db_exec(conn, '''
        SELECT id, config, score, total, started_at, submitted_at
        FROM exam_sessions
        WHERE submitted_at IS NOT NULL
        ORDER BY submitted_at DESC
        LIMIT 100
    ''')
    rows = [row_to_dict(r) for r in cur.fetchall()]
    conn.close()
    sessions = []
    for r in rows:
        try:
            cfg = json.loads(r['config'])
            pct = round(r['score'] / r['total'] * 100, 1) if r['total'] else 0
            topics = []
            for folder, ts in cfg.get('selections', {}).items():
                for topic in ts:
                    topics.append(f"{folder.replace('_',' ')} › {topic.replace('_',' ')}")
            sessions.append({
                'id': r['id'],
                'student': cfg.get('student_name', 'Student'),
                'score': r['score'],
                'total': r['total'],
                'percentage': pct,
                'topics': topics,
                'duration': cfg.get('duration', '—'),
                'submitted_at': str(r['submitted_at'])[:16].replace('T', ' ')
            })
        except:
            continue
    return jsonify(sessions)


# ─────────────────────────────────────────────
# NOTES ROUTES
# ─────────────────────────────────────────────
@app.route('/notes')
def notes_home():
    conn = get_db()
    cur = db_exec(conn, '''
        SELECT subject, COUNT(*) as chapter_count
        FROM study_notes GROUP BY subject ORDER BY subject
    ''')
    subjects = [row_to_dict(r) for r in cur.fetchall()]
    conn.close()
    return render_template('notes_home.html', subjects=subjects)


@app.route('/notes/<subject>')
def notes_subject(subject):
    conn = get_db()
    cur = db_exec(conn, '''
        SELECT topic, COUNT(*) as chapter_count
        FROM study_notes WHERE subject=? GROUP BY topic ORDER BY topic
    ''', (subject,))
    topics = [row_to_dict(r) for r in cur.fetchall()]
    conn.close()
    return render_template('notes_subject.html', subject=subject, topics=topics)


@app.route('/notes/<subject>/<topic>')
def notes_topic(subject, topic):
    conn = get_db()
    # Check if any chapters have subtopics defined
    cur = db_exec(conn, '''
        SELECT subtopic, COUNT(*) as chapter_count
        FROM study_notes WHERE subject=? AND topic=? AND subtopic IS NOT NULL AND subtopic != ''
        GROUP BY subtopic ORDER BY subtopic
    ''', (subject, topic))
    subtopics = [row_to_dict(r) for r in cur.fetchall()]

    if subtopics:
        conn.close()
        return render_template('notes_topic.html', subject=subject, topic=topic,
                               subtopics=subtopics, chapters=[])

    # No subtopics — show chapters directly
    cur = db_exec(conn, '''
        SELECT id, chapter_num, chapter_title_te, chapter_title_en, pages_ref, sections_json
        FROM study_notes WHERE subject=? AND topic=?
        ORDER BY chapter_num
    ''', (subject, topic))
    chapters = [row_to_dict(r) for r in cur.fetchall()]
    conn.close()
    for ch in chapters:
        try:
            secs = json.loads(ch.get('sections_json') or '[]')
            total_words = sum(len((s.get('audio') or s.get('text') or '').split()) for s in secs)
            ch['est_secs']  = max(5, round(total_words / (130 / 60))) if total_words else 0
            ch['sec_count'] = len(secs)
        except Exception:
            ch['est_secs']  = 0
            ch['sec_count'] = 0
    return render_template('notes_topic.html', subject=subject, topic=topic,
                           subtopics=[], chapters=chapters)


@app.route('/notes/<subject>/<topic>/<subtopic>')
def notes_subtopic(subject, topic, subtopic):
    """List chapters within a subtopic (e.g. Ancient / Medieval / Modern)."""
    conn = get_db()
    cur = db_exec(conn, '''
        SELECT id, chapter_num, chapter_title_te, chapter_title_en, pages_ref, sections_json
        FROM study_notes WHERE subject=? AND topic=? AND subtopic=?
        ORDER BY chapter_num
    ''', (subject, topic, subtopic))
    chapters = [row_to_dict(r) for r in cur.fetchall()]
    conn.close()
    for ch in chapters:
        try:
            secs = json.loads(ch.get('sections_json') or '[]')
            total_words = sum(len((s.get('audio') or s.get('text') or '').split()) for s in secs)
            ch['est_secs']  = max(5, round(total_words / (130 / 60))) if total_words else 0
            ch['sec_count'] = len(secs)
        except Exception:
            ch['est_secs']  = 0
            ch['sec_count'] = 0
    return render_template('notes_subtopic.html', subject=subject, topic=topic,
                           subtopic=subtopic, chapters=chapters)


@app.route('/notes/<subject>/<topic>/<int:chapter_id>')
def notes_chapter(subject, topic, chapter_id):
    conn = get_db()
    cur = db_exec(conn, 'SELECT * FROM study_notes WHERE id=?', (chapter_id,))
    chapter = row_to_dict(cur.fetchone())
    conn.close()
    if not chapter:
        return redirect('/notes')
    sections = json.loads(chapter['sections_json'])
    # Pre-compute estimated total seconds (130 wpm at 1×) for the chapter header
    try:
        total_words = sum(len((s.get('audio') or s.get('text') or '').split()) for s in sections)
        ch_est_secs = max(5, round(total_words / (130 / 60))) if total_words else 0
    except Exception:
        ch_est_secs = 0
    return render_template('notes_chapter.html',
                           subject=subject, topic=topic,
                           chapter=chapter, sections=sections,
                           ch_est_secs=ch_est_secs)


@app.route('/api/notes/add', methods=['POST'])
@admin_required
def notes_add():
    d = request.json
    conn = get_db()
    db_exec(conn, '''
        INSERT INTO study_notes
        (subject, topic, chapter_num, chapter_title_te, chapter_title_en, pages_ref, sections_json)
        VALUES (?,?,?,?,?,?,?)
    ''', (
        d['subject'], d['topic'], int(d['chapter_num']),
        d['chapter_title_te'], d['chapter_title_en'],
        d.get('pages_ref', ''), d.get('sections_json', '[]')
    ))
    conn.commit()
    conn.close()
    return jsonify({'success': True})


@app.route('/api/notes/delete', methods=['POST'])
@admin_required
def notes_delete():
    d = request.json
    conn = get_db()
    db_exec(conn, 'DELETE FROM study_notes WHERE id=?', (d['id'],))
    conn.commit()
    conn.close()
    return jsonify({'success': True})


@app.route('/api/notes/list')
def notes_list():
    conn = get_db()
    cur = db_exec(conn, '''
        SELECT id, subject, topic, chapter_num, chapter_title_te, chapter_title_en, pages_ref
        FROM study_notes ORDER BY subject, topic, chapter_num
    ''')
    rows = [row_to_dict(r) for r in cur.fetchall()]
    conn.close()
    return jsonify(rows)


@app.route('/api/notes/seed', methods=['POST'])
def notes_seed():
    """Seed Chapter 1 Indian History. Add ?force=1 to overwrite existing."""
    force = request.args.get('force', '0') == '1'
    conn = get_db()
    # Ensure study_notes table exists (handles older Railway deployments)
    if USE_POSTGRES:
        cur0 = conn.cursor()
        cur0.execute('''CREATE TABLE IF NOT EXISTS study_notes (
            id SERIAL PRIMARY KEY,
            subject TEXT NOT NULL, topic TEXT NOT NULL,
            chapter_num INTEGER NOT NULL,
            chapter_title_te TEXT NOT NULL, chapter_title_en TEXT NOT NULL,
            pages_ref TEXT DEFAULT '', sections_json TEXT NOT NULL DEFAULT '[]',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )''')
        conn.commit(); cur0.close()
    else:
        conn.execute('''CREATE TABLE IF NOT EXISTS study_notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            subject TEXT NOT NULL, topic TEXT NOT NULL,
            chapter_num INTEGER NOT NULL,
            chapter_title_te TEXT NOT NULL, chapter_title_en TEXT NOT NULL,
            pages_ref TEXT DEFAULT '', sections_json TEXT NOT NULL DEFAULT '[]',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )''')
        conn.commit()
    cur = db_exec(conn, "SELECT id FROM study_notes WHERE subject='GK' AND topic='Indian_History' AND chapter_num=1")
    existing = cur.fetchone()
    if existing and not force:
        conn.close()
        return jsonify({'message': 'Already seeded. Use ?force=1 to overwrite.'})
    if existing and force:
        db_exec(conn, "DELETE FROM study_notes WHERE subject='GK' AND topic='Indian_History' AND chapter_num=1")
        conn.commit()

    ch1_sections = [
        {
            "title": "చరిత్ర – నిర్వచనాలు",
            "sub": "History · Culture · Civilisation అర్థాలు",
            "audio": "నమస్కారం! భారతదేశ చరిత్ర అధ్యాయం 1 మొదలుపెడుతున్నాం. చరిత్ర అంటే ఏమిటి? మన దేశంలో, ప్రపంచంలోని వివిధ ప్రాంతాల్లో మానవ సమాజం ఆవిర్భావం ఎలా జరిగింది? సంస్కృతి, నాగరికత ఏ విధంగా పరిణామం చెందాయి? సామాజిక, ఆర్థిక, మత, రాజకీయ వ్యవస్థలు ఎలా మారాయి? ఈ అంశాలన్నీ మనకు తెలియజేసే శాస్త్రమే చరిత్ర — History. ఇప్పుడు మూడు నిర్వచనాలు గుర్తుపెట్టుకోండి. మొదటిది — చరిత్ర, అంటే History: మానవ సమాజ ఆవిర్భావం, సంస్కృతి, నాగరికత, వ్యవస్థల పరిణామాన్ని వివరించే శాస్త్రం. రెండవది — సంస్కృతి, అంటే Culture: ఒక జీవన విధానం. ఒక జాతి ఎలా జీవిస్తుంది, ఏమి నమ్ముతుంది, ఏమి ఆచరిస్తుంది — అదే సంస్కృతి. మూడవది — నాగరికత, అంటే Civilisation: సంస్కృతిలో ఒక ప్రత్యేకమైన అభివృద్ధి సాధించిన పరిణామ దశను నాగరికత అని అంటారు. సరళంగా చెప్పాలంటే — సంస్కృతి అనేది ఒక చెట్టు లాంటిది. నాగరికత అనేది ఆ చెట్టుకు పూసే పువ్వు. చరిత్ర అనేది ఆ మొత్తం ప్రయాణాన్ని నమోదు చేసే పుస్తకం. Mini Recap: చరిత్ర అంటే మానవ పరిణామ శాస్త్రం. సంస్కృతి అంటే జీవన విధానం. నాగరికత అంటే ప్రత్యేక అభివృద్ధి దశ. మళ్ళీ చెప్పండి — చరిత్ర, సంస్కృతి, నాగరికత!"
        },
        {
            "title": "హిస్టరీ పదం పుట్టుక – హెరోడోటస్ – Indology",
            "sub": "హిస్టోరియా (Greek) · హెరోడోటస్ · Father of History · సర్ విలియం జోన్స్",
            "audio": "చరిత్రను ఇంగ్లీష్‌లో హిస్టరీ అని అంటారు. ఈ హిస్టరీ అనే పదం ఎక్కడ నుండి వచ్చింది? గ్రీకు భాషలో ఉన్న హిస్టోరియా అనే పదం నుండి వచ్చింది. హిస్టోరియా అంటే — పరిశోధించి తెలుసుకొనుట — Inquiry, Knowledge acquired by investigation. ఇప్పుడు అందరూ చెప్పండి — హిస్టరీ పదం ఎక్కడ నుండి వచ్చింది? హిస్టోరియా! మళ్ళీ — హిస్టోరియా! EXAM ALERT! చరిత్ర పితామహుడు ఎవరు? హెరోడోటస్. హెరోడోటస్, హెరోడోటస్, హెరోడోటస్! ఇతను గ్రీకు చరిత్ర పితామహుడు — Father of History. ఇతని గ్రంథం పేరు — The Histories. భారత చరిత్ర, సంస్కృతులు, భాష మరియు సాహిత్య అధ్యయనాన్ని ఇండాలజీ అంటారు. భారత ఇండాలజీ పితామహుని పేరు? సర్ విలియం జోన్స్. సర్ విలియం జోన్స్, సర్ విలియం జోన్స్! Quick fire: Father of History అంటే హెరోడోటస్. The Histories అంటే హెరోడోటస్ గ్రంథం. Father of Indology అంటే సర్ విలియం జోన్స్."
        },
        {
            "title": "మతపరమైన ఆధారాలు",
            "sub": "వేద సాహిత్యం · జైన సాహిత్యం · బౌద్ధ సాహిత్యం",
            "audio": "చారిత్రక ఆధారాలు రెండు రకాలు — లిఖిత ఆధారాలు మరియు పురావస్తు ఆధారాలు. లిఖిత ఆధారాలలో మళ్ళీ రెండు రకాలు — స్వదేశీ సాహిత్యం మరియు విదేశీ సాహిత్యం. స్వదేశీ సాహిత్యంలో రెండు రకాలు — మతపరమైన సాహిత్యం మరియు లౌకిక సాహిత్యం. మతపరమైన ఆధారాల్లో మూడు ముఖ్యమైనవి వినండి. మొదటిది వేద సాహిత్యం. ఇందులో వేదాలు, బ్రాహ్మణాలు, అరణ్యకాలు, ఉపనిషత్తులు, ఉపవేదాలు, వేదాంగాలు, పురాణాలు మరియు ఇతిహాసాలు ఉంటాయి. రెండవది జైన సాహిత్యం. జైన పవిత్ర గ్రంథాలైన అంగులు మరియు జైన కవులు రచించిన జైన కల్పసూత్ర, పరిశిష్ట పర్వన్ మరియు కథాసరిత్సాగరం వంటి గ్రంథాలు జైన సాహిత్యానికి చెందుతాయి. మూడవది బౌద్ధ సాహిత్యం. బౌద్ధ మత పవిత్ర గ్రంథాలైన త్రిపిటకాలు మరియు బౌద్ధ సన్యాసి నాగసేనుడు రచించిన మిలిందపన్న, ఆచార్య నాగార్జునుడు రచించిన గ్రంథాలు ఈ సాహిత్యానికి చెందుతాయి. EXAM ALERT: జైన కల్పసూత్ర, బౌద్ధ త్రిపిటకాలు, మిలిందపన్న — ఈ మూడూ తప్పక గుర్తుంచుకోండి!"
        },
        {
            "title": "లౌకిక ఆధారాలు – ముఖ్య గ్రంథాలు",
            "sub": "అర్థశాస్త్రం · రాజతరంగిణి · నీతిసారం · హర్షచరిత్ర",
            "audio": "లౌకిక సాహిత్యం మతాలకు అతీతంగా రూపొందించబడింది. ఇవి రాజ్య పాలన, రాజనీతి, సామాజిక విషయాలను వివరిస్తాయి. EXAM ALERT! అర్థశాస్త్రం — దీన్ని చాణక్యుడు రచించాడు. చాణక్యుడు, చాణక్యుడు, చాణక్యుడు! ఇతనికి కౌటిల్యుడు మరియు విష్ణు గుప్తుడు అని కూడా పేర్లు కలవు. ఒక్క రచయితకు మూడు పేర్లు — చాణక్యుడు, కౌటిల్యుడు, విష్ణు గుప్తుడు! ఈ గ్రంథం మౌర్య పరిపాలనను గురించి వివరిస్తుంది. రాజతరంగిణి — దీన్ని కల్హణుడు రచించాడు. కల్హణుడు, కల్హణుడు! ఇది కాశ్మీరు రాజవంశాల చరిత్రను వివరిస్తుంది. దీనికి కొనసాగింపుగా జోనరాజు రచించిన దివ్య రాజతరంగిణి, శ్రీవర రచించిన జైన రాజతరంగిణి కూడా ఉన్నాయి. నీతిసారం — దీన్ని కామందకుడు రచించాడు. ఈ గ్రంథం గుప్తుల పరిపాలనను వివరిస్తుంది. హర్ష చరిత్ర — దీన్ని బాణుడు రచించాడు. బాణుడు, బాణుడు! Quick Recap: చాణక్యుడు అంటే అర్థశాస్త్రం. కల్హణుడు అంటే రాజతరంగిణి. కామందకుడు అంటే నీతిసారం. బాణుడు అంటే హర్షచరిత్ర."
        },
        {
            "title": "ఇతర లౌకిక గ్రంథాలు – 9 ముఖ్య గ్రంథాలు",
            "sub": "మహాభాష్యం · ముద్రారాక్షసం · పృథ్వీరాజ్ రాసో వరకు",
            "audio": "EXAM ALERT! ఇప్పుడు చాలా ముఖ్యమైన విభాగం — ఇతర లౌకిక గ్రంథాలు. ఒక్కొక్కటి జాగ్రత్తగా వినండి. మొదటిది మహాభాష్యం — రచయిత పతంజలి. పతంజలి, పతంజలి! ఈ గ్రంథం మౌర్యానంతర వంశాల గురించి వివరిస్తుంది. రెండవది బృహత్కథ — రచయిత గుణాఢ్యుడు. గుణాఢ్యుడు, గుణాఢ్యుడు! ఇది శాతవాహన కాలం నాటి గ్రంథం. మూడవది గాథాసప్తశతి — రచయిత హాలుడు. హాలుడు, హాలుడు! ఇది కూడా శాతవాహనుల కాలపు గ్రంథం. గుర్తుంచుకోండి: పతంజలి, గుణాఢ్యుడు, హాలుడు — ముగ్గురూ మొదటి మూడు గ్రంథాల రచయితలు. నాల్గవది ముద్రారాక్షసం — రచయిత విశాఖదత్తుడు. విశాఖదత్తుడు, విశాఖదత్తుడు! ఇది మౌర్యవంశ స్థాపన గురించి వివరిస్తుంది. ఐదవది దేవీచంద్రగుప్తం — రచయిత కూడా విశాఖదత్తుడే! ఒక రచయిత రెండు గ్రంథాలు — ముద్రారాక్షసం మరియు దేవీచంద్రగుప్తం. ఆరవది కౌముది మహోత్సవం — రచయిత విజ్జికుడు. ఇది మొదటి చంద్రగుప్తుని పట్టాభిషేకం గురించి. ఏడవది విక్రమాంక దేవచరిత్ర — రచయిత బిల్హణుడు. బిల్హణుడు, బిల్హణుడు! ఇది కళ్యాణి చాళుక్య రాజు తైభువనమల్ల గురించి. ఎనిమిదవది పృథ్వీరాజ్ విజయం — రచయిత జయనకుడు. పృథ్వీరాజ్ చౌహాన్ మూడు విజయాలు వివరిస్తుంది. తొమ్మిదవది పృథ్వీరాజ్ రాసో — రచయిత చాంద్ బర్దాయి. చాంద్ బర్దాయి, చాంద్ బర్దాయి! ఇది కూడా పృథ్వీరాజ్ చౌహాన్ మూడు గురించే. EXAM TRICK: విశాఖదత్తుడు రెండు గ్రంథాలు రాశాడు — ముద్రారాక్షసం మరియు దేవీచంద్రగుప్తం. పృథ్వీరాజ్ చౌహాన్ గురించి రెండు గ్రంథాలు — పృథ్వీరాజ్ విజయం అంటే జయనకుడు, పృథ్వీరాజ్ రాసో అంటే చాంద్ బర్దాయి."
        },
        {
            "title": "గ్రీకు ఆధారాలు – ఇండికా గ్రంథం",
            "sub": "మెగస్తనీస్ · చంద్రగుప్త మౌర్య · సెల్యూకస్ నికేటర్",
            "audio": "ఇప్పుడు విదేశీ సాహిత్య ఆధారాలు వినండి. అనేక మంది విదేశీయులు భారతదేశంలోకి రాయబారులుగా, పర్యాటకులుగా మరియు వ్యాపారస్తులుగా వచ్చి వారి అనుభవాలను గ్రంథాల రూపంలో వివరించారు. EXAM ALERT! గ్రీకు ఆధారాల్లో అత్యంత ముఖ్యమైనది — ఇండికా గ్రంథం. ఈ గ్రంథాన్ని మెగస్తనీస్ రచించాడు. మెగస్తనీస్, మెగస్తనీస్, మెగస్తనీస్! మూడుసార్లు చెప్పండి — మెగస్తనీస్! మెగస్తనీస్ ఎవరు? ఇతను సిరియా పాలకుడైన సెల్యూకస్ నికేటర్ యొక్క రాయబారిగా చంద్రగుప్త మౌర్య ఆస్థానానికి వచ్చాడు. చంద్రగుప్త మౌర్య, చంద్రగుప్త మౌర్య! మౌర్య సామ్రాజ్య స్థాపకుడు. ఇండికా గ్రంథంలో ఏముంది? మౌర్య పరిపాలనా అంశాలను, దక్షిణ ప్రాంతంలోని పరిపాలనా అంశాలను వివరిస్తుంది. Formula: మెగస్తనీస్ అంటే ఇండికా. ఒక్కసారి చెప్పండి — మెగస్తనీస్ అంటే ఇండికా!"
        },
        {
            "title": "పెరిప్లస్ ఆఫ్ ది ఎరిత్రియన్ సీ",
            "sub": "అజ్ఞాత నావికుడు (Unknown Sailor) · రాజకీయ · వాణిజ్య అంశాలు",
            "audio": "EXAM ALERT! ఇది చాలా చాలా ముఖ్యమైన గ్రంథం — పెరిప్లస్ ఆఫ్ ది ఎరిత్రియన్ సీ. Periplus of the Erythraean Sea. ఈ పేరు మళ్ళీ చెప్పండి — పెరిప్లస్ ఆఫ్ ది ఎరిత్రియన్ సీ! ఈ గ్రంథాన్ని ఎవరు రచించారు? ఒక అజ్ఞాత నావికుడు — Unknown Sailor! అజ్ఞాత నావికుడు, అజ్ఞాత నావికుడు! రచయిత పేరు తెలియదు — కానీ గ్రంథం చాలా ముఖ్యమైనది. EXAM ALERT: పెరిప్లస్ రచయిత ఎవరు అని అడిగితే — అజ్ఞాత నావికుడు, Unknown Sailor అని చెప్పాలి! ఈ గ్రంథంలో ఏముంది? భారతీయ రాజకీయ అంశాలు, వాణిజ్య అంశాలు మరియు జాతిపరమైన అంశాలను వివరిస్తుంది. ముఖ్యంగా భారత్ మరియు రోమ్ మధ్య వ్యాపార సంబంధాలు ఇందులో వివరంగా ఉన్నాయి. Formula: పెరిప్లస్ అంటే అజ్ఞాత నావికుడు. అజ్ఞాత నావికుడు అంటే పెరిప్లస్. గుర్తుపెట్టుకోండి!"
        },
        {
            "title": "లాటిన్ ఆధారాలు · శ్రీలంక సాహిత్యం",
            "sub": "నాచురల్ హిస్టరీ (ప్లీని) · దీపవంశ · మహావంశ · పాళీ భాష",
            "audio": "ఇప్పుడు లాటిన్ మరియు శ్రీలంక ఆధారాలు వినండి. లాటిన్ ఆధారాలు: EXAM ALERT! నాచురల్ హిస్టరీ — ఈ గ్రంథాన్ని ప్లీని రచించాడు. ప్లీని, ప్లీని, ప్లీని! ఈ గ్రంథం మౌర్యుల కాలపు పరిపాలన అంశాలను వివరిస్తుంది. Formula: ప్లీని అంటే నాచురల్ హిస్టరీ. నాచురల్ హిస్టరీ అంటే ప్లీని. ఇప్పుడు శ్రీలంక సాహిత్యం వినండి. EXAM ALERT! రెండు అత్యంత ముఖ్యమైన గ్రంథాలు — ఒకటి దీపవంశ, రెండు మహావంశ. దీపవంశ అంటే The Chronicle of the Island — ద్వీపం చరిత్ర. మహావంశ అంటే The Great Chronicle — మహా చరిత్ర. ఇవి సింహళానికి చెందిన బౌద్ధ మత గ్రంథాలు. పాళీ భాషలో రచించబడ్డాయి. పాళీ భాషలో పాళీ భాషలో! ఈ గ్రంథాలు భారతదేశంలో బౌద్ధమతానికి సంబంధించిన, మౌర్యులకు సంబంధించిన విలువైన సమాచారాన్ని ఇస్తున్నాయి. Quick Recap: ప్లీని అంటే నాచురల్ హిస్టరీ లాటిన్ ఆధారం. దీపవంశ మరియు మహావంశ అంటే శ్రీలంక గ్రంథాలు పాళీ భాష."
        },
        {
            "title": "చైనీస్ ఆధారాలు – ఫాహియాన్ & హ్యూయెన్ త్సాంగ్",
            "sub": "ఫో-కువో-కి · సి-యు-కి · King of Travellers · హర్షవర్ధనుడు",
            "audio": "EXAM ALERT! చైనీస్ ఆధారాలు — ఇవి exam లో చాలా ముఖ్యమైనవి. మొదటి చైనీస్ గ్రంథం — ఫో-కువో-కి. ఈ గ్రంథాన్ని ఫాహియాన్ అనే చైనా యాత్రికుడు రచించాడు. ఫాహియాన్, ఫాహియాన్, ఫాహియాన్! ఫాహియాన్ మొదటి చైనా యాత్రికుడు! మొదటి చైనా యాత్రికుడు అంటే ఫాహియాన్. ఇతను రెండవ చంద్రగుప్తుని కాలంలో భారత్‌కు వచ్చాడు. రెండవ చంద్రగుప్తుడు, రెండవ చంద్రగుప్తుడు! రెండవ చైనీస్ గ్రంథం — సి-యు-కి. ఈ గ్రంథాన్ని హ్యూయెన్ త్సాంగ్ రచించాడు. హ్యూయెన్ త్సాంగ్, హ్యూయెన్ త్సాంగ్, హ్యూయెన్ త్సాంగ్! ఇతను వైనాకు చెందిన బౌద్ధ సన్యాసి, పండితుడు మరియు యాత్రికుడు. EXAM ALERT! హ్యూయెన్ త్సాంగ్‌ను యాత్రికుల రాజు — King of Travellers అంటారు. చెప్పండి — King of Travellers ఎవరు? హ్యూయెన్ త్సాంగ్! ఇతను కనౌజ్ పరిపాలించిన హర్షవర్ధనుని కాలంలో భారత్‌కు వచ్చాడు. తూర్పు వేంగి చాళుక్యుల కుళ్ళ విష్ణువర్ధనుడు, పల్లవుల కాలం మొదటి నరసింహ వర్మన్, బాదామి చాళుక్య రెండవ పులకేశిని సందర్శించాడు. Shortcut: ఫాహియాన్ అంటే ఫో-కువో-కి అంటే రెండవ చంద్రగుప్తుడు. హ్యూయెన్ త్సాంగ్ అంటే సి-యు-కి అంటే హర్షవర్ధనుడు అంటే King of Travellers."
        },
        {
            "title": "అరబిక్ · తిబెటన్ ఆధారాలు",
            "sub": "అల్-బెరూని · కితాబ్-ఉల్-హింద్ · తారానాథ్ · Founder of Indology",
            "audio": "EXAM ALERT! అరబిక్ సాహిత్యం నుండి అత్యంత ముఖ్యమైన గ్రంథం — కితాబ్-ఉల్-హింద్, Kitab-ul-Hind. ఈ గ్రంథాన్ని అల్-బెరూని రచించాడు. అల్-బెరూని, అల్-బెరూని, అల్-బెరూని! అల్-బెరూని ఎవరు? ఇతను మహ్మద్ ఘజని యొక్క ఆస్థాన విద్వాంసుడు. ఈ గ్రంథంలో భారతదేశ ప్రజల జీవన విధానాన్ని వివరించాడు. EXAM ALERT! అల్-బెరూనికి రెండు బిరుదులు — మొదటిది Founder of Indology — ఇండాలజీ స్థాపకుడు. రెండవది Father of Comparative Religion — తులనాత్మక మత శాస్త్రం పితామహుడు. చెప్పండి — అల్-బెరూని అంటే కితాబ్-ఉల్-హింద్ అంటే Founder of Indology! తిబెటన్ సాహిత్యం వినండి. EXAM ALERT! The History of Tibet — ఈ గ్రంథాన్ని తారానాథ్ రచించాడు. తారానాథ్, తారానాథ్! ఇతను పదిహేడవ శతాబ్దంలో భారత్‌లో గల అన్ని బౌద్ధ ప్రాంతాలను తిరిగి ఈ పుస్తకాన్ని వ్రాశాడు. అశోక చక్రవర్తికి సంబంధించిన విలువైన సమాచారాన్ని ఇస్తుంది. మరొక తిబెటన్ గ్రంథం — దివ్యవదన. Quick Recap: అల్-బెరూని అంటే కితాబ్-ఉల్-హింద్ అరబిక్. తారానాథ్ అంటే The History of Tibet తిబెటన్. దివ్యవదన అంటే మరొక తిబెటన్ గ్రంథం."
        },
        {
            "title": "పురావస్తు ఆధారాలు – శాసనాలు పరిచయం",
            "sub": "Inscriptions · ఎపిగ్రఫీ · పేలియోగ్రఫీ · మొదటి సంస్కృత శాసనం",
            "audio": "ఇప్పుడు పురావస్తు ఆధారాలు వినండి. ఆర్కియాలజిస్టులు చరిత్రకు సంబంధించిన శాసనాలు, నాణెములు, కట్టడాలు మరియు వాటి అవశేషాలు, శిల్పాలను ఆధారాలుగా ఉపయోగిస్తారు. శాసనాలు అంటే ఏమిటి? రాయి, ఇటుక, లోహం లేదా ఏదైనా గట్టి ఉపరితలంపై లిఖించబడిన లేదా రంగుతో వేయబడిన చారిత్రక, మతపరమైన లేదా ఇంకా ఏదైనా రికార్డునే శాసనం అంటారు. EXAM ALERT! రెండు ముఖ్యమైన పదాలు గుర్తుపెట్టుకోండి. మొదటిది ఎపిగ్రఫీ — శాసన అధ్యయనం. రెండవది పేలియోగ్రఫీ — ప్రాచీన లిపుల అధ్యయనం. చెప్పండి — శాసన అధ్యయనం అంటే ఎపిగ్రఫీ! ప్రాచీన లిపులు అంటే పేలియోగ్రఫీ! EXAM ALERT! భారత్‌లో మొదటి సంస్కృత శాసనం — రుద్రదమనుడి జునాఘడ్ శాసనం. రుద్రదమనుడు, రుద్రదమనుడు! జునాఘడ్ శాసనం! భారతదేశంలో ప్రాచీన కాల మొదటి దశలో బ్రాహ్మీ, ఖరోష్ఠి మరియు గ్రీకు లిపుల గల శాసనాలు వేయబడ్డాయి. తదనంతర కాలంలో సంస్కృత శాసనాలు వేయబడ్డాయి."
        },
        {
            "title": "శాసనాల 4 రకాలు",
            "sub": "రాజాజ్ఞలు · అంకిత · దాన · స్మారక శాసనాలు – అశోకుడు – నలంద తామ్ర శాసనం",
            "audio": "EXAM ALERT! శాసనాల 4 రకాలు — ఇవి తప్పక వస్తాయి. వినండి. ఒకటి: రాజాజ్ఞలు — Rock Edicts. రాజు యొక్క ఆజ్ఞలను మరియు ఉత్తర్వులను ప్రజలకు తెలియజేయుటకు మొట్టమొదట అశోకుడు శాసన రూపంలో వేశాడు. అశోకుడు, అశోకుడు! రెండు: అంకిత శాసనాలు — Dedicative Inscription. ఏదైనా ఇతరులకు అంకితం చేయుటను శాసన రూపంలో వేయుట. మూడు: దాన శాసనాలు — Donative Inscription. రాజులు గాని వారి భార్యలు గాని పురోహితులకు లేదా ఇతర ధార్మిక సంస్థలకు దానం చేసిన భూముల గురించి రాగి వలకలపై రాయించి వేయిస్తే వాటినే దాన శాసనాలు అంటారు. EXAM ALERT! ముఖ్యమైన ఉదాహరణ — గుప్తుల కాలం నాటి నలంద తామ్ర శాసనం — Copper Plate Inscription బీహార్. ఈ శాసనంలో బ్రాహ్మణులకు అగ్రహారాలను ఇవ్వడం గురించి పేర్కొనబడింది. ఈ శాసనంలోనే మొదటిసారిగా అగ్రహార అనే పదం కనిపించింది! అగ్రహార పదం మొదటిసారి అంటే నలంద తామ్ర శాసనం! నాలుగు: స్మారక శాసనాలు — Commemorative Inscription. భౌగోళిక పరిస్థితులు, సమకాలీన ఆర్థిక, మత సాంస్కృతిక పరిస్థితులు, పాలక వంశాల పేర్లు, యుద్ధాలు, మంత్రుల విజయాలు వంటివి నమోదు చేసేవి. ఉదాహరణలు: అశోకుని శాసనాలు, భారవేలుని హాతిగుంఫా శాసనం, గౌతమి బాలశ్రీ నాసిక్ శాసనం, రుద్రదమనుని జునాఘడ్ శాసనం, సముద్రగుప్తుని అలహాబాద్ ప్రశస్తి, చంద్రగుప్తుని మెహ్రాలి శాసనం, రెండవ పులకేశి ఐహోళ్ళు శాసనం. 4 రకాలు మళ్ళీ చెప్పండి: రాజాజ్ఞలు, అంకిత, దాన, స్మారక!"
        },
        {
            "title": "నాణెములు – న్యూమిస్మాటిక్స్",
            "sub": "Numismatics · మౌర్యులు · ఇందో-గ్రీకులు · గుప్తులు · రాజకీయ సమాచారం",
            "audio": "శాసనాల తర్వాత, మరొక ముఖ్యమైన పురావస్తు ఆధారం — నాణెములు, అంటే Coins. EXAM ALERT! నాణెముల అధ్యయనాన్ని న్యూమిస్మాటిక్స్ అంటారు. న్యూమిస్మాటిక్స్, న్యూమిస్మాటిక్స్! నాణెముల ద్వారా ఏమి తెలుస్తుంది? రాజకీయ, ఆర్థిక, సాంస్కృతిక సమాచారం అందజేస్తున్నాయి. ముఖ్యమైన నాణేల ఉదాహరణలు వినండి. మొదటిది మౌర్యుల విద్వంక నాణేలు — మౌర్య సామ్రాజ్యం గురించి తెలుపుతాయి. రెండవది ఇందో-గ్రీకులు రెండువైపుల ముద్రించిన నాణేలు — రెండు సంస్కృతుల కలయిక చూపుతాయి. మూడవది గుప్తుల నాణేలు — గరుడ లాంఛనం, లక్ష్మి మొదలైనవి చెక్కిన నాణేలు రాజకీయ, ఆర్థిక, సాంస్కృతిక సమాచారం అందజేస్తున్నాయి. విభిన్న లోహాలు: బంగారు, వెండి, రాగి, సీసం మరియు పాటీన్ మొదలైన లోహాలతో నాణేలు ముద్రించారు. నాణెముల అధ్యయనం అంటే న్యూమిస్మాటిక్స్. గుర్తుపెట్టుకోండి!"
        },
        {
            "title": "కాల నిర్ధారణ పద్ధతులు – 5 Dating Methods",
            "sub": "రేడియోకార్బన్ (విల్లర్డ్ లిబ్బి) · పొటాషియం-అర్గాన్ · థర్మోల్యూమినిసెన్స్ · డెండ్రోక్రోనాలజీ",
            "audio": "EXAM ALERT! ఇప్పుడు చాలా ముఖ్యమైన పట్టిక — వస్తు అవశేషాల కాల నిర్ధారణ పద్ధతులు. 5 పద్ధతులు శ్రద్ధగా వినండి. పద్ధతి ఒకటి: రేడియోకార్బన్ పద్ధతి — C 14. శాస్త్రవేత్త విల్లర్డ్ లిబ్బి అమెరికా. విల్లర్డ్ లిబ్బి, విల్లర్డ్ లిబ్బి! అనువైన వస్తువు — సేంద్రియ పదార్థం, అంటే ఎముక, దంతాలు. కాల వ్యాప్తి — 20,000 నుండి 4,00,000 సంవత్సరాలు. EXAM ALERT: C 14 అంటే విల్లర్డ్ లిబ్బి! పద్ధతి రెండు: పొటాషియం-అర్గాన్ పద్ధతి — K-A 40. శాస్త్రవేత్త మెక్‌డూగల్. మెక్‌డూగల్! అనువైన వస్తువు — అగ్నిశిల. కాల వ్యాప్తి — అపరిమితం. పద్ధతి మూడు: థర్మోల్యూమినిసెన్స్ పద్ధతి. శాస్త్రవేత్త ఇటికిన్స్. ఇటికిన్స్, ఇటికిన్స్! అనువైన వస్తువు — కుండలు. కాల వ్యాప్తి — 10,000 సంవత్సరాలు. పద్ధతి నాలుగు: అమైనో ఆమ్ల రెసిమేషన్ పద్ధతి. అనువైన వస్తువు — ఎముక, సముద్ర కర్చురాలు. కాల వ్యాప్తి — 1 లక్ష సంవత్సరాలు. పద్ధతి ఐదు: డెండ్రోక్రోనాలజీ పద్ధతి. అనువైన వస్తువు — వృక్షాల వార్షిక వలయాలు. కాల వ్యాప్తి — 7,500 సంవత్సరాలు. EXAM QUICK MEMORY: C 14 అంటే లిబ్బి అంటే ఎముక. K-A అంటే మెక్‌డూగల్ అంటే అగ్నిశిల. థర్మో అంటే ఇటికిన్స్ అంటే కుండలు. డెండ్రో అంటే చెట్ల వలయాలు."
        },
        {
            "title": "వాస్తు రీతి మరియు శిల్పాలు",
            "sub": "Nagara · Dravida · Vesara · Iconography · Indo-Gothic",
            "audio": "ఇప్పుడు వాస్తు రీతి మరియు శిల్పాలు వినండి. ప్రాచీన వాస్తురీతి మరియు శిల్పాల అధ్యయనాన్ని ఇకనోగ్రఫీ అంటారు. ఇకనోగ్రఫీ, ఇకనోగ్రఫీ! EXAM ALERT! మూడు ముఖ్యమైన వాస్తు శైలులు — ఒకటి నగరశైలి అంటే Nagara. ఉత్తర భారతదేశంలో అభివృద్ధి చెందింది. రెండు ద్రావిడ శైలి అంటే Dravida. దక్షిణ భారతదేశంలో అభివృద్ధి చెందింది. మూడు వేసర శైలి అంటే Vesara. పై రెండు శైలుల కలయిక. చెప్పండి — మూడు శైలులు? నగరశైలి, ద్రావిడ శైలి, వేసర శైలి! మౌర్యుల కాలంలో భవనాలు వెదురుగా కలపతో నిర్మించడం వల్ల కాలగమనంలో అవశేషాలు లభించకుండా పోయాయి. కానీ తరువాత కాలంలో వచ్చిన గుప్తులు మరియు మధ్యయుగంలో వివిధ రాజవంశాలు వాస్తు రీతి మరియు శిల్పకళలో వైవిధ్యాన్ని కనబరిచాయి. ఆధునిక యుగంలో బ్రిటిషర్ల ప్రభావం వల్ల ఇందో-గోథిక్ మరియు నియో-రోమన్ శైలులు అందుబాటులోకి వచ్చాయి. Nagara అంటే ఉత్తరం. Dravida అంటే దక్షిణం. Vesara అంటే రెండింటి కలయిక. మళ్ళీ చెప్పండి!"
        },
        {
            "title": "వస్తు అవశేషాలు – కుండలు (Pottery)",
            "sub": "మెహర్గర్ · కుమ్మరి చక్రం · సింధూ నాగరికత",
            "audio": "ఆర్కియాలజిస్టులు తవ్వకాలు జరిపేటపుడు వివిధ కాలాలకు సంబంధించిన కుండలు, వ్యవసాయపరమైన ఆధారాలు, గృహ నిర్మాణ అవశేషాలు అభివ్యక్తి వస్తు అవశేషాలుగా పిలుస్తారు. EXAM ALERT! భారతదేశంలో మొట్టమొదటగా మెహర్గర్‌లో కుమ్మరి చక్రం బయటపడింది. మెహర్గర్, మెహర్గర్! మళ్ళీ చెప్పండి — భారత్‌లో మొదటి కుమ్మరి చక్రం ఎక్కడ? మెహర్గర్! సింధూ నాగరికత పట్టణమైన హారప్పాలో కుమ్మరి చక్రం బయలుదేరడం వల్ల హారప్పాలో కుండల పరిశ్రమ ఉందని నిర్ధారణకు రావడానికి ఆధారమైంది. అదేవిధంగా పరిపాట్లో లోహాలు మరియు రంగుహారులో లభ్యం కావడం వల్ల ఆ ప్రదేశాలలో పరిపండించినట్లుగా తెలియవస్తుంది. వివిధ కాలాల్లో వివిధ రకాల కుండలు తయారు చేయడం వల్ల ఆ కాలం నాటి పరిస్థితులు అర్థమగును. మెహర్గర్ అంటే మొదటి కుమ్మరి చక్రం అంటే భారత్‌లో pottery మొదలు. గుర్తుపెట్టుకోండి!"
        },
        {
            "title": "గుర్తుపెట్టుకోండి! – అధ్యాయం 1 పూర్తి సారాంశం",
            "sub": "Exam Quick Recap · Important Names · Key Terms · Tables",
            "audio": "అధ్యాయం 1 పూర్తయింది! ఇప్పుడు గుర్తుపెట్టుకోండి విభాగం. అన్ని ముఖ్యమైన అంశాలు rapid fire గా చెప్తాను — మీరు వెంటనే మనసులో repeat చేయండి. ముఖ్యమైన వ్యక్తులు మరియు వారి గ్రంథాలు వినండి. హెరోడోటస్ అంటే The Histories అంటే Father of History గ్రీకు. సర్ విలియం జోన్స్ అంటే Father of Indology భారతం. చాణక్యుడు అంటే కౌటిల్యుడు అంటే విష్ణు గుప్తుడు అంటే అర్థశాస్త్రం. కల్హణుడు అంటే రాజతరంగిణి. బాణుడు అంటే హర్షచరిత్ర. పతంజలి అంటే మహాభాష్యం. విశాఖదత్తుడు అంటే ముద్రారాక్షసం మరియు దేవీచంద్రగుప్తం — రెండు గ్రంథాలు! చాంద్ బర్దాయి అంటే పృథ్వీరాజ్ రాసో. మెగస్తనీస్ అంటే ఇండికా అంటే చంద్రగుప్త మౌర్య ఆస్థానం. అజ్ఞాత నావికుడు అంటే పెరిప్లస్ ఆఫ్ ది ఎరిత్రియన్ సీ. ప్లీని అంటే నాచురల్ హిస్టరీ లాటిన్. ఫాహియాన్ అంటే ఫో-కువో-కి అంటే రెండవ చంద్రగుప్తుడు అంటే మొదటి చైనా యాత్రికుడు. హ్యూయెన్ త్సాంగ్ అంటే సి-యు-కి అంటే హర్షవర్ధనుడు అంటే King of Travellers. అల్-బెరూని అంటే కితాబ్-ఉల్-హింద్ అంటే Founder of Indology అంటే Father of Comparative Religion. తారానాథ్ అంటే The History of Tibet అంటే అశోకుడు. దీపవంశ మరియు మహావంశ అంటే శ్రీలంక పాళీ భాష మౌర్యుల సమాచారం. శాసనాల 4 రకాలు: రాజాజ్ఞలు అంటే అశోకుడు. అంకిత. దాన. స్మారక. మళ్ళీ — రాజాజ్ఞలు, అంకిత, దాన, స్మారక! కాల నిర్ధారణ పద్ధతులు: C 14 అంటే లిబ్బి. K-A అంటే మెక్‌డూగల్. థర్మో అంటే ఇటికిన్స్ అంటే కుండలు. డెండ్రో అంటే చెట్ల వలయాలు. వాస్తు శైలులు: నగరశైలి అంటే ఉత్తరం. ద్రావిడ అంటే దక్షిణం. వేసర అంటే కలయిక. ముఖ్య పదాలు: ఎపిగ్రఫీ అంటే శాసన అధ్యయనం. పేలియోగ్రఫీ అంటే ప్రాచీన లిపులు. న్యూమిస్మాటిక్స్ అంటే నాణేల అధ్యయనం. ఇకనోగ్రఫీ అంటే శిల్పకళ అధ్యయనం. మొదటి సంస్కృత శాసనం అంటే రుద్రదమనుడి జునాఘడ్ శాసనం. మొదటి కుమ్మరి చక్రం అంటే మెహర్గర్. అగ్రహార పదం మొదటి ప్రయోగం అంటే నలంద తామ్ర శాసనం గుప్తుల కాలం. అభినందనలు! అధ్యాయం 1 పూర్తిగా చదివారు. శుభాకాంక్షలు!"
        }
    ]

    db_exec(conn, '''
        INSERT INTO study_notes
        (subject, topic, subtopic, chapter_num, chapter_title_te, chapter_title_en, pages_ref, sections_json)
        VALUES (?,?,?,?,?,?,?,?)
    ''', ('GK', 'Indian_History', 'Ancient', 1, 'చరిత్ర – పరిచయం',
          'Introduction to History', '1-6', json.dumps(ch1_sections, ensure_ascii=False)))
    conn.commit()
    conn.close()
    return jsonify({'success': True, 'message': 'Chapter 1 seeded with 17 sections successfully'})


# ─────────────────────────────────────────────
# ART & CULTURE — CHAPTER 1 SEED (Notes)
# ─────────────────────────────────────────────

@app.route('/api/notes/seed_ac1', methods=['POST'])
def notes_seed_ac1():
    """Seed Art & Culture Ch1 — GK / Art_Culture. Add ?force=1 to overwrite."""
    force = request.args.get('force', '0') == '1'
    conn = get_db()
    # Ensure study_notes table exists (handles older Railway deployments)
    if USE_POSTGRES:
        cur0 = conn.cursor()
        cur0.execute('''CREATE TABLE IF NOT EXISTS study_notes (
            id SERIAL PRIMARY KEY,
            subject TEXT NOT NULL, topic TEXT NOT NULL,
            chapter_num INTEGER NOT NULL,
            chapter_title_te TEXT NOT NULL, chapter_title_en TEXT NOT NULL,
            pages_ref TEXT DEFAULT '', sections_json TEXT NOT NULL DEFAULT '[]',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )''')
        conn.commit(); cur0.close()
    else:
        conn.execute('''CREATE TABLE IF NOT EXISTS study_notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            subject TEXT NOT NULL, topic TEXT NOT NULL,
            chapter_num INTEGER NOT NULL,
            chapter_title_te TEXT NOT NULL, chapter_title_en TEXT NOT NULL,
            pages_ref TEXT DEFAULT '', sections_json TEXT NOT NULL DEFAULT '[]',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )''')
        conn.commit()
    cur = db_exec(conn, "SELECT id FROM study_notes WHERE subject='GK' AND topic='Art_Culture' AND chapter_num=1")
    if cur.fetchone():
        if not force:
            conn.close()
            return jsonify({'message': 'Already seeded. Use ?force=1 to overwrite.'})
        db_exec(conn, "DELETE FROM study_notes WHERE subject='GK' AND topic='Art_Culture' AND chapter_num=1")
        conn.commit()

    ac1_sections = [
        {
            "title": "పరిచయం — వాస్తుశిల్పం, శిల్పకళ, కుండల కళ",
            "sub": "Introduction · Architecture · Sculpture · Pottery",
            "audio": """స్వాగతం! మీరు ఇప్పుడు Art and Culture — అధ్యాయం 1 వినబోతున్నారు. అంశం: భారతీయ వాస్తుశిల్పం, శిల్పకళ మరియు కుండల కళ.

మొదటి ప్రశ్న — వాస్తుశిల్పం, శిల్పకళ, కుండల కళ — ఇవి ఒక్కటేనా? కాదు! మూడూ వేర్వేరు కళారూపాలు.

వాస్తుశిల్పం (Architecture) అంటే — భవనాలను అందంగా, పటిష్టంగా నిర్మించే కళ. ఉదాహరణ: తాజ్ మహల్, ఖజురాహో, ఎర్రకోట.

శిల్పకళ (Sculpture) అంటే — రాయి, లోహం, మట్టితో మూడు పరిమాణాల (3D) కళాకృతులు చేయడం. ఒకే వస్తువు వాడతారు — రాయి, కంచు, లేదా దంతం. ఉదాహరణ: నటరాజు, నాట్యకత్తె, గాంధార బుద్ధుడు.

కుండల కళ (Pottery) అంటే — మట్టిని అచ్చులో వేసి అధిక ఉష్ణోగ్రతలో కాల్చి పాత్రలు, విగ్రహాలు తయారు చేయడం. మూడు రకాలు — Earthenware, Stoneware, Porcelain.

EXAM ALERT! వాస్తుశిల్పానికి గణితం, ఇంజినీరింగ్ అవసరం. శిల్పకళకు సృజనాత్మకత ముఖ్యం. కుండల కళకు అధిక ఉష్ణోగ్రత కాల్చడం అవసరం. ఈ తేడాలు పరీక్షలో నేరుగా వస్తాయి!

Mini Recap: Architecture = భవన నిర్మాణం. Sculpture = 3D కళాకృతి. Pottery = మట్టి కాల్చిన కళ. ఈ మూడు మాటలు గుర్తుంచుకోండి!"""
        },
        {
            "title": "ప్రాచీన భారత వాస్తుశిల్పం వర్గీకరణ",
            "sub": "Classification · 5 Periods · Harappan to South Indian",
            "audio": """ప్రాచీన భారత వాస్తుశిల్పాన్ని 5 కాలాలలో వర్గీకరించారు. ఈ 5 కాలాలు గుర్తుపెట్టుకుంటే మొత్తం చరిత్ర అర్థమవుతుంది!

ఒకటి: హరప్పా కళ (Harappan Art) — 3300 BCE నుండి 1500 BCE వరకు. భారతదేశపు మొదటి పట్టణ నాగరికత.

రెండు: మౌర్య కళ (Mauryan Art) — 322 BCE నుండి 185 BCE వరకు. అశోకుని కాలంలో అత్యుత్తమ స్థాయి.

మూడు: మౌర్యానంతర కళ (Post-Mauryan Art) — 200 BCE నుండి 300 CE వరకు. గాంధార, మథుర, అమరావతి పాఠశాలలు.

నాలుగు: గుప్త కళ (Gupta Art) — 4వ నుండి 6వ శతాబ్దం CE వరకు. భారతదేశపు స్వర్ణ యుగం — అజంతా, ఎల్లోరా ఈ కాలంలోనే!

అయిదు: దక్షిణ భారత దేవాలయ వాస్తుశిల్పం (South Indian Temple Architecture) — పల్లవులు, చోళులు, హోయ్సళులు, విజయనగర.

Call and Response: మొదటి పట్టణ నాగరికత ఏది? — హరప్పా! స్వర్ణ యుగం ఏ కాలం? — గుప్త కాలం! అమరావతి పాఠశాల ఏ కాలంలో ఉద్భవించింది? — మౌర్యానంతర కాలం!

Master Formula: H–M–PM–G–T అని గుర్తుంచుకోండి. హరప్పా, మౌర్య, Post-Mauryan, గుప్త, Temple Styles — ఈ క్రమంలో చరిత్ర నడుస్తుంది!"""
        },
        {
            "title": "హరప్పా నగర ప్రణాళిక మరియు వాస్తుశిల్పం",
            "sub": "Harappan Town Planning · Grid · Great Bath · Granary · Dockyard",
            "audio": """హరప్పా నాగరికత — హరప్పా నాగరికత — హరప్పా నాగరికత! 3300 BCE నుండి 1500 BCE వరకు. దీన్నే సింధూ నది నాగరికత లేదా భారతదేశపు మొదటి పట్టణ నాగరికత అంటారు.

ముఖ్య స్థలాలు: హరప్పా (పాకిస్తాన్‌లో రావి నది ఒడ్డున), మొహెంజో-దారో (సింధు నది ఒడ్డున), మరియు లోథాల్ (గుజరాత్).

నగర ప్రణాళిక విశేషాలు: మొదటిది — Grid Pattern. వీధులు తూర్పు-పడమర, ఉత్తర-దక్షిణ దిశలలో నేరుగా కొట్టవచ్చిన గీతల వలె ఉంటాయి. రెండవది — రెండు భాగాలు: పై కోట (Citadel) — పాలకులకు, కింద పట్టణం (Lower Town) — సామాన్య ప్రజలకు.

EXAM ALERT! కాల్చిన ఇటుకలు (Burnt Bricks) ప్రధాన నిర్మాణ వస్తువు. ఇటుక పరిమాణాల నిష్పత్తి 4:2:1 — ఇది ఆనాటి ప్రమాణీకరణకు నిదర్శనం!

మహా స్నాన కుండం (Great Bath) — మహా స్నాన కుండం — మహా స్నాన కుండం! మొహెంజో-దారోలో ఉంది. మొత్తం ప్రపంచంలో ఇది మొట్టమొదటి స్నానపు కుండం. పొడవు 12 మీటర్లు, వెడల్పు 7 మీటర్లు, లోతు 2.4 మీటర్లు. నీరు చొరబడకుండా Bitumen (బిటుమెన్) అంటించారు — మత ప్రయోజనాల కోసం వాడేవారు!

మురుగు వ్యవస్థ (Drainage System) — ప్రతి ఇంటికి మురుగుకాలువ ఉండేది. భూమి కింద కప్పబడిన కాలువలు — ఆ కాలంలోనే ఇంత అభివృద్ధి!

లోథాల్ — లోథాల్ — లోథాల్! గుజరాత్‌లో ఉంది. భారతదేశపు మొదటి నౌకాశ్రయం (First Dockyard)! ఇది పరీక్షలో తరచుగా అడుగుతారు.

Mini Recap: Grid, Burnt Bricks, Drainage, Citadel + Lower Town, Granaries, Great Bath, Dockyard — ఈ 7 మాటలు హరప్పా గురించి ఏ ప్రశ్నకైనా సమాధానం!"""
        },
        {
            "title": "హరప్పా శిల్పాలు, ముద్రలు మరియు కుండలు",
            "sub": "Dancing Girl · Priest King · Male Torso · Seals · Pottery",
            "audio": """హరప్పా శిల్పాలలో మూడు అత్యంత ముఖ్యమైనవి పరీక్షలో వస్తాయి!

మొదటిది: నాట్యకత్తె (Dancing Girl) — నాట్యకత్తె — నాట్యకత్తె! మొహెంజో-దారోలో లభించింది. కేవలం 4 అంగుళాల ఎత్తు. కంచు (Bronze) తో తయారు చేశారు. మైనపు పోత పద్ధతి (Lost Wax / Cire Perdue) లో తయారు చేశారు. ఎడమ చేతిపై మోచేయి వరకు గాజులు, నిలువు త్రిభంగ భంగిమలో నిలబడి ఉంటుంది!

EXAM ALERT! మైనపు పోత పద్ధతి అంటే: ముందు మైనంతో శిల్పం చేస్తారు → మట్టితో కప్పుతారు → నిప్పులో వేస్తే మైనం కరిగిపోతుంది → ఆ ఖాళీలో కరిగిన కంచు పోస్తారు → చల్లారిన తర్వాత మట్టి పగులగొడతారు → శిల్పం తయారు!

రెండవది: పూజారి రాజు (Priest King) — పూజారి రాజు — పూజారి రాజు! మొహెంజో-దారోలో లభించింది. స్టీటైట్ (Steatite) రాయిలో తయారు. శాలువాపై త్రిపర్ణ (Trefoil) నమూనా — పరీక్షలో ఈ నమూన పేరు అడుగుతారు!

మూడవది: పురుష మేను (Male Torso) — హరప్పాలో లభించింది. ఎర్ర ఇసుక రాయి (Red Sandstone). మెడపై, భుజాలపై రంధ్రాలు — తల, చేతులు వేర్వేరుగా తయారు చేసి అమర్చేవారు!

ముద్రలు (Seals): మొత్తం 2000 పైగా ముద్రలు లభించాయి. ముఖ్యంగా స్టీటైట్ రాయిలో. ముద్రలపై రాత — చిత్రలిపి (Pictographic) — ఇంకా అర్థం కాలేదు! రాత కుడి వైపు నుండి ఎడమ వైపుకు చదువుతారు. అత్యంత సాధారణ జంతువు — ఏకశృంగి (Unicorn)!

కుండలు: రెండు రకాలు — సాదా కుండలు (ధాన్యం నిల్వకు) మరియు చిత్రిత కుండలు (ఎర్ర నేపథ్యంపై నల్ల రంగు — Black on Red)!

Mini Recap: Dancing Girl = Bronze + Lost Wax + Mohenjo-daro. Priest King = Steatite + Trefoil + Mohenjo-daro. Male Torso = Red Sandstone + Harappa. Seals = Steatite + Pictographic + Unicorn + Undeciphered!"""
        },
        {
            "title": "మౌర్య కళ పరిచయం — అశోకుని కళాత్మక విప్లవం",
            "sub": "Mauryan Art · 322–185 BCE · Court Art vs Popular Art",
            "audio": """మౌర్య కళ — మౌర్య కళ — మౌర్య కళ! కాలం: 322 BCE నుండి 185 BCE వరకు. ముఖ్య పాలకులు: చంద్రగుప్త మౌర్యుడు, బిందుసారుడు, అశోకుడు.

ఒక నిమిషం ఆగండి — మౌర్య కళ అర్థం చేసుకోవాలంటే అశోకుని కథ తెలుసుకోవాలి!

అశోకుడు (273–232 BCE) మొదట్లో యుద్ధప్రియుడు. 261 BCE లో కళింగ యుద్ధంలో లక్షల మంది చనిపోవడం చూసి మనసు విరిగింది. బౌద్ధమతం స్వీకరించాడు. తర్వాత ఏం చేశాడు? బౌద్ధ ధర్మాన్ని ప్రజలకు చేర్చడానికి స్తంభాలపై శాసనాలు చెక్కించాడు, స్తూపాలు నిర్మించాడు, సన్యాసులకు గుహలు కేటాయించాడు. అందుకే మౌర్య కళ = అశోకుని కళ!

మౌర్య కళ రెండు రకాలు:
మొదటిది — రాజాశ్రయ కళ (Court Art): రాజులు నిర్మించిన స్తంభాలు, స్తూపాలు, గుహలు, రాజభవనాలు — రాజకీయ మరియు మత ప్రయోజనాల కోసం.

రెండవది — జన కళ (Popular Art): సామాన్య ప్రజల కళ — యక్ష, యక్షి విగ్రహాలు, NBPW కుండలు — దైనందిన జీవితాన్ని ప్రతిబింబిస్తాయి.

EXAM ALERT! మొహెంజో-దారో తర్వాత పాటలీపుత్ర (ఇప్పటి Patna, Bihar) మౌర్య రాజధాని. చంద్రగుప్తుని రాజభవనం అక్కడ ఉండేది. గ్రీకు రాయబారి మెగస్తనీస్ దాన్ని చూసి అద్భుతంగా ఉందని రాశాడు!"""
        },
        {
            "title": "అశోకుని స్తంభాలు — జాతీయ చిహ్నానికి మూలం",
            "sub": "Ashokan Pillars · Sarnath Lion Capital · National Emblem",
            "audio": """అశోకుని స్తంభాలు — అశోకుని స్తంభాలు — అశోకుని స్తంభాలు! ఇవి పరీక్షలో అత్యంత ముఖ్యమైన అంశం!

స్తంభ నిర్మాణం 4 భాగాలలో ఉంటుంది:
ఒకటి — దండం (Shaft): ఒకే రాతి ముక్కతో (Monolith) చేసిన దండం. చునార్ ఇసుక రాయి. 40 నుండి 50 అడుగుల ఎత్తు! చాలా మెరుగు పెట్టబడింది.

రెండు — అగ్రభాగం (Capital): పై భాగంలో జంతు విగ్రహాలు — సింహం, ఎద్దు, ఏనుగు, గుర్రం.

మూడు — Abacus: అగ్రభాగం కింద అందమైన భాగం. పూలు, జంతువులు, రేఖాగణిత నమూనాలు. ఇక్కడ పర్షియన్ ప్రభావం కనిపిస్తుంది.

నాలుగు — Finial: అత్యంత పైన తలక్రిందుల తామర పూల ఆకారం లేదా గంట ఆకారం.

EXAM ALERT! సారనాథ్ సింహ స్తంభం (Sarnath Lion Capital) — సారనాథ్ సింహ స్తంభం — ఇది భారతదేశపు జాతీయ చిహ్నం (National Emblem)! ఇందులో 4 సింహాలు వీపు వీపు ఆనించి నిలబడి ఉంటాయి. కింద Abacus పై 4 జంతువులు — సింహం, ఏనుగు, గుర్రం, ఎద్దు — మరియు 4 ధర్మ చక్రాలు ఉన్నాయి. పైన పెద్ద ధర్మ చక్రం ఉంది — ఇదే జాతీయ జెండాలోని అశోక చక్రం!

Call and Response: జాతీయ చిహ్నం ఏ స్తంభం నుండి వచ్చింది? — సారనాథ్ సింహ స్తంభం! స్తంభాలు దేనితో తయారు చేశారు? — చునార్ ఇసుక రాయి! స్తంభాల దండం ఎలా చేశారు? — ఏకశిల (Monolith)!"""
        },
        {
            "title": "మౌర్య స్తంభాలు vs పర్షియన్ స్తంభాలు + స్తూపాలు",
            "sub": "Pillar Comparison · Sanchi Stupa · Stupa Parts",
            "audio": """మౌర్య స్తంభాలు vs పర్షియన్ స్తంభాలు — ఈ పోలిక పరీక్షలో తరచుగా వస్తుంది!

మౌర్య స్తంభాల విశేషాలు: దండం ఏకశిల (ఒకే రాయి ముక్క). నున్నగా, సరళంగా ఉంటుంది. దండంపై Capital figure ఉండదు. శాసనాలు మొదట మూడో పురుషంలో, తర్వాత మొదటి పురుషంలో మారతాయి.

పర్షియన్ స్తంభాల విశేషాలు: దండం అనేక రాయి ముక్కలను పేర్చి చేస్తారు. దండంపై నిలువు పాళ్ళు (Fluted surface). నిర్మాణ నమూనా చాలా క్లిష్టంగా ఉంటుంది.

Memory Trick: మౌర్య = MONO-SMOOTH. పర్షియన్ = MULTI-FLUTED!

ఇప్పుడు స్తూపాలు — స్తూపాలు — స్తూపాలు! స్తూపం అంటే బౌద్ధ మహాపురుషుల అస్తికలు పాతిపెట్టి, దానిపైన నిర్మించిన పవిత్రమైన కట్టడం.

స్తూపం 6 భాగాలు: అండ (Anda) — అర్ధగోళాకార గుమ్మటం, ఆకాశాన్ని సూచిస్తుంది. హర్మిక (Harmika) — పైన చతుర్భుజాకార రాతి కంచె, దేవతల నివాసం. యష్టి (Yasti) — మధ్యలో కొనగోలు కర్ర, విశ్వ అక్షం. ఛత్రం (Chattra) — 3 గొడుగులు, బౌద్ధమతపు 3 రత్నాలు: బుద్ధ, ధర్మ, సంఘ. మేధి (Medhi) — ప్రదక్షిణ చేయడానికి వేదిక. తోరణం (Torana) — 4 దిక్కులలో అలంకారమైన ద్వారాలు, జాతక కథలు చెక్కారు.

EXAM ALERT! సాంచి స్తూపం (Sanchi Stupa) — సాంచి స్తూపం — మధ్యప్రదేశ్‌లో ఉంది. అశోకుడు నిర్మించాడు. పురాతన రాతి స్తూపం! UNESCO వారసత్వ స్థలం! నాలుగు తోరణాలు అత్యంత అలంకారమైనవి!"""
        },
        {
            "title": "మౌర్య గుహలు + యక్ష శిల్పాలు + NBPW కుండలు",
            "sub": "Barabar Caves · Yaksha Yakshi · NBPW Pottery",
            "audio": """మౌర్య గుహలు — మొదటి రాతి గుహలు! బరాబర్ గుహలు (Barabar Caves) — బిహార్‌లో ఉన్నాయి. దశరథుడు (అశోకుని మనవడు) నిర్మించాడు. భారతదేశంలో పురాతన రాతి గుహలు ఇవే!

EXAM ALERT! బరాబర్ గుహలు బౌద్ధులకు కాదు — ఆజీవకులకు (Ajivikas) కేటాయించారు! ఇది పరీక్షలో ట్రిక్ ప్రశ్నగా వస్తుంది! గుహ లోపల గోడలు అద్దంలా మెరిసేవి — Mauryan Polish అంటారు!

యక్ష, యక్షి శిల్పాలు (Yaksha, Yakshi): జన కళకు చెందిన శిల్పాలు. యక్షులు, యక్షిణులు అంటే ప్రకృతి దేవతలు. ముఖ్యమైనది: దీదార్‌గంజ్ యక్షి (Didarganj Yakshi) — పాటలీపుత్రలో లభించింది. సారనాథ్ ఇసుక రాయిలో తయారు. Mauryan Polish అద్భుతంగా ఉంటుంది!

NBPW కుండలు (Northern Black Polished Ware) — NBPW — NBPW! ఉత్తర నల్ల మెరుపు కుండలు. మౌర్య కాలానికి చెందిన ప్రత్యేక కుండలు. నల్లగా, అద్దంలా మెరుస్తాయి. వ్యాపారులు, ఉన్నత వర్గాలు వాడేవారు. ఇవి మౌర్య కాలానికి గుర్తింపు ముద్ర!

Mini Recap: మౌర్య కళ = స్తంభాలు + స్తూపాలు + గుహలు + యక్ష శిల్పాలు + NBPW కుండలు. అన్నీ అశోకుని కాలం (273–232 BCE) లోనే అభివృద్ధి చెందాయి!"""
        },
        {
            "title": "మౌర్యానంతర కళ — గాంధార పాఠశాల",
            "sub": "Post-Mauryan · 200 BCE–300 CE · Gandhara School · Greek Influence",
            "audio": """మౌర్యానంతర కళ (Post-Mauryan Art) — మౌర్యానంతర కళ! కాలం: 200 BCE నుండి 300 CE వరకు. ముఖ్య వంశాలు: శుంగులు, కుషాన్లు, శాతవాహనులు.

ఈ కాలంలో అత్యంత ముఖ్యమైన విషయం ఏమిటంటే — బుద్ధుని మొదటిసారి మానవ రూపంలో చిత్రించడం ఇక్కడే మొదలైంది! మౌర్య కాలంలో బుద్ధుని చిహ్నాల ద్వారా చూపించేవారు. ఇప్పుడు మొదటిసారి మూడు మహా పాఠశాలలు ఉద్భవించాయి!

గాంధార పాఠశాల (Gandhara School) — గాంధార పాఠశాల — గాంధార పాఠశాల!

ప్రదేశం: వాయువ్య సరిహద్దు — పాకిస్తాన్, అఫ్ఘానిస్తాన్.
పాలకులు: కుషాన్ రాజులు.
వస్తువు: బూడిద/నీలి-బూడిద స్కిస్ట్ రాయి (Grey/Blue-grey Schist).
ప్రభావం: గ్రీకు-రోమన్ (Hellenistic) ప్రభావం!

EXAM ALERT! గాంధార బుద్ధుని విశేషాలు: అలలు అలలు జుట్టు (Wavy hair) — గ్రీకు శైలి! బలమైన శరీరం (Muscular body). టోగా వంటి దుస్తులు. ముఖం గ్రీకు, ఆచారం భారతీయ — ఈ కలయిక గాంధార పాఠశాల ప్రత్యేకత!

Call and Response: గాంధార పాఠశాల ఎక్కడ ఉద్భవించింది? — పాకిస్తాన్, అఫ్ఘానిస్తాన్! గాంధార రాయి ఏది? — బూడిద స్కిస్ట్! ఏ ప్రభావం కనిపిస్తుంది? — గ్రీకు-రోమన్!"""
        },
        {
            "title": "మథుర మరియు అమరావతి పాఠశాలలు",
            "sub": "Mathura School · Amaravati School · AP Students Must Know",
            "audio": """మథుర పాఠశాల (Mathura School) — మథుర పాఠశాల — మథుర పాఠశాల!

ప్రదేశం: మథుర, ఉత్తరప్రదేశ్ — కృష్ణా నది ఒడ్డు.
పాలకులు: కుషాన్ రాజులు.
వస్తువు: మచ్చల ఎర్ర ఇసుక రాయి (Spotted Red Sandstone).
ప్రభావం: స్వదేశీ భారతీయ శైలి — బయటి ప్రభావం లేదు!

మథుర బుద్ధుని విశేషాలు: గుండు తల (Shaved head). భారతీయ ముఖ లక్షణాలు. అత్యంత ముఖ్యం — హిందూ, జైన, బౌద్ధ మూడు మతాల శిల్పాలు మథురలో తయారయ్యాయి!

అమరావతి పాఠశాల (Amaravati School) — అమరావతి పాఠశాల — అమరావతి పాఠశాల! ఆంధ్రప్రదేశ్ విద్యార్థులకు ఇది అత్యంత ముఖ్యం!

ప్రదేశం: కృష్ణా-గోదావరి డెల్టా, ఆంధ్రప్రదేశ్!
పాలకులు: శాతవాహన రాజులు.
వస్తువు: తెల్లటి పాలరాయి (White Marble)!
ప్రభావం: స్వతంత్రంగా అభివృద్ధి — బయట ప్రభావం లేదు!

EXAM ALERT! అమరావతి బుద్ధుని విశేషాలు: త్రిభంగ భంగిమ (Tribhanga posture) — శరీరం 3 చోట్ల వంగుతుంది! సన్నగా, అందంగా — దంతం వంటి సూక్ష్మ నాణ్యత. కదలికలతో కూడిన కథన శిల్పాలు (Dynamic and Narrative).

మూడు పాఠశాలల పోలిక: గాంధార = బూడిద రాయి + గ్రీకు శైలి. మథుర = ఎర్ర రాయి + స్వదేశీ + 3 మతాలు. అమరావతి = తెల్ల పాలరాయి + AP + త్రిభంగ!

Call and Response: అమరావతి పాఠశాల ఏ రాష్ట్రంలో? — ఆంధ్రప్రదేశ్! ఏ రాజులు పోషించారు? — శాతవాహనులు! అమరావతి వస్తువు ఏది? — తెల్ల పాలరాయి!"""
        },
        {
            "title": "గుప్త కళ — భారతదేశపు స్వర్ణ యుగం",
            "sub": "Gupta Period · 4th–6th CE · Golden Age · Dashavatara Temple · Sarnath Buddha",
            "audio": """గుప్త కళ — గుప్త కళ — గుప్త కళ! కాలం: 4వ నుండి 6వ శతాబ్దం CE. దీన్నే భారతదేశపు స్వర్ణ యుగం (Golden Age) అంటారు!

గుప్త కాలంలో శిల్పకళ అత్యున్నత స్థాయికి చేరింది. సారనాథ్ బుద్ధుడు (Sarnath Buddha) — సారనాథ్ బుద్ధుడు! చున్నార్ ఇసుక రాయి. ముఖంపై అపూర్వమైన శాంతి భావన. సన్నటి పారదర్శకమైన దుస్తులు. ఇది గుప్త శిల్పకళకు అత్యుత్తమ ఉదాహరణ!

గుప్త దేవాలయ వాస్తుశిల్పం: దశావతార దేవాలయం (Dashavatara Temple) — దశావతార దేవాలయం — దేవగఢ్, ఉత్తరప్రదేశ్! గుప్త దేవాలయ వాస్తుశిల్పానికి అత్యుత్తమ ఉదాహరణ. పంచాయతన శైలి — కేంద్ర మందిరం + 4 మూలల్లో 4 చిన్న మందిరాలు.

ఉదయగిరి గుహలు (Udayagiri Caves) — మధ్యప్రదేశ్! గుప్త కాలంలో అత్యంత ముఖ్యమైన గుహలు. గుహ 5లో వరాహ శిల్పం (Varaha relief) — విష్ణువు వరాహ అవతారంలో భూమిని రక్షిస్తున్న దృశ్యం!

EXAM ALERT! గుప్త కాలంలో మొదటిసారి హిందూ దేవాలయాలు రాయిలో నిర్మించబడ్డాయి. ముందు మట్టి, చెక్క దేవాలయాలే ఉండేవి. గుప్తులే రాతి దేవాలయ నిర్మాణం ప్రారంభించారు!

Mini Recap: గుప్త కళ = స్వర్ణ యుగం + సారనాథ్ బుద్ధుడు + దశావతార దేవాలయం + పంచాయతన శైలి + ఉదయగిరి వరాహ శిల్పం!"""
        },
        {
            "title": "అజంతా మరియు ఎల్లోరా గుహలు",
            "sub": "Ajanta 29 Caves · Ellora 34 Caves · UNESCO · Paintings vs Sculptures",
            "audio": """అజంతా — అజంతా — అజంతా! ఎల్లోరా — ఎల్లోరా — ఎల్లోరా! రెండూ మహారాష్ట్రలో ఉన్నాయి. రెండూ UNESCO వారసత్వ స్థలాలు. కానీ తేడాలు చాలా ఉన్నాయి!

అజంతా గుహలు: మొత్తం 29 గుహలు — 4 చైత్యాలు + 25 విహారాలు. కేవలం బౌద్ధ మత గుహలు మాత్రమే! కాలం: 2వ శతాబ్దం BCE నుండి 6వ శతాబ్దం CE. ఔరంగాబాద్ జిల్లా, వాఘోర నది ఒడ్డున. అజంతా ప్రత్యేకత — చిత్రలేఖనం (Paintings)! గోడలు, కప్పులపై చిత్రాలు. Fresco-secco పద్ధతిలో సున్నపు పూత పై చిత్రాలు.

EXAM ALERT! అజంతా అత్యంత ప్రసిద్ధ చిత్రాలు: గుహ 1 లో బోధిసత్వ పద్మపాణి (Bodhisattva Padmapani) — అజంతాలో అత్యంత ప్రసిద్ధమైన చిత్రం! గుహ 16 లో మరణిస్తున్న రాకుమారి (Dying Princess). రంగులు: ఎర్ర ఖనిజ రంగు, పసుపు, ఆకుపచ్చ, నీలి లాపిస్ రాయి, నల్ల దీప మసి.

ఎల్లోరా గుహలు: మొత్తం 34 గుహలు — 12 బౌద్ధ + 17 హిందూ + 5 జైన. మూడు మతాలు కలిసి ఉన్నాయి — మత సహనానికి చిహ్నం! కాలం: 5వ నుండి 11వ శతాబ్దం CE. ఎల్లోరా ప్రత్యేకత — శిల్పాలు మరియు వాస్తుశిల్పం!

కైలాశ దేవాలయం (Kailash Temple) — కైలాశ దేవాలయం — ఎల్లోరా గుహ 16! ప్రపంచంలో అతి పెద్ద ఏకశిలా రాతి దేవాలయం! రాష్ట్రకూట రాజు కృష్ణ I నిర్మించాడు!

Call and Response: అజంతా అంటే? — చిత్రాలు (Paintings)! ఎల్లోరా అంటే? — శిల్పాలు (Sculptures)! అజంతాలో ఎన్ని మతాలు? — ఒకే ఒక్కటి — బౌద్ధం! ఎల్లోరాలో? — మూడు మతాలు!"""
        },
        {
            "title": "హిందూ దేవాలయ భాగాలు",
            "sub": "Temple Parts · Garbhagriha · Shikhara · Mandapa · Gopuram · Torana",
            "audio": """హిందూ దేవాలయం కేవలం పూజా స్థలం మాత్రమే కాదు — అది ఒక సంపూర్ణ విశ్వ నమూనా (Cosmic Symbol)!

దేవాలయం పర్వతాన్ని సూచిస్తుంది — మేరు పర్వతాన్ని! శిఖరం పైకి వెళ్ళే కొద్దీ సన్నబడటం — మనిషి నుండి దేవుని వైపు ప్రయాణాన్ని సూచిస్తుంది. లోపలి గర్భగృహం చీకటిగా ఉంటుంది — తల్లి గర్భాన్ని సూచిస్తుంది!

దేవాలయ ప్రధాన భాగాలు:
గర్భగృహం (Garbhagriha) — అంత:పురం: దేవాలయంలో అత్యంత పవిత్రమైన గది. ప్రధాన విగ్రహం ఇక్కడ ఉంటుంది. చీకటిగా, చతురస్రంగా ఉంటుంది. పురోహితుడు మాత్రమే ప్రవేశించగలడు!

శిఖరం / విమానం (Shikhara / Vimana) — గర్భగృహం పైన ఉన్న శిఖరం. ఉత్తర భారతదేశంలో శిఖరం — వంపు ఆకారం. దక్షిణ భారతదేశంలో విమానం — మెట్ల పిరమిడ్ ఆకారం!

మండపం (Mandapa) — గర్భగృహం ముందున్న స్తంభాల మండపం. పూజ, సంగీత, నృత్య కార్యక్రమాలు ఇక్కడ జరుగుతాయి.

గోపురం (Gopuram) — దక్షిణ భారత దేవాలయాల అలంకారమైన ప్రవేశ ద్వారం. విమానం కంటే ఎత్తుగా ఉండవచ్చు!

అంతరాళం (Antarala) — మండపం మరియు గర్భగృహం మధ్య సంధి స్థలం.

EXAM ALERT! వాహనం (Vahana) = దేవుని వాహనం — శివునికి నంది. జగతి (Jagati) = దేవాలయమంతా నిలబడే ఎత్తైన వేదిక!"""
        },
        {
            "title": "మూడు దేవాలయ శైలులు — నాగర, ద్రావిడ, వేసర",
            "sub": "Nagara · Dravida · Vesara · Key Differences",
            "audio": """మూడు దేవాలయ శైలులు — నాగర, ద్రావిడ, వేసర! ఈ మూడు పరీక్షలో తప్పకుండా వస్తాయి!

నాగర శైలి (Nagara Style) — ఉత్తర భారతదేశం. శిఖరం వంపు ఆకారంలో ఉంటుంది — పర్వతం వంటిది. సరిహద్దు గోడ (Compound Wall) ఉండదు. నీటి తొట్టి తప్పనిసరి కాదు. ఉదాహరణలు: ఖజురాహో (మధ్యప్రదేశ్), లింగరాజ (ఒడిశా). ఉప రకాలు: లతీన, వలభి, శేఖర.

ద్రావిడ శైలి (Dravida Style) — దక్షిణ భారతదేశం. విమానం మెట్ల పిరమిడ్ ఆకారంలో ఉంటుంది — చదునైన పైభాగం. గోపురం ఉంటుంది — విమానం కంటే ఎత్తుగా ఉండవచ్చు! ప్రాకారాలు (Compound Walls) తప్పనిసరి. పుష్కరిణి (Temple Tank) తప్పనిసరి! ఉదాహరణలు: బృహదీశ్వర (తంజావూర్), మీనాక్షి, తీర దేవాలయం.

వేసర శైలి (Vesara Style) — డెక్కన్ — కర్ణాటక, మహారాష్ట్ర. నాగర + ద్రావిడ మిశ్రమం! చాళుక్య శైలి అని కూడా అంటారు. ముఖ్య వంశాలు: చాళుక్యులు, హోయ్సళులు, రాష్ట్రకూటులు. ఉదాహరణలు: పట్టదకల్ దేవాలయాలు, హోయ్సళేశ్వర (హాలేబిడ్).

EXAM ALERT! Memory Trick: N–D–V = "North Curves, South Steps, Deccan Blends"!
నాగర = ఉత్తరం = వంపు శిఖరం = గోడ లేదు.
ద్రావిడ = దక్షిణం = మెట్ల విమానం = గోపురం + ప్రాకారం + పుష్కరిణి.
వేసర = డెక్కన్ = రెండింటి మిశ్రమం!

Call and Response: Gopuram ఏ శైలి ప్రత్యేకత? — ద్రావిడ! Curvilinear Shikhara ఏ శైలి? — నాగర! పుష్కరిణి ఏ శైలిలో తప్పనిసరి? — ద్రావిడ!"""
        },
        {
            "title": "పల్లవ వంశం — మహాబలిపురం మరియు తీర దేవాలయం",
            "sub": "Pallava Dynasty · Mahabalipuram · Shore Temple · Five Rathas",
            "audio": """పల్లవ వంశం — పల్లవ వంశం — పల్లవ వంశం! కాలం: 4వ నుండి 9వ శతాబ్దం CE. దక్షిణ భారతదేశపు దేవాలయ నిర్మాణ చరిత్రకు పల్లవులే పునాది!

మహాబలిపురం (Mahabalipuram / Mamallapuram) — తమిళనాడు. పల్లవుల అత్యంత ముఖ్యమైన స్థలం!

మహాబలిపురంలో మూడు అద్భుతాలు:
మొదటిది — పంచ రథాలు (Five Rathas) — పంచ రథాలు! 5 ఏకశిలా రాతి దేవాలయాలు. ప్రతి ఒక్కటీ ఒకే రాయి నుండి తొలిచారు! పాండవుల పేర్లు పెట్టారు — ధర్మరాజ, భీమ, అర్జున, నకుల-సహదేవ రథాలు.

రెండవది — తీర దేవాలయం (Shore Temple) — తీర దేవాలయం! సముద్ర ఒడ్డున నిలబడింది. దక్షిణ భారతదేశపు అత్యంత పురాతన స్వతంత్ర నిర్మిత రాతి దేవాలయం! UNESCO వారసత్వ స్థలం.

మూడవది — అర్జునుని తపస్సు (Arjuna's Penance) — ప్రపంచంలో అతి పెద్ద రాతి శిల్ప చిత్రణ!

EXAM ALERT! పల్లవ నిర్మాణ శైలి పరిణామం: రాతి గుహలు → ఏకశిలా రథాలు → స్వతంత్ర రాతి దేవాలయాలు! కాంచీపురం పల్లవ రాజధాని — కైలాసనాథ దేవాలయం అక్కడ అత్యంత పురాతనమైనది!

Call and Response: తీర దేవాలయం ఎక్కడ ఉంది? — మహాబలిపురం! పంచ రథాలు ఎవరి పేర్లు? — పాండవులు! పల్లవ రాజధాని ఏది? — కాంచీపురం!"""
        },
        {
            "title": "చోళ వంశం — బృహదీశ్వర దేవాలయం",
            "sub": "Chola Dynasty · Brihadeeswara · Raja Raja Chola · 216 ft · UNESCO",
            "audio": """చోళ వంశం — చోళ వంశం — చోళ వంశం! కాలం: 9వ నుండి 13వ శతాబ్దం CE. దక్షిణ భారత దేవాలయ నిర్మాణం చోళుల వద్ద గరిష్ట స్థాయికి చేరింది!

బృహదీశ్వర దేవాలయం (Brihadeeswara Temple) — బృహదీశ్వర దేవాలయం — తంజావూర్, తమిళనాడు! రాజ రాజ చోళ I నిర్మించాడు. పూర్తిగా గ్రానైట్ రాయితో నిర్మించారు. 1010 CE లో పూర్తయింది. UNESCO వారసత్వ స్థలం!

EXAM ALERT! అద్భుతమైన విశేషాలు:
విమానం 216 అడుగుల ఎత్తు — భారతదేశంలో అత్యంత ఎత్తైన విమానం!
మధ్యాహ్నం 12 గంటలకు విమానం నీడ నేలపై పడదు — ఇంజినీరింగ్ అద్భుతం!
పై కుంభం (Kumbam) దాదాపు 80 టన్నులు బరువు — యంత్రాలు లేకుండా ఎత్తారు!

గంగైకొండచోళపురం (Gangaikondacholapuram) — రాజేంద్ర చోళ I నిర్మించాడు — రాజ రాజ చోళ I కొడుకు. గంగా నది వరకు జయించిన విజయాన్ని జరుపుకున్నాడు. విమానం కొంచెం వంపుగా ఉంటుంది — బృహదీశ్వర కంటే తేడా!

నటరాజ దేవాలయం (Nataraja Temple) — చిదంబరం — మరొక ప్రసిద్ధ చోళ దేవాలయం.

Call and Response: బృహదీశ్వర దేవాలయం ఎవరు నిర్మించారు? — రాజ రాజ చోళ I! విమానం ఎత్తు? — 216 అడుగులు! ఏ రాయితో నిర్మించారు? — గ్రానైట్!"""
        },
        {
            "title": "హోయ్సళ మరియు విజయనగర వాస్తుశిల్పం",
            "sub": "Hoysala · Halebid · Star-shaped plan · Vijayanagara · Hampi · Musical Pillars",
            "audio": """హోయ్సళ వంశం (Hoysala Dynasty) — హోయ్సళ వంశం! కాలం: 11వ నుండి 14వ శతాబ్దం CE.

హోయ్సళేశ్వర దేవాలయం (Hoysaleswara Temple) — హాలేబిడ్, కర్ణాటక! రాజు విష్ణువర్ధన నిర్మించాడు. హోయ్సళ వంశపు ప్రత్యేక లక్షణం — నక్షత్రాకార (Stellate) నేలపై నమూనా! మొత్తం బయటి గోడ సూక్ష్మమైన సాబుసరాయి (Soapstone) చెక్కడాలతో నిండి ఉంటుంది. నిరంతర వరుసలలో ఏనుగులు, గుర్రాలు, దేవుళ్ళ శిల్పాలు!

చెన్నకేశవ దేవాలయం (Chennakeshava Temple) — బేలూర్. శాలభంజికలు (bracket figures) మరియు దర్పణ సుందరి (lady looking in mirror) శిల్పాలకు ప్రసిద్ధి!

EXAM ALERT! హోయ్సళ వంశం = స్టెల్లేట్ నమూనా + సాబుసరాయి చెక్కడాలు + హాలేబిడ్!

విజయనగర సామ్రాజ్యం (Vijayanagara Empire) — విజయనగర — విజయనగర! కాలం: 14వ నుండి 17వ శతాబ్దం CE. హంపి (Hampi) — కర్ణాటక. UNESCO వారసత్వ స్థలం. మొఘలుల ముందు అతి పెద్ద సామ్రాజ్య నగరం!

విఠల దేవాలయం (Vittala Temple) — విఠల దేవాలయం! హంపిలో ఉంది. సంగీత స్తంభాలు (Musical Pillars) — తాకితే సంగీత స్వరాలు వస్తాయి! ముందు రాతి రథం (Stone Chariot) ఉంటుంది — హంపి చిహ్నం!

Call and Response: సంగీత స్తంభాలు ఏ దేవాలయంలో ఉన్నాయి? — విఠల దేవాలయం, హంపి! హోయ్సళ ప్రత్యేక నమూనా ఏది? — నక్షత్రాకారం (Stellate)! హంపి ఏ వంశానికి రాజధాని? — విజయనగర సామ్రాజ్యం!"""
        },
        {
            "title": "మధ్యకాలీన వాస్తుశిల్పం — ఇండో-ఇస్లామిక్ శైలి + ఢిల్లీ సుల్తానేట్",
            "sub": "Medieval · Indo-Islamic · Arcuate Style · Qutb Minar · Delhi Sultanate",
            "audio": """మధ్యకాలీన వాస్తుశిల్పం — 11వ శతాబ్దంలో ఇస్లామిక్ శైలి భారతదేశంలోకి వచ్చింది. ఇండో-ఇస్లామిక్ శైలి ఉద్భవించింది — రెండు సంస్కృతుల అద్భుతమైన కలయిక!

హిందూ శైలి (Trabeate) vs ఇస్లామిక్ శైలి (Arcuate):
హిందూ శైలిలో: నిలువు స్తంభాలపై అడ్డ రాళ్ళు పేర్చేవారు. ఆర్చ్ ఉండదు. మానవ, జంతు చిత్రాలు ఉంటాయి.
ఇస్లామిక్ శైలిలో: ఆర్చ్ మరియు గుమ్మటాలు. రేఖాగణిత నమూనాలు (Arabesque). మినార్లు (Minarets) — నమాజ్ పిలుపు కోసం. Pietra Dura — పాలరాయిలో రత్నాలు పొదగడం. Charbagh — 4 భాగాల పర్షియన్ తోట.

EXAM ALERT! కుతుబ్ మినార్ (Qutb Minar) — కుతుబ్ మినార్ — కుతుబ్ మినార్! ఢిల్లీలో ఉంది. 73 మీటర్ల ఎత్తు. కుతుబ్-ఉద్-దీన్ ఐబక్ 1 అంతస్తు నిర్మించాడు. ఇల్తుత్మిష్ 3 అంతస్తులు పూర్తి చేశాడు. ఫిరూజ్ షా తుఘ్లక్ చివరి 2 అంతస్తులు కట్టాడు. ఎర్ర ఇసుక రాయి + పాలరాయి. UNESCO వారసత్వ స్థలం! భారతదేశంలో అత్యంత ఎత్తైన మినార్!

కువ్వత్-ఉల్-ఇస్లాం మసీదు (Quwwat-ul-Islam Mosque) — ఢిల్లీలో నిర్మించిన మొట్టమొదటి మసీదు!

Call and Response: కుతుబ్ మినార్ ఎత్తు? — 73 మీటర్లు! మొదట ఎవరు నిర్మించారు? — కుతుబ్-ఉద్-దీన్ ఐబక్! ఎన్ని అంతస్తులు? — 5!"""
        },
        {
            "title": "మొఘల్ వాస్తుశిల్పం మరియు ప్రాంతీయ శైలులు",
            "sub": "Mughal Architecture · Taj Mahal · Rajput · Sikh · Modern Architects",
            "audio": """మొఘల్ వాస్తుశిల్పం — మొఘల్ వాస్తుశిల్పం — భారత వాస్తుశిల్పంలో స్వర్ణ అధ్యాయం!

తాజ్ మహల్ (Taj Mahal) — తాజ్ మహల్ — తాజ్ మహల్! ఆగ్రా, ఉత్తరప్రదేశ్. షాజహాన్ తన భార్య ముంతాజ్ మహల్ స్మరణలో నిర్మించాడు. 1632 నుండి 1653 CE — 22 సంవత్సరాలు నిర్మించారు! మక్రానా పాలరాయి (Makrana Marble). ముఖ్య వాస్తుశిల్పి: ఉస్తాద్ అహ్మద్ లహౌరి! Pietra Dura పని అద్భుతంగా ఉంటుంది. Charbagh తోట నమూనా! UNESCO వారసత్వ స్థలం!

రాజపుత్ర వాస్తుశిల్పం: నాగర హిందూ శైలి + మొఘల్ అంశాలు. జరోఖాలు (overhanging balconies), ఛత్రులు (dome-shaped pavilions), జాలీలు (perforated stone screens). ముఖ్య కట్టడాలు: ఆంబర్ కోట (జైపూర్), మెహ్రాన్‌గఢ్ కోట (జోధ్‌పూర్), చిత్తోర్‌గఢ్ కోట.

సిక్కు వాస్తుశిల్పం: మొఘల్ + రాజపుత్ర ప్రభావం. చెక్కిన వంపు అలంకారాలు. పితల, రాగి పలకలు అలంకారానికి. ముఖ్యంగా పంజాబ్ ప్రాంతంలో.

EXAM ALERT! ఆధునిక వాస్తుశిల్పం: లారీ బేకర్ (Laurie Baker) — "పేదల వాస్తుశిల్పి"! స్థానిక వస్తువులు, Filler Slab పద్ధతి, కేరళలో పని చేశారు. బి.వి. దోషి (B.V. Doshi) — 2018లో ప్రిట్జ్కర్ పురస్కారం! భారతదేశంలో మొదటి ప్రిట్జ్కర్ విజేత! IIM బెంగళూరు నిర్మించారు. చండీగఢ్ — లే కర్బూజియే (Le Corbusier) నగర ప్రణాళిక — భారతదేశపు మొదటి ప్రణాళికాబద్ధ నగరం!

రాష్ట్రపతి భవన్ — ఎడ్విన్ లుట్యెన్స్ (Edwin Lutyens) నిర్మించారు. 340 గదులు. మొఘల్ + క్లాసికల్ + భారతీయ మిశ్రమ శైలి!"""
        },
        {
            "title": "అధ్యాయం సారాంశం — పరీక్ష ముఖ్యాంశాలు",
            "sub": "Chapter Recap · Master Formula · Must Remember",
            "audio": """అభినందనలు! Art and Culture అధ్యాయం 1 పూర్తి చేశారు! ఇప్పుడు అన్ని ముఖ్యాంశాలు ఒకే చోట పునశ్చరణ చేద్దాం!

Master Formula: H–M–PM–G–T–S–Me–Mo గుర్తుంచుకోండి:
హరప్పా → మౌర్య → మౌర్యానంతర → గుప్త → దేవాలయ శైలులు → దక్షిణ వంశాలు → మధ్యకాలం → ఆధునికం!

అత్యంత ముఖ్యమైన పాయింట్లు:
నాట్యకత్తె = కంచు + Lost Wax + మొహెంజో-దారో.
పూజారి రాజు = స్టీటైట్ + Trefoil + మొహెంజో-దారో.
ముద్రలు = స్టీటైట్ + చిత్రలిపి + ఏకశృంగి + అర్థం కాలేదు.
సారనాథ్ సింహ స్తంభం = జాతీయ చిహ్నం + అశోకుడు.
సాంచి స్తూపం = అశోకుడు + మధ్యప్రదేశ్ + UNESCO.
బరాబర్ గుహలు = ఆజీవకులకు + పురాతన రాతి గుహలు.
గాంధార = బూడిద రాయి + గ్రీకు ప్రభావం + పాకిస్తాన్.
మథుర = ఎర్ర రాయి + స్వదేశీ + 3 మతాలు.
అమరావతి = తెల్ల పాలరాయి + AP + శాతవాహనులు + త్రిభంగ.
అజంతా = 29 గుహలు + చిత్రాలు + కేవలం బౌద్ధం.
ఎల్లోరా = 34 గుహలు + శిల్పాలు + 3 మతాలు + కైలాశ దేవాలయం.
బృహదీశ్వరం = 216 అడుగులు + రాజ రాజ చోళ I + గ్రానైట్ + UNESCO.
హంపి విఠల దేవాలయం = సంగీత స్తంభాలు + రాతి రథం.
కుతుబ్ మినార్ = 73 మీటర్లు + ఐబక్ + UNESCO.
తాజ్ మహల్ = షాజహాన్ + ముంతాజ్ + 22 సంవత్సరాలు + మక్రానా పాలరాయి.
లారీ బేకర్ = పేదల వాస్తుశిల్పి.
బి.వి. దోషి = ప్రిట్జ్కర్ 2018 + మొదటి భారతీయుడు.

ట్రిక్ ప్రశ్నలు: కైలాసనాథ దేవాలయం = కాంచీపురం = పల్లవులు. కైలాశ దేవాలయం = ఎల్లోరా = రాష్ట్రకూటులు. ఈ రెండూ వేర్వేరు! అజంతాలో 3 మతాలా? లేదు — కేవలం బౌద్ధం! మధ్యాహ్నం తంజావూర్ విమానం నీడ పడదు — ఇది తరచుగా వస్తుంది!

మీరు ఈ అన్ని విషయాలు నేర్చుకున్నారు. AP High Court Section Officer 2026 పరీక్షలో ఈ అధ్యాయం నుండి అత్యధిక ప్రశ్నలు వస్తాయి. శుభాకాంక్షలు!"""
        }
    ]

    db_exec(conn, '''
        INSERT INTO study_notes
        (subject, topic, chapter_num, chapter_title_te, chapter_title_en, pages_ref, sections_json)
        VALUES (?,?,?,?,?,?,?)
    ''', ('GK', 'Art_Culture', 1,
          'భారతీయ వాస్తుశిల్పం, శిల్పకళ మరియు కుండల కళ',
          'Indian Architecture, Sculpture & Pottery',
          '1-40',
          json.dumps(ac1_sections, ensure_ascii=False)))
    conn.commit()
    conn.close()
    return jsonify({'success': True, 'message': f'Art & Culture Chapter 1 seeded with {len(ac1_sections)} sections successfully'})


# ─────────────────────────────────────────────
# CHAPTER MCQ ROUTES
# ─────────────────────────────────────────────

@app.route('/api/mcq/chapter/<int:chapter_id>')
def get_chapter_mcqs(chapter_id):
    """Return all MCQs for a chapter (shuffled)."""
    conn = get_db()
    cur = db_exec(conn, '''
        SELECT id, section_idx, difficulty, exam_type, q_te, opt_a, opt_b, opt_c, opt_d, correct, explanation_te
        FROM chapter_mcqs WHERE study_note_id=? ORDER BY section_idx, id
    ''', (chapter_id,))
    rows = [row_to_dict(r) for r in cur.fetchall()]
    conn.close()
    random.shuffle(rows)
    return jsonify({'mcqs': rows, 'count': len(rows)})


@app.route('/api/mcq/chapter/<int:chapter_id>/delete', methods=['POST'])
def delete_chapter_mcqs(chapter_id):
    conn = get_db()
    db_exec(conn, 'DELETE FROM chapter_mcqs WHERE study_note_id=?', (chapter_id,))
    conn.commit()
    conn.close()
    return jsonify({'success': True})


@app.route('/api/mcq/seed_ch1', methods=['POST'])
def seed_ch1_mcqs():
    """Seed all Chapter 1 MCQs. Add ?force=1 to overwrite."""
    try:
        return _seed_ch1_mcqs_inner()
    except Exception as exc:
        import traceback
        tb = traceback.format_exc()
        print("MCQ SEED ERROR:", tb)
        return jsonify({'success': False, 'error': str(exc), 'traceback': tb}), 500

def _seed_ch1_mcqs_inner():
    force = request.args.get('force', '0') == '1'
    conn = get_db()
    # Ensure chapter_mcqs table exists (handles deployments where init_db ran before this table was added)
    if USE_POSTGRES:
        cur0 = conn.cursor()
        cur0.execute('''CREATE TABLE IF NOT EXISTS chapter_mcqs (
            id SERIAL PRIMARY KEY,
            study_note_id INTEGER NOT NULL,
            section_idx INTEGER NOT NULL DEFAULT 0,
            difficulty INTEGER NOT NULL DEFAULT 1,
            q_te TEXT NOT NULL,
            opt_a TEXT NOT NULL,
            opt_b TEXT NOT NULL,
            opt_c TEXT NOT NULL,
            opt_d TEXT NOT NULL,
            correct TEXT NOT NULL,
            explanation_te TEXT NOT NULL DEFAULT '',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )''')
        conn.commit()
        cur0.close()
    else:
        conn.execute('''CREATE TABLE IF NOT EXISTS chapter_mcqs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            study_note_id INTEGER NOT NULL,
            section_idx INTEGER NOT NULL DEFAULT 0,
            difficulty INTEGER NOT NULL DEFAULT 1,
            q_te TEXT NOT NULL,
            opt_a TEXT NOT NULL,
            opt_b TEXT NOT NULL,
            opt_c TEXT NOT NULL,
            opt_d TEXT NOT NULL,
            correct TEXT NOT NULL,
            explanation_te TEXT NOT NULL DEFAULT '',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )''')
        conn.commit()
    # Get chapter 1 id
    cur = db_exec(conn, "SELECT id FROM study_notes WHERE subject='GK' AND topic='Indian_History' AND chapter_num=1")
    row = cur.fetchone()
    if not row:
        conn.close()
        return jsonify({'error': 'Chapter 1 not seeded yet. Seed notes first.'}), 400
    ch_id = row_to_dict(row)['id']

    cur2 = db_exec(conn, 'SELECT COUNT(*) as c FROM chapter_mcqs WHERE study_note_id=?', (ch_id,))
    count = row_to_dict(cur2.fetchone())['c']
    if count > 0 and not force:
        conn.close()
        return jsonify({'message': f'Already has {count} MCQs. Use ?force=1 to overwrite.'})
    if count > 0 and force:
        db_exec(conn, 'DELETE FROM chapter_mcqs WHERE study_note_id=?', (ch_id,))
        conn.commit()

    # ── ALL 61 MCQs ──
    # Format: (section_idx, difficulty, q_te, a, b, c, d, correct, explanation_te)
    mcqs = [
        # ── SECTION 0: Definitions ──
        (0, 1,
         "చరిత్ర (History) అంటే ఏమిటి?",
         "a) ఒక జీవన విధానం (A way of life)",
         "b) మానవ సమాజ పరిణామాన్ని వివరించే శాస్త్రం (Science explaining human society evolution)",
         "c) సంస్కృతిలో అభివృద్ధి దశ (Stage of development in culture)",
         "d) ప్రాచీన లిపుల అధ్యయనం (Study of ancient scripts)",
         "b",
         "చరిత్ర అంటే మానవ సమాజ ఆవిర్భావం, సంస్కృతి, నాగరికత, వ్యవస్థల పరిణామాన్ని వివరించే శాస్త్రం."),
        (0, 1,
         "నాగరికత (Civilisation) అంటే?",
         "a) ఒక జీవన విధానం (A way of life)",
         "b) మానవ పరిణామ శాస్త్రం (Science of human evolution)",
         "c) సంస్కృతిలో ప్రత్యేక అభివృద్ధి దశ (Special stage of development in culture)",
         "d) ప్రాచీన చరిత్ర అధ్యయనం (Study of ancient history)",
         "c",
         "సంస్కృతిలో ఒక ప్రత్యేకమైన అభివృద్ధి సాధించిన పరిణామ దశను నాగరికత అంటారు. సంస్కృతి = జీవన విధానం; నాగరికత = దాని ఉన్నత రూపం."),
        (0, 2,
         "కిందివాటిలో సరైన జత ఏది?",
         "a) చరిత్ర = జీవన విధానం",
         "b) సంస్కృతి = మానవ పరిణామ శాస్త్రం",
         "c) నాగరికత = సంస్కృతిలో అభివృద్ధి దశ (Civilisation = Stage of development in Culture)",
         "d) ఇండాలజీ = గ్రీకు చరిత్ర అధ్యయనం (Indology = Study of Greek history)",
         "c",
         "సరైన జతలు: చరిత్ర = మానవ పరిణామ శాస్త్రం; సంస్కృతి = జీవన విధానం; నాగరికత = సంస్కృతిలో అభివృద్ధి దశ."),

        # ── SECTION 1: Herodotus + Indology ──
        (1, 1,
         "'హిస్టరీ' పదం ఏ గ్రీకు పదం నుండి వచ్చింది?",
         "a) Herodotus (హెరోడోటస్)",
         "b) Historía (హిస్టోరియా)",
         "c) Indology (ఇండాలజీ)",
         "d) Epigraphy (ఎపిగ్రఫీ)",
         "b",
         "హిస్టరీ అనే పదం గ్రీకు భాషలోని Historía (హిస్టోరియా) నుండి వచ్చింది. అర్థం — పరిశోధించి తెలుసుకొనుట (Inquiry; Knowledge by investigation)."),
        (1, 1,
         "Father of History (చరిత్ర పితామహుడు) అని పిలవబడే వ్యక్తి ఎవరు?",
         "a) Sir William Jones (సర్ విలియం జోన్స్)",
         "b) Megasthenes (మెగస్తనీస్)",
         "c) Herodotus (హెరోడోటస్)",
         "d) Al-Biruni (అల్-బెరూని)",
         "c",
         "హెరోడోటస్ అనే గ్రీకు మహాపురుషుడిని Father of History అని పేర్కొంటారు. ఆయన రాసిన గ్రంథం పేరు 'The Histories'."),
        (1, 1,
         "హెరోడోటస్ రాసిన గ్రంథం పేరు?",
         "a) Indica (ఇండికా)",
         "b) The Histories (ది హిస్టరీస్)",
         "c) Natural History (నాచురల్ హిస్టరీ)",
         "d) Kitab-ul-Hind (కితాబ్-ఉల్-హింద్)",
         "b",
         "హెరోడోటస్ (Father of History) రాసిన గ్రంథం 'The Histories'. ఇందులో గ్రీకు-పర్షియన్ యుద్ధాలు మరియు ఆసియా సంస్కృతులు వర్ణించబడ్డాయి."),
        (1, 2,
         "భారత Indology పితామహుడు (Father of Indian Indology) ఎవరు?",
         "a) Herodotus (హెరోడోటస్)",
         "b) Megasthenes (మెగస్తనీస్)",
         "c) Al-Biruni (అల్-బెరూని)",
         "d) Sir William Jones (సర్ విలియం జోన్స్)",
         "d",
         "భారత చరిత్ర, సంస్కృతులు, భాష మరియు సాహిత్య అధ్యయనాన్ని Indology (ఇండాలజీ) అంటారు. భారత Indology పితామహుడిగా Sir William Jones ను పిలుస్తారు."),

        # ── SECTION 2: Religious Sources ──
        (2, 1,
         "జైన సాహిత్యానికి చెందిన గ్రంథం ఏది?",
         "a) Tripitakas (త్రిపిటకాలు)",
         "b) Jain Kalpasootra (జైన కల్పసూత్ర)",
         "c) Arthashastra (అర్థశాస్త్రం)",
         "d) Rigveda (ఋగ్వేదం)",
         "b",
         "Jain Kalpasootra జైన సాహిత్యానికి చెందింది. Tripitakas బౌద్ధ సాహిత్యానికి చెందుతాయి."),
        (2, 1,
         "బౌద్ధ సాహిత్యానికి చెందిన గ్రంథం ఏది?",
         "a) Jain Kalpasootra (జైన కల్పసూత్ర)",
         "b) Ashtadhyayi (అష్టాధ్యాయి)",
         "c) Milindapanna (మిలిందపన్న)",
         "d) Arthashastra (అర్థశాస్త్రం)",
         "c",
         "Milindapanna బౌద్ధ సాహిత్యానికి చెందింది. ఇది బౌద్ధ సన్యాసి నాగసేనుడు రచించాడు."),
        (2, 2,
         "కిందివాటిలో సరికానిది ఏది?",
         "a) Tripitakas — బౌద్ధ సాహిత్యం",
         "b) Jain Kalpasootra — జైన సాహిత్యం",
         "c) Milindapanna — వేద సాహిత్యం (Vedic literature)",
         "d) Aranyakas — వేద సాహిత్యం (Vedic literature)",
         "c",
         "Milindapanna వేద సాహిత్యానికి చెందినది కాదు. ఇది బౌద్ధ సాహిత్యానికి చెందుతుంది."),
        (2, 2,
         "వేద సాహిత్యంలో భాగం కానిది ఏది?",
         "a) Brahmanas (బ్రాహ్మణాలు)",
         "b) Aranyakas (అరణ్యకాలు)",
         "c) Kalpasootra (కల్పసూత్ర)",
         "d) Upanishads (ఉపనిషత్తులు)",
         "c",
         "Kalpasootra జైన సాహిత్యానికి చెందుతుంది, వేద సాహిత్యానికి కాదు. వేద సాహిత్యంలో వేదాలు, బ్రాహ్మణాలు, అరణ్యకాలు, ఉపనిషత్తులు, పురాణాలు వస్తాయి."),

        # ── SECTION 3: Main Secular Sources ──
        (3, 1,
         "అర్థశాస్త్రం (Arthashastra) రచయిత ఎవరు?",
         "a) Kalhana (కల్హణుడు)",
         "b) Kamandaka (కామందకుడు)",
         "c) Chanakya (చాణక్యుడు)",
         "d) Bana (బాణుడు)",
         "c",
         "అర్థశాస్త్రం చాణక్యుడు (కౌటిల్యుడు / విష్ణు గుప్తుడు) రచించాడు. ఇది మౌర్య పరిపాలనను వివరిస్తుంది."),
        (3, 1,
         "రాజతరంగిణి (Rajatarangini) రచయిత ఎవరు?",
         "a) Chanakya (చాణక్యుడు)",
         "b) Kalhana (కల్హణుడు)",
         "c) Bana (బాణుడు)",
         "d) Patanjali (పతంజలి)",
         "b",
         "రాజతరంగిణి కల్హణుడు రచించాడు. ఇది కాశ్మీరు రాజవంశాల చరిత్రను వివరిస్తుంది."),
        (3, 2,
         "చాణక్యుడి (Chanakya) ఇతర పేర్లు ఏవి?",
         "a) Kalhana మరియు Bana",
         "b) Kautilya (కౌటిల్యుడు) మరియు Vishnugupta (విష్ణు గుప్తుడు)",
         "c) Patanjali మరియు Gunadhyda",
         "d) Hala మరియు Kamandaka",
         "b",
         "చాణక్యుడికి Kautilya (కౌటిల్యుడు) మరియు Vishnugupta (విష్ణు గుప్తుడు) అని కూడా పేర్లు కలవు."),
        (3, 1,
         "హర్షచరిత్ర (Harshacharita) రచయిత ఎవరు?",
         "a) Kamandaka (కామందకుడు)",
         "b) Kalhana (కల్హణుడు)",
         "c) Chanakya (చాణక్యుడు)",
         "d) Bana (బాణుడు)",
         "d",
         "హర్షచరిత్ర బాణుడు రచించాడు. ఇది హర్షవర్ధనుని పరిపాలన విశేషాలను తెలియజేస్తుంది."),
        (3, 2,
         "నీతిసారం (Nitisara) గురించి సరైనది ఏది?",
         "a) Kalhana రచించాడు, మౌర్య పరిపాలన గురించి",
         "b) Kamandaka రచించాడు, గుప్తుల పరిపాలన గురించి",
         "c) Bana రచించాడు, హర్షవర్ధనుని గురించి",
         "d) Chanakya రచించాడు, రాజతరంగిణి అని పేరు",
         "b",
         "నీతిసారం Kamandaka (కామందకుడు) రచించాడు. ఇది గుప్తుల పరిపాలన అంశాలను వివరిస్తుంది."),

        # ── SECTION 4: 9 Other Secular Texts ──
        (4, 1,
         "మహాభాష్యం (Mahabhashya) రచయిత ఎవరు?",
         "a) Gunadhyda (గుణాఢ్యుడు)",
         "b) Patanjali (పతంజలి)",
         "c) Hala (హాలుడు)",
         "d) Vishakhadatta (విశాఖదత్తుడు)",
         "b",
         "మహాభాష్యం Patanjali (పతంజలి) రచించాడు. ఇది మౌర్యానంతర వంశాల గురించి వివరిస్తుంది."),
        (4, 1,
         "ముద్రారాక్షసం (Mudrarakshasa) రచయిత ఎవరు?",
         "a) Patanjali (పతంజలి)",
         "b) Gunadhyda (గుణాఢ్యుడు)",
         "c) Vishakhadatta (విశాఖదత్తుడు)",
         "d) Bilhana (బిల్హణుడు)",
         "c",
         "ముద్రారాక్షసం Vishakhadatta రచించాడు. ఇది మౌర్యవంశ స్థాపన గురించి వివరిస్తుంది."),
        (4, 3,
         "Vishakhadatta రాసిన రెండు గ్రంథాలు ఏవి?",
         "a) Mahabhashya మరియు Brihatkatha",
         "b) Mudrarakshasa (ముద్రారాక్షసం) మరియు Devichandraguptam (దేవీచంద్రగుప్తం)",
         "c) Prithviraj Vijayam మరియు Prithviraj Raso",
         "d) Gathasaptashati మరియు Koumudi Mahotsavam",
         "b",
         "Vishakhadatta ముద్రారాక్షసం (మౌర్యవంశ స్థాపన) మరియు దేవీచంద్రగుప్తం (గుప్తుల కాలం) రెండూ రాశాడు."),
        (4, 2,
         "పృథ్వీరాజ్ రాసో (Prithviraj Raso) రచయిత ఎవరు?",
         "a) Jayanaka (జయనకుడు)",
         "b) Bilhana (బిల్హణుడు)",
         "c) Chand Bardai (చాంద్ బర్దాయి)",
         "d) Vijjika (విజ్జికుడు)",
         "c",
         "పృథ్వీరాజ్ రాసో Chand Bardai రచించాడు. ఇది పృథ్వీరాజ్ చౌహాన్-3 గురించి."),
        (4, 2,
         "Brihatkatha మరియు Gathasaptashati రెండు గ్రంథాలు ఏ కాలానికి చెందినవి?",
         "a) Maurya period (మౌర్య కాలం)",
         "b) Satavahana period (శాతవాహన కాలం)",
         "c) Gupta period (గుప్త కాలం)",
         "d) Harsha period (హర్ష కాలం)",
         "b",
         "Brihatkatha (Gunadhyda) మరియు Gathasaptashati (Hala) రెండూ శాతవాహన కాలానికి చెందిన గ్రంథాలు."),
        (4, 3,
         "పృథ్వీరాజ్ చౌహాన్-3 గురించి రాసిన రెండు గ్రంథాల రచయితలు?",
         "a) Patanjali మరియు Gunadhyda",
         "b) Jayanaka (జయనకుడు) మరియు Chand Bardai (చాంద్ బర్దాయి)",
         "c) Bilhana మరియు Vijjika",
         "d) Vishakhadatta మరియు Hala",
         "b",
         "Prithviraj Vijayam (జయనకుడు) మరియు Prithviraj Raso (చాంద్ బర్దాయి) రెండూ పృథ్వీరాజ్ చౌహాన్-3 గురించి రాసిన గ్రంథాలు."),
        (4, 2,
         "కళ్యాణి చాళుక్య రాజు Tribhuvanamalla గురించి రాసిన గ్రంథం?",
         "a) Mudrarakshasa (ముద్రారాక్షసం)",
         "b) Koumudi Mahotsavam (కౌముది మహోత్సవం)",
         "c) Vikramanka Devacharitra (విక్రమాంక దేవచరిత్ర)",
         "d) Prithviraj Vijayam (పృథ్వీరాజ్ విజయం)",
         "c",
         "Vikramanka Devacharitra Bilhana (బిల్హణుడు) రచించాడు. ఇది కళ్యాణి చాళుక్య రాజు Tribhuvanamalla గురించి వివరిస్తుంది."),
        (4, 2,
         "మొదటి చంద్రగుప్తుని పట్టాభిషేకం గురించి రాసిన గ్రంథం?",
         "a) Devichandraguptam (దేవీచంద్రగుప్తం)",
         "b) Koumudi Mahotsavam (కౌముది మహోత్సవం)",
         "c) Mudrarakshasa (ముద్రారాక్షసం)",
         "d) Vikramanka Devacharitra (విక్రమాంక దేవచరిత్ర)",
         "b",
         "Koumudi Mahotsavam Vijjika (విజ్జికుడు) రచించాడు. ఇది మొదటి చంద్రగుప్తుని పట్టాభిషేకం గురించి."),

        # ── SECTION 5: Greek – Indica ──
        (5, 1,
         "Indica (ఇండికా) గ్రంథం రచయిత ఎవరు?",
         "a) Pliny (ప్లీని)",
         "b) Fa-Hien (ఫాహియాన్)",
         "c) Megasthenes (మెగస్తనీస్)",
         "d) Al-Biruni (అల్-బెరూని)",
         "c",
         "Indica మెగస్తనీస్ రచించాడు. ఇతను Seleucus Nicator రాయబారిగా Chandragupta Maurya ఆస్థానానికి వచ్చాడు."),
        (5, 2,
         "Megasthenes ఏ రాజు ఆస్థానానికి రాయబారిగా వచ్చాడు?",
         "a) Harshavardhan (హర్షవర్ధనుడు)",
         "b) Chandragupta Maurya (చంద్రగుప్త మౌర్య)",
         "c) Chandragupta II (రెండవ చంద్రగుప్తుడు)",
         "d) Ashoka (అశోకుడు)",
         "b",
         "Megasthenes సెల్యూకస్ నికేటర్ రాయబారిగా Chandragupta Maurya ఆస్థానానికి వచ్చాడు. Chandragupta Maurya మౌర్య సామ్రాజ్య స్థాపకుడు."),
        (5, 3,
         "Megasthenes ఏ రాజు పంపించిన రాయబారి?",
         "a) Ashoka (అశోకుడు)",
         "b) Chandragupta Maurya (చంద్రగుప్త మౌర్య)",
         "c) Seleucus Nicator (సెల్యూకస్ నికేటర్)",
         "d) Alexander (అలెగ్జాండర్)",
         "c",
         "Megasthenes సిరియా పాలకుడైన Seleucus Nicator యొక్క రాయబారిగా Chandragupta Maurya ఆస్థానానికి వచ్చాడు."),

        # ── SECTION 6: Periplus ──
        (6, 1,
         "Periplus of the Erythraean Sea (పెరిప్లస్ ఆఫ్ ది ఎరిత్రియన్ సీ) రచయిత ఎవరు?",
         "a) Megasthenes (మెగస్తనీస్)",
         "b) Pliny (ప్లీని)",
         "c) Unknown Sailor (అజ్ఞాత నావికుడు)",
         "d) Fa-Hien (ఫాహియాన్)",
         "c",
         "Periplus of the Erythraean Sea ని ఒక అజ్ఞాత నావికుడు (Unknown Sailor) రాశాడు. రచయిత పేరు తెలియదు."),
        (6, 2,
         "Periplus of the Erythraean Sea గ్రంథం ఏ విషయాలు వివరిస్తుంది?",
         "a) మౌర్య కాలం రాజనీతి మాత్రమే",
         "b) బౌద్ధ మత సమాచారం",
         "c) భారతీయ రాజకీయ, వాణిజ్య మరియు జాతిపరమైన అంశాలు (Political, trade and ethnic aspects)",
         "d) శాతవాహన వంశ చరిత్ర",
         "c",
         "Periplus భారతీయ రాజకీయ, వాణిజ్య మరియు జాతిపరమైన అంశాలను వివరిస్తుంది. భారత్-Rome వ్యాపార సంబంధాలు ప్రత్యేకంగా ఇందులో ఉన్నాయి."),
        (6, 3,
         "గ్రీకు ఆధారాల్లో రచయిత పేరు తెలియని గ్రంథం ఏది?",
         "a) Indica (ఇండికా)",
         "b) Periplus of the Erythraean Sea (పెరిప్లస్ ఆఫ్ ది ఎరిత్రియన్ సీ)",
         "c) Natural History (నాచురల్ హిస్టరీ)",
         "d) The Histories (ది హిస్టరీస్)",
         "b",
         "Periplus of the Erythraean Sea రచయిత పేరు తెలియదు. అందుకే అజ్ఞాత నావికుడు (Unknown Sailor) అని పిలుస్తారు."),

        # ── SECTION 7: Latin + Sri Lanka ──
        (7, 1,
         "Natural History (నాచురల్ హిస్టరీ) రచయిత ఎవరు?",
         "a) Megasthenes (మెగస్తనీస్)",
         "b) Pliny (ప్లీని)",
         "c) Fa-Hien (ఫాహియాన్)",
         "d) Taranath (తారానాథ్)",
         "b",
         "Natural History Pliny రచించాడు. ఇది లాటిన్ ఆధారం. మౌర్యుల కాలపు పరిపాలన అంశాలను వివరిస్తుంది."),
        (7, 1,
         "Dipavamsa మరియు Mahavamsa గ్రంథాలు ఏ భాషలో రాశారు?",
         "a) Sanskrit (సంస్కృతం)",
         "b) Tamil (తమిళం)",
         "c) Pali (పాళీ)",
         "d) Prakrit (ప్రాకృతం)",
         "c",
         "Dipavamsa మరియు Mahavamsa శ్రీలంక (సింహళ) బౌద్ధ మత గ్రంథాలు. Pali భాషలో రచించబడ్డాయి."),
        (7, 2,
         "Dipavamsa అంటే English లో?",
         "a) The Great Chronicle (ది గ్రేట్ క్రానికల్)",
         "b) The Chronicle of the Island (ది క్రానికల్ ఆఫ్ ది ఐలాండ్)",
         "c) History of Tibet (హిస్టరీ ఆఫ్ టిబెట్)",
         "d) Natural History (నాచురల్ హిస్టరీ)",
         "b",
         "Dipavamsa అంటే The Chronicle of the Island (ద్వీపం చరిత్ర). Mahavamsa అంటే The Great Chronicle (మహా చరిత్ర)."),

        # ── SECTION 8: Chinese Sources ──
        (8, 1,
         "King of Travellers (యాత్రికుల రాజు) అని పిలవబడే యాత్రికుడు ఎవరు?",
         "a) Fa-Hien (ఫాహియాన్)",
         "b) Megasthenes (మెగస్తనీస్)",
         "c) Huien Tsang (హ్యూయెన్ త్సాంగ్)",
         "d) Al-Biruni (అల్-బెరూని)",
         "c",
         "హ్యూయెన్ త్సాంగ్‌ను యాత్రికుల రాజు (King of Travellers) అంటారు. ఇతను బౌద్ధ సన్యాసి, పండితుడు మరియు యాత్రికుడు."),
        (8, 1,
         "Fa-Hien (ఫాహియాన్) రాసిన గ్రంథం ఏది?",
         "a) Si-Yu-Ki (సి-యు-కి)",
         "b) Fo-Kuo-Ki (ఫో-కువో-కి)",
         "c) Indica (ఇండికా)",
         "d) Natural History (నాచురల్ హిస్టరీ)",
         "b",
         "Fa-Hien ఫో-కువో-కి రాశాడు. Huien Tsang సి-యు-కి రాశాడు."),
        (8, 2,
         "మొదటి Chinese యాత్రికుడు (First Chinese traveller) ఎవరు?",
         "a) Huien Tsang (హ్యూయెన్ త్సాంగ్)",
         "b) Fa-Hien (ఫాహియాన్)",
         "c) Taranath (తారానాథ్)",
         "d) Al-Biruni (అల్-బెరూని)",
         "b",
         "Fa-Hien మొదటి Chinese యాత్రికుడు. ఇతను రెండవ Chandragupta (Chandragupta II) కాలంలో భారత్‌కు వచ్చాడు."),
        (8, 2,
         "Huien Tsang ఏ రాజు కాలంలో భారత్‌కు వచ్చాడు?",
         "a) Chandragupta Maurya (చంద్రగుప్త మౌర్య)",
         "b) Chandragupta II (రెండవ చంద్రగుప్తుడు)",
         "c) Harshavardhan (హర్షవర్ధనుడు)",
         "d) Ashoka (అశోకుడు)",
         "c",
         "Huien Tsang కనౌజ్ పరిపాలించిన Harshavardhan కాలంలో భారత్‌కు వచ్చాడు. ఇతను Si-Yu-Ki రాశాడు."),

        # ── SECTION 9: Arabic + Tibetan ──
        (9, 1,
         "Kitab-ul-Hind (కితాబ్-ఉల్-హింద్) రచయిత ఎవరు?",
         "a) Taranath (తారానాథ్)",
         "b) Fa-Hien (ఫాహియాన్)",
         "c) Al-Biruni (అల్-బెరూని)",
         "d) Pliny (ప్లీని)",
         "c",
         "Kitab-ul-Hind Al-Biruni రచించాడు. ఇతను Mahmud of Ghazni యొక్క ఆస్థాన విద్వాంసుడు."),
        (9, 2,
         "Al-Biruni కి ఇవ్వబడిన బిరుదులు ఏవి?",
         "a) Father of History మరియు King of Travellers",
         "b) Founder of Indology మరియు Father of Comparative Religion",
         "c) Father of Indology మరియు Father of History",
         "d) King of Travellers మరియు Father of Indology",
         "b",
         "Al-Biruni ని 'Founder of Indology' మరియు 'Father of Comparative Religion' అంటారు."),
        (9, 2,
         "'The History of Tibet' రచయిత ఎవరు?",
         "a) Al-Biruni (అల్-బెరూని)",
         "b) Fa-Hien (ఫాహియాన్)",
         "c) Huien Tsang (హ్యూయెన్ త్సాంగ్)",
         "d) Taranath (తారానాథ్)",
         "d",
         "The History of Tibet Taranath రచించాడు. ఇతను 17వ శతాబ్దంలో భారత్‌లో గల అన్ని బౌద్ధ ప్రాంతాలను తిరిగి ఈ పుస్తకాన్ని వ్రాశాడు. Ashoka గురించి విలువైన సమాచారం ఇస్తుంది."),

        # ── SECTION 10: Inscriptions Intro ──
        (10, 1,
         "శాసన అధ్యయనాన్ని (Study of Inscriptions) ఏమని అంటారు?",
         "a) Palaeography (పేలియోగ్రఫీ)",
         "b) Epigraphy (ఎపిగ్రఫీ)",
         "c) Numismatics (న్యూమిస్మాటిక్స్)",
         "d) Iconography (ఇకనోగ్రఫీ)",
         "b",
         "శాసన అధ్ययనాన్ని Epigraphy అంటారు. ప్రాచీన లిపుల అధ్యయనాన్ని Palaeography అంటారు."),
        (10, 1,
         "భారత్‌లో మొదటి సంస్కృత శాసనం (First Sanskrit Inscription) ఏది?",
         "a) Hatigumpha Inscription (హాతిగుంఫా శాసనం)",
         "b) Junaghad Inscription of Rudradaman (రుద్రదమనుడి జునాఘడ్ శాసనం)",
         "c) Nasik Inscription (నాసిక్ శాసనం)",
         "d) Aihole Inscription (ఐహోళ్ళు శాసనం)",
         "b",
         "భారత్‌లో మొదటి సంస్కృత శాసనంగా Rudradaman (రుద్రదమనుడు) యొక్క Junaghad Inscription కీర్తింపబడింది."),
        (10, 2,
         "ప్రాచీన లిపుల అధ్యయనాన్ని (Study of Ancient Scripts) ఏమని అంటారు?",
         "a) Epigraphy (ఎపిగ్రఫీ)",
         "b) Numismatics (న్యూమిస్మాటిక్స్)",
         "c) Palaeography (పేలియోగ్రఫీ)",
         "d) Iconography (ఇకనోగ్రఫీ)",
         "c",
         "ప్రాచీన లిపుల అధ్యయనాన్ని Palaeography అంటారు. శాసన అధ్యయనాన్ని Epigraphy అంటారు."),

        # ── SECTION 11: 4 Types of Inscriptions ──
        (11, 1,
         "అశోకుడు వేసిన శాసనాలు ఏ రకానికి చెందినవి?",
         "a) Dedicative Inscription (అంకిత శాసనాలు)",
         "b) Rock Edicts (రాజాజ్ఞలు)",
         "c) Donative Inscription (దాన శాసనాలు)",
         "d) Commemorative Inscription (స్మారక శాసనాలు)",
         "b",
         "రాజు యొక్క ఆజ్ఞలను మరియు ఉత్తర్వులను ప్రజలకు తెలియజేయుటకు మొట్టమొదట అశోకుడు Rock Edicts (రాజాజ్ఞలు) వేశాడు."),
        (11, 2,
         "Nalanda Copper Plate Inscription (నలంద తామ్ర శాసనం) ఏ రకానికి చెందింది?",
         "a) Rock Edicts (రాజాజ్ఞలు)",
         "b) Dedicative Inscription (అంకిత శాసనాలు)",
         "c) Donative Inscription (దాన శాసనాలు)",
         "d) Commemorative Inscription (స్మారక శాసనాలు)",
         "c",
         "నలంద తామ్ర శాసనం Donative Inscription (దాన శాసనం) కు ఉదాహరణ. గుప్తుల కాలంలో బ్రాహ్మణులకు అగ్రహారాలు ఇవ్వడం గురించి ఇందులో పేర్కొనబడింది."),
        (11, 3,
         "'Agrahara' (అగ్రహార) అనే పదం మొదటిసారి ఏ శాసనంలో కనిపించింది?",
         "a) Ashokan Edicts (అశోకుని శాసనాలు)",
         "b) Junaghad Inscription (జునాఘడ్ శాసనం)",
         "c) Nalanda Copper Plate Inscription (నలంద తామ్ర శాసనం)",
         "d) Aihole Inscription (ఐహోళ్ళు శాసనం)",
         "c",
         "గుప్తుల కాలం నాటి Nalanda Copper Plate Inscription లో మొదటిసారిగా 'Agrahara' (అగ్రహార) అనే పదం కనిపించింది."),
        (11, 2,
         "Samudragupta యొక్క Allahabad Prashasti శాసనం ఏ రకానికి చెందింది?",
         "a) Rock Edicts (రాజాజ్ఞలు)",
         "b) Donative Inscription (దాన శాసనాలు)",
         "c) Dedicative Inscription (అంకిత శాసనాలు)",
         "d) Commemorative Inscription (స్మారక శాసనాలు)",
         "d",
         "Samudragupta యొక్క Allahabad Prashasti స్మారక శాసనానికి (Commemorative Inscription) ఉదాహరణ. భౌగోళిక పరిస్థితులు, పాలక వంశాల పేర్లు, విజయాలు నమోదు చేస్తుంది."),
        (11, 3,
         "శాసనాల 4 రకాలు సరైన క్రమంలో ఏవి?",
         "a) రాజాజ్ఞలు, స్మారక, దాన, అంకిత",
         "b) Rock Edicts (రాజాజ్ఞలు), Dedicative (అంకిత), Donative (దాన), Commemorative (స్మారక)",
         "c) అంకిత, రాజాజ్ఞలు, స్మారక, దాన",
         "d) దాన, అంకిత, రాజాజ్ఞలు, స్మారక",
         "b",
         "శాసనాల 4 రకాలు: 1. Rock Edicts (రాజాజ్ఞలు) 2. Dedicative (అంకిత శాసనాలు) 3. Donative (దాన శాసనాలు) 4. Commemorative (స్మారక శాసనాలు)."),

        # ── SECTION 12: Numismatics ──
        (12, 1,
         "నాణెముల అధ్యయనాన్ని (Study of Coins) ఏమని అంటారు?",
         "a) Epigraphy (ఎపిగ్రఫీ)",
         "b) Palaeography (పేలియోగ్రఫీ)",
         "c) Numismatics (న్యూమిస్మాటిక్స్)",
         "d) Iconography (ఇకనోగ్రఫీ)",
         "c",
         "నాణెముల అధ్యయనాన్ని Numismatics (న్యూమిస్మాటిక్స్) అంటారు."),
        (12, 2,
         "గుప్తుల నాణేలపై ఉన్న ముఖ్యమైన లాంఛనం ఏది?",
         "a) Chakra (చక్రం)",
         "b) Nandi (నంది)",
         "c) Garuda (గరుడ)",
         "d) Lion (సింహం)",
         "c",
         "గుప్తుల నాణేలపై Garuda (గరుడ) లాంఛనం చెక్కబడింది. ఇవి రాజకీయ, ఆర్థిక, సాంస్కృతిక సమాచారం అందజేస్తున్నాయి."),
        (12, 3,
         "Indo-Greek (ఇందో-గ్రీకుల) నాణేల ప్రత్యేకత ఏమిటి?",
         "a) ఒక వైపు మాత్రమే ముద్రించబడ్డాయి (Single side)",
         "b) రెండు వైపుల ముద్రించబడ్డాయి (Both sides)",
         "c) బంగారంతో మాత్రమే తయారు చేయబడ్డాయి",
         "d) అశోకుని చిత్రం ఉంటుంది",
         "b",
         "Indo-Greek లు రెండువైపుల ముద్రించిన నాణేలు చేశారు. ఇవి రెండు సంస్కృతుల కలయికను చూపుతాయి."),

        # ── SECTION 13: Dating Methods ──
        (13, 1,
         "C¹⁴ Radiocarbon dating పద్ధతి కనుగొన్న శాస్త్రవేత్త ఎవరు?",
         "a) McDougal (మెక్‌డూగల్)",
         "b) Atkins (ఇటికిన్స్)",
         "c) Willard Libby (విల్లర్డ్ లిబ్బి)",
         "d) Dendro",
         "c",
         "C¹⁴ Radiocarbon dating పద్ధతిని అమెరికాకు చెందిన Willard Libby కనుగొన్నాడు. ఇది సేంద్రియ పదార్థాలకు (ఎముక, దంతాలు) వర్తిస్తుంది. కాల వ్యాప్తి: 20,000–4,00,000 సంవత్సరాలు."),
        (13, 2,
         "కుండలకు (Pottery) అనువైన dating పద్ధతి ఏది?",
         "a) Radiocarbon — C¹⁴ (రేడియోకార్బన్)",
         "b) Potassium-Argon — K-A⁴⁰ (పొటాషియం-అర్గాన్)",
         "c) Thermoluminescence (థర్మోల్యూమినిసెన్స్)",
         "d) Dendrochronology (డెండ్రోక్రోనాలజీ)",
         "c",
         "కుండలకు (Pottery) Thermoluminescence పద్ధతి అనువైనది. శాస్త్రవేత్త Atkins (ఇటికిన్స్). కాల వ్యాప్తి 10,000 సంవత్సరాలు."),
        (13, 3,
         "అగ్నిశిల (Igneous Rock) dating కు అనువైన పద్ధతి ఏది?",
         "a) Radiocarbon — C¹⁴ (రేడియోకార్బన్)",
         "b) Potassium-Argon — K-A⁴⁰ (పొటాషియం-అర్గాన్)",
         "c) Thermoluminescence (థర్మోల్యూమినిసెన్స్)",
         "d) Dendrochronology (డెండ్రోక్రోనాలజీ)",
         "b",
         "Potassium-Argon (K-A⁴⁰) పద్ధతి అగ్నిశిలకు అనువైనది. శాస్త్రవేత్త McDougal. కాల వ్యాప్తి అపరిమితం."),
        (13, 2,
         "వృక్షాల వార్షిక వలయాల (Annual tree rings) dating పద్ధతి ఏది?",
         "a) Amino Acid Racemization (అమైనో ఆమ్ల రెసిమేషన్)",
         "b) Thermoluminescence (థర్మోల్యూమినిసెన్స్)",
         "c) Dendrochronology (డెండ్రోక్రోనాలజీ)",
         "d) Radiocarbon — C¹⁴ (రేడియోకార్బన్)",
         "c",
         "వృక్షాల వార్షిక వలయాలకు Dendrochronology పద్ధతి అనువైనది. కాల వ్యాప్తి 7,500 సంవత్సరాలు."),
        (13, 3,
         "అపరిమిత (Unlimited) కాల వ్యాప్తి కలిగిన dating పద్ధతి ఏది?",
         "a) Radiocarbon — C¹⁴ (రేడియోకార్బన్)",
         "b) Thermoluminescence (థర్మోల్యూమినిసెన్స్)",
         "c) Potassium-Argon — K-A⁴⁰ (పొటాషియం-అర్గాన్)",
         "d) Dendrochronology (డెండ్రోక్రోనాలజీ)",
         "c",
         "Potassium-Argon (K-A⁴⁰) పద్ధతి అపరిమిత కాల వ్యాప్తి కలిగి ఉంది. మెక్‌డూగల్ దీన్ని అభివృద్ధి చేశాడు."),

        # ── SECTION 14: Architecture ──
        (14, 1,
         "ఉత్తర భారతదేశంలో ఏ వాస్తు శైలి అభివృద్ధి చెందింది?",
         "a) Dravida style (ద్రావిడ శైలి)",
         "b) Vesara style (వేసర శైలి)",
         "c) Nagara style (నగరశైలి)",
         "d) Indo-Gothic style (ఇందో-గోథిక్)",
         "c",
         "ఉత్తర భారతదేశంలో Nagara style (నగరశైలి) అభివృద్ధి చెందింది. దక్షిణ భారతదేశంలో Dravida style అభివృద్ధి చెందింది."),
        (14, 2,
         "Vesara style (వేసర శైలి) అంటే ఏమిటి?",
         "a) ఉత్తర భారత ప్రత్యేక శైలి",
         "b) దక్షిణ భారత ప్రత్యేక శైలి",
         "c) Nagara మరియు Dravida శైలుల కలయిక (Combination of Nagara and Dravida)",
         "d) British ప్రభావంతో వచ్చిన శైలి",
         "c",
         "Vesara style Nagara మరియు Dravida శైలుల కలయిక. ఇది ప్రధానంగా Deccan ప్రాంతంలో కనిపిస్తుంది."),
        (14, 2,
         "ప్రాచీన వాస్తురీతి మరియు శిల్పాల అధ్యయనాన్ని ఏమని అంటారు?",
         "a) Epigraphy (ఎపిగ్రఫీ)",
         "b) Numismatics (న్యూమిస్మాటిక్స్)",
         "c) Iconography (ఇకనోగ్రఫీ)",
         "d) Palaeography (పేలియోగ్రఫీ)",
         "c",
         "ప్రాచీన వాస్తురీతి మరియు శిల్పాల అధ్యయనాన్ని Iconography (ఇకనోగ్రఫీ) అంటారు."),

        # ── SECTION 15: Pottery ──
        (15, 1,
         "భారతదేశంలో మొదటి కుమ్మరి చక్రం (Potter's wheel) ఎక్కడ బయటపడింది?",
         "a) Harappa (హారప్పా)",
         "b) Mohenjo-daro (మొహెంజో-దారో)",
         "c) Mehurgar (మెహర్గర్)",
         "d) Taxila (తక్షశిల)",
         "c",
         "భారతదేశంలో మొట్టమొదటగా Mehurgar (మెహర్గర్) లో కుమ్మరి చక్రం బయటపడింది."),
        (15, 2,
         "Amino Acid Racemization పద్ధతి ఏ వస్తువులకు అనువైనది?",
         "a) Pottery (కుండలు)",
         "b) Igneous Rock (అగ్నిశిల)",
         "c) Bone and Marine shells (ఎముక మరియు సముద్ర కర్చురాలు)",
         "d) Tree rings (వృక్షాల వలయాలు)",
         "c",
         "Amino Acid Racemization పద్ధతి ఎముక మరియు సముద్ర కర్చురాలకు అనువైనది. కాల వ్యాప్తి 1 లక్ష సంవత్సరాలు."),
    ]

    insert_sql = '''INSERT INTO chapter_mcqs
        (study_note_id, section_idx, difficulty, q_te, opt_a, opt_b, opt_c, opt_d, correct, explanation_te)
        VALUES (?,?,?,?,?,?,?,?,?,?)'''
    try:
        for i, m in enumerate(mcqs):
            db_exec(conn, insert_sql, (ch_id,) + m)
        conn.commit()
    except Exception as e:
        try: conn.rollback()
        except: pass
        conn.close()
        raise RuntimeError(f'INSERT failed at MCQ index (after commit): {e}')
    conn.close()
    return jsonify({'success': True, 'message': f'{len(mcqs)} MCQs seeded for Chapter 1!'})


# ─────────────────────────────────────────────────────────────────────────────
# CHAPTER 2 — INDIAN HISTORY: పూర్వచారిత్రక సంస్కృతులు (Pre-Historic Cultures)
# ─────────────────────────────────────────────────────────────────────────────
@app.route('/api/notes/seed_ch2_ih', methods=['POST'])
def notes_seed_ch2_ih():
    """Seed Chapter 2 Indian History - Pre-Historic Cultures. Add ?force=1 to overwrite."""
    force = request.args.get('force', '0') == '1'
    conn = get_db()
    if USE_POSTGRES:
        cur0 = conn.cursor()
        cur0.execute('''CREATE TABLE IF NOT EXISTS study_notes (
            id SERIAL PRIMARY KEY, subject TEXT NOT NULL, topic TEXT NOT NULL,
            chapter_num INTEGER NOT NULL, chapter_title_te TEXT NOT NULL,
            chapter_title_en TEXT NOT NULL, pages_ref TEXT DEFAULT '',
            sections_json TEXT NOT NULL DEFAULT '[]',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
        conn.commit(); cur0.close()
    else:
        conn.execute('''CREATE TABLE IF NOT EXISTS study_notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT, subject TEXT NOT NULL, topic TEXT NOT NULL,
            chapter_num INTEGER NOT NULL, chapter_title_te TEXT NOT NULL,
            chapter_title_en TEXT NOT NULL, pages_ref TEXT DEFAULT '',
            sections_json TEXT NOT NULL DEFAULT '[]',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
        conn.commit()

    cur = db_exec(conn, "SELECT id FROM study_notes WHERE subject='GK' AND topic='Indian_History' AND chapter_num=2")
    existing = cur.fetchone()
    if existing and not force:
        conn.close()
        return jsonify({'message': 'Already seeded. Use ?force=1 to overwrite.'})
    if existing and force:
        db_exec(conn, "DELETE FROM study_notes WHERE subject='GK' AND topic='Indian_History' AND chapter_num=2")
        conn.commit()

    ch2_sections = [
        {
            "title": "పరిచయం — పూర్వచారిత్రక సంస్కృతులు",
            "sub": "Pre-Historic Cultures · Gordon Childe · History Classifications",
            "audio": """స్వాగతం! మీరు ఇప్పుడు భారతదేశ చరిత్ర — అధ్యాయం 2 వినబోతున్నారు. అంశం: పూర్వచారిత్రక సంస్కృతులు — Pre-Historic Cultures.

ప్రాచీన భారతదేశ చరిత్రను తెలుసుకోవడానికి మనకు పురావస్తు ఆధారాలు, వాజ్మయాలు, శాసనాలు, రచనలు మరియు నాణేలు ఉపయోగపడతాయి. అయితే ఒక చాలా ముఖ్యమైన విషయం ఏమిటంటే — లిపి పుట్టుకతోనే నాగరికత ఆవిర్భవించిందని ప్రముఖ చరిత్రకారుడు గోర్డన్ చైల్డ్ (Gordon Childe) అభిప్రాయపడ్డారు. ఆయన రాసిన పుస్తకం పేరు What happened in History — 1942లో ప్రచురితమైంది.

చరిత్ర అధ్యయనం కోసం దాన్ని మూడు ప్రధాన యుగాలుగా విభజించవచ్చు:

మొదటిది — చారిత్రకపూర్వ యుగం లేదా Pre-historic Age. ఇందులో లిఖిత పూర్వక ఆధారాలు లభించవు, కేవలం పురావస్తు ఆధారాలు మాత్రమే లభిస్తాయి. ఉదాహరణ — ఆది మానవుల కాలం అంటే Period of Primitive Man.

రెండవది — చారిత్రక సంధికాల యుగం లేదా Proto-historic Age. ఇందులో పురావస్తు ఆధారాలు లభిస్తాయి, లిఖిత పూర్వక ఆధారాలు కూడా లభిస్తాయి — అయితే ఆ లిపిని ఇంకా చదవలేని స్థితిలో ఉంటాయి. ఉదాహరణ — సింధూ నాగరికత. ఆ నాగరికత యొక్క చిత్ర లిపి అంటే Pictography ని ఇప్పటి వరకు కూడా చరిత్రకారులు అర్థం చేసుకోలేదు.

మూడవది — చారిత్రక యుగం లేదా Historic Age. ఇందులో లిఖిత పూర్వక ఆధారాలు మరియు పురావస్తు ఆధారాలు రెండూ లభిస్తాయి. ఉదాహరణ — రాజులు మరియు రాణులు పాలించిన కాలం.

ఈ అధ్యాయంలో మనం ముఖ్యంగా Pre-historic Age గురించి సంపూర్ణంగా నేర్చుకుంటాం. శిలాయుగం నుండి ఇనుపయుగం వరకు, మొగాలిత్ సంస్కృతి వరకు — అన్ని విషయాలు వివరంగా చర్చిద్దాం.

Mini Recap: గోర్డన్ చైల్డ్ పుస్తకం — What happened in History — 1942. మూడు యుగాలు — Pre-historic, Proto-historic, Historic. సింధూ నాగరికత — Proto-historic కు ఉదాహరణ."""
        },
        {
            "title": "శిలాయుగ విభజన మరియు ఆర్కియాలాజికల్ సర్వే ఆఫ్ ఇండియా",
            "sub": "Thomson's Classification · Stone Age Periods · ASI History",
            "audio": """ఇప్పుడు శిలాయుగ విభజన మరియు ఆర్కియాలాజికల్ సర్వే ఆఫ్ ఇండియా గురించి నేర్చుకుందాం.

చారిత్రకపూర్వ యుగాన్ని మొదట మూడు భాగాలుగా విభజించింది క్రిస్టియన్ జూర్గన్‌సన్ థామ్సన్ (Christian Jorgensen Thomson):
మొదటిది — శిలాయుగం అంటే Stone Age
రెండవది — కంచు యుగం అంటే Bronze Age
మూడవది — ఇనుప యుగం అంటే Iron Age

ఇప్పుడు ఇంకొంచెం వివరంగా — చారిత్రకపూర్వ యుగాన్ని నాలుగు భాగాలుగా విభజించవచ్చు:

మొదటిది — ప్రాచీన శిలాయుగం లేదా పాతరాతి యుగం: క్రీ.పూ. 10 లక్షల సంవత్సరాల నుండి క్రీ.పూ. 10,000 సంవత్సరాల వరకు. ఇది అత్యంత దీర్ఘకాలమైన యుగం.

రెండవది — మధ్య శిలాయుగం: క్రీ.పూ. 10,000 నుండి క్రీ.పూ. 8,000 వరకు.

మూడవది — నవీన లేదా నూతన శిలాయుగం: క్రీ.పూ. 8,000 నుండి క్రీ.పూ. 4,000 వరకు.

నాల్గవది — తాంబ్ర లేదా రాగి శిలాయుగం: క్రీ.పూ. 4,000 నుండి క్రీ.పూ. 3,000 వరకు.

ఈ కాలాలు గుర్తుపెట్టుకోండి: 10 లక్ష నుండి 10 వేల వరకు ప్రాచీన; 10 వేల నుండి 8 వేల వరకు మధ్య; 8 వేల నుండి 4 వేల వరకు నవీన; 4 వేల నుండి 3 వేల వరకు రాగి శిలాయుగం.

ఇప్పుడు ఆర్కియాలాజికల్ సర్వే ఆఫ్ ఇండియా గురించి తెలుసుకుందాం. ఇది 1861లో అలెగ్జాండర్ కన్నింగ్‌హామ్ (Alexander Cunningham) ఆధ్వర్యంలో ఏర్పాటైంది. కన్నింగ్‌హామ్‌ను Father of Indian Archaeology మరియు ASI యొక్క The First Director General గా పేర్కొంటారు. లార్డ్ కర్జన్ 1904లో ప్రాచీన కట్టడాల పరిరక్షణ కోసం ఒక చట్టాన్ని చేసి భారత పురావస్తు శాఖను పునరుద్ధరించారు. ప్రస్తుతం భారత ప్రభుత్వం యొక్క సాంస్కృతిక మంత్రిత్వశాఖ ఆధీనంలో పురావస్తు పరిశోధన మరియు సాంస్కృతిక కట్టడాల సంరక్షణకు తోడ్పడుతుంది.

Mini Recap: థామ్సన్ — మూడు యుగాలు. నాలుగు శిలాయుగాలు — 10L, 10T, 8T, 4T, 3T. ASI వ్యవస్థాపకుడు — అలెగ్జాండర్ కన్నింగ్‌హామ్ — 1861."""
        },
        {
            "title": "ప్రాచీన శిలాయుగం — పరిచయం",
            "sub": "Palaeolithic Age · Old Stone Age · Robert Bruce Foote · Quartzite Culture",
            "audio": """ఇప్పుడు ప్రాచీన శిలాయుగం లేదా Palaeolithic Age గురించి వివరంగా నేర్చుకుందాం.

గ్రీకు భాషలో పేలియో అంటే ప్రాచీనం మరియు లిథ్స్ లేదా లిథిక్ అంటే రాతి లేదా శిల అని అర్థం. కాబట్టి Palaeolithic అంటే పాత రాయి యుగం లేదా Old Stone Age అన్నమాట. ఈ యుగంలో స్ఫటికశిల అంటే Quartzite అనే రాయిని వాడడం వల్ల ఈ సంస్కృతిని Quartzite సంస్కృతి అంటారు.

ఈ శిలాయుగానికి సంబంధించిన తొలి ప్రదేశం — First Site — ను రాబర్ట్ బ్రూస్ ఫుట్ (Robert Bruce Foote) 1863లో తమిళనాడులోని పల్లవరం దగ్గర కనుగొన్నాడు. ఫుట్‌ను Father of Indian Prehistory అని పిలుస్తారు. ఇది చాలా ముఖ్యమైన విషయం — గుర్తుపెట్టుకోండి.

ఈ యుగం యొక్క వాతావరణం మంచుతో కప్పబడి ఉండటం వల్ల దీన్ని Pleistocene లేదా మంచు యుగం అంటే Ice Age అంటారు.

శివాలిక్ హిమాలయ ప్రాంతంలో రామాపిథికస్, శివ పిథికస్ మానవుల అవశేషాలు లభ్యమయ్యాయి. నర్మదా నది ప్రాంతంలో నియాండర్తల్ మానవ అవశేషాలు లభ్యమయ్యాయి. ఈ శిలాయుగ అంతానికి ఆధునిక మానవుడైన హోమో సేపియన్స్ (Homo Sapiens) — లాటిన్ భాషలో దీనికి అర్థం తెలివైన వాడు — ఆవిర్భవించాడు.

ఈ కాలపు మానవుడు మొట్టమొదటిసారిగా రాతి పనిముట్లను ఉపయోగించడం జరిగింది. ఈ కాలపు ఆర్థిక వ్యవస్థ ప్రధానంగా Hunting and Gathering Economy రకానికి చెందినది — అంటే వేట మరియు ఆహార సేకరణ. మానవులు చిన్న చిన్న గుంపులుగా అంటే Bands గా నివసించేవారు.

Mini Recap: Palaeolithic = పాత రాయి యుగం. ఫుట్ — Father of Indian Prehistory — 1863 — పల్లవరం. క్వార్ట్‌జైట్ సంస్కృతి. హోమో సేపియన్స్ ఈ యుగం చివరలో వచ్చారు."""
        },
        {
            "title": "దిగువ ప్రాచీన శిలాయుగం — పరికరాలు మరియు స్థావరాలు",
            "sub": "Lower Palaeolithic · Hominids · Chopping Stones · Hand Axes · Sites",
            "audio": """ఇప్పుడు ప్రాచీన శిలాయుగంలో మొదటి విభాగం — దిగువ ప్రాచీన శిలాయుగం లేదా Lower Palaeolithic గురించి నేర్చుకుందాం.

ప్రాచీన శిలాయుగాన్ని మూడు భాగాలుగా విభజించారు: అ) దిగువ ప్రాచీన, బ) మధ్య ప్రాచీన, స) ఎగువ ప్రాచీన.

దిగువ ప్రాచీన శిలాయుగం క్రీ.పూ. 10 లక్ష సంవత్సరాల నుండి క్రీ.పూ. 1 లక్ష సంవత్సరాల వరకు కొనసాగింది.

ఈ కాలపు తొలి ఆనవాళ్ళు లభించిన ప్రాంతంగా పహల్‌గామ్ (కాశ్మీర్) గుర్తించబడింది.

ఈ ప్రాంతపు మానవుడిగా హోమినిడ్స్ అని పిలుస్తారు. ఆది మానవుడి పిలవబడే హోమో హాబిలిస్ మరియు హోమో ఎరెక్టస్ గా పరివర్తన చెందాడు. ఈ మానవుల జీవితం జంతువుల జీవన విధానాన్ని పోలి ఉండేది.

మానవుడు సంచార జీవనం అంటే Nomadic గడుపుతూ, వేటను ప్రధాన వృత్తిగా కలిగియున్నారు.

ఈ యుగంలో మానవుడు ఉపయోగించిన పరికరాలు: పెద్దపెద్ద ఆకారాలలో ఉండే గొడ్డలి రాళ్ళు అంటే Chopping Stones, చేతి గొడ్డళ్ళు అంటే Hand Axes, వృత్తాకారపు రాళ్ళు అంటే Discoids — వీటిని వేటలో, ఆహార సేకరణలో ఉపయోగించారు.

రాతిగొడ్డళ్ళ పరిశ్రమను అత్తిరాంపక్కం, మడమదురై — తమిళనాడులో — రాబర్ట్ బ్రూస్‌ఫుట్ కనుగొన్నాడు.

ముఖ్యమైన Lower Palaeolithic స్థావరాలు గుర్తుపెట్టుకోండి:
మధ్యప్రదేశ్ — హైరాపంగాబాద్, ఆదాంగర్, భింబెట్కా గుహాలు.
ఉత్తరప్రదేశ్ — సిసోలి, లలిత్‌పూర్.
రాజస్థాన్ — జలోర్, పుష్కర్.
మహారాష్ట్ర — నేవాసా.
కర్ణాటక — గుల్బర్గా, అనగవాడి, బాగల్‌కోట్, హుసనగి లోయ.
తెలంగాణ — మహాబూట్‌నగర్, నల్లొండ.
తమిళనాడు — అత్తిరాంపక్కం, వడమదురై, బూడిదమాను వంక.
కాశ్మీర్ — పహల్‌గామ్.

Mini Recap: Lower Palaeolithic — 10 లక్ష నుండి 1 లక్ష సంవత్సరాలు. పహల్‌గామ్ — తొలి ఆనవాళ్ళు. హోమినిడ్స్ → హోమో ఎరెక్టస్. Chopping Stones, Hand Axes ప్రధాన పరికరాలు."""
        },
        {
            "title": "భింబెట్కా గుహాలు — ప్రపంచ వారసత్వ కేంద్రం",
            "sub": "Bhimbetka Caves · Vishnu Shridhar Wakankar · UNESCO · Rock Paintings",
            "audio": """ఇప్పుడు భింబెట్కా గుహాల గురించి వివరంగా నేర్చుకుందాం. ఇవి చాలా ముఖ్యమైన పరీక్షా విషయాలు.

భింబెట్కా గుహాలను 1957లో విష్ణు శ్రీధర్ వాకంకర్ (Vishnu Shridhar Wakankar) అనే పురావస్తు శాస్త్రవేత్త కనుగొన్నారు. మనం గుర్తుపెట్టుకోవాల్సిన సంవత్సరాలు: కనుగొన్నది 1957; UNESCO వారు దీన్ని 2003లో ప్రపంచ వారసత్వ కేంద్రంగా అంటే World Heritage Site గా గుర్తించారు.

ఈ గుహాలు మధ్యప్రదేశ్‌లో ఉన్నాయి. ఇవి ప్రాచీన, మధ్య, నవీన మరియు తాంబ్ర శిలాయుగాలకు చెందినవి.

ప్రాచీన శిలాయుగపు తొలి చిత్రాలు భింబెట్కా మధ్యప్రదేశ్ గుహాలలో లభ్యమయ్యాయి. ఇందులో ఎరుపు మరియు మూడు ఆకుపచ్చ రంగులను వాడి అడవి దున్నలు, పులులు, ఏనుగులు మరియు అడవి పందులు వంటి జంతువులను చిత్రించారు.

ఈ గుహాలలోని చిత్రాలు చాలా అందంగా ఉన్నాయి — రాతిపై మానవులు జంతువులను వేటాడుతున్నట్లు ఉండే దృశ్యాలు అత్యంత సుందరంగా చిత్రించబడ్డాయి. ఈ వేటకు గాను విల్లు బాణం, కత్తులు మరియు ఈటెలను ఉపయోగించినట్లు తెలుస్తుంది. గుర్రాలపై వేటాడే పురుషుల దృశ్యాలు, నృత్యం చేస్తున్న మహిళల చిత్రాలు మరియు తేనెను సేకరిస్తున్న చిత్రాలు ఆకర్షణీయంగా చిత్రించబడ్డాయి.

గుర్తుపెట్టుకోవాల్సిన ముఖ్య విషయాలు:
మొదట కనుగొన్నది — విష్ణు శ్రీధర్ వాకంకర్ — 1957.
UNESCO World Heritage Site — 2003.
స్థానం — మధ్యప్రదేశ్.
చిత్రాలు — ప్రాచీన, మధ్య, నవీన, తాంబ్ర శిలాయుగాలకు చెందినవి.
రంగులు — ఎరుపు మరియు ఆకుపచ్చ.

Mini Recap: భింబెట్కా — 1957 — వాకంకర్ — మధ్యప్రదేశ్ — UNESCO 2003. తొలి రాతి చిత్రాలు ఇక్కడే లభ్యమయ్యాయి."""
        },
        {
            "title": "మధ్య మరియు ఎగువ ప్రాచీన శిలాయుగం",
            "sub": "Middle Palaeolithic · Upper Palaeolithic · Homo Erectus · Nevasa Culture · Homo Sapiens",
            "audio": """ఇప్పుడు మధ్య ప్రాచీన శిలాయుగం మరియు ఎగువ ప్రాచీన శిలాయుగం గురించి నేర్చుకుందాం.

మధ్య ప్రాచీన శిలాయుగం (Middle Palaeolithic Age):
ఈ యుగ స్థావరాలు 1939లో సోన్ లోయ (ఉత్తరప్రదేశ్), నర్మదా లోయ (గుజరాత్) మరియు కర్నూలు (ఆంధ్రప్రదేశ్)లో బయల్పడినవి.

మధ్య ప్రాచీన శిలాయుగ తొలి మానవుని హోమో ఎరెక్టస్ (Homo Erectus) అని అంటారు. తరువాత రూపాంతరం చెంది నియాండర్తల్ మానవుడు అయినాడు.

మధ్య ప్రాచీన శిలాయుగ స్థావరాలలో లభ్యమైన పనిముట్లు రేగులు అంటే Flakes. ఈ యుగంలో బయల్పడిన స్థావరాలన్నింటికీ గల సంస్కృతి పేరు నేవాసా సంస్కృతి (Nevasa Culture). నేవాసా సంస్కృతికి H.D. సంకాలియా నామకరణం చేశారు.

నేవాసా సంస్కృతిలో అంతర్భాగంగా మహారాష్ట్రలో ప్రధాన స్థావరాలు: నేవాసా మరియు మధుమేశ్వర్. అలాగే పశ్చిమ బెంగాల్‌లో పురియా మరియు మధ్యప్రదేశ్‌లో మానాపూర్, ఆదాంగర్. పై అన్ని ప్రాంతాలలో లభించిన పనిముట్లు ఒక్కో రకంగా లభించాయి. తమిళనాడులోని గుడియాం గుహాలో క్వార్ట్‌జైట్ వాడినారు.

ఇప్పుడు ఎగువ ప్రాచీన శిలాయుగం (Upper Palaeolithic Age):
ఇది హిమయుగం అంటే Ice Age యొక్క చివరి దశకు సంబంధించినది. ఈ కాలంలో హోమో సేపియన్ (Homo Sapiens) అనే మానవుడు అంటే Wise Man పరిణామం చెందాడు.

ఎగువ ప్రాచీన శిలాయుగంలో మానవుడు ఉపయోగించిన ప్రధాన పరికరాలుగా చిన్న కత్తులు, గీటురాయి, రాయి, కత్రి, Burin, Pointer లు గుర్తించబడ్డాయి.

ఉష్ట్రపక్షి (Ostrich) యొక్క పెంకుతో చేయబడిన పూసలు మహారాష్ట్రలోని పాటన్‌లో లభించాయి. ఎగువ ప్రాచీన స్థావరమైన కర్నూలు నందు ఖడ్గమృగము శిలాజం లభించింది.

ముఖ్యమైన ఎగువ ప్రాచీన స్థావరాలు: అనంతపురం జిల్లా రేబిగుంట, కర్నూలు జిల్లా ముచ్చట్ల చింతమానుగవి, పంజాబ్‌లోని బేలన్ లోయ, గుజరాత్ విసాది, మహారాష్ట్ర పాటన్, మధ్యప్రదేశ్ భింబెట్కా.

Mini Recap: మధ్య — Homo Erectus → Neandertal. Nevasa Culture — H.D. Sankalia. ఎగువ — Homo Sapiens (Wise Man). ఉష్ట్రపక్షి పూసలు — పాటన్ (MH)."""
        },
        {
            "title": "మధ్య శిలాయుగం — పరిచయం మరియు లక్షణాలు",
            "sub": "Mesolithic Age · Microlithic Age · Holocene · Microliths · Dog Domestication",
            "audio": """ఇప్పుడు మధ్య శిలాయుగం లేదా మెసోలిథిక్ యుగం (Mesolithic Age) గురించి నేర్చుకుందాం. దీన్ని సూక్ష్మ శిలాయుగం లేదా Microlithic Age అని కూడా అంటారు.

ఇది పూర్వ చారిత్రకయుగ సంస్కృతులలో రెండవ ప్రధాన యుగం. ఈ యుగంలో హోలోసీన్ యుగం (Holocene Epoch) ప్రారంభమైంది — అంటే మంచు కరగడం మొదలై వాతావరణం మారడం జరిగింది.

వేట వృత్తితో పాటు, ఆహారం సేకరించే స్థాయి ఎదిగింది. ఆంధ్రప్రదేశ్‌లో కర్నూలు, రేగింటలలో మొదటగా పూడ్చిపెట్టిన ప్రదేశాలు (Burial Grounds) కనుగొనబడ్డాయి — ఇది చాలా ముఖ్యమైన విషయం.

సూక్ష్మ శిలాయుగంలో మానవుడు వాడిన రాతి పరికరాలు 1 సెం.మీ నుండి 8 సెం.మీ మధ్య ఉండేవి — వీటినే Microliths అంటారు. ఇటువంటి సూక్ష్మ శిలలను Cammiade (కమ్మియాడ్) అనే అర్కియాలజిస్ట్ వింధ్యపర్వత ప్రాంతాలలో కనుగొన్నారు.

సూక్ష్మ శిలాయుగ స్థావరాలలో నిప్పు వినియోగించినట్లు ఆనవాళ్ళు లభ్యమయ్యాయి. క్రీ.పూ. 5000 B.C. నుండి పశువులను మచ్చిక చేసుకుంటూ ఆనవాళ్ళు లభ్యమైనాయి — బగోర్ (రాజస్థాన్), ఆదాంగర్ (మధ్యప్రదేశ్)లో ఆనవాళ్ళు లభ్యమైనవి.

ముఖ్యమైన విషయం: ఈ యుగంలో మొట్టమొదటిసారిగా కుక్కను పెంపు జంతువుగా మచ్చిక చేసుకున్నారు.

మధ్య శిలాయుగ స్థావరాల పట్టిక:
పశ్చిమ బెంగాల్ — బీర్‌భాన్‌పూర్, తిరుస్వేలి.
తమిళనాడు — తిరుస్వేలి.
ఉత్తరప్రదేశ్ — బేలన్ లోయ.
రాజస్థాన్ — బగోర్, తిల్వారా, హాత్‌పురా, సోజత్.
గుజరాత్ — లంఫ్‌నాజ్, వల్లనా, హీర్‌పూర్, అఖేజ్.
ఉత్తరప్రదేశ్ — సరాయ్ నహర్ రాయ్, మోర్హాన పహర్, లేఖాహియా, చోపాని మండో.

Mini Recap: Mesolithic = సూక్ష్మ శిలాయుగం. Holocene ప్రారంభం. Microliths — 1 నుండి 8 సెం.మీ. Burial Grounds — కర్నూలు, రేగింటల (AP). 5000 BC నుండి కుక్క మచ్చిక."""
        },
        {
            "title": "మధ్య శిలాయుగం — ముఖ్య స్థావరాలు",
            "sub": "Bagor · Sarai Nahar Rai · Adangur · Chopani Mando · Lanfunaj",
            "audio": """ఇప్పుడు మధ్య శిలాయుగపు ముఖ్య స్థావరాల గురించి ఒక్కొక్కటిగా వివరంగా నేర్చుకుందాం. ఇవి పరీక్షలో తరచూ అడిగే విషయాలు.

మొదటిది — బగోర్ గోదలు (రాజస్థాన్):
ఇది చాలా నేలలు కల్లిన గడిసెల ఆనవాళ్ళు లభించిన స్థావరం. ఇది మధ్య శిలాయుగంలో అత్యంత దీర్ఘకాలం వ్యాపించిన స్థావరం — మేరా!

రెండవది — సరాయ్ నహర్ రాయ్ (ఉత్తరప్రదేశ్):
సూక్ష్మశిలాయుగంలో విల్లంబులు, బాణాలు మరియు తుండి ఎముకను ఆయుధాలుగా ఉపయోగించినట్లు ఆనవాళ్ళు లభించిన ప్రాంతం. మొట్టమొదటగా కృత్రిమంగా గృహాల నిర్మాణం జరిగినట్లు ఆనవాళ్ళు లభించాయి — అనగా భారతదేశంలో తొలిసారిగా గృహాల నిర్మాణం ఈ యుగంలోనే జరిగిందని చరిత్రకారుల అభిప్రాయం.

మూడవది — ఆదాంగర్ (మధ్యప్రదేశ్):
పశుపోషణకు సంబంధించిన ఆధారాలు ఈ ప్రదేశంలో లభ్యమైనవి మరియు ఖడ్గమృగాన్ని వేటాడుతున్న చిత్రం కూడా ఇక్కడ లభించింది.

నాల్గవది — చోపాని మండో (ఉత్తరప్రదేశ్):
అనేక పురావస్తు ఆధారాల వలన తొలిసారిగా సూక్ష్మశిలాయుగంలో గుడిసెల వంటి నిర్మాణాలు, చదువైన నేలలు కల్లి ఉన్నట్లు ఆనవాళ్ళు బయల్పడిన ప్రాంతం. ఇక్కడ లభించిన చేతితో తయారైన కుండలను (Handmade Pottery) బట్టి మన దేశంలో మొదటగా కుండల తయారీ మధ్యశిలాయుగంలో ప్రారంభమైనట్లు తెలుస్తుంది.

అయిదవది — లంఫ్‌నాజ్ (గుజరాత్):
సూక్ష్మ శిలాయుగ పరికరాలు, అస్థిపంజరాలు మరియు జంతువుల అస్థికలతో బయల్పడిన తొలి ప్రాంతం.

ఇవి గుర్తుపెట్టుకోండి:
బగోర్ → దీర్ఘకాల స్థావరం.
సరాయ్ నహర్ రాయ్ → తొలి కృత్రిమ గృహాలు.
ఆదాంగర్ → పశుపోషణ + ఖడ్గమృగ చిత్రం.
చోపాని మండో → తొలి కుండల తయారీ (Handmade Pottery).
లంఫ్‌నాజ్ → సూక్ష్మ పరికరాలు + జంతు అస్థికలు.

Mini Recap: బగోర్ — దీర్ఘకాలం. సరాయ్ నహర్ రాయ్ — తొలి గృహాలు. చోపాని మండో — తొలి కుండలు. లంఫ్‌నాజ్ — అస్థిపంజరాలు."""
        },
        {
            "title": "నవీన శిలాయుగం — పరిచయం మరియు మెహర్‌గఢ్",
            "sub": "Neolithic Age · John Lubbock · Neolithic Revolution · Mehrgarh · Agriculture",
            "audio": """ఇప్పుడు నవీన శిలాయుగం లేదా కొత్త రాతియుగం అంటే Neolithic Age గురించి నేర్చుకుందాం.

జాన్ లుబ్బాక్ (John Lubbock) ఈ యుగానికి నామకరణం చేశాడు. ఈ యుగంలో అనేక విప్లవాత్మక మార్పులు చోటుచేసుకున్నాయని గోర్డన్ చైల్డ్ అన్నాడు — దాన్ని Neolithic Revolution అంటే నవీన శిలాయుగ విప్లవం అంటారు. భారత ఉపఖండంలో వాయువ్య దిశలో నవీన శిలాయుగం ఆవిర్భవించిన కచ్చీ మైదానాలలో (Kacchi Plains) — ప్రస్తుత పాకిస్తాన్, పశ్చిమ పాకిస్తాన్ మరియు బెలూచిస్తాన్‌కు వర్తిల్లింది.

నవీన శిలాయుగం యొక్క నాలుగు ప్రధాన లక్షణాలు గుర్తుపెట్టుకోండి:
మొదటిది — వ్యవసాయాన్ని చేపట్టడం. ముఖ్యమైన నోట్: చరిత్రకారుల ప్రకారం ప్రపంచంలో మొదటగా వ్యవసాయం చేపట్టిన ప్రదేశం — నైలు నది ప్రాంతం (ఈజిప్ట్).
రెండవది — పశుసంవరన మచ్చిక చేయడం.
మూడవది — రాతి పరికరాలను సానపెట్టడం (Polished Stone Tools).
నాల్గవది — మృణ్మయ పాత్రల తయారీ అంటే Pottery.

ఇప్పుడు అత్యంత ముఖ్యమైన మెహర్‌గఢ్ (Mehrgarh) గురించి:
ఇది భారత ఉపఖండంలో మొదటి, ప్రసిద్ధి చెందిన నవీన శిలాయుగ స్థావరం — ప్రస్తుత పాకిస్తాన్ బెలూచిస్తాన్‌లో ఉంది. జీన్-ఫ్రాంకోయిస్ జారిజ్ (Jean-Francois Jarrige) మొదటగా తవ్వకాలు జరిపి ఈ ప్రదేశాన్ని కనుగొన్నారు.

మెహర్‌గఢ్‌లో క్రీ.పూ. 4000 నాటికే మొదటగా బార్లీ, గోధుమలు మరియు పత్తిని పండించిన ఆనవాళ్ళు ఇక్కడ లభ్యమైనవి కావున దీనిని Bread Basket of Balochistan అంటారు. అనగా మొట్టమొదటగా వ్యవసాయాన్ని చేపట్టమైనది మరియు ప్రపంచంలో పత్తిని పండించిన మొట్టమొదటి ప్రజలు మెహర్‌గఢ్ ప్రజలే. అదే విధంగా కుమ్మరి చక్రంతో (Potter's Wheel) కుండలు చేసిన ఆధారాలు ఇక్కడ బయల్పడినవి. ఇక్కడి ప్రజలు మధ్య ఆసియాలో వెలసిన సమకాలీన నాగరికతా సంస్కృతులతో సాంఘికత్వాన్ని పెంచుకున్నారని తెలుస్తుంది.

Mini Recap: జాన్ లుబ్బాక్ — నవీన శిలాయుగానికి నామకరణం. గోర్డన్ చైల్డ్ — Neolithic Revolution. మెహర్‌గఢ్ — బెలూచిస్తాన్ — Bread Basket. తొలి పత్తి సాగు — మెహర్‌గఢ్. కుమ్మరి చక్రం ఇక్కడే మొదట."""
        },
        {
            "title": "నవీన శిలాయుగం — కాశ్మీర్ మరియు బీహార్ స్థావరాలు",
            "sub": "Burzahom · Gufkral · Pit Dwellings · Double Burial · Chirand",
            "audio": """ఇప్పుడు నవీన శిలాయుగపు ముఖ్య స్థావరాలు — ముఖ్యంగా కాశ్మీర్ మరియు బీహార్ స్థావరాల గురించి నేర్చుకుందాం.

బూర్జాహోమ్ (Burzahom — జమ్మూ & కాశ్మీర్):
ఇది జీలం నది ఒడ్డున వర్ధిల్లిన ప్రముఖ స్థావరం. బూర్జాహోమ్ అనగా కాశ్మీరీ భాషలో బిర్చ్ అనే వృక్షజాతి లేదా పుట్టిన చోటు అని అర్థం. బూర్జాహోమ్ విశిష్ట లక్షణాలుగా గుహాలలో జనావాసాలు అంటే Pit Dwellings మరియు యజమానితో పాటు కుక్కను ఖననం చేసే ద్వంద్వ ఖనన పద్ధతులు అంటే Double Burial System ఉండటం. ఇవి చాలా ముఖ్యమైన విషయాలు.

గుఫ్‌క్రల్ (Gufkral — జమ్మూ & కాశ్మీర్):
కాశ్మీర్‌లో వర్ధిల్లిన ప్రముఖ నవీన శిలాయుగ స్థావరం. గుఫ్‌క్రల్ అనే పదానికి కుమ్మరివాని గుహ అని అర్థం ఉంది. ఇక్కడ కుండల తయారీ, ఆహార ధాన్యాలు, పువ్వు దినుసులు మరియు ఖనన పద్ధతులు వంటి ఆధారాలు లభ్యమైనవి.

చోపాని మండో:
తొలి పురాతన ప్రాచీనశిలాయుగం నుండి నవీనశిలాయుగం వరకూ అన్ని యుగాలు కొనసాగిన ప్రాంతం.

చిరండ్ (Chirand — బీహార్):
ఇది బీహార్‌లోని సరణ్ జిల్లాలో ఉంది. ఎర్రమట్టితో చేసిన పాముబొమ్మ, ఎముకలతో చేసిన సూది మరియు ఆభరణాలు, బొమ్మలు, ఆయుధాలు లభ్యమయ్యాయి. అదే విధంగా వరి, గోధుమ మరియు బార్లీ పంటలు పండించినట్లు ఆనవాళ్ళు తెలుసుంది.

చాలా ముఖ్యమైన నోట్: ప్రపంచంలో మొట్టమొదటిసారిగా వరి పండించిన ప్రజలు నవీన శిలాయుగానికి చెందిన కోల్డీహవా ప్రజలు (ఉత్తరప్రదేశ్). ఇది పరీక్షలో తరచూ అడిగే విషయం.

నవీన శిలాయుగ ముఖ్య స్థావరాల పట్టిక:
జమ్మూ & కాశ్మీర్ — బూర్జాహోమ్, గుఫ్‌క్రల్.
కర్ణాటక — మస్కి, బ్రహ్మగిరి, తేక్కల్‌కోట, పిక్లిహాల్, హళ్ళూరు, థిరుమకుడాలు నరసిపురా, సంగనకళ్ళు.
తమిళనాడు — పియంపల్లి.
తెలంగాణ — ఉట్నూర్.
మేఘాలయ — గారో కొండలు.
బీహార్ — చిరండ్.
ఉత్తరప్రదేశ్ — మీర్జాపూర్, అలహాబాద్.

Mini Recap: బూర్జాహోమ్ — Pit Dwellings + Double Burial. గుఫ్‌క్రల్ — కుమ్మరివాని గుహ. చిరండ్ — బీహార్ — అలంకారాలు. తొలి వరి — కోల్డీహవా (UP)."""
        },
        {
            "title": "నవీన శిలాయుగం — దక్షిణ భారత స్థావరాలు",
            "sub": "South India Neolithic · Ash Mounds · Brahmagiri · Utnur · Sanganakallu",
            "audio": """ఇప్పుడు నవీన శిలాయుగపు దక్షిణ భారత స్థావరాల గురించి వివరంగా నేర్చుకుందాం.

దక్షిణ భారతంలో ఆధునిక లేదా నవీన శిలాయుగం క్రీస్తు పూర్వం 2000 సంవత్సరంలో ప్రారంభమైంది. అన్ని దక్షిణ భారతదేశ నవీన స్థావరాలలో సాధారణంగా బయల్పడిన ఉమ్మడి అంశంగా బూడిద దిబ్బలు (Ash Mounds) మరియు రాగులు మరియు ఉలవల పంట వ్యవసాయాన్ని గురించి చెప్పవచ్చు.

పెద్ద పెద్ద దుంగలతో చేసిన పదవలు లభించిన ప్రదేశాలు:
తెలంగాణ — ఉట్నూర్.
ఆంధ్రప్రదేశ్ — పాలవాయి, నాగార్జున కొండ.
తమిళనాడు — పియంపల్లి.
కర్ణాటక — తేక్కల్‌కోట, మస్కి, పిక్లిహాల్, బ్రహ్మగిరి, సంగనకళ్ళు.

సంగనకళ్ళు స్థావరంపై పరిశోధన చేసినది సుబ్బారావు కాగ. బ్రహ్మగిరి స్థావరంపై మోర్టిమర్ వీలర్ పరిశోధన చేశారు.

మస్కిలో చక్రంతో తయారు చేసిన కుండలు మరియు గుడి సెలు, ఎద్ద, గుండ్రా బొమ్మ బయల్పడ్డాయి. తేక్కల్‌కోట్‌లో బంగారు ఆభరణాలు మరియు ధాన్యాన్ని విసిరే తిరగలిరాయి లభించాయి.

నవీన శిలాయుగ స్థావరాల పూర్తి పట్టిక:
1. బూర్జాహోమ్ — జమ్మూ & కాశ్మీర్
2. గుఫ్‌క్రల్ — జమ్మూ & కాశ్మీర్
3. మస్కి — కర్ణాటక
4. బ్రహ్మగిరి — కర్ణాటక
5. తేక్కల్‌కోట — కర్ణాటక
6. పిక్లిహాల్ — కర్ణాటక
7. హళ్ళూరు — కర్ణాటక
8. థిరుమకుడాలు నరసిపురా — కర్ణాటక
9. సంగనకళ్ళు — కర్ణాటక
10. పియంపల్లి — తమిళనాడు
11. ఉట్నూర్ — తెలంగాణ
12. గారో కొండలు — మేఘాలయ
13. చిరండ్ — బీహార్
14. మీర్జాపూర్ — ఉత్తరప్రదేశ్
15. అలహాబాద్ — ఉత్తరప్రదేశ్

Mini Recap: దక్షిణ — 2000 BC నుండి. బూడిద దిబ్బలు ముఖ్య లక్షణం. బ్రహ్మగిరి — మోర్టిమర్ వీలర్. తేక్కల్‌కోట్ — బంగారు ఆభరణాలు. మొత్తం 15 ముఖ్య స్థావరాలు."""
        },
        {
            "title": "లోహాయుగం — తాంబ్ర శిలాయుగ సంస్కృతులు పరిచయం",
            "sub": "Metal Age · Chalcolithic · Copper · Harappa · Late Harappan Cultures",
            "audio": """ఇప్పుడు లోహాయుగం అంటే Metal Age గురించి, ముఖ్యంగా తాంబ్ర శిలాయుగ సంస్కృతులు గురించి నేర్చుకుందాం.

శిలాయుగ సంస్కృతుల తరువాత వర్ధిల్లింది లోహాయుగం. భూమి మీద మానవుడు ఉపయోగించిన తొలి లోహముగా రాగి (Copper)ని చెప్పవచ్చు. ప్రాచీన మానవుడు రాగిని వినియోగించినప్పటికీ శిలల వినియోగాన్ని ఆపలేదు. అందుకే తొలిదశ లోహ సంస్కృతులకు వచ్చిన పేరు తాంబ్ర శిలాయుగ సంస్కృతులు (Chalcolithic Cultures). సాంకేతిక పరిభాషలో CHALCO అంటే రాగి అని అర్థం.

భారత ఉపఖండంలో తాంబ్రశిలాయుగంలో వర్ధిల్లిన మహోన్నత నాగరికత సింధు లేదా హరప్పా నాగరికత. హరప్పా నాగరికత క్షీణతకు గురైనా సమకాలంగా కొన్ని తాంబ్ర శిలాయుగ సంస్కృతులు వర్ధిల్లటం గమనార్హం. ఆవిధంగా హరప్పా నాగరికతలో అభివృద్ధి చెందిన దశ తరువాత సంస్కృతులకే గల పేరు హారప్పానంతర సంస్కృతులు (Late Harappan Culture). పురావస్తు శాస్త్రవేత్త ప్రకారం హారప్పానంతర సంస్కృతులు క్రీ.పూ. 2000 నుండి క్రీ.పూ. 500 వరకు వర్ధిల్లినవి.

భారతదేశంలో వర్ధిల్లిన ప్రధాన హారప్పానంతర సంస్కృతుల జాబితా గుర్తుపెట్టుకోండి:
1. జుకర్ సంస్కృతి (Jhukar Culture)
2. ఝంగర్ సంస్కృతి (Jhangar Culture)
3. అహార్ లేదా బనాస్ సంస్కృతి
4. సాల్వదా సంస్కృతి
5. చిరాండ్ సంస్కృతి
6. మాల్వా సంస్కృతి
7. జోర్వే సంస్కృతి
8. కాయధా సంస్కృతి
9. దక్షిణ భారతదేశపు తాంబ్ర శిలాయుగ సంస్కృతి

ఈ సంస్కృతులన్నీ రాగి మరియు కుండల తయారీని ప్రధాన అంశాలుగా కలిగి ఉంటాయి. వివిధ ప్రాంతాలలో వివిధ రకాల కుండల రంగులు, ఆకారాలు మరియు పరికరాల ద్వారా ఒక్కొక్క సంస్కృతిని గుర్తిస్తారు. ఈ విభిన్న ప్రాంతాలలో వర్ధిల్లిన హారప్పానంతర సంస్కృతుల మధ్య భేదాన్ని గుర్తించడానికి ఉపకరించే అంశాలుగా రాగి లోహం మరియు కుండల తయారీ ప్రధాన పాత్ర పోషించాయి.

Mini Recap: రాగి = తొలి లోహం. CHALCO = రాగి. Chalcolithic = తాంబ్రశిలాయుగ. హారప్పానంతర సంస్కృతులు = Late Harappan — క్రీ.పూ. 2000 నుండి 500 వరకు. మొత్తం 9 ప్రధాన సంస్కృతులు."""
        },
        {
            "title": "జుకర్ సంస్కృతి మరియు ఝంగర్ సంస్కృతి",
            "sub": "Jhukar Culture · Jhangar Culture · Chanhu-daro · OCP · Copper Needles",
            "audio": """ఇప్పుడు మొదటి రెండు హారప్పానంతర సంస్కృతులు — జుకర్ మరియు ఝంగర్ గురించి వివరంగా నేర్చుకుందాం.

జుకర్ సంస్కృతి (Jhukar Culture):
జుకర్ సంస్కృతికి సంబంధించిన ప్రముఖ స్థావరాలు చాన్హుదారో (Chanhu-daro), జుకర్ మరియు అమి. ఇది పశ్చిమాసియాలోని సంస్కృతులతో అనేక సామీప్యతలు కల్గి ఉంది.

జుకర్ సంస్కృతిలో లక్షణాలు వివరంగా:
మొదటిది — కుండలు: గోధుమ లేదా మూడురు గోధుమ వర్ణం గల పాత్రలు వాడారు. గోధుమ వర్ణపు పాత్రపై ఎర్రని గీతలు ఉండినవి. గోధుమ వర్ణపు పాత్ర మీద ఆకృతులు చిత్రించిన పాత్రలనే Ochre-Coloured Pottery (OCP) అంటారు. ఇది చాలా పరీక్షలలో అడిగే విషయం.

రెండవది — పరికరాలు: ఈ సంస్కృతిలో వినియోగపడిన పరికరాలు — రాగితో తయారు చేయబడిన సూచులు అంటే Copper Needles, కంచు గొడ్డళ్ళు అంటే Bronze Axes, మరియు ముద్రికలు మరియు ఫేయాన్స్ అంటే Seals-Pheyans.

మూడవది — సంబంధాలు: ఈ సంస్కృతి పశ్చిమాసియాలోని అనేక సంస్కృతులతో సామీప్యతలు కలిగి ఉంది — ఇది అంతర్జాతీయ వ్యాపార సంబంధాలకు సూచన.

ఝంగర్ సంస్కృతి (Jhangar Culture):
సింధ ప్రాంతంలోని ఝంగర్‌లో బయల్పడిన హారప్పానంతర సంస్కృతియే ఝంగర్ సంస్కృతి. ఈ సంస్కృతి ఆనవాళ్ళు కూడా లభించిన స్థావరంగా చాన్హుదారో గుర్తించబడింది — అంటే చాన్హుదారోలో జుకర్ మరియు ఝంగర్ రెండూ లభించాయి. ఈ సంస్కృతిలో వినియోగించిన పాత్రలు గచ్చకాయ రంగువి.

ప్రముఖ హారప్పానంతర సంస్కృతి స్థావరము దైమాబాద్ (మహారాష్ట్ర). ఈ హారప్పానంతర సంస్కృతులు బయటకు వర్ధిల్లిన ప్రధాన తాంబ్ర శిలాయుగ సంస్కృతి స్థావరాలు నదిలోయల వెంబడి వర్ధిల్లినవి.

ఈ హారప్పానంతర సంస్కృతులతో బయటపడిన ప్రముఖ తాంబ్రశిలాయుగ సంస్కృతులు:
1. అహార్ లేదా బనాస్ సంస్కృతి
2. సాల్వదా సంస్కృతి
3. మాల్వా సంస్కృతి
4. జోర్వే సంస్కృతి
5. కాయధా సంస్కృతి
6. చిరాండ్ సంస్కృతి
7. దక్షిణ భారతదేశపు తాంబ్ర శిలాయుగ సంస్కృతి

Mini Recap: జుకర్ — చాన్హుదారో, జుకర్, అమి — OCP పాత్రలు + Copper Needles + Bronze Axes. ఝంగర్ — సింధ — గచ్చకాయ రంగు పాత్రలు — చాన్హుదారో కూడా. దైమాబాద్ — ప్రముఖ స్థావరం."""
        },
        {
            "title": "అహార్/బనాస్ మరియు సాల్వదా సంస్కృతులు",
            "sub": "Ahar-Banas Culture · Savalda Culture · Black Red Ware · Copper Tools",
            "audio": """ఇప్పుడు రెండు ముఖ్యమైన తాంబ్ర శిలాయుగ సంస్కృతుల గురించి నేర్చుకుందాం.

అహార్ లేదా బనాస్ సంస్కృతి (Ahar/Banas Culture, క్రీ.పూ. 1500):
ఇది భారతదేశంలో రాజస్థాన్ రాష్ట్రంలోని ఆగ్నేయ ప్రాంతాలలో వర్ధిల్లింది. సారవంతమైన బనాస్ బేరచ్-అహార్ నదీలోయల ప్రాంతంలో వర్ధిల్లిన సంస్కృతి. ఈ సంస్కృతికి అహార్-బనాస్ సంస్కృతి అని పేరువచ్చుటకు కారణం ఈ సంస్కృతిలో ప్రథమ స్థావరం అహార్ వద్ద బయల్పడటమే. కావున ఆర్కియాలజి ప్రకారం దీనిని Type Site అంటారు.

అహార్ సంస్కృతిలో వినియోగించిన విలక్షణమైన కుండలు నలుపు మరియు ఎరుపు రంగు కుండలు (Black & Red Ware). అహార్ సంస్కృతి బాగోర్, తాంబవతి లేదా గణేశ్వర్, గిలాండ్, బాలాతల్, ఓజియానా లలో ప్రతిబింబించింది. ఈ సంస్కృతిలో విస్తారంగా రాగి పనిముట్లు వినియోగించారు. ఖేత్రీ ప్రాంతంలో రాగి నిక్షేపాలను వీరు వాడారు.

ముఖ్యమైన Did You Know విషయాలు:
అత్యధిక సంఖ్యలో రాగి పనిముట్లు లభించిన ప్రదేశం — తాంబవతి.
రాగి పనిముట్లతోపాటు కొన్ని శిలా పరికరాలు కూడా లభించిన స్థావరం — గిలాండ్.
మట్టి ఇటుకలతోపాటు కాల్చిన ఇటుకల ఆనవాళ్ళు బయల్పడిన స్థావరం — గిలాండ్.

సాల్వదా సంస్కృతి (Savalda Culture):
ఇది తపతి మరియు ప్రవర నదీలోయలలో వెలసిల్లింది. గోధుమ, ఎరుపు, గోధుమ-ఉదా రంగులు కలసిన కుండలు ఈ సంస్కృతిలో వినియోగించినవి. ఇనామ్‌గావ్‌లో కాల్చిన మట్టితో చేయబడిన నాలుగు కాళ్ళ కుండలతో భూస్థాపితం చేసినట్లు ఆనవాళ్ళు బయల్పడ్డాయి. ఈ సంస్కృతిలో దీర్ఘచతురస్రాకార నివాస గృహాలు నిర్మించబడినవి (Rectangle Shaped Houses). బార్లీ, గోధుమ, చిక్కుడు, బాజ్రా, పెసలు, మినుమలు మరియు కందులు వంటి పంటలు పండించారు.

Mini Recap: అహార్/బనాస్ — రాజస్థాన్ — Black & Red Ware — Type Site అహార్. అత్యధిక రాగి — తాంబవతి. కాల్చిన ఇటుకలు — గిలాండ్. సాల్వదా — తపతి-ప్రవర నదులు — Rectangle Houses."""
        },
        {
            "title": "చిరాండ్, మాల్వా మరియు జోర్వే సంస్కృతులు",
            "sub": "Chirand Culture · Malwa Culture · Jorwe Culture · Inam Gaon · Daimabad",
            "audio": """ఇప్పుడు మూడు ముఖ్యమైన సంస్కృతులు — చిరాండ్, మాల్వా మరియు జోర్వే గురించి నేర్చుకుందాం.

చిరాండ్ సంస్కృతి (Chirand Culture, క్రీ.పూ. 1600):
ఇది తూర్పు భారతదేశంలో వెలసిల్లింది. ఈ ప్రస్తుతం బీహార్ రాష్ట్రంలో సరణ్ జిల్లాలో ఉన్న ఒక ప్రాంతం. ఇక్కడ తెల్లని పూత గల నలుపు మరియు ఎరుపు కుండలను ఉపయోగించారు. ఈ సంస్కృతిలో గోధుమ, బార్లీ వరి వంటి పంటలను పండించారు. పాక్షిక ఖననమును పాటించినట్లు ఆనవాళ్ళు పాండు రాజా దిబి (పశ్చిమ బెంగాల్)లో బయల్పడినవి. ఇది పశ్చిమ బెంగాల్‌లో కనుగొన్న మొదటి తాంబ్ర శిలాయుగ స్థావరం.

మాల్వా సంస్కృతి (Malwa Culture, క్రీ.పూ. 1700):
ఇది మధ్యప్రదేశ్ మరియు మహారాష్ట్రలోని పీఠ లోయలలో వెలసిల్లింది. తాంబ్ర శిలాయుగ సంస్కృతులలో మొదటిసారిగా పూతపోసిన కుండలను ఉపయోగించిందిమైది. ఈ సంస్కృతిలో ఉలులు, బానవు మొనలు, గాజాలు, టుంగరమూలు మరియు గాలాలు వంటి రాగి పనిముట్లను తయారు చేశారు. ముఖ్య స్థావరాలు: నవ్‌దతోలి (మహారాష్ట్ర), దైమాబాద్ (మహారాష్ట్ర), ఇనామ్‌గావ్ (మహారాష్ట్ర), నగోడా (మధ్యప్రదేశ్), విదిశ (మధ్యప్రదేశ్), ఎరాన్ (మధ్యప్రదేశ్).

Did You Know: క్రమపద్ధతిలో గృహ నిర్మాణం — ఇనామ్‌గావ్. రాగికంకణాలు, బంగారంతో చేయబడిన ఉంగరాలు — ఇనామ్‌గావ్. పండించిన పంటలు — బార్లీ, గోధుమ, వరి, జొన్న, బాజ్రా, మినకోలు, శనగలు.

జోర్వే సంస్కృతి (Jorwe Culture, క్రీ.పూ. 1400-700):
మాల్వా సంస్కృతి యొక్క కొనసాగింపు దశయే జోర్వే సంస్కృతి. మధ్య భారతదేశపు మరియు దక్కన్ పీఠభూమి ప్రాంతాల్లో వర్ధిల్లిన తాంబ్రశిలాయుగ స్థావరాలన్నిటిలో పెద్దవి జోర్వే (మహారాష్ట్ర) సంస్కృతి స్థావరాలు. ప్రధాన స్థావరాలుగా జోర్వే, నేవాసా, నాసిక్, నవ్‌దతోలి, దైమాబాద్, ఇనామ్‌గావ్. నారింజ రంగు కుండలు ఉపయోగించబడ్డాయి. అధిక భాగం మరణించిన వారిని పెద్ద కుండలలో ఉంచి పూడ్చిపెట్టుట ఒక ప్రత్యేక అంశం.

Did You Know: ఒక కోటగోడ వంటి నిర్మాణం బయల్పడిన స్థావరం — ఇనామ్‌గావ్. 100 కంటే ఎక్కువ ఇళ్ళు — ఇనామ్‌గావ్. ఈ సంస్కృతి దశకు చెందిన నాలుగు పెద్ద రాగి వస్తువులు లభించిన స్థావరం — దైమాబాద్.

Mini Recap: చిరాండ్ — బీహార్ — తెల్లని పూత కుండలు. మాల్వా — మొదట పూతపోసిన కుండలు — నవ్‌దతోలి. జోర్వే — నారింజ రంగు — పెద్ద కుండలలో ఖననం."""
        },
        {
            "title": "కాయధా సంస్కృతి మరియు దక్షిణ భారత తాంబ్ర శిలాయుగం",
            "sub": "Kayatha Culture · South India Chalcolithic · Kupgal · Piklihal · Rock Paintings",
            "audio": """ఇప్పుడు కాయధా సంస్కృతి మరియు దక్షిణ భారతదేశంలోని తాంబ్ర శిలాయుగ సంస్కృతుల గురించి నేర్చుకుందాం.

కాయధా సంస్కృతి (Kayatha Culture, క్రీ.పూ. 2000-1800):
మధ్యభారతదేశంలో చంబల్ నది లోయలో వెంబడి వర్ధిల్లింది. ఇది మధ్యప్రదేశ్ రాష్ట్రంలోని ఉజ్జయిని పట్టణానికి సమీపంగా ఉంది. ఈ సంస్కృతిలోగల మరొక ముఖ్య స్థావరంగా కాలీసింధ్ ను పిలుస్తారు. ఈ సంస్కృతిలో వినియోగించిన కుండలు వృత్తాకార ఆకృతిని కలిగి ఉన్నాయి.

దక్షిణ భారతదేశంలో తాంబ్ర శిలాయుగ సంస్కృతులు (Chalcolithic Cultures of South India):
దక్షిణ భారతదేశంలోని తాంబ్ర శిలాయుగ స్థావరాలలో రాతి, రాగి, కంచు పరికరాలతోపాటు ఎముకలతో చేసిన వస్తువులు లభించినవి. ఇక్కడ చదవైన గొడ్డళ్ళు, సూడంటు రాళ్ళు అనే లోహ పరికరాలు బయల్పడ్డాయి. అయితే ఇక్కడ కత్తుల పరిశ్రమ ప్రత్యేక పరిశ్రమగా అభివృద్ధి చెందింది. ఈ సంస్కృతులలో చిత్రాలు కుప్గల్, మస్కి, పిక్లిహాల్ లో గుర్తించబడ్డాయి.

ఈ స్థావరాలలో చిత్రించిన చిత్రాలలో అంశాలు ఒంటరిగా లేదా మందలతో ఉన్న జంతువులు. తాంబ్ర శిలాయుగంలో దక్షిణ భారతదేశంలో రాగులు, పప్పుదినుసులు పండించబడ్డాయి.

దక్షిణ భారతదేశంలో నవీన శిలాయుగంతో పాటు తాంబ్ర శిలాయుగం వర్ధిల్లింది. దక్షిణ భారత తాంబ్ర శిలాయుగ స్థావరాలు:
1. ఉట్నూర్ (తెలంగాణ)
2. పాల్వాయ్ (కర్ణాటక)
3. కోడేకల్ (కర్ణాటక)
4. కుప్గల్ (కర్ణాటక)
5. పిక్లిహాల్ (కర్ణాటక)
6. బ్రహ్మగిరి (కర్ణాటక)

Mini Recap: కాయధా — చంబల్ నది — ఉజ్జయిని సమీపం — వృత్తాకార కుండలు. దక్షిణ భారత తాంబ్రశిలాయుగం — కత్తుల పరిశ్రమ ప్రత్యేకత. చిత్రాలు — కుప్గల్, మస్కి, పిక్లిహాల్."""
        },
        {
            "title": "రాగి కుప్పెల సంస్కృతి మరియు గంగ-యమునా అంతర్వేది",
            "sub": "Copper Hoards · Upper Ganga-Yamuna Doab · Gangeria · B.B. Lal · OCP",
            "audio": """ఇప్పుడు ఎగువ గంగ-యమునా అంతర్వేది ప్రాంతంలో తాంబ్ర శిలాయుగ సంస్కృతుల గురించి నేర్చుకుందాం.

రాగి కుప్పెల సంస్కృతికి అనుబంధంగా ఉన్న రాగి హర్పూన్ (Copper Harpoon)ను మొదటగా బీతూర్ (ఉత్తరప్రదేశ్)లో 1822లో కనుగొన్నారు. ఈ విలక్షణమైన రాగి కుప్పెల సంస్కృతి విస్తరణ ఎగువగా మైదానముల నుండి గుజరాత్ వరకు మరియు హర్యానా నుండి కర్ణాటక వరకు జరిగింది.

ఎగువ గంగ-యమునా అంతర్వేది ప్రాంతంలో ఒకదానిని వెంట ఒకటి నడుస్తూ వర్ధిల్లినవి మూడు విధాలైన సంస్కృతులు:
1. రాగి కుప్పెలు (Copper Hoards)
2. ముదరు గోధుమ రంగు కుండల సంస్కృతి (Ochre-Coloured Pottery — OCP)
3. నలుపు మరియు ఎరుపు కుండల సంస్కృతి (Black and Red Ware — BRW)

రాగి కుప్పెల సంస్కృతి స్థావరాలు:
మధ్యప్రదేశ్ — గోండి, కలాన్స్ మరియు గంగేరియా (అతిపెద్దది).
దక్షిణ బీహార్ — హోమి మరియు బారాగుండా.
పశ్చిమ బెంగాల్ — తామాజురి.
ఒరిస్సా — దున్యా మరియు భగ్గా పీర్.
కర్ణాటక — కళ్ళూరు.
గుజరాత్ — లోథల్.

Did You Know — చాలా ముఖ్యమైన విషయాలు:
అత్యధిక సంఖ్యలో వస్తువులు లభించిన రాగి కుప్పెల సంస్కృతి స్థావరం — గంగేరియా (మధ్యప్రదేశ్). ఇది పరీక్షలో తరచూ అడుగుతారు.
పురాజీవ ఆకృతికి సంబంధించిన ఒక ముఖ్య మాత్రం లభ్యమైన స్థావరం — లోథల్.
ఈ రాగి కుప్పెల సంస్కృతికి సంబంధించి విశేష పరిశోధన చేసిన పురావస్తు శాస్త్రవేత్త — బి.బి. లాల్ (B.B. Lal).
రాగి కుప్పెల సంస్కృతితోపాటు ఈ స్థావరాలలో బయల్పడినవి గోధుమ రంగు కుండలు (OCP).

గోధుమరంగు పాత్రల సంస్కృతి (OCP, క్రీ.పూ. 2000-1500):
రాగి కుప్పెల (Copper Hoards Culture) సంస్కృతి స్థావరాలలో గోధుమ వర్ణం గల కుండలు బయల్పడినవి. కావున దీని OCP (Ochre Coloured Pottery) అంటారు. గోధుమ వర్ణపు కుండల సంస్కృతిని కనుగొని, నామకరణం చేసిన శాస్త్రవేత్తగా బి.బి.లాల్‌ను పిలుస్తారు. తొలిసారిగా ఈ సంస్కృతి ఉత్తరప్రదేశ్ నందలి రాజమూర్ (వరను) మరియు బిసోలిలో బయల్పడింది.

ప్రధాన OCP స్థావరాలు: బహదరాబాద్, రాజాపూర్‌వర్సను, బిసోలి, సాయ్‌పాయ్ (ఉత్తరప్రదేశ్).

Mini Recap: రాగి కుప్పెల — 1822 — బీతూర్. అత్యధిక వస్తువులు — గంగేరియా (MP). పరిశోధన — B.B. Lal. OCP = గోధుమ రంగు పాత్రలు — తొలిసారి — బిసోలి (UP)."""
        },
        {
            "title": "BRW సంస్కృతి మరియు ఇనుపయుగం",
            "sub": "Black Red Ware · Iron Age · PGW Culture · Aryans · Vedic Culture",
            "audio": """ఇప్పుడు నలుపు-ఎరుపు పాత్రల సంస్కృతి (BRW) మరియు ఇనుపయుగం గురించి నేర్చుకుందాం.

నలుపు మరియు ఎరుపు పాత్రల సంస్కృతి (BRW Culture):
ఇది మొదటిగా అతరంజీఖేరాలో కనుగొనబడింది. ఈ సంస్కృతి OCP మరియు PGW సంస్కృతుల మధ్యకాలంలో వర్ధిల్లింది. దీనిలో చక్రంతో కుండలను తయారు చేస్తారు. కుండను లోపలివైపు కాళ్ళ వలన లోపల నలుపు రంగు ఉండును. కాగా కుండ పైభాగం ఎరుపు రంగుతో పూత చేయబడింది. ఇది గంగ-యమునా అంతర్వేది ప్రాంతంలోనేకాక తూర్పు రాజస్థాన్‌లోని కొన్ని ప్రదేశాలలో కూడా వర్ధిల్లింది. రాజస్థాన్‌లో అహార్ మరియు గిలాండ్‌లో ఈ స్థావరాలు బయల్పడినవి. PGW సంస్కృతి కాలంలో కూడా వర్ధిల్లిన కొన్ని BRW సంస్కృతి స్థావరాలుగా హస్తినాపురం మరియు ఆలంగీర్‌పూర్ గురింపు పొందాయి.

ఆయో యుగం లేదా ఇనుపయుగం (Iron Age):
లోహయుగ పరిణామాలలో చివరి దశ ఆయో యుగం లేదా ఇనుపయుగం (Iron Age) ప్రారంభం. భారతదేశంలో ఇనుపయుగం దాదాపు క్రీ.పూ. 1000 సంవత్సరాల నుండి ప్రారంభమైంది. భారత ఉపఖండంలో ఇనుప లోహ వాడకాన్ని ప్రవేశపెట్టిన వారు ఆర్యులు.

ఇనుపయుగ నాగరికత, సంస్కృతులకు వేదసంస్కృతి చక్కటి ఉదాహరణ. లోహ, సాంకేతిక పరిజ్ఞానం అందుబాటులోకి రావడంతో వివిధ వృత్తులు, వ్యవసాయంలో ఇనుప నాగలి వాడకం, గొద్దలి, ఎద్దుల బండి, తూనికలు, ఒడెల నిర్మాణం, పరికరాల తయారీ వంటి రంగాలు ఎంతో అభివృద్ధి సాధించి, ఆధునాతనమైన సువ్యవస్థిత పట్టణ, గ్రామీణ జీవన విధానాలు ఒక దాని తరువాత ఒకటి వెలుగులోకి రావటం ఈ లోహయుగపు విశేషత.

భారతదేశంలో క్రీ.శ. 1946లో తొలిసారిగా ఇనుపయుగ సంస్కృతులు బయల్పడిన స్థావరంగా అహిచ్ఛత్రము లేదా అచ్చిచత్రము ఉండేది. అహిచ్ఛత్రాలో బయల్పడిన సంస్కృతిని PGW సంస్కృతి అంటారు. పెయింటెడ్ గ్రేవేర్ (PGW) అనగా గచ్చకాయ రంగు లేదా బూడిద వర్ణం గల పాత్రలు.

Mini Recap: BRW — అతరంజీఖేరా — OCP+PGW మధ్య కాలం. Iron Age — 1000 BC — ఆర్యులు ప్రవేశపెట్టారు. వేదసంస్కృతి — Iron Age ప్రతీక. PGW — అహిచ్ఛత్రం — 1946 — గచ్చకాయ రంగు పాత్రలు."""
        },
        {
            "title": "దక్షిణ భారత మొగాలిత్ సంస్కృతులు",
            "sub": "Megalithic Culture · Dolmens · Cysts · Menhirs · Sacrophagus · Mudumal",
            "audio": """ఇప్పుడు అత్యంత ముఖ్యమైన దక్షిణ భారతదేశంలోని మొగాలిత్ సంస్కృతులు (Megalithic Culture of South India) గురించి నేర్చుకుందాం.

ఇది దక్షిణ భారతదేశంలో తాంబ్ర శిలాయుగ సంస్కృతుల తదనంతరం వర్ధిల్లింది. స్థానిక పరిభాషలో మెగాలిత్‌లను రాక్షస గుళ్ళు (సమాధులు) అని అంటారు. రాక్షస గుళ్ళు అంటే పెద్ద రాళ్ళ లేదా పాండవ గుళ్ళు అని అర్థం. ఈ సంస్కృతి దక్షిణ భారతదేశంలో ఆయో యుగం (ఇనుపయుగం) సంస్కృతిని ప్రతిబింబింపజేస్తుంది. అందుకే ఈ మెగాలిత్ సంస్కృతిని బృహత్‌శిలా నిర్మాణాల యుగం అంటారు.

దక్షిణ భారతదేశంలో ఇనుపయుగానికి సంబంధించి బయల్పడిన మొట్టమొదటి స్థావరాలుగా కర్ణాటక రాష్ట్రంలోని పిక్లిహాల్ మరియు హళ్ళూరులను చెప్పారు.

బ్రూస్ ఫుట్, మోర్టిమర్ వీలర్, ఎస్.కృష్ణస్వామి అయ్యంగార్ దక్షిణ భారతదేశంలో పూర్వచారిత్రకయుగ మరియు చారిత్రకయుగ స్థావరాలకు సంబంధించి విస్తృత పరిశోధనలు నిర్వహించారు.

మెగాలిత్ సంస్కృతి స్థావరాలలో ఎరుపు-నలుపు కుండలు మరియు బూడిద రంగు కుండలను వినియోగించారు. మహారాష్ట్రలో బయల్పడిన జూనాపాని ప్రముఖ మెగాలిత్ సంస్కృతి స్థావరంగా ఉండేది.

తెలుగు రాష్ట్రాలలో జానంపేట, రాయగిరి, ఆలేశ్వరం, నాగార్జున కొండలో మరియు తమిళనాడులోని అదిచనల్లూర్‌లో మెగాలిత్ స్థావరాలు లభించాయి.

మెగాలిత్‌ రకాలు — ఇవి చాలా ముఖ్యమైనవి:

మొదటిది — శిలాపేటికలు (Dolmens): రాతి ఫలకాలతో పేటెను నిర్మించి, అందులో శవాన్ని ఉంచి, దానిపై రాతి ఫలకను మూతగా ఉంచడం.

రెండవది — ప్రస్తరికలు (Cysts): శిలాపేటికను భూమిలో పాతిపెట్టి దాని చుట్టూ భూమిపైన పెద్ద రాళ్ళను నాటడం.

మూడవది — శిలాస్తంభాలు (Menhirs): మృతుని పూడ్చిన చోటే నాటే శిలాస్తంభం.

నాల్గవది — శవకోష్టిక (Sacrophagus): మట్టితో వివిధ ఆకారాలలో శవపేటికలు నిర్మించి దానిలో మృతుని దేహాన్ని పూడ్చిపెట్టడం. కానీ ఈ శవపేటిక అడుగు భాగంలో 6 లేదా 8 కాళ్ళు ఉంటాయి. భారతదేశం అంతటిలో అద్వితీయమైన, అసమానమైన ఈ శవపేటిక కర్నూలు జిల్లాలోని శంఖవరంలో దొరికింది. గోరె ఆకారపు శవకోష్టిక — శంఖవరం (కర్నూలు).

ముదుమాల్ మెన్హీర్స్ (శిలాస్తంభాలు) — చాలా ముఖ్యమైన విషయం:
UNESCO ప్రపంచ వారసత్వ ప్రదేశాల తాత్కాలిక జాబితాలో (2024) తెలంగాణ రాష్ట్రం, నారాయణపేట జిల్లాలో కృష్ణనది ఒడ్డున ఉన్న ముదుమాల్‌కు చెందిన మెన్హీర్స్ చోటు సంపాదించింది. దక్షిణాసియాలోనే ఇలాంటి అమరిక ఉన్న అతిపెద్ద ప్రాంతం ఇది. ఇవి దాదాపు 3500-4000 సంవత్సరాల పురాతనమైనవి. స్థానిక ప్రజలు ఈ మెన్హీర్‌లను పవిత్రంగా భావిస్తారు. వీటిని నిలువరాల తిమ్మప్ప అని, ఇందులో ఒక మెన్హీర్‌ను ఎల్లమ్మ దేవతగా పూజిస్తారు.

Mini Recap: మెగాలిత్ = రాక్షస గుళ్ళు = పాండవ గుళ్ళు. నాలుగు రకాలు — Dolmens, Cysts, Menhirs, Sacrophagus. శంఖవరం (కర్నూలు) — ప్రత్యేక శవకోష్టిక. ముదుమాల్ — తెలంగాణ — UNESCO తాత్కాలిక జాబితా 2024."""
        },
        {
            "title": "యునెస్కో ప్రపంచ వారసత్వ ప్రదేశాలు",
            "sub": "UNESCO World Heritage Sites · India · 36 Cultural Sites · Bhimbetka · Taj Mahal",
            "audio": """చివరిగా, పరీక్షకు చాలా ఉపయోగపడే యునెస్కో ప్రపంచ వారసత్వ ప్రదేశాల గురించి నేర్చుకుందాం.

భారతదేశంలో ప్రస్తుతం 44 ప్రదేశాలను యునెస్కో వారు ప్రపంచ వారసత్వ ప్రదేశాలుగా గుర్తించగా, వాటిలో 36 సాంస్కృతికపరమైనవి, 7 సహజసిద్ధమైన ప్రదేశాలు మరియు 1 మిశ్రమ రకానికి చెందినది.

ముఖ్యమైన సాంస్కృతిక ప్రదేశాలు మరియు నోటిఫికేషన్ సంవత్సరాలు:
1983లో గుర్తించబడినవి — తాజ్‌మహాల్ (ఉత్తరప్రదేశ్), అజంతా గుహాలు (మహారాష్ట్ర), ఆగ్రా కోట (ఉత్తరప్రదేశ్), ఎల్లోరా గుహాలు (మహారాష్ట్ర).
1984లో — మహాబలిపురం స్మారక చిహ్నాల సమూహం (తమిళనాడు).
1986లో — కొణార్క్ సూర్యదేవాలయం (ఒడిషా), ఖజురహో శిల్పాలు మరియు నిర్మాణాలు (మధ్యప్రదేశ్), హంపిలో నిర్మాణాలు మరియు శిల్పాలు (కర్ణాటక), గోవాలోని చర్చిలు కాన్వెంట్లు, ఫతేపూర్ సిక్రీ (ఉత్తరప్రదేశ్).
1987లో — పట్టదకల్‌లో కట్టడాలు (కర్ణాటక), చోళపురం మరియు ధారాసురంలోని బృహదీశ్వరాలయం (తమిళనాడు 1987, 2004).
1989లో — సాంచీ బౌద్ధ కట్టడాలు (మధ్యప్రదేశ్).
1993లో — హుమాయూన్ సమాధి (ఢిల్లీ), కుతుబ్‌మినార్ మరియు సమీప కట్టడాలు (ఢిల్లీ).
1999లో — మహాబోధి ఆలయం — బోధ్‌గయ (బీహార్; 1999, 2005, 2008).
2003లో — భింబెట్కా రాతి గుహాలు (మధ్యప్రదేశ్). మనం ఈ అధ్యాయంలో చదివిన భింబెట్కా!
2004లో — చంపానేర్-పావాగడ్ పురావస్తు పార్క్ (గుజరాత్).
2010లో — జంతర్ మంతర్ (జైపూర్, రాజస్థాన్).
2014లో — నలందా పురావస్తు ప్రదేశం (బీహార్).
2019లో — రాంప్ప దేవాలయం రుద్రేశ్వర ఆలయం (తెలంగాణ). మన తెలంగాణ నుండి!
2021లో — ధోలవీర్: హరప్పా నగరం (గుజరాత్), హోయసల పవిత్ర భూండాలు (కర్ణాటక).
2023లో — శాంతినికేతన్ (పశ్చిమ బెంగాల్), మూయిదమ్మ-అహోమ్ రాజవంశం యొక్క దిబ్బ-ఖనన వ్యవస్థ (అసోం).
2024లో — మరాఠా మిలిటరీ ల్యాండ్‌స్కేప్స్ (మహారాష్ట్ర/తమిళనాడు).

గుర్తుపెట్టుకోవాల్సిన విశేషాలు: తెలంగాణ నుండి రాంప్ప దేవాలయం (2019) UNESCO గుర్తింపు పొందింది. ముదుమాల్ మెన్హీర్స్ తాత్కాలిక జాబితాలో (2024) ఉన్నాయి.

మొత్తం అధ్యాయం 2 రివ్యూ: ప్రి-హిస్టోరిక్ కల్చర్స్ అంటే — శిలాయుగం నుండి మొదలై, మెసోలిథిక్, నియోలిథిక్, చాల్కోలిథిక్, ఇనుపయుగం మరియు మొగాలిత్ వరకు మానవుని ప్రయాణం. ప్రతి సంస్కృతి ఒక మెట్టు — మానవుడు ఎదుగుతూ వచ్చిన చరిత్ర. బాగా చదవండి, విజయం సాధించండి!

Mini Recap: భారతదేశంలో 44 UNESCO ప్రదేశాలు — 36 సాంస్కృతిక. భింబెట్కా — 2003. రాంప్ప దేవాలయం — తెలంగాణ — 2019. ధోలవీర్ హరప్పా — 2021."""
        },
    ]

    db_exec(conn, '''INSERT INTO study_notes
        (subject, topic, chapter_num, chapter_title_te, chapter_title_en, pages_ref, sections_json)
        VALUES (?,?,?,?,?,?,?)''',
        ('GK', 'Indian_History', 2,
         'పూర్వచారిత్రక సంస్కృతులు',
         'Pre-Historic Cultures',
         '7-20',
         json.dumps(ch2_sections, ensure_ascii=False)))
    conn.commit()
    conn.close()
    return jsonify({'success': True, 'message': f'Chapter 2 (Pre-Historic Cultures) seeded with {len(ch2_sections)} sections!'})


@app.route('/api/mcq/seed_ch2', methods=['POST'])
def seed_ch2_mcqs():
    try:
        return _seed_ch2_mcqs_inner()
    except Exception as e:
        import traceback
        return jsonify({'success': False, 'error': str(e), 'trace': traceback.format_exc()}), 500

def _seed_ch2_mcqs_inner():
    conn = get_db()

    # Ensure chapter_mcqs table exists (matches Ch1 schema: difficulty INTEGER)
    if USE_POSTGRES:
        db_exec(conn, '''CREATE TABLE IF NOT EXISTS chapter_mcqs (
            id SERIAL PRIMARY KEY,
            study_note_id INTEGER NOT NULL,
            section_idx INTEGER NOT NULL,
            difficulty INTEGER NOT NULL DEFAULT 1,
            q_te TEXT NOT NULL,
            opt_a TEXT NOT NULL,
            opt_b TEXT NOT NULL,
            opt_c TEXT NOT NULL,
            opt_d TEXT NOT NULL,
            correct TEXT NOT NULL,
            explanation_te TEXT NOT NULL DEFAULT ''
        )''')
    else:
        db_exec(conn, '''CREATE TABLE IF NOT EXISTS chapter_mcqs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            study_note_id INTEGER NOT NULL,
            section_idx INTEGER NOT NULL,
            difficulty INTEGER NOT NULL DEFAULT 1,
            q_te TEXT NOT NULL,
            opt_a TEXT NOT NULL,
            opt_b TEXT NOT NULL,
            opt_c TEXT NOT NULL,
            opt_d TEXT NOT NULL,
            correct TEXT NOT NULL,
            explanation_te TEXT NOT NULL DEFAULT ""
        )''')

    # Find the Chapter 2 study note id
    cur = db_exec(conn, "SELECT id FROM study_notes WHERE topic='Indian_History' AND chapter_num=2")
    row = cur.fetchone()
    if not row:
        conn.close()
        return jsonify({'success': False, 'error': 'Chapter 2 study note not found. Please seed chapter 2 notes first.'}), 400
    note_id = row_to_dict(row)['id']

    # Delete existing MCQs for this chapter to avoid duplicates
    db_exec(conn, "DELETE FROM chapter_mcqs WHERE study_note_id=?", (note_id,))

    # 75 MCQs across 20 sections (sec 0-19), 3-4 per section
    mcqs = [
        # ── SEC 0: పరిచయం (3 Qs) ──────────────────────────────────────────────
        (0,1,
         'పూర్వచారిత్రక కాలాన్ని మూడు యుగాలుగా విభజించిన పండితుడు ఎవరు?',
         'జాన్ లుబ్బాక్','గోర్డన్ చైల్డ్','రాబర్ట్ బ్రూస్ ఫుట్','మోర్టిమర్ వీలర్',
         'B',
         'గోర్డన్ చైల్డ్ పూర్వచారిత్రక కాలాన్ని Pre-historic, Proto-historic, Historic అని మూడు యుగాలుగా విభజించారు.'),

        (0,1,
         'సింధు నాగరికత ఏ చారిత్రక విభాగంలోకి వస్తుంది?',
         'పూర్వచారిత్రక (Pre-historic)','ఆధునిక చరిత్ర','ప్రాచీన చారిత్రక (Proto-historic)','మధ్యకాలీన చరిత్ర',
         'C',
         'సింధు నాగరికత Proto-historic (ఆది చారిత్రక) కాలానికి చెందినది — లిపి చదవబడలేదు కాబట్టి పూర్తి చరిత్ర కాదు.'),

        (0,2,
         'పూర్వచారిత్రక కాలం అంటే ఏమిటి?',
         'లిపి ఆవిష్కరణ తర్వాత కాలం','లిఖిత ఆధారాలు లేని కాలం','వేద రచనల కాలం','సింధు నాగరికత కాలం',
         'B',
         'లిఖిత ఆధారాలు లేని కాలాన్ని Pre-historic (పూర్వచారిత్రక) కాలం అంటారు.'),

        # ── SEC 1: శిలాయుగ విభజన + ASI (4 Qs) ──────────────────────────────
        (1,1,
         'శిలాయుగాన్ని మూడు భాగాలుగా విభజించిన పండితుడు ఎవరు?',
         'కన్నింగ్‌హామ్','జాన్ లుబ్బాక్','C.J.థామ్‌సన్','గోర్డన్ చైల్డ్',
         'C',
         'డెన్మార్క్ పురావస్తు శాస్త్రవేత్త C.J.థామ్‌సన్ చారిత్రకపూర్వ యుగాన్ని శిలాయుగం (Stone Age), కంచు యుగం (Bronze Age), ఇనుప యుగం (Iron Age) అని మూడు భాగాలుగా విభజించారు.'),

        (1,2,
         'Archaeological Survey of India (ASI) ఏ సంవత్సరంలో స్థాపించబడింది?',
         '1850','1858','1861','1875',
         'C',
         'ASI 1861లో అలెగ్జాండర్ కన్నింగ్‌హామ్ నేతృత్వంలో స్థాపించబడింది.'),

        (1,1,
         'శిలాయుగంలో తొలిదశ పేరేమిటి?',
         'మెసోలిథిక్','నియోలిథిక్','పాలియోలిథిక్','చాల్కోలిథిక్',
         'C',
         'శిలాయుగంలో తొలిదశను పాలియోలిథిక్ (ప్రాచీన శిలాయుగం) అంటారు.'),

        (1,3,
         'ASIని స్థాపించిన తొలి డైరెక్టర్ జనరల్ ఎవరు?',
         'రాబర్ట్ బ్రూస్ ఫుట్','అలెగ్జాండర్ కన్నింగ్‌హామ్','H.D.సంకాలియా','జాన్ మార్షల్',
         'B',
         'అలెగ్జాండర్ కన్నింగ్‌హామ్ ASI యొక్క తొలి డైరెక్టర్ జనరల్.'),

        # ── SEC 2: ప్రాచీన శిలాయుగం పరిచయం (3 Qs) ──────────────────────────
        (2,1,
         'భారత పూర్వచారిత్రక శాస్త్ర పితామహుడిగా పేరొందిన వ్యక్తి ఎవరు?',
         'మోర్టిమర్ వీలర్','జాన్ మార్షల్','రాబర్ట్ బ్రూస్ ఫుట్','H.D.సంకాలియా',
         'C',
         'రాబర్ట్ బ్రూస్ ఫుట్ 1863లో పల్లవరం వద్ద తొలి పాలియోలిథిక్ పనిముట్టు కనుగొన్నారు — "Father of Indian Prehistory" అంటారు.'),

        (2,2,
         'భారతదేశంలో తొలి పాలియోలిథిక్ పనిముట్టు 1863లో ఎక్కడ కనుగొనబడింది?',
         'భింబెట్కా','అత్తిరాంపక్కం (పల్లవరం)','బాగోర్','సారై నహర్ రాయ్',
         'B',
         'రాబర్ట్ బ్రూస్ ఫుట్ 1863లో తమిళనాడులోని పల్లవరం (అత్తిరాంపక్కం) వద్ద తొలి పాలియోలిథిక్ పనిముట్టు కనుగొన్నారు.'),

        (2,2,
         'పాలియోలిథిక్ సంస్కృతిలో ముఖ్యంగా ఉపయోగించిన రాయి ఏది?',
         'గ్రానైట్','బసాల్ట్','క్వార్ట్‌జైట్','లైమ్‌స్టోన్',
         'C',
         'పాలియోలిథిక్ కాలంలో ముఖ్యంగా క్వార్ట్‌జైట్ రాయిని పనిముట్లకు ఉపయోగించారు — కాబట్టి దీన్ని Quartzite Culture అంటారు.'),

        # ── SEC 3: దిగువ ప్రాచీన శిలాయుగం (4 Qs) ──────────────────────────
        (3,2,
         'దిగువ పాలియోలిథిక్ కాలం ఎంత కాలానికి చెందినది?',
         '10 లక్షల నుండి 1 లక్ష సంవత్సరాల క్రితం','50,000 నుండి 10,000 క్రితం','5 లక్షల నుండి 50,000 క్రితం','20 లక్షల నుండి 5 లక్షల క్రితం',
         'A',
         'దిగువ పాలియోలిథిక్ కాలం దాదాపు 10 లక్షల సంవత్సరాల నుండి 1 లక్ష సంవత్సరాల క్రితం వరకు ఉంటుంది.'),

        (3,1,
         'దిగువ పాలియోలిథిక్ కాలంలో ఉపయోగించిన ముఖ్య పనిముట్టు ఏది?',
         'మైక్రోలిత్‌లు','హ్యాండ్ ఆక్సెస్ మరియు చాపింగ్ స్టోన్స్','పాట్టరీ','లోహ ఆయుధాలు',
         'B',
         'దిగువ పాలియోలిథిక్ కాలంలో Hand Axes (హ్యాండ్ ఆక్సెస్) మరియు Chopping Stones (చాపింగ్ స్టోన్స్) ముఖ్య పనిముట్లు.'),

        (3,3,
         'పాహల్‌గామ్ ఏ రాష్ట్రంలో ఉంది మరియు ఏ కాలానికి చెందిన స్థావరం?',
         'హిమాచల్ ప్రదేశ్ — మెసోలిథిక్','కాశ్మీర్ — దిగువ పాలియోలిథిక్','ఉత్తరప్రదేశ్ — నియోలిథిక్','రాజస్థాన్ — చాల్కోలిథిక్',
         'B',
         'పాహల్‌గామ్ కాశ్మీర్‌లో దిగువ పాలియోలిథిక్ కాలానికి చెందిన ముఖ్యమైన స్థావరం.'),

        (3,2,
         'దిగువ పాలియోలిథిక్ కాలంలో జీవించిన మానవ జాతి ఏది?',
         'హోమో సేపియన్స్','హోమినిడ్లు','హోమో ఎరెక్టస్','ఆధునిక మానవుడు',
         'B',
         'దిగువ పాలియోలిథిక్ కాలంలో హోమినిడ్లు (Hominids) జీవించేవారు.'),

        # ── SEC 4: భింబెట్కా గుహాలు (4 Qs) ──────────────────────────────────
        (4,1,
         'భింబెట్కా గుహాలు ఏ రాష్ట్రంలో ఉన్నాయి?',
         'ఉత్తరప్రదేశ్','రాజస్థాన్','మధ్యప్రదేశ్','మహారాష్ట్ర',
         'C',
         'భింబెట్కా గుహాలు మధ్యప్రదేశ్‌లో రాయ్‌సేన్ జిల్లాలో ఉన్నాయి.'),

        (4,2,
         'భింబెట్కా గుహాలను ఏ సంవత్సరంలో, ఎవరు కనుగొన్నారు?',
         '1950 — మోర్టిమర్ వీలర్','1963 — H.D.సంకాలియా','1957 — V.S.వాకణ్కర్','1947 — రాబర్ట్ బ్రూస్ ఫుట్',
         'C',
         'V.S.వాకణ్కర్ 1957లో భింబెట్కా గుహాలను కనుగొన్నారు.'),

        (4,1,
         'భింబెట్కా గుహాలు UNESCO వారసత్వ ప్రదేశంగా ఏ సంవత్సరంలో గుర్తించబడ్డాయి?',
         '1983','1993','2003','2013',
         'C',
         'భింబెట్కా గుహాలు 2003లో UNESCO ప్రపంచ వారసత్వ ప్రదేశంగా గుర్తించబడ్డాయి.'),

        (4,2,
         'భింబెట్కా గుహాల్లో ఏ రకమైన చిత్రాలు కనుగొనబడ్డాయి?',
         'శిలా శాసనాలు','వేట, జంతువుల రాతి చిత్రాలు','లోహపు ముద్రలు','మట్టి బొమ్మలు',
         'B',
         'భింబెట్కా గుహాల్లో వేటాడటం, జంతువులు, నృత్యాలు చిత్రించిన రాక్ పెయింటింగ్‌లు ఉన్నాయి.'),

        # ── SEC 5: మధ్య + ఎగువ పాలియోలిథిక్ (4 Qs) ────────────────────────
        (5,2,
         'మధ్య పాలియోలిథిక్ కాలంలో నేవాసా సంస్కృతిని అధ్యయనం చేసిన పండితుడు ఎవరు?',
         'గోర్డన్ చైల్డ్','V.S.వాకణ్కర్','H.D.సంకాలియా','రాబర్ట్ బ్రూస్ ఫుట్',
         'C',
         'H.D.సంకాలియా మహారాష్ట్రలోని నేవాసా వద్ద మధ్య పాలియోలిథిక్ పరిశోధనలు నిర్వహించారు.'),

        (5,1,
         'ఎగువ పాలియోలిథిక్ కాలంలో ఆవిర్భవించిన మానవ జాతి ఏది?',
         'హోమినిడ్లు','హోమో ఎరెక్టస్','హోమో సేపియన్స్','నియాండర్తల్',
         'C',
         'ఎగువ పాలియోలిథిక్ (Upper Palaeolithic) కాలంలో ఆధునిక మానవుడైన హోమో సేపియన్స్ ఆవిర్భవించాడు.'),

        (5,3,
         'మహారాష్ట్రలోని పాటన్ వద్ద పాలియోలిథిక్ కాలానికి చెందిన ఏ అద్భుతమైన ఆధారం కనుగొనబడింది?',
         'బంగారు ఆభరణాలు','నిడుపాటి శవకోష్టిక','ఆస్ట్రిచ్ గుడ్డు పెంకులు','మట్టి ముద్రలు',
         'C',
         'మహారాష్ట్రలోని పాటన్ వద్ద ఆస్ట్రిచ్ (ఉష్ట్రపక్షి) యొక్క పెంకుతో చేసిన పూసలు కనుగొనబడ్డాయి — ఎగువ ప్రాచీన శిలాయుగానికి చెందిన ముఖ్యమైన ఆధారాలు.'),

        (5,2,
         'మధ్య పాలియోలిథిక్ కాలంలో జీవించిన మానవ జాతి ఏది?',
         'హోమో ఎరెక్టస్','హోమో సేపియన్స్','హోమినిడ్లు','క్రో-మాగ్నాన్',
         'A',
         'మధ్య పాలియోలిథిక్ కాలంలో హోమో ఎరెక్టస్ జీవించేవారు.'),

        # ── SEC 6: మెసోలిథిక్ పరిచయం (4 Qs) ────────────────────────────────
        (6,1,
         'మెసోలిథిక్ కాలంలో ఉపయోగించిన చిన్న పనిముట్ల పేరేమిటి?',
         'మైక్రోలిత్‌లు','మెగాలిత్‌లు','హ్యాండ్ ఆక్సెస్','డోల్మెన్లు',
         'A',
         'మెసోలిథిక్ కాలంలో 1-8 సెం.మీ. పొడవుండే చిన్న పనిముట్లను మైక్రోలిత్‌లు అంటారు.'),

        (6,2,
         'మెసోలిథిక్ కాలంలో సమాధి స్థావరాలు ఆంధ్రప్రదేశ్‌లో ఎక్కడ కనుగొనబడ్డాయి?',
         'అమరావతి మరియు నాగార్జునకొండ','కర్నూలు మరియు రేణిగుంట','హంపి మరియు బళ్లారి','ఏలూరు మరియు విజయవాడ',
         'B',
         'మెసోలిథిక్ కాలానికి చెందిన సమాధి స్థావరాలు (Burial Grounds) కర్నూలు మరియు రేణిగుంటలో కనుగొనబడ్డాయి.'),

        (6,2,
         'మెసోలిథిక్ కాలం ఏ భూగర్భ శాస్త్ర యుగంలో ఉంది?',
         'ప్లీస్టోసీన్','హోలోసీన్','మయోసీన్','పీలియోసీన్',
         'B',
         'మెసోలిథిక్ కాలం హోలోసీన్ (Holocene) భూగర్భ శాస్త్ర యుగంలో ఉంది — దాదాపు 10,000 సంవత్సరాల క్రితం మొదలైంది.'),

        (6,3,
         'కుక్కను పెంపుడు జంతువుగా మొట్టమొదట పెంచిన ఆధారం ఏ మెసోలిథిక్ స్థావరంలో దొరికింది?',
         'సారై నహర్ రాయ్','చోపాని మాండో','బాగోర్','అడంగూర్',
         'C',
         'రాజస్థాన్‌లోని బాగోర్‌లో క్రీ.పూ. 5000కు చెందిన కుక్క అస్థిపంజరం కనుగొనబడింది — భారతదేశంలో కుక్క పెంపకానికి తొలి ఆధారం.'),

        # ── SEC 7: మెసోలిథిక్ స్థావరాలు (4 Qs) ─────────────────────────────
        (7,1,
         'మెసోలిథిక్ కాలంలో మొట్టమొదటి ఇళ్ళు నిర్మించిన స్థావరం ఏది?',
         'బాగోర్','అడంగూర్','చోపాని మాండో','సారై నహర్ రాయ్',
         'D',
         'ఉత్తరప్రదేశ్‌లోని సారై నహర్ రాయ్‌లో మెసోలిథిక్ కాలపు మొట్టమొదటి ఇళ్ళ ఆధారాలు కనుగొనబడ్డాయి.'),

        (7,2,
         'మెసోలిథిక్ కాలంలో మొట్టమొదటి కుమ్మరి పాత్రలు ఏ స్థావరంలో కనుగొనబడ్డాయి?',
         'సారై నహర్ రాయ్','బాగోర్','చోపాని మాండో','లన్‌ఫూనాజ్',
         'C',
         'ఉత్తరప్రదేశ్‌లోని చోపాని మాండో మెసోలిథిక్ కాలంలో మొట్టమొదటి పాట్టరీ (కుమ్మరి పాత్రలు) కనుగొన్న స్థావరం.'),

        (7,3,
         'ఖడ్గమృగం (Rhinoceros) చిత్రానికి ప్రసిద్ధి పొందిన మెసోలిథిక్ స్థావరం ఏది?',
         'బాగోర్','అడంగూర్','చోపాని మాండో','సారై నహర్ రాయ్',
         'B',
         'ఆంధ్రప్రదేశ్‌లోని అడంగూర్ ఖడ్గమృగం (Rhinoceros) రాక్ పెయింటింగ్‌కు ప్రసిద్ధి.'),

        (7,1,
         'భారతదేశంలో దీర్ఘకాలం నివాసం ఉన్న మెసోలిథిక్ స్థావరం ఏది?',
         'సారై నహర్ రాయ్','అడంగూర్','చోపాని మాండో','బాగోర్',
         'D',
         'రాజస్థాన్‌లోని బాగోర్ భారతదేశంలో అతిదీర్ఘకాలం నివాసం ఉన్న (longest occupied) మెసోలిథిక్ స్థావరం.'),

        # ── SEC 8: నియోలిథిక్ + మెహర్‌గఢ్ (4 Qs) ───────────────────────────
        (8,1,
         '"నియోలిథిక్" అనే పదాన్ని మొట్టమొదట ఉపయోగించిన పండితుడు ఎవరు?',
         'గోర్డన్ చైల్డ్','C.J.థామ్‌సన్','జాన్ లుబ్బాక్','అలెగ్జాండర్ కన్నింగ్‌హామ్',
         'C',
         'జాన్ లుబ్బాక్ "Neolithic" అనే పదాన్ని మొట్టమొదట ఉపయోగించారు.'),

        (8,2,
         '"Bread Basket of Ancient India" అని పిలువబడే స్థావరం ఏది?',
         'మొహెంజోదారో','హరప్పా','మెహర్‌గఢ్','లోతల్',
         'C',
         'మెహర్‌గఢ్‌ను "Bread Basket of Ancient India" అంటారు — ఇక్కడ తొలి వ్యవసాయ ఆధారాలు కనుగొనబడ్డాయి.'),

        (8,3,
         'ప్రపంచంలో మొట్టమొదటి పత్తి పంట ఆధారాలు ఏ స్థావరంలో కనుగొనబడ్డాయి?',
         'హరప్పా','మొహెంజోదారో','మెహర్‌గఢ్','కాలీబంగన్',
         'C',
         'మెహర్‌గఢ్‌లో ప్రపంచంలో మొట్టమొదటి పత్తి పంట (Cotton Cultivation) ఆధారాలు కనుగొనబడ్డాయి.'),

        (8,2,
         'మెహర్‌గఢ్ తవ్వకాలు నిర్వహించిన ఫ్రెంచ్ పురావస్తు శాస్త్రవేత్త ఎవరు?',
         'H.D.సంకాలియా','మోర్టిమర్ వీలర్','జాన్-ఫ్రాంకోయిస్ జారిజ్','V.S.వాకణ్కర్',
         'C',
         'మెహర్‌గఢ్ తవ్వకాలు జాన్-ఫ్రాంకోయిస్ జారిజ్ నేతృత్వంలో 1974 నుండి నిర్వహించబడ్డాయి.'),

        # ── SEC 9: కాశ్మీర్ + బీహార్ నియోలిథిక్ (4 Qs) ─────────────────────
        (9,1,
         'బుర్జాహోమ్‌లో ఏ విశేషమైన నియోలిథిక్ ఆనవాళ్ళు కనుగొనబడ్డాయి?',
         'అగ్ని కుండాలు','గుఫ్కల్ గుహలు','గుంతల నివాసాలు మరియు డబుల్ బేరియల్','పాత్ర సమాధులు',
         'C',
         'కాశ్మీర్‌లోని బుర్జాహోమ్‌లో గుంతల నివాసాలు (Pit Dwellings) మరియు డబుల్ బేరియల్ (మానవుడు-జంతువు కలిసి సమాధి) కనుగొనబడ్డాయి.'),

        (9,2,
         '"కుమ్మరి గుహ" అని అర్థం వచ్చే నియోలిథిక్ స్థావరం ఏది?',
         'బుర్జాహోమ్','చిరాండ్','కొల్దిహ్వా','గుఫ్కల్',
         'D',
         'కాశ్మీర్‌లోని గుఫ్కల్ (Gufkral) అంటే "కుమ్మరి గుహ" అని అర్థం. ఇది ముఖ్యమైన నియోలిథిక్ స్థావరం.'),

        (9,3,
         'భారతదేశంలో తొలి వరి పంట ఆధారాలు ఏ స్థావరంలో కనుగొనబడ్డాయి?',
         'చిరాండ్ (బీహార్)','మెహర్‌గఢ్','కొల్దిహ్వా (ఉత్తరప్రదేశ్)','బుర్జాహోమ్ (కాశ్మీర్)',
         'C',
         'ఉత్తరప్రదేశ్‌లోని కొల్దిహ్వాలో భారతదేశంలో తొలి వరి పంట (Rice Cultivation) ఆధారాలు కనుగొనబడ్డాయి.'),

        (9,2,
         'బీహార్‌లో నియోలిథిక్ కాలానికి చెందిన ముఖ్యమైన స్థావరం ఏది?',
         'బాగోర్','బుర్జాహోమ్','చిరాండ్','నేవాసా',
         'C',
         'బీహార్‌లో నియోలిథిక్ కాలానికి చెందిన ముఖ్యమైన స్థావరం చిరాండ్ (Chirand).'),

        # ── SEC 10: దక్షిణ భారత నియోలిథిక్ (3 Qs) ─────────────────────────
        (10,1,
         'దక్షిణ భారతదేశంలో నియోలిథిక్ స్థావరాలకు సంబంధించిన అత్యంత విలక్షణమైన లక్షణం ఏది?',
         'బంగారు ఆభరణాలు','నల్ల మరియు ఎరుపు పాత్రలు','బూడిద దిబ్బలు (Ash Mounds)','రాతి గుహలు',
         'C',
         'దక్షిణ భారతదేశంలో నియోలిథిక్ స్థావరాలకు బూడిద దిబ్బలు (Ash Mounds) విలక్షణ లక్షణం.'),

        (10,2,
         'దక్షిణ భారతదేశంలో నియోలిథిక్ స్థావరాలను పరిశోధించిన ప్రముఖ పండితుడు ఎవరు మరియు ఏ స్థావరం?',
         'H.D.సంకాలియా — నేవాసా','మోర్టిమర్ వీలర్ — బ్రహ్మగిరి','రాబర్ట్ బ్రూస్ ఫుట్ — మద్రాస్','V.S.వాకణ్కర్ — సాంచీ',
         'B',
         'మోర్టిమర్ వీలర్ కర్ణాటకలోని బ్రహ్మగిరి వద్ద దక్షిణ భారత నియోలిథిక్ పరిశోధనలు నిర్వహించారు.'),

        (10,3,
         'నియోలిథిక్ కాలానికి చెందిన బంగారు ఆభరణాలు ఏ స్థావరంలో కనుగొనబడ్డాయి?',
         'బ్రహ్మగిరి','టేక్కలకోట','హళ్ళూర్','పిక్లిహాల్',
         'B',
         'కర్ణాటకలోని టేక్కలకోట (Teklakota) వద్ద నియోలిథిక్ కాలానికి చెందిన బంగారు ఆభరణాలు కనుగొనబడ్డాయి.'),

        # ── SEC 11: లోహాయుగం పరిచయం (3 Qs) ─────────────────────────────────
        (11,1,
         'మానవుడు మొట్టమొదట వినియోగించిన లోహం ఏది?',
         'ఇనుము','బంగారం','రాగి (కాపర్)','కాంస్యం',
         'C',
         'మానవుడు మొట్టమొదట వినియోగించిన లోహం రాగి (Copper) — కాబట్టి ఈ కాలాన్ని "చాల్కోలిథిక్" అంటారు.'),

        (11,2,
         '"చాల్కోలిథిక్" అనే పదంలో "చాల్కో" అంటే ఏమిటి?',
         'ఇనుము','రాగి (కాపర్)','కాంస్యం','బంగారం',
         'B',
         'చాల్కోలిథిక్ అనే పదం గ్రీకు పదాల నుండి వచ్చింది: చాల్కో = రాగి (Copper), లిథోస్ = రాయి (Stone).'),

        (11,3,
         'భారతదేశంలో చాల్కోలిథిక్ (Late Harappan) సంస్కృతులు ఏ కాలానికి చెందినవి?',
         'క్రీ.పూ. 5000-3000','క్రీ.పూ. 2000-500','క్రీ.పూ. 3500-2500','క్రీ.పూ. 1000-500',
         'B',
         'భారతదేశంలో చాల్కోలిథిక్ (Late Harappan) సంస్కృతులు దాదాపు క్రీ.పూ. 2000-500 కాలానికి చెందినవి.'),

        # ── SEC 12: జుకర్ + ఝంగర్ (4 Qs) ───────────────────────────────────
        (12,2,
         'జుకర్ సంస్కృతి ముఖ్యంగా ఏ స్థావరంతో సంబంధం కలిగి ఉంది?',
         'మొహెంజోదారో','హరప్పా','చాన్హు-దారో','కాలీబంగన్',
         'C',
         'జుకర్ సంస్కృతి చాన్హు-దారో, జుకర్, అమ్రి స్థావరాలతో సంబంధం కలిగి ఉంది — చాన్హు-దారో ముఖ్య స్థావరం.'),

        (12,1,
         'OCP (Ochre Coloured Pottery) యొక్క రంగు ఏమిటి?',
         'నలుపు','గేరు రంగు (ఎరుపు-నారింజ)','నీలం','పసుపు',
         'B',
         'OCP అంటే Ochre Coloured Pottery — గేరు రంగు (ఎరుపు-నారింజ) పాత్రలు.'),

        (12,3,
         'ఝంగర్ సంస్కృతిలో వాడిన పాత్రల రంగు ఏమిటి?',
         'నల్ల మరియు ఎరుపు','తెలుపు మరియు నీలం','గచ్చకాయ రంగు','నారింజ రంగు',
         'C',
         'ఝంగర్ సంస్కృతిలో గచ్చకాయ రంగు (Gachkaya color) పాత్రలు వాడేవారు.'),

        (12,2,
         'మహారాష్ట్రలోని డైమాబాద్‌లో కనుగొన్న నాలుగు పెద్ద కాంస్య శిల్పాలు ఏ సంస్కృతికి చెందినవి?',
         'జుకర్ సంస్కృతి','అహార్ సంస్కృతి','జోర్వే సంస్కృతి','మాల్వా సంస్కృతి',
         'C',
         'డైమాబాద్ జోర్వే సంస్కృతికి చెందిన స్థావరం — ఇక్కడ 4 పెద్ద కాంస్య శిల్పాలు కనుగొనబడ్డాయి.'),

        # ── SEC 13: అహార్/బనాస్ + సాల్వదా (4 Qs) ───────────────────────────
        (13,1,
         'అహార్ సంస్కృతికి మరొక పేరేమిటి?',
         'జోర్వే సంస్కృతి','బనాస్ సంస్కృతి','మాల్వా సంస్కృతి','కాయధా సంస్కృతి',
         'B',
         'అహార్ సంస్కృతిని బనాస్ సంస్కృతి అని కూడా పిలుస్తారు.'),

        (13,2,
         'అహార్ సంస్కృతిలో అత్యధిక రాగి వస్తువులు ఏ స్థావరంలో కనుగొనబడ్డాయి?',
         'అహార్','గిలాండ్','తాంబావతి','బనాస్',
         'C',
         'అహార్ సంస్కృతిలో అత్యధిక రాగి వస్తువులు తాంబావతి (Tambavati) స్థావరంలో కనుగొనబడ్డాయి.'),

        (13,3,
         'అహార్ సంస్కృతిలో కాల్చిన ఇటుక నిర్మాణాలు ఏ స్థావరంలో బయల్పడ్డాయి?',
         'అహార్','తాంబావతి','గిలాండ్','దైమాబాద్',
         'C',
         'అహార్ సంస్కృతిలో కాల్చిన ఇటుక నిర్మాణాలు (Burnt Bricks) గిలాండ్ (Gilaund) స్థావరంలో బయల్పడ్డాయి.'),

        (13,2,
         'సాల్వదా సంస్కృతి ఏ నదుల మధ్య వ్యాపించి ఉంది?',
         'గంగ మరియు యమునా','కావేరి మరియు కృష్ణ','తాపి మరియు ప్రవర','గోదావరి మరియు తుంగభద్ర',
         'C',
         'సాల్వదా సంస్కృతి మహారాష్ట్రలో తాపి-ప్రవర నదుల మధ్య వ్యాపించి ఉంది.'),

        # ── SEC 14: మాల్వా + జోర్వే + ఇనామ్‌గావ్ (4 Qs) ────────────────────
        (14,2,
         'మొట్టమొదటి కాల్చిన పాత్రలు (First Fired Pottery) ఏ చాల్కోలిథిక్ సంస్కృతికి చెందినవి?',
         'జోర్వే సంస్కృతి','అహార్ సంస్కృతి','మాల్వా సంస్కృతి','కాయధా సంస్కృతి',
         'C',
         'మాల్వా సంస్కృతి మొట్టమొదటి కాల్చిన పాత్రలకు (First Fired Pottery) ప్రసిద్ధి.'),

        (14,1,
         'జోర్వే సంస్కృతిలో పాత్రల రంగు ఏమిటి?',
         'నల్ల మరియు ఎరుపు','నారింజ రంగు','గేరు రంగు','తెలుపు',
         'B',
         'జోర్వే సంస్కృతి నారింజ రంగు (Orange Pottery) పాత్రలకు ప్రసిద్ధి.'),

        (14,3,
         'జోర్వే సంస్కృతిలో మృతదేహాలను ఎలా పూడ్చేవారు?',
         'అగ్నిసంస్కారం చేసేవారు','నదిలో వదిలేవారు','పెద్ద మట్టి పాత్రల్లో పూడ్చేవారు','శిలాస్తంభాలు నాటేవారు',
         'C',
         'జోర్వే సంస్కృతిలో మృతదేహాలను పెద్ద మట్టి పాత్రలు (Large Pots)లో పూడ్చేవారు.'),

        (14,2,
         'ఇనామ్‌గావ్ (Inam Gaon) ఏ సంస్కృతికి చెందిన స్థావరం మరియు దానికి ప్రత్యేకత ఏమిటి?',
         'మాల్వా సంస్కృతి — తొలి పాత్రలు','అహార్ సంస్కృతి — బంగారు ఆభరణాలు','జోర్వే సంస్కృతి — కోట లాంటి నిర్మాణం','కాయధా సంస్కృతి — రాతి చిత్రాలు',
         'C',
         'ఇనామ్‌గావ్ జోర్వే సంస్కృతికి చెందినది — ఇక్కడ కోట వంటి నిర్మాణ ఆధారాలు కనుగొనబడ్డాయి.'),

        # ── SEC 15: కాయధా + దక్షిణ భారత చాల్కోలిథిక్ (3 Qs) ──────────────
        (15,2,
         'కాయధా (Kayatha) సంస్కృతి ఏ నదీ తీరంలో ఉంది?',
         'నర్మదా','గోదావరి','కావేరి','చంబల్',
         'D',
         'కాయధా సంస్కృతి మధ్యప్రదేశ్‌లో ఉజ్జయిని సమీపంలో చంబల్ నది తీరంలో వ్యాపించి ఉంది.'),

        (15,1,
         'దక్షిణ భారత చాల్కోలిథిక్ కాలపు రాతి చిత్రాలు ఏ స్థావరాల్లో బయల్పడ్డాయి?',
         'భింబెట్కా మరియు అజంతా','కుప్పగల్, మాస్కీ మరియు పిక్లిహాల్','అమరావతి మరియు నాగార్జునకొండ','హంపి మరియు బళ్లారి',
         'B',
         'దక్షిణ భారత చాల్కోలిథిక్ కాలపు రాక్ పెయింటింగ్‌లు కుప్పగల్, మాస్కీ మరియు పిక్లిహాల్‌లో బయల్పడ్డాయి.'),

        (15,3,
         'కాయధా సంస్కృతికి ప్రసిద్ధమైన పనిముట్టు ఏమిటి?',
         'సూదులు (Needles)','కత్తి పరిశ్రమ (Knife Industry)','గొడ్డళ్ళు (Axes)','ఈటెలు (Spears)',
         'B',
         'కాయధా సంస్కృతి చాకు/కత్తి పరిశ్రమ (Knife Industry)కు ప్రసిద్ధి.'),

        # ── SEC 16: రాగి కుప్పెలు + OCP (4 Qs) ─────────────────────────────
        (16,3,
         'భారతదేశంలో తొలిసారిగా రాగి హార్పూన్ (Copper Harpoon) 1822లో ఎక్కడ కనుగొనబడింది?',
         'మధ్యప్రదేశ్‌లోని గాంగేరియా','ఉత్తరప్రదేశ్‌లోని బిహర్ (Bihaur)','రాజస్థాన్‌లోని బాగోర్','బీహార్‌లోని చిరాండ్',
         'B',
         '1822లో ఉత్తరప్రదేశ్‌లోని బిహర్ (Bihaur)లో తొలిసారిగా రాగి హార్పూన్ కనుగొనబడింది.'),

        (16,2,
         'భారతదేశంలో అత్యధిక రాగి వస్తువులు ఏ స్థావరంలో కనుగొనబడ్డాయి?',
         'బిహర్ (UP)','గాంగేరియా (MP)','లోతల్ (గుజరాత్)','డైమాబాద్ (MH)',
         'B',
         'మధ్యప్రదేశ్‌లోని గాంగేరియా (Gangeria)లో భారతదేశంలో అత్యధిక రాగి వస్తువులు కనుగొనబడ్డాయి.'),

        (16,3,
         'రాగి కుప్పెలపై పరిశోధనలు నిర్వహించిన ముఖ్యమైన పండితుడు ఎవరు?',
         'H.D.సంకాలియా','B.B.లాల్','గోర్డన్ చైల్డ్','V.S.వాకణ్కర్',
         'B',
         'B.B.లాల్ (Braj Basi Lal) రాగి కుప్పెలపై (Copper Hoards) విస్తృత పరిశోధనలు నిర్వహించారు.'),

        (16,2,
         'OCP (Ochre Coloured Pottery) మొట్టమొదట ఉత్తరప్రదేశ్‌లోని ఏ స్థావరంలో కనుగొనబడింది?',
         'కొల్దిహ్వా','బిసోలి','సారై నహర్ రాయ్','చోపాని మాండో',
         'B',
         'OCP (Ochre Coloured Pottery) మొట్టమొదట ఉత్తరప్రదేశ్‌లోని బిసోలి (Bisoli) స్థావరంలో కనుగొనబడింది.'),

        # ── SEC 17: BRW + ఇనుపయుగం + PGW (4 Qs) ───────────────────────────
        (17,3,
         'BRW (Black and Red Ware) మొట్టమొదట ఏ స్థావరంలో కనుగొనబడింది?',
         'అహిచ్ఛత్రం','నేవాసా','అతరంజీఖేరా','కాయధా',
         'C',
         'BRW (నల్ల మరియు ఎరుపు పాత్రలు) మొట్టమొదట ఉత్తరప్రదేశ్‌లోని అతరంజీఖేరా (Ataranjibera) స్థావరంలో కనుగొనబడింది.'),

        (17,1,
         'భారతదేశంలో ఇనుపయుగం ఎప్పుడు ప్రారంభమైంది?',
         'క్రీ.పూ. 3000','క్రీ.పూ. 2000','క్రీ.పూ. 1000','క్రీ.పూ. 500',
         'C',
         'భారతదేశంలో ఇనుపయుగం దాదాపు క్రీ.పూ. 1000 సంవత్సరాలలో ప్రారంభమైంది.'),

        (17,2,
         'భారత ఉపఖండంలో ఇనుప వాడకాన్ని ఎవరు ప్రవేశపెట్టారు?',
         'ద్రావిడులు','ముండాలు','ఆర్యులు','కుషాన్లు',
         'C',
         'భారత ఉపఖండంలో ఇనుప లోహ వాడకాన్ని ప్రవేశపెట్టినవారు ఆర్యులు.'),

        (17,3,
         'PGW (Painted Grey Ware) సంస్కృతి మొట్టమొదట ఏ స్థావరంలో, ఏ సంవత్సరంలో బయల్పడింది?',
         'నేవాసా — 1950','అహిచ్ఛత్రం — 1946','అతరంజీఖేరా — 1944','కాయధా — 1948',
         'B',
         'PGW సంస్కృతి 1946లో ఉత్తరప్రదేశ్‌లోని అహిచ్ఛత్రం (Ahichchhatra)లో మొట్టమొదట బయల్పడింది.'),

        # ── SEC 18: మొగాలిత్ సంస్కృతి (5 Qs) ───────────────────────────────
        (18,1,
         'మొగాలిత్ నిర్మాణాలను స్థానికంగా ఏమని పిలుస్తారు?',
         'బూడిద దిబ్బలు','అగ్నికుండాలు','రాక్షస గుళ్ళు లేదా పాండవ గుళ్ళు','శిలా స్తంభాలు',
         'C',
         'మొగాలిత్ నిర్మాణాలను స్థానికంగా రాక్షస గుళ్ళు లేదా పాండవ గుళ్ళు అంటారు.'),

        (18,2,
         'శిలాపేటికలు (Dolmens) అంటే ఏమిటి?',
         'భూమిలో పాతిన శిలాస్తంభాలు','రాతి ఫలకాలతో నిర్మించి మూత పెట్టిన పేటె','మట్టి కాళ్ళతో శవపేటిక','చుట్టూ రాళ్ళు నాటిన సమాధి',
         'B',
         'డోల్మెన్ (Dolmen) అంటే రాతి ఫలకాలతో పేటెను నిర్మించి, అందులో శవాన్ని ఉంచి దానిపై రాతి మూత పెట్టడం.'),

        (18,3,
         'భారతదేశంలో అద్వితీయమైన 6-8 కాళ్ళు కలిగిన శవపేటిక ఏ జిల్లాలో కనుగొనబడింది?',
         'నల్గొండ','వరంగల్','కర్నూలు','మహబూబ్‌నగర్',
         'C',
         'గోరె ఆకారంలో 6-8 కాళ్ళతో ఉన్న ప్రత్యేకమైన శవకోష్టిక (Sacrophagus) కర్నూలు జిల్లాలోని శంఖవరంలో కనుగొనబడింది.'),

        (18,2,
         'దక్షిణ భారతదేశంలో ఇనుపయుగానికి సంబంధించిన తొలి స్థావరాలు ఏ రాష్ట్రంలో ఉన్నాయి?',
         'తమిళనాడు','ఆంధ్రప్రదేశ్','కర్ణాటక','కేరళ',
         'C',
         'దక్షిణ భారతదేశంలో ఇనుపయుగానికి సంబంధించిన తొలి స్థావరాలు కర్ణాటకలోని పిక్లిహాల్ మరియు హళ్ళూర్.'),

        (18,3,
         'ముదుమాల్ మెన్హీర్స్ UNESCO తాత్కాలిక జాబితాలో ఏ సంవత్సరం చేర్చబడ్డాయి మరియు అవి ఏ జిల్లాలో ఉన్నాయి?',
         '2019 — వరంగల్ జిల్లా','2021 — నిజామాబాద్ జిల్లా','2024 — నారాయణపేట జిల్లా','2023 — మహబూబ్‌నగర్ జిల్లా',
         'C',
         'ముదుమాల్ మెన్హీర్స్ 2024లో UNESCO తాత్కాలిక జాబితాలో చేర్చబడ్డాయి — తెలంగాణ రాష్ట్రంలోని నారాయణపేట జిల్లాలో ఉన్నాయి.'),

        # ── SEC 19: UNESCO (3 Qs) ─────────────────────────────────────────────
        (19,1,
         'భింబెట్కా UNESCO వారసత్వ హోదాను ఏ సంవత్సరంలో పొందింది?',
         '1983','1993','2003','2013',
         'C',
         'భింబెట్కా రాతి గుహాలు 2003లో UNESCO ప్రపంచ వారసత్వ ప్రదేశంగా గుర్తించబడ్డాయి.'),

        (19,2,
         'తెలంగాణ నుండి UNESCO వారసత్వ హోదా పొందిన దేవాలయం ఏది మరియు ఏ సంవత్సరం?',
         'యాదాద్రి దేవాలయం — 2021','రాంప్ప దేవాలయం — 2019','వేయి స్తంభాల దేవాలయం — 2015','కాళేశ్వరం — 2018',
         'B',
         'తెలంగాణ నుండి రాంప్ప (రుద్రేశ్వర) దేవాలయం 2019లో UNESCO ప్రపంచ వారసత్వ ప్రదేశంగా గుర్తించబడింది.'),

        (19,3,
         'భారతదేశంలో మొత్తం ఎన్ని UNESCO ప్రపంచ వారసత్వ ప్రదేశాలు ఉన్నాయి మరియు వాటిలో సాంస్కృతిక ప్రదేశాలు ఎన్ని?',
         '40 మొత్తం — 32 సాంస్కృతిక','42 మొత్తం — 34 సాంస్కృతిక','44 మొత్తం — 36 సాంస్కృతిక','46 మొత్తం — 38 సాంస్కృతిక',
         'C',
         'భారతదేశంలో 44 UNESCO ప్రపంచ వారసత్వ ప్రదేశాలు ఉన్నాయి — వాటిలో 36 సాంస్కృతిక, 7 సహజసిద్ధ, 1 మిశ్రమ రకం.'),
    ]

    # Insert all MCQs
    for m in mcqs:
        sec, diff, q, a, b, c, d, ans, exp = m
        db_exec(conn,
            '''INSERT INTO chapter_mcqs
               (study_note_id, section_idx, difficulty, q_te, opt_a, opt_b, opt_c, opt_d, correct, explanation_te)
               VALUES (?,?,?,?,?,?,?,?,?,?)''',
            (note_id, sec, diff, q, a, b, c, d, ans, exp))

    conn.commit()
    conn.close()
    return jsonify({'success': True, 'message': f'Chapter 2 MCQs seeded! Total: {len(mcqs)} questions across 20 sections.'})


# ─────────────────────────────────────────────────────────────────────────────
# Chapter 3 Seed Routes (సింధు నాగరికత)
# ─────────────────────────────────────────────────────────────────────────────
try:
    from seed_ch3 import _seed_ch3_notes_inner, _seed_ch3_mcqs_inner
    _SEED_CH3_LOADED = True
except Exception as _e:
    _SEED_CH3_LOADED = False
    print(f"[WARN] seed_ch3.py not loaded: {_e}")

@app.route('/api/notes/seed_ch3_ih', methods=['POST'])
def notes_seed_ch3_ih():
    """Seed Chapter 3 Indian History – Indus Civilisation. Add ?force=1 to overwrite."""
    if not _SEED_CH3_LOADED:
        return jsonify({'success': False, 'error': 'seed_ch3.py not found'}), 500
    force = request.args.get('force', '0') == '1'
    conn = get_db()
    try:
        result = _seed_ch3_notes_inner(conn, db_exec, row_to_dict, USE_POSTGRES, force=force)
        return jsonify(result)
    except Exception as e:
        import traceback
        return jsonify({'success': False, 'error': str(e), 'trace': traceback.format_exc()}), 500
    finally:
        conn.close()

@app.route('/api/mcq/seed_ch3', methods=['POST'])
def seed_ch3_mcqs():
    """Seed Chapter 3 MCQs."""
    if not _SEED_CH3_LOADED:
        return jsonify({'success': False, 'error': 'seed_ch3.py not found'}), 500
    conn = get_db()
    try:
        result = _seed_ch3_mcqs_inner(conn, db_exec, row_to_dict, USE_POSTGRES)
        return jsonify(result)
    except Exception as e:
        import traceback
        return jsonify({'success': False, 'error': str(e), 'trace': traceback.format_exc()}), 500
    finally:
        conn.close()


@app.route('/api/fix/mcq_correct_field', methods=['POST'])
def fix_mcq_correct_field():
    """One-time fix: repair chapter_mcqs rows where correct is not one of a/b/c/d.
    Also fixes known wrong answers (e.g., Brahui tribe question)."""
    conn = get_db()
    try:
        ph = '%s' if USE_POSTGRES else '?'
        fixed = 0

        # Fix 1: Brahui tribe question — correct answer is 'c'
        cur = db_exec(conn,
            f"UPDATE chapter_mcqs SET correct = {ph} WHERE q_te LIKE {ph} AND (correct != {ph})",
            ('c', '%సింధు నాగరికత వారసులు%', 'c'))
        fixed += cur.rowcount if hasattr(cur, 'rowcount') else 0

        # Fix 2: Any row where correct is not a valid option letter
        if USE_POSTGRES:
            cur2 = db_exec(conn,
                "SELECT COUNT(*) FROM chapter_mcqs WHERE correct NOT IN ('a','b','c','d','A','B','C','D')")
        else:
            cur2 = db_exec(conn,
                "SELECT COUNT(*) FROM chapter_mcqs WHERE correct NOT IN ('a','b','c','d','A','B','C','D')")
        bad_count = cur2.fetchone()[0]

        if not USE_POSTGRES:
            conn.commit()
        return jsonify({'success': True, 'fixed_rows': fixed, 'still_invalid': bad_count})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500
    finally:
        conn.close()


# ── CHAPTER 4: వేద నాగరికత ─────────────────────────────────────────────────
try:
    from seed_ch4 import _seed_ch4_notes_inner, _seed_ch4_mcqs_inner
    _SEED_CH4_LOADED = True
except Exception as _e:
    _SEED_CH4_LOADED = False
    print(f"[WARN] seed_ch4.py not loaded: {_e}")

@app.route('/api/notes/seed_ch4_ih', methods=['POST'])
def notes_seed_ch4_ih():
    if not _SEED_CH4_LOADED:
        return jsonify({'success': False, 'error': 'seed_ch4.py not found'}), 500
    conn = get_db()
    try:
        force = request.args.get('force', '0') == '1'
        result = _seed_ch4_notes_inner(conn, db_exec, row_to_dict, USE_POSTGRES, force=force)
        return jsonify(result)
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500
    finally:
        conn.close()

@app.route('/api/mcq/seed_ch4', methods=['POST'])
def seed_ch4_mcqs():
    if not _SEED_CH4_LOADED:
        return jsonify({'success': False, 'error': 'seed_ch4.py not found'}), 500
    conn = get_db()
    try:
        result = _seed_ch4_mcqs_inner(conn, db_exec, row_to_dict, USE_POSTGRES)
        return jsonify(result)
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500
    finally:
        conn.close()

# ── CHAPTER 5: మత సంస్కరణోద్యమాలు ─────────────────────────────────────────────
try:
    from seed_ch5 import _seed_ch5_notes_inner, _seed_ch5_mcqs_inner
    _SEED_CH5_LOADED = True
except Exception as _e:
    _SEED_CH5_LOADED = False
    print(f"[WARN] seed_ch5.py not loaded: {_e}")

@app.route('/api/notes/seed_ch5_ih', methods=['POST'])
def notes_seed_ch5_ih():
    if not _SEED_CH5_LOADED:
        return jsonify({'success': False, 'error': 'seed_ch5.py not found'}), 500
    conn = get_db()
    try:
        force = request.args.get('force', '0') == '1'
        result = _seed_ch5_notes_inner(conn, db_exec, row_to_dict, USE_POSTGRES, force=force)
        return jsonify(result)
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500
    finally:
        conn.close()

@app.route('/api/mcq/seed_ch5', methods=['POST'])
def seed_ch5_mcqs():
    if not _SEED_CH5_LOADED:
        return jsonify({'success': False, 'error': 'seed_ch5.py not found'}), 500
    conn = get_db()
    try:
        result = _seed_ch5_mcqs_inner(conn, db_exec, row_to_dict, USE_POSTGRES)
        return jsonify(result)
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500
    finally:
        conn.close()

# ── CHAPTER 6: మగధ సామ్రాజ్యం ─────────────────────────────────────────────────
try:
    from seed_ch6 import _seed_ch6_notes_inner, _seed_ch6_mcqs_inner
    _SEED_CH6_LOADED = True
except Exception as _e:
    _SEED_CH6_LOADED = False
    print(f"[WARN] seed_ch6.py not loaded: {_e}")

@app.route('/api/notes/seed_ch6_ih', methods=['POST'])
def notes_seed_ch6_ih():
    if not _SEED_CH6_LOADED:
        return jsonify({'success': False, 'error': 'seed_ch6.py not found'}), 500
    conn = get_db()
    try:
        force = request.args.get('force', '0') == '1'
        result = _seed_ch6_notes_inner(conn, db_exec, row_to_dict, USE_POSTGRES, force=force)
        return jsonify(result)
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500
    finally:
        conn.close()

@app.route('/api/mcq/seed_ch6', methods=['POST'])
def seed_ch6_mcqs():
    if not _SEED_CH6_LOADED:
        return jsonify({'success': False, 'error': 'seed_ch6.py not found'}), 500
    conn = get_db()
    try:
        # Auto-seed notes first (no-op if already present) so MCQ seed always finds them
        _seed_ch6_notes_inner(conn, db_exec, row_to_dict, USE_POSTGRES, force=False)
        result = _seed_ch6_mcqs_inner(conn, db_exec, row_to_dict, USE_POSTGRES)
        return jsonify(result)
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500
    finally:
        conn.close()


# ── CHAPTER 7: విదేశీ దండయాత్రలు ─────────────────────────────────────────────
try:
    from seed_ch7 import _seed_ch7_notes_inner, _seed_ch7_mcqs_inner
    _SEED_CH7_LOADED = True
except Exception as _e:
    _SEED_CH7_LOADED = False
    print(f"[WARN] seed_ch7.py not loaded: {_e}")

@app.route('/api/notes/seed_ch7_ih', methods=['POST'])
def notes_seed_ch7_ih():
    if not _SEED_CH7_LOADED:
        return jsonify({'success': False, 'error': 'seed_ch7.py not found'}), 500
    conn = get_db()
    try:
        force = request.args.get('force', '0') == '1'
        result = _seed_ch7_notes_inner(conn, db_exec, row_to_dict, USE_POSTGRES, force=force)
        return jsonify(result)
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500
    finally:
        conn.close()

@app.route('/api/mcq/seed_ch7', methods=['POST'])
def seed_ch7_mcqs():
    if not _SEED_CH7_LOADED:
        return jsonify({'success': False, 'error': 'seed_ch7.py not found'}), 500
    conn = get_db()
    try:
        # Auto-seed notes first (no-op if already present) so MCQ seed always finds them
        _seed_ch7_notes_inner(conn, db_exec, row_to_dict, USE_POSTGRES, force=False)
        result = _seed_ch7_mcqs_inner(conn, db_exec, row_to_dict, USE_POSTGRES)
        return jsonify(result)
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500
    finally:
        conn.close()


# ── CHAPTER 8: మౌర్యసామ్రాజ్యము ─────────────────────────────────────────────
try:
    from seed_ch8 import _seed_ch8_notes_inner, _seed_ch8_mcqs_inner
    _SEED_CH8_LOADED = True
except Exception as _e:
    _SEED_CH8_LOADED = False
    print(f"[WARN] seed_ch8.py not loaded: {_e}")

@app.route('/api/notes/seed_ch8_ih', methods=['POST'])
def notes_seed_ch8_ih():
    if not _SEED_CH8_LOADED:
        return jsonify({'success': False, 'error': 'seed_ch8.py not found'}), 500
    conn = get_db()
    try:
        force = request.args.get('force', '0') == '1'
        result = _seed_ch8_notes_inner(conn, db_exec, row_to_dict, USE_POSTGRES, force=force)
        return jsonify(result)
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500
    finally:
        conn.close()

@app.route('/api/mcq/seed_ch8', methods=['POST'])
def seed_ch8_mcqs():
    if not _SEED_CH8_LOADED:
        return jsonify({'success': False, 'error': 'seed_ch8.py not found'}), 500
    conn = get_db()
    try:
        _seed_ch8_notes_inner(conn, db_exec, row_to_dict, USE_POSTGRES, force=False)
        result = _seed_ch8_mcqs_inner(conn, db_exec, row_to_dict, USE_POSTGRES)
        return jsonify(result)
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500
    finally:
        conn.close()


# ── CHAPTER 9: మౌర్యుల అనంతర కాలం ──────────────────────────────────────────
try:
    from seed_ch9 import _seed_ch9_notes_inner, _seed_ch9_mcqs_inner
    _SEED_CH9_LOADED = True
except Exception as _e:
    _SEED_CH9_LOADED = False
    print(f"[WARN] seed_ch9.py not loaded: {_e}")

@app.route('/api/notes/seed_ch9_ih', methods=['POST'])
def notes_seed_ch9_ih():
    if not _SEED_CH9_LOADED:
        return jsonify({'success': False, 'error': 'seed_ch9.py not found'}), 500
    conn = get_db()
    try:
        force = request.args.get('force', '0') == '1'
        result = _seed_ch9_notes_inner(conn, db_exec, row_to_dict, USE_POSTGRES, force=force)
        return jsonify(result)
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500
    finally:
        conn.close()

@app.route('/api/mcq/seed_ch9', methods=['POST'])
def seed_ch9_mcqs():
    if not _SEED_CH9_LOADED:
        return jsonify({'success': False, 'error': 'seed_ch9.py not found'}), 500
    conn = get_db()
    try:
        _seed_ch9_notes_inner(conn, db_exec, row_to_dict, USE_POSTGRES, force=False)
        result = _seed_ch9_mcqs_inner(conn, db_exec, row_to_dict, USE_POSTGRES)
        return jsonify(result)
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500
    finally:
        conn.close()


try:
    from seed_ch10 import _seed_ch10_notes_inner, _seed_ch10_mcqs_inner
    _SEED_CH10_LOADED = True
except Exception as _e:
    _SEED_CH10_LOADED = False
    print(f"[WARN] seed_ch10.py not loaded: {_e}")

@app.route('/api/notes/seed_modern_ch1', methods=['POST'])
def notes_seed_modern_ch1():
    if not _SEED_CH10_LOADED:
        return jsonify({'success': False, 'error': 'seed_ch10.py not found'}), 500
    conn = get_db()
    try:
        force = request.args.get('force', '0') == '1'
        result = _seed_ch10_notes_inner(conn, db_exec, row_to_dict, USE_POSTGRES, force=force)
        return jsonify(result)
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500
    finally:
        conn.close()

@app.route('/api/mcq/seed_modern_ch1', methods=['POST'])
def seed_modern_ch1_mcqs():
    if not _SEED_CH10_LOADED:
        return jsonify({'success': False, 'error': 'seed_ch10.py not found'}), 500
    conn = get_db()
    try:
        _seed_ch10_notes_inner(conn, db_exec, row_to_dict, USE_POSTGRES, force=False)
        result = _seed_ch10_mcqs_inner(conn, db_exec, row_to_dict, USE_POSTGRES)
        return jsonify(result)
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500
    finally:
        conn.close()


# ─────────────────────────────────────────────────────────────────────────────
# SEED ALL ANCIENT — seeds ch1-ch9 notes + MCQs in one shot
# ─────────────────────────────────────────────────────────────────────────────

@app.route('/api/notes/seed_all_ancient', methods=['POST'])
def seed_all_ancient():
    """Seed ALL Ancient Indian History chapters (ch1-ch9) notes + MCQs in one call.
    Uses the app's own test client to hit each seed endpoint sequentially.
    Add ?force=1 to overwrite existing data."""
    force = request.args.get('force', '0') == '1'
    qs = '?force=1' if force else ''
    results = []
    client = app.test_client()

    # Notes endpoints first, then MCQ endpoints
    notes_routes = [
        f'/api/notes/seed{qs}',          # ch1
        f'/api/notes/seed_ch2_ih{qs}',   # ch2
        f'/api/notes/seed_ch3_ih{qs}',   # ch3
        f'/api/notes/seed_ch4_ih{qs}',   # ch4
        f'/api/notes/seed_ch5_ih{qs}',   # ch5
        f'/api/notes/seed_ch6_ih{qs}',   # ch6
        f'/api/notes/seed_ch7_ih{qs}',   # ch7
        f'/api/notes/seed_ch8_ih{qs}',   # ch8
        f'/api/notes/seed_ch9_ih{qs}',   # ch9
    ]
    mcq_routes = [
        '/api/mcq/seed_ch1',
        '/api/mcq/seed_ch2',
        '/api/mcq/seed_ch3',
        '/api/mcq/seed_ch4',
        '/api/mcq/seed_ch5',
        '/api/mcq/seed_ch6',
        '/api/mcq/seed_ch7',
        '/api/mcq/seed_ch8',
        '/api/mcq/seed_ch9',
    ]

    for i, route in enumerate(notes_routes, start=1):
        try:
            resp = client.post(route)
            data = resp.get_json() or {}
            results.append({'ch': i, 'type': 'notes', 'status': resp.status_code,
                            'msg': data.get('message', data.get('success', str(data)))})
        except Exception as e:
            results.append({'ch': i, 'type': 'notes', 'error': str(e)})

    for i, route in enumerate(mcq_routes, start=1):
        try:
            resp = client.post(route)
            data = resp.get_json() or {}
            results.append({'ch': i, 'type': 'mcqs', 'status': resp.status_code,
                            'msg': data.get('message', data.get('success', str(data)))})
        except Exception as e:
            results.append({'ch': i, 'type': 'mcqs', 'error': str(e)})

    all_ok = all('error' not in r for r in results)
    return jsonify({'success': all_ok, 'total_steps': len(results), 'results': results})


# ── Run init_db on import (works with gunicorn on Railway AND locally) ──
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
