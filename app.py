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
    cur = db_exec(conn, '''
        SELECT id, chapter_num, chapter_title_te, chapter_title_en, pages_ref, sections_json
        FROM study_notes WHERE subject=? AND topic=?
        ORDER BY chapter_num
    ''', (subject, topic))
    chapters = [row_to_dict(r) for r in cur.fetchall()]
    conn.close()
    return render_template('notes_topic.html', subject=subject, topic=topic, chapters=chapters)


@app.route('/notes/<subject>/<topic>/<int:chapter_id>')
def notes_chapter(subject, topic, chapter_id):
    conn = get_db()
    cur = db_exec(conn, 'SELECT * FROM study_notes WHERE id=?', (chapter_id,))
    chapter = row_to_dict(cur.fetchone())
    conn.close()
    if not chapter:
        return redirect('/notes')
    sections = json.loads(chapter['sections_json'])
    return render_template('notes_chapter.html',
                           subject=subject, topic=topic,
                           chapter=chapter, sections=sections)


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
@admin_required
def notes_seed():
    """Seed Chapter 1 Indian History. Add ?force=1 to overwrite existing."""
    force = request.args.get('force', '0') == '1'
    conn = get_db()
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
            "audio": "EXAM ALERT! ఇప్పుడు చాలా ముఖ్యమైన పట్టిక — వస్తు అవశేషాల కాల నిర్ధారణ పద్ధతులు. 5 పద్ధతులు శ్రద్ధగా వినండి. పద్ధతి ఒకటి: రేడియోకార్బన్ పద్ధతి — C 14. శాస్త్రవేత్త విల్లర్డ్ లిబ్బి అమెరికా. విల్లర్డ్ లిబ్బి, విల్లర్డ్ లిబ్బి! అనువైన వస్తువు — సేంద్రియ పదార్థం, అంటే ఎముక, దంతాలు. కాల వ్యాప్తి — 20,000 నుండి 4,00,000 సంవత్సరాలు. EXAM ALERT: C 14 అంటే విల్లర్డ్ లిబ్బి! పద్ధతి రెండు: పొటాషియం-అర్గాన్ పద్ధతి — K-A 40. శాస్త్రవేత్త మెక్‌డూగల్. మెక్‌డూగల్! అనువైన వస్తువు — అగ్నిశిల. కాల వ్యాప్తి — అపరిమితం. పద్ధతి మూడు: థర్మోల్యూమినిసెన్స్ పద్ధతి. శాస్త్రవేత్త బట్కిన్స్. బట్కిన్స్, బట్కిన్స్! అనువైన వస్తువు — కుండలు. కాల వ్యాప్తి — 10,000 సంవత్సరాలు. పద్ధతి నాలుగు: అమైనో ఆమ్ల రెసిమేషన్ పద్ధతి. అనువైన వస్తువు — ఎముక, సముద్ర కర్చురాలు. కాల వ్యాప్తి — 1 లక్ష సంవత్సరాలు. పద్ధతి ఐదు: డెండ్రోక్రోనాలజీ పద్ధతి. అనువైన వస్తువు — వృక్షాల వార్షిక వలయాలు. కాల వ్యాప్తి — 7,500 సంవత్సరాలు. EXAM QUICK MEMORY: C 14 అంటే లిబ్బి అంటే ఎముక. K-A అంటే మెక్‌డూగల్ అంటే అగ్నిశిల. థర్మో అంటే బట్కిన్స్ అంటే కుండలు. డెండ్రో అంటే చెట్ల వలయాలు."
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
            "audio": "అధ్యాయం 1 పూర్తయింది! ఇప్పుడు గుర్తుపెట్టుకోండి విభాగం. అన్ని ముఖ్యమైన అంశాలు rapid fire గా చెప్తాను — మీరు వెంటనే మనసులో repeat చేయండి. ముఖ్యమైన వ్యక్తులు మరియు వారి గ్రంథాలు వినండి. హెరోడోటస్ అంటే The Histories అంటే Father of History గ్రీకు. సర్ విలియం జోన్స్ అంటే Father of Indology భారతం. చాణక్యుడు అంటే కౌటిల్యుడు అంటే విష్ణు గుప్తుడు అంటే అర్థశాస్త్రం. కల్హణుడు అంటే రాజతరంగిణి. బాణుడు అంటే హర్షచరిత్ర. పతంజలి అంటే మహాభాష్యం. విశాఖదత్తుడు అంటే ముద్రారాక్షసం మరియు దేవీచంద్రగుప్తం — రెండు గ్రంథాలు! చాంద్ బర్దాయి అంటే పృథ్వీరాజ్ రాసో. మెగస్తనీస్ అంటే ఇండికా అంటే చంద్రగుప్త మౌర్య ఆస్థానం. అజ్ఞాత నావికుడు అంటే పెరిప్లస్ ఆఫ్ ది ఎరిత్రియన్ సీ. ప్లీని అంటే నాచురల్ హిస్టరీ లాటిన్. ఫాహియాన్ అంటే ఫో-కువో-కి అంటే రెండవ చంద్రగుప్తుడు అంటే మొదటి చైనా యాత్రికుడు. హ్యూయెన్ త్సాంగ్ అంటే సి-యు-కి అంటే హర్షవర్ధనుడు అంటే King of Travellers. అల్-బెరూని అంటే కితాబ్-ఉల్-హింద్ అంటే Founder of Indology అంటే Father of Comparative Religion. తారానాథ్ అంటే The History of Tibet అంటే అశోకుడు. దీపవంశ మరియు మహావంశ అంటే శ్రీలంక పాళీ భాష మౌర్యుల సమాచారం. శాసనాల 4 రకాలు: రాజాజ్ఞలు అంటే అశోకుడు. అంకిత. దాన. స్మారక. మళ్ళీ — రాజాజ్ఞలు, అంకిత, దాన, స్మారక! కాల నిర్ధారణ పద్ధతులు: C 14 అంటే లిబ్బి. K-A అంటే మెక్‌డూగల్. థర్మో అంటే బట్కిన్స్ అంటే కుండలు. డెండ్రో అంటే చెట్ల వలయాలు. వాస్తు శైలులు: నగరశైలి అంటే ఉత్తరం. ద్రావిడ అంటే దక్షిణం. వేసర అంటే కలయిక. ముఖ్య పదాలు: ఎపిగ్రఫీ అంటే శాసన అధ్యయనం. పేలియోగ్రఫీ అంటే ప్రాచీన లిపులు. న్యూమిస్మాటిక్స్ అంటే నాణేల అధ్యయనం. ఇకనోగ్రఫీ అంటే శిల్పకళ అధ్యయనం. మొదటి సంస్కృత శాసనం అంటే రుద్రదమనుడి జునాఘడ్ శాసనం. మొదటి కుమ్మరి చక్రం అంటే మెహర్గర్. అగ్రహార పదం మొదటి ప్రయోగం అంటే నలంద తామ్ర శాసనం గుప్తుల కాలం. అభినందనలు! అధ్యాయం 1 పూర్తిగా చదివారు. శుభాకాంక్షలు!"
        }
    ]

    db_exec(conn, '''
        INSERT INTO study_notes
        (subject, topic, chapter_num, chapter_title_te, chapter_title_en, pages_ref, sections_json)
        VALUES (?,?,?,?,?,?,?)
    ''', ('GK', 'Indian_History', 1, 'చరిత్ర – పరిచయం',
          'Introduction to History', '1-6', json.dumps(ch1_sections, ensure_ascii=False)))
    conn.commit()
    conn.close()
    return jsonify({'success': True, 'message': 'Chapter 1 seeded with 17 sections successfully'})


