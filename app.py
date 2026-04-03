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
    """Seed Chapter 1 Indian History if not already present."""
    conn = get_db()
    cur = db_exec(conn, "SELECT id FROM study_notes WHERE subject='GK' AND topic='Indian_History' AND chapter_num=1")
    if cur.fetchone():
        conn.close()
        return jsonify({'message': 'Already seeded'})

    ch1_sections = [
        {"title": "చరిత్ర అంటే ఏమిటి?", "sub": "History · Culture · Civilisation నిర్వచనాలు",
         "audio": "స్నేహితులారా, ఒక్కసారి ఊహించండి. మీరు అప్పుడే నిద్ర లేచారు, కిటికీ బయటికి చూస్తే అక్కడ అరణ్యాలు, నదులు, గుహలు కనిపిస్తున్నాయి. ఆ గుహల్లో మన పూర్వికులు జీవించారు. వాళ్ళు ఎలా జీవించారు? వాళ్ళ సమాజం ఏ విధంగా పరిణామం చెందింది? ఈ ప్రశ్నలన్నింటికీ సమాధానం ఇచ్చే శాస్త్రమే చరిత్ర! ప్రపంచంలోని వివిధ ప్రాంతాల్లో మానవ సమాజ ఆవిర్భావం, సంస్కృతి, నాగరికత ఏ విధంగా పరిణామం చెందుతూ వచ్చాయి? సామాజిక, ఆర్థిక, మత, రాజకీయ వ్యవస్థలు ఎలా మారుతూ వచ్చాయి? అని మనకు తెలియజేసే శాస్త్రమే చరిత్ర. సంస్కృతి అనగా ఒక జీవన విధానము. నాగరికత అనగా సంస్కృతిలో ఒక ప్రత్యేకమైన అభివృద్ధి సాధించిన పరిణామ దశ. అంటే నాగరికత అనేది సంస్కృతి యొక్క ఉన్నత రూపం!"},
        {"title": "హిస్టరీ పదం పుట్టుక", "sub": "హిస్టోరియా (గ్రీకు) · హెరోడోటస్ · Father of History",
         "audio": "చరిత్రను ఇంగ్లీష్‌లో హిస్టరీ అని అంటారు. హిస్టరీ అనే పదం హిస్టోరియా అనే గ్రీకు పదం నుండి వచ్చింది. హిస్టోరియా అనగా పరిశోధించి తెలుసుకొనుట, అంటే Inquiry, Knowledge acquired by investigation. హెరోడోటస్ అనే గ్రీకు మహాపురుషుడిని చరిత్ర పితామహుడు, Father of History అని పేర్కొంటారు. ఆయన క్రీస్తు పూర్వం ఐదవ శతాబ్దంలో జీవించారు. ఆయన రాసిన మహాగ్రంథం పేరు The Histories. ఇందులో గ్రీకు పర్షియన్ యుద్ధాలు, Egyptian civilisation, Asian cultures అన్నీ క్రమబద్ధంగా వర్ణించారు."},
        {"title": "ఇండాలజీ & సర్ విలియం జోన్స్", "sub": "Indology · Father of Indian Indology",
         "audio": "భారతచరిత్ర, సంస్కృతులు, భాష మరియు సాహిత్య అధ్యయనాన్ని ఇండాలజీ అంటారు. భారత ఇండాలజీ పితామహుడిగా సర్ విలియం జోన్స్‌ను పిలుస్తారు. ఆయన సంస్కృత భాషను నేర్చుకొని, 1784లో Asiatic Society of Bengal స్థాపించారు. సంస్కృతం, లాటిన్, గ్రీకు అన్నీ ఒకే మాతృభాష నుండి వచ్చాయని ఆయన నిరూపించారు. ఇదే Indo-European Language Family Theory కి పునాది!"},
        {"title": "మంచు యుగాలు – Ice Ages", "sub": "Pleistocene · Holocene · మానవ ఆవిర్భావం",
         "audio": "క్రీస్తు పూర్వం ఐదు లక్షల సంవత్సరాల పరకుగలు దశ తొలి శిలాయుగం. ఆ కాలాన్ని ప్లీస్టోసీన్ అంటారు. ఇదే తొలి మంచు యుగం, First Ice Age. ఆ కాలంలో భూమి మొత్తం మంచుతో కప్పబడి ఉండేది. తర్వాత మంచు కరిగి నీరు ఏర్పడ్డాయి. జీవం తిరిగి చిగురించింది. సంస్కృతి పురోగమించింది. ఈ దశను హెలోసీన్ అంటారు. ఇది రెండవ మంచు యుగం. ఇదే ప్రస్తుతం మనం జీవిస్తున్న దశ. మానవుడు ఆస్ట్రలో పిథికస్ భూమిపై ఉద్భవించి ఐదు లక్షల సంవత్సరాల కాలం పూర్తి అవుతుంది."},
        {"title": "చారిత్రక ఆధారాలు – పరిచయం", "sub": "Literary Sources · Archaeological Sources",
         "audio": "మన పూర్వీకులు ఏం చేశారో మనకు ఎలా తెలుస్తుంది? చరిత్రకారులు రెండు రకాల ఆధారాలు ఉపయోగిస్తారు. మొదటిది లిఖిత ఆధారాలు అంటే Literary Sources, రాసినవి, చదివినవి. రెండవది పురావస్తు ఆధారాలు అంటే Archaeological Sources, తవ్వకాల్లో దొరికినవి. లిఖిత ఆధారాలు మళ్ళా రెండు రకాలు. స్వదేశీ సాహిత్యం మరియు విదేశీ సాహిత్యం. ఇవన్నీ కలిపి మనకు చరిత్ర పుట్టింది!"},
        {"title": "స్వదేశీ సాహిత్యం – మతపరమైనది", "sub": "వేదాలు · బౌద్ధ · జైన సాహిత్యం",
         "audio": "స్వదేశీ సాహిత్యం రెండు భాగాలు. మొదటిది మతపరమైన సాహిత్యం. రెండవది లౌకిక సాహిత్యం. మతపరమైన సాహిత్యంలో ముఖ్యమైనవి వేద సాహిత్యం. నాలుగు వేదాలు ఋగ్వేదం, సామవేదం, యజుర్వేదం, అథర్వవేదం. ఇవి భారత జ్ఞాన సంపదకు పునాదులు! వేదాల తర్వాత వచ్చినవి ఉపనిషత్తులు, ఆరణ్యకాలు, బ్రాహ్మణాలు. బౌద్ధ సాహిత్యం అంటే త్రిపిటకాలు. జైన సాహిత్యం అంటే అంగాలు మరియు ఉపాంగాలు."},
        {"title": "స్వదేశీ సాహిత్యం – లౌకికం", "sub": "అర్థశాస్త్రం · రాజతరంగిణి · పురాణాలు · పాణిని",
         "audio": "లౌకిక సాహిత్యం అంటే మతేతర రచనలు. అష్టాధ్యాయి అంటే పాణిని రాసిన సంస్కృత వ్యాకరణ గ్రంథం. నాలుగు వేల సూత్రాలతో సంస్కృత భాష నిర్మాణాన్ని వివరించారు! అర్థశాస్త్రం అంటే కౌటిల్యుడు, చాణక్యుడు రాసిన గ్రంథం. రాజనీతి, ఆర్థిక వ్యవస్థ, యుద్ధ వ్యూహాలు అన్నింటినీ వివరిస్తుంది. రాజతరంగిణి అంటే కల్హణుడు రాసిన కశ్మీర్ చరిత్ర. పురాణాలు అంటే పదునెనిమిది మహాపురాణాలు రాజవంశాల వంశావళి తెలుపుతాయి."},
        {"title": "విదేశీ సాహిత్యం – గ్రీకు & లాటిన్", "sub": "మెగస్తనీస్ Indica · Pliny Natural History",
         "audio": "విదేశీ సాహిత్యం అంటే విదేశీయులు భారత్ గురించి రాసిన రచనలు. గ్రీకు సాహిత్యం అంటే మెగస్తనీస్ చంద్రగుప్త మౌర్య కాలంలో పాటలీపుత్రంలో గ్రీకు రాయబారిగా నివసించారు. ఆయన రాసిన ఇండికా అనే గ్రంథం భారత జనజీవనం, రాజ్యపాలన, సమాజం గురించి అద్భుత వర్ణన. లాటిన్ సాహిత్యం అంటే ప్లీనీ రాసిన నాచురల్ హిస్టరీ. ఇందులో భారతదేశంతో రోమన్ వ్యాపారం, సుగంధ ద్రవ్యాలు, పట్టు వ్యాపారం గురించి వివరాలున్నాయి."},
        {"title": "విదేశీ సాహిత్యం – చైనీస్ & శ్రీలంక", "sub": "ఫా-హియాన్ · హ్యూయాన్-త్సాంగ్ · దీపవంశ · మహావంశ",
         "audio": "చైనీస్ సాహిత్యం చాలా ముఖ్యమైనది. ఫా-హియాన్ క్రీస్తు శకం మూడువందల తొంభై తొమ్మిది నుండి నాలుగువందల పద్నాలుగు మధ్య భారత్‌కు వచ్చిన చైనీస్ బౌద్ధ యాత్రికుడు. హ్యూయాన్-త్సాంగ్ హర్షవర్ధనుడి కాలంలో భారత్‌కు వచ్చారు. ఆయన్ని King of Travellers, యాత్రికుల రాజు అంటారు. Fo-Kuo-Ki అనే గ్రంథం రాశారు. శ్రీలంక సాహిత్యం అంటే దీపవంశ, The Chronicle of the Island. మహావంశ, The Great Chronicle. ఇవి బౌద్ధ మత వ్యాప్తి, అశోక చక్రవర్తి చరిత్రకు అద్భుత ఆధారాలు."},
        {"title": "విదేశీ సాహిత్యం – జైన, టిబెట్, అరబిక్", "sub": "తారానాథ్ · అల్-బిరూని · కితాబ్-ఉల్-హింద్",
         "audio": "జైన్ సాహిత్యం అంటే జైన గ్రంథాలు అంగాలు, ఉపాంగాలు. భారత సమాజ, వ్యాపార, తాత్విక అంశాలు వివరిస్తాయి. టిబెటన్ సాహిత్యం అంటే తారానాథ్ రాసిన The History of Tibet. బౌద్ధ మతం టిబెట్‌కు వ్యాప్తి, భారత-టిబెట్ సాంస్కృతిక సంబంధాల గురించి తెలుపుతుంది. అల్-బిరూని పదకొండవ శతాబ్దంలో గజనీ మహ్మద్‌తో భారత్‌కు వచ్చారు. ఆయన రాసిన కితాబ్-ఉల్-హింద్ అనే గ్రంథం భారత జ్ఞాన సంపద, సమాజం, మతం గురించి విలువైన వివరాలిస్తుంది. ఆయన్ను Founder of Indology అని కూడా అంటారు!"},
        {"title": "పురావస్తు ఆధారాలు – శాసనాలు", "sub": "Rock · Pillar · Cave · Copper Plate Inscriptions",
         "audio": "శాసనాలు అంటే రాళ్ళపై, స్తంభాలపై, రాగి రేకులపై రాసిన చారిత్రక పత్రాలు. ప్రపంచంలో నూట డెభ్భై ఐదు భాషల్లో శాసనాలు లభించాయి! శాసనాల రకాలు నాలుగు. మొదటిది రాక్ ఎడిట్స్ అంటే రాళ్ళపై చెక్కిన శాసనాలు. రెండవది పిల్లర్ ఎడిట్స్ అంటే స్తంభాలపై చెక్కిన శాసనాలు. మూడవది కేవ్ ఇన్స్క్రిప్షన్స్ అంటే గుహలలో చెక్కిన శాసనాలు. నాల్గవది కాపర్ ప్లేట్ ఇన్స్క్రిప్షన్స్ అంటే రాగి రేకులపై రాసిన శాసనాలు. ప్రయోజనం ప్రకారం శాసనాలు నాలుగు రకాలు. రాజశాసనాలు, దాన శాసనాలు, స్మారక శాసనాలు, అంకిత శాసనాలు."},
        {"title": "నాణేలు & కుండలు", "sub": "Numismatics · OCP · PGW · NBP Pottery",
         "audio": "నాణేల అధ్యయనాన్ని Numismatics అంటారు. నాణేలపై రాజుల చిత్రాలు, పేర్లు, తేదీలు, రాజ్య చిహ్నాలు ఉంటాయి. రాజవంశాల కాలనిర్ణయానికి ఇవి అద్భుత ఆధారాలు! కుండలు కాలనిర్ణయానికి అద్భుతమైన ఆధారాలు. మొదటిది ఓసీపీ అంటే Ochre Coloured Pottery. క్రీస్తు పూర్వం రెండు వేల నుండి నాలుగువందల సంవత్సరాల కాలానికి చెందినవి. రెండవది పీజీడబ్ల్యూ అంటే Painted Grey Ware. క్రీస్తు పూర్వం ఒక వేల సంవత్సరాల కాలానికి చెందినవి. వేదకాలపు నాగరికతకు చెందినవి. మూడవది ఎన్‌బీపీ అంటే Northern Black Polished Ware. క్రీస్తు పూర్వం ఏడువందల తర్వాతి కాలానికి చెందినవి. మౌర్య కాలానికి చెందినవి."},
        {"title": "వాస్తు శిల్పాలు – 3 శైలులు", "sub": "Nagara · Dravida · Vesara Architecture Styles",
         "audio": "పురావస్తు ఆధారాలలో చివరగా వాస్తు శిల్పాలు. ఇవి పూర్తిగా చరిత్రకు అద్దం పట్టే ఆధారాలు! భారత దేవాలయ నిర్మాణ శైలులు మూడు. మొదటిది నాగర శైలి. ఇది ఉత్తర భారతంలో వాడుకలో ఉంది. శిఖరాలు గుండ్రంగా, వక్రరేఖల్లో ఉంటాయి. రెండవది ద్రావిడ శైలి. దక్షిణ భారతంలో ప్రచారంలో ఉంది. గోపురాలు పెద్దవిగా, అడ్డంగా ఉంటాయి. మూడవది వేసర శైలి. నాగర మరియు ద్రావిడ శైలుల మిశ్రమం. దక్కన్ ప్రాంతంలో ఎక్కువగా కనిపిస్తుంది. చాళుక్య, రాష్ట్రకూట వంశాల కాలంలో అభివృద్ధి చెందింది."},
        {"title": "Mind Map – సంక్షిప్త సారాంశం", "sub": "అధ్యాయం 1 పూర్తి Mind Mapping | Revision",
         "audio": "అధ్యాయం ఒకటి యొక్క పూర్తి సారాంశం వినండి. ఆధారాలు రెండు రకాలు. లిఖితపూర్వక ఆధారాలు మరియు పురావస్తు ఆధారాలు. విదేశీ సాహిత్యం అంటే ఇండికా మెగస్తనీస్, నాచురల్ హిస్టరీ ప్లీనీ, దీపవంశ మహావంశ, హ్యూయాన్-త్సాంగ్, తారానాథ్ రాసిన The History of Tibet, కితాబ్-ఉల్-హింద్ అల్-బిరూని. స్వదేశీ సాహిత్యం అంటే వేద, బౌద్ధ, జైన గ్రంథాలు, పాణిని అష్టాధ్యాయి, కౌటిల్య అర్థశాస్త్రం, రాజతరంగిణి, పురాణాలు. పురావస్తు ఆధారాలు అంటే శాసనాలు, వాస్తు శిల్పాలు, నాణేలు మరియు కుండలు. గుర్తుంచుకోండి! చరిత్ర అంటే లిఖిత ఆధారాలు మరియు పురావస్తు ఆధారాలు రెండింటి కలయిక. ఈ అధ్యాయం పూర్తయింది. అభినందనలు!"}
    ]

    db_exec(conn, '''
        INSERT INTO study_notes
        (subject, topic, chapter_num, chapter_title_te, chapter_title_en, pages_ref, sections_json)
        VALUES (?,?,?,?,?,?,?)
    ''', ('GK', 'Indian_History', 1, 'చరిత్ర – పరిచయం',
          'Introduction to History', '1-6', json.dumps(ch1_sections, ensure_ascii=False)))
    conn.commit()
    conn.close()
    return jsonify({'success': True, 'message': 'Chapter 1 seeded successfully'})


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