# ─────────────────────────────────────────────
# CHAPTER MCQ ROUTES
# ─────────────────────────────────────────────

@app.route('/api/mcq/chapter/<int:chapter_id>')
def get_chapter_mcqs(chapter_id):
    """Return all MCQs for a chapter (shuffled)."""
    conn = get_db()
    cur = db_exec(conn, '''
        SELECT id, section_idx, difficulty, q_te, opt_a, opt_b, opt_c, opt_d, correct, explanation_te
        FROM chapter_mcqs WHERE study_note_id=? ORDER BY section_idx, id
    ''', (chapter_id,))
    rows = [row_to_dict(r) for r in cur.fetchall()]
    conn.close()
    random.shuffle(rows)
    return jsonify({'mcqs': rows, 'count': len(rows)})


@app.route('/api/mcq/chapter/<int:chapter_id>/delete', methods=['POST'])
@admin_required
def delete_chapter_mcqs(chapter_id):
    conn = get_db()
    db_exec(conn, 'DELETE FROM chapter_mcqs WHERE study_note_id=?', (chapter_id,))
    conn.commit()
    conn.close()
    return jsonify({'success': True})


@app.route('/api/mcq/seed_ch1', methods=['POST'])
@admin_required
def seed_ch1_mcqs():
    """Seed all Chapter 1 MCQs. Add ?force=1 to overwrite."""
    force = request.args.get('force', '0') == '1'
    conn = get_db()
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
         "b) Butkins (బట్కిన్స్)",
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
         "కుండలకు (Pottery) Thermoluminescence పద్ధతి అనువైనది. శాస్త్రవేత్త Butkins. కాల వ్యాప్తి 10,000 సంవత్సరాలు."),
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
    for m in mcqs:
        db_exec(conn, insert_sql, (ch_id,) + m)
    conn.commit()
    conn.close()
    return jsonify({'success': True, 'message': f'{len(mcqs)} MCQs seeded for Chapter 1!'})

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
