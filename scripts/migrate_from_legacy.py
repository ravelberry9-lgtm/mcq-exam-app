#!/usr/bin/env python3
"""
scripts/migrate_from_legacy.py
Migrates _legacy/database.db + static/notes HTML files into v3 schema.

Run:
    DATABASE_URL="sqlite:////tmp/app_v3_migrated.db" python scripts/migrate_from_legacy.py

Decisions documented here:
  - GK/General Knowledge PYQ (384) -> indian_history (catch-all historical GK)
  - AP General PYQ (65)            -> ap_geography
  - Sports PYQ (12)                -> current_affairs
  - chapter_mcqs difficulty 4      -> H (no v3 equivalent above H)
  - Indian_Polity HTML (90 files)  -> indian_constitution chapters 1-90
  - study_notes ch conflicts       -> when (subject, ch_num) taken, use max+1
  - HTML notes body stored as body_en (all legacy HTML is bilingual inline)
"""
import sys, os, json, sqlite3, hashlib, glob, re
from pathlib import Path
from datetime import datetime

ROOT = Path(__file__).resolve().parent.parent
LEGACY_DB = ROOT / "_legacy" / "database.db"
LEGACY_NOTES = ROOT / "_legacy" / "static" / "notes"
LEGACY_DIR   = ROOT / "_legacy"
ARCHIVE_DIR  = ROOT / "_legacy" / "archived_dropped"
ERRORS_FILE  = ROOT / "migration_errors.json"

sys.path.insert(0, str(ROOT))

# ── Subject taxonomy ──────────────────────────────────────────────
SUBJECTS = [
    ("indian_history",      "Indian History",                "భారత చరిత్ర",                  1),
    ("indian_constitution", "Indian Constitution",           "భారత రాజ్యాంగం",                2),
    ("ap_history",          "AP Social & Cultural History",  "ఆంధ్రప్రదేశ్ చరిత్ర",           3),
    ("indian_geography",    "Indian Geography",              "భారత భూగోళశాస్త్రం",            4),
    ("ap_geography",        "AP Geography",                  "ఆంధ్రప్రదేశ్ భూగోళశాస్త్రం",     5),
    ("indian_economy",      "Indian Economy",                "భారత ఆర్థిక వ్యవస్థ",           6),
    ("ap_economy",          "AP Economy",                    "ఆంధ్రప్రదేశ్ ఆర్థిక వ్యవస్థ",    7),
    ("science_technology",  "Science & Technology",          "సైన్స్ & సాంకేతికత",            8),
    ("indian_society",      "Indian Society",                "భారత సమాజం",                   9),
    ("mental_ability",      "Mental Ability",                "మానసిక సామర్థ్యం",             10),
    ("current_affairs",     "Current Affairs",               "ప్రస్తుత వ్యవహారాలు",          11),
]

# ── Legacy topic → v3 subject slug ───────────────────────────────
TOPIC_TO_SLUG = {
    # study_notes topics
    "Indian_Polity":     "indian_constitution",
    "Indian_History":    "indian_history",
    "AP_Geography":      "ap_geography",
    "AP_Current_Affairs":"current_affairs",
    # questions folder/topic
    "Art_Culture":       "ap_history",
    "General_Science":   "science_technology",
    "Everyday_Science":  "science_technology",
    "Indian_Economy":    "indian_economy",
    "Mental_Ability":    "mental_ability",
    "AP_Current_Affairs_2026": "current_affairs",
    # pyq_questions topics
    "Art & Culture":       "ap_history",
    "Indian History":      "indian_history",
    "Indian Geography":    "indian_geography",
    "Constitution & Polity":"indian_constitution",
    "Economy & Finance":   "indian_economy",
    "Science & Technology":"science_technology",
    "Current Affairs":     "current_affairs",
    "Sports":              "current_affairs",
    "AP General":          "ap_geography",
    "General Knowledge":   "indian_history",
}

ARCHIVE_TOPICS   = {"International_Current_Affairs", "Consumer_Protection"}
ARCHIVE_FOLDERS  = {"National_CA"}
DIFF_MAP         = {1: "E", 2: "M", 3: "H", 4: "H"}

# HTML dir → subject slug mapping
HTML_DIR_TO_SLUG = {
    "Indian_Geography": "indian_geography",
    "AP_Geography":     "ap_geography",
    "Indian_Polity":    "indian_constitution",
    "Art_Culture":      "ap_history",
    "General_Science":  "science_technology",
    "AP_Current_Affairs":"current_affairs",
}

def md5q(s): return hashlib.md5((s or "").encode("utf-8", "replace")).hexdigest()

errors = []
def log_err(table, row_id, msg):
    errors.append({"table": table, "id": row_id, "error": msg})
    print(f"  [ERR] {table} id={row_id}: {msg}")


# ── DB helpers ────────────────────────────────────────────────────
def get_or_create_subject(cur, slug, name_en, name_te, sort_order):
    cur.execute("SELECT id FROM subjects WHERE slug=?", (slug,))
    row = cur.fetchone()
    if row:
        return row[0]
    cur.execute(
        "INSERT INTO subjects (slug,name_en,name_te,sort_order) VALUES (?,?,?,?)",
        (slug, name_en, name_te, sort_order)
    )
    return cur.lastrowid

def get_or_create_chapter(cur, subject_id, chapter_num, title_en, title_te=""):
    """Upsert chapter by (subject_id, chapter_num). If num taken by diff title, use max+1."""
    cur.execute("SELECT id, title_en FROM chapters WHERE subject_id=? AND chapter_num=?",
                (subject_id, chapter_num))
    row = cur.fetchone()
    if row:
        if row[1] == title_en:
            return row[0]  # exact match, reuse
        # conflict: same num, different title → use max+1
        cur.execute("SELECT COALESCE(MAX(chapter_num),0) FROM chapters WHERE subject_id=?",
                    (subject_id,))
        chapter_num = cur.fetchone()[0] + 1

    cur.execute(
        "INSERT INTO chapters (subject_id, chapter_num, title_en, title_te, est_read_minutes)"
        " VALUES (?,?,?,?,?)",
        (subject_id, chapter_num, title_en, title_te or title_en, 20)
    )
    return cur.lastrowid

def upsert_question(cur, q_hash, subject_id, chapter_id, source_type,
                    q_en, q_te, opts_en, opts_te, correct, difficulty,
                    explanation_en, explanation_te, pyq_year=None, pyq_paper=None):
    cur.execute("SELECT id FROM questions WHERE q_hash=?", (q_hash,))
    row = cur.fetchone()
    if row:
        return row[0], False  # already exists
    correct = (correct or "a").strip().lower()
    if correct not in ("a","b","c","d","e"):
        correct = "a"
    cur.execute(
        """INSERT INTO questions
           (subject_id, chapter_id, source_type, difficulty,
            question_en, question_te, options_en, options_te,
            correct_answer, explanation_en, explanation_te,
            pyq_year, pyq_paper, q_hash, created_at, updated_at)
           VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
        (subject_id, chapter_id, source_type, difficulty or "M",
         q_en, q_te,
         json.dumps(opts_en or {}, ensure_ascii=False),
         json.dumps(opts_te or {}, ensure_ascii=False),
         correct, explanation_en, explanation_te,
         pyq_year, pyq_paper, q_hash,
         datetime.utcnow().isoformat(), datetime.utcnow().isoformat())
    )
    return cur.lastrowid, True


# ── Schema setup for fresh DB ─────────────────────────────────────
def init_db(cur):
    """Create v3 tables if they don't exist (for fresh /tmp DB)."""
    cur.executescript("""
    CREATE TABLE IF NOT EXISTS subjects (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        slug TEXT UNIQUE NOT NULL,
        name_en TEXT NOT NULL,
        name_te TEXT NOT NULL,
        sort_order INTEGER DEFAULT 0
    );
    CREATE TABLE IF NOT EXISTS chapters (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        subject_id INTEGER NOT NULL REFERENCES subjects(id),
        chapter_num INTEGER NOT NULL,
        title_en TEXT NOT NULL,
        title_te TEXT NOT NULL,
        est_read_minutes INTEGER DEFAULT 20,
        UNIQUE(subject_id, chapter_num)
    );
    CREATE TABLE IF NOT EXISTS notes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        chapter_id INTEGER NOT NULL REFERENCES chapters(id),
        section_num INTEGER NOT NULL,
        heading_en TEXT,
        heading_te TEXT,
        body_en TEXT,
        body_te TEXT,
        UNIQUE(chapter_id, section_num)
    );
    CREATE TABLE IF NOT EXISTS pages (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        slug TEXT UNIQUE NOT NULL,
        title_en TEXT NOT NULL,
        title_te TEXT NOT NULL,
        body_en TEXT,
        body_te TEXT,
        page_type TEXT DEFAULT 'page',
        visible INTEGER DEFAULT 1,
        created_at TEXT,
        updated_at TEXT
    );
    CREATE TABLE IF NOT EXISTS questions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        subject_id INTEGER NOT NULL REFERENCES subjects(id),
        chapter_id INTEGER REFERENCES chapters(id),
        source_type TEXT NOT NULL,
        pyq_year TEXT,
        pyq_paper TEXT,
        difficulty TEXT DEFAULT 'M',
        question_en TEXT,
        question_te TEXT,
        options_en TEXT,
        options_te TEXT,
        correct_answer TEXT NOT NULL,
        explanation_en TEXT,
        explanation_te TEXT,
        passage_id INTEGER,
        q_hash TEXT UNIQUE,
        created_at TEXT,
        updated_at TEXT
    );
    CREATE INDEX IF NOT EXISTS idx_q_subj ON questions(subject_id);
    CREATE INDEX IF NOT EXISTS idx_q_ch   ON questions(chapter_id);
    CREATE INDEX IF NOT EXISTS idx_q_hash ON questions(q_hash);
    CREATE TABLE IF NOT EXISTS exam_sessions (
        id TEXT PRIMARY KEY,
        device_id TEXT NOT NULL,
        config TEXT NOT NULL,
        question_ids TEXT NOT NULL,
        answers TEXT DEFAULT '{}',
        confidences TEXT DEFAULT '{}',
        started_at TEXT,
        submitted_at TEXT,
        score INTEGER,
        total INTEGER
    );
    """)


# ── Step 1: Seed subjects ─────────────────────────────────────────
def step_subjects(cur):
    print("\n=== STEP 1: Subjects ===")
    slug_to_id = {}
    for slug, en, te, order in SUBJECTS:
        sid = get_or_create_subject(cur, slug, en, te, order)
        slug_to_id[slug] = sid
    print(f"  {len(slug_to_id)} subjects ready")
    return slug_to_id

# ── Step 2: Chapters + Notes from study_notes DB rows ────────────
def step_study_notes(src, cur, slug_to_id):
    print("\n=== STEP 2: study_notes → chapters + notes ===")
    src.row_factory = sqlite3.Row
    rows = src.execute(
        "SELECT * FROM study_notes ORDER BY topic, subtopic, chapter_num, id"
    ).fetchall()
    ch_created = note_created = 0
    sn_to_chapter = {}  # study_note id → new chapter id

    # Pre-compute which study_note_ids are referenced in chapter_mcqs but missing
    # so we can create placeholder chapters for them
    all_sn_ids = {r["id"] for r in rows}
    referenced_ids = set(
        r[0] for r in src.execute(
            "SELECT DISTINCT study_note_id FROM chapter_mcqs"
        ).fetchall()
    )
    missing_ids = referenced_ids - all_sn_ids
    # Infer subject for missing IDs by nearest neighbor in sorted study_notes
    sorted_sn = sorted(rows, key=lambda r: r["id"])
    def infer_slug_for_missing(mid):
        # find closest existing study_note_id and use its topic
        best = min(sorted_sn, key=lambda r: abs(r["id"] - mid), default=None)
        if best:
            return TOPIC_TO_SLUG.get(best["topic"])
        return "indian_history"
    for mid in sorted(missing_ids):
        slug = infer_slug_for_missing(mid)
        subject_id = slug_to_id.get(slug)
        if not subject_id:
            continue
        cur.execute("SELECT COALESCE(MAX(chapter_num),0) FROM chapters WHERE subject_id=?",
                    (subject_id,))
        next_num = cur.fetchone()[0] + 1
        ch_id = get_or_create_chapter(
            cur, subject_id, next_num,
            f"Chapter (recovered, sn_id={mid})"
        )
        sn_to_chapter[mid] = ch_id
        ch_created += 1
    print(f"  placeholder chapters for {len(missing_ids)} missing study_note_ids")

    for r in rows:
        topic = r["topic"]
        slug = TOPIC_TO_SLUG.get(topic)
        if not slug:
            log_err("study_notes", r["id"], f"unmapped topic: {topic}")
            continue
        subject_id = slug_to_id.get(slug)
        if not subject_id:
            continue

        ch_id = get_or_create_chapter(
            cur, subject_id, r["chapter_num"],
            r["chapter_title_en"] or f"Chapter {r['chapter_num']}",
            r["chapter_title_en"] or ""
        )
        sn_to_chapter[r["id"]] = ch_id
        ch_created += 1

        # Insert sections from sections_json
        try:
            sections = json.loads(r["sections_json"] or "[]")
        except Exception:
            sections = []

        for i, sec in enumerate(sections, 1):
            # Handle double-encoded JSON items
            if isinstance(sec, str):
                try:
                    sec = json.loads(sec)
                except Exception:
                    sec = {"title": sec, "sub": ""}
            if not isinstance(sec, dict):
                continue
            heading = sec.get("title", "")
            body_val = sec.get("sub", "")
            if isinstance(body_val, list):
                body = "<br>".join(str(x) for x in body_val)
            else:
                body = str(body_val) if body_val else ""
            cur.execute(
                "INSERT OR IGNORE INTO notes "
                "(chapter_id, section_num, heading_en, heading_te, body_en, body_te)"
                " VALUES (?,?,?,?,?,?)",
                (ch_id, i, heading, "", body, "")
            )
            note_created += 1

    print(f"  chapters upserted: {ch_created}, notes created: {note_created}")
    return sn_to_chapter

# ── Step 3: Migrate chapter_mcqs ─────────────────────────────────
def step_chapter_mcqs(src, cur, slug_to_id, sn_to_chapter):
    print("\n=== STEP 3: chapter_mcqs → questions ===")
    rows = src.execute("SELECT * FROM chapter_mcqs").fetchall()
    ins = skipped = err = 0
    for r in rows:
        try:
            sn_id = r[1]  # study_note_id
            ch_id = sn_to_chapter.get(sn_id)
            if ch_id is None:
                log_err("chapter_mcqs", r[0], f"no chapter for study_note_id {sn_id}")
                err += 1
                continue

            # Get subject from chapter
            cur.execute("SELECT subject_id FROM chapters WHERE id=?", (ch_id,))
            subj_row = cur.fetchone()
            if not subj_row:
                err += 1; continue
            subject_id = subj_row[0]

            diff_int = r[3]  # difficulty int 1-4
            diff = DIFF_MAP.get(diff_int, "M")
            q_te = r[5] or ""
            correct = (r[10] or "a").strip().lower()
            if correct not in ("a","b","c","d","e"):
                correct = "a"

            opts_te = {"a": r[6] or "", "b": r[7] or "", "c": r[8] or "", "d": r[9] or ""}

            q_hash = md5q(f"cm:{r[0]}:{q_te[:80]}")
            _, created = upsert_question(
                cur, q_hash, subject_id, ch_id, "chapter",
                None, q_te, {}, opts_te, correct, diff,
                None, r[11]  # explanation_te
            )
            if created: ins += 1
            else: skipped += 1
        except Exception as e:
            log_err("chapter_mcqs", r[0], str(e))
            err += 1
    print(f"  inserted: {ins}, skipped(dup): {skipped}, errors: {err}")
    return ins


# ── Step 4: Migrate questions table (GK/AP_HC/Mental_Ability) ────
def step_questions(src, cur, slug_to_id):
    print("\n=== STEP 4: questions table → questions + archive ===")
    rows = src.execute("SELECT * FROM questions").fetchall()
    # cols: id,folder,topic,source_file,passage,passage_group_id,
    #       question_text,option_a-e,correct_answer,difficulty,explanation,question_order,created_at
    ins = skipped = archived = err = 0
    archive_rows = []

    for r in rows:
        try:
            folder = r[1] or ""
            topic  = r[2] or ""

            # Archive decision
            if folder in ARCHIVE_FOLDERS or topic in ARCHIVE_TOPICS:
                archive_rows.append({
                    "id": r[0], "folder": folder, "topic": topic,
                    "question_text": r[6],
                    "option_a": r[7], "option_b": r[8],
                    "option_c": r[9], "option_d": r[10], "option_e": r[11],
                    "correct_answer": r[12], "difficulty": r[13],
                    "explanation": r[14]
                })
                archived += 1
                continue

            # Map topic to slug
            slug = TOPIC_TO_SLUG.get(topic) or TOPIC_TO_SLUG.get(folder)
            if not slug:
                log_err("questions", r[0], f"unmapped folder/topic: {folder}/{topic}")
                err += 1
                continue

            # AP Economy split: Indian_Economy rows mentioning Andhra
            q_text = r[6] or ""
            if topic == "Indian_Economy" and ("Andhra" in q_text or "ఆంధ్ర" in q_text):
                slug = "ap_economy"

            subject_id = slug_to_id.get(slug)
            if not subject_id:
                err += 1; continue

            correct = (r[12] or "a").strip().lower()
            diff_val = r[13]
            if isinstance(diff_val, int):
                diff = DIFF_MAP.get(diff_val, "M")
            else:
                diff = str(diff_val).upper()[:1] if diff_val else "M"
                if diff not in ("E","M","H"): diff = "M"

            opts_en = {}
            for k, v in zip("abcde", [r[7],r[8],r[9],r[10],r[11]]):
                if v: opts_en[k] = v

            q_hash = md5q(f"q:{r[0]}:{q_text[:80]}")
            _, created = upsert_question(
                cur, q_hash, subject_id, None, "practice",
                q_text, None, opts_en, {}, correct, diff,
                r[14], None  # explanation_en, no te
            )
            if created: ins += 1
            else: skipped += 1
        except Exception as e:
            log_err("questions", r[0], str(e))
            err += 1

    # Write archive JSON
    ARCHIVE_DIR.mkdir(parents=True, exist_ok=True)
    archive_path = ARCHIVE_DIR / "intl_ca.json"
    with open(archive_path, "w", encoding="utf-8") as f:
        json.dump(archive_rows, f, ensure_ascii=False, indent=2)
    print(f"  inserted: {ins}, skipped(dup): {skipped}, archived: {archived}, errors: {err}")
    print(f"  archive written: {archive_path} ({len(archive_rows)} rows)")
    return ins, archived

# ── Step 5: Migrate pyq_questions ────────────────────────────────
def step_pyq(src, cur, slug_to_id):
    print("\n=== STEP 5: pyq_questions → questions ===")
    rows = src.execute("SELECT * FROM pyq_questions").fetchall()
    # cols: id,topic,year,paper,question_number,question_text,
    #       option_a,option_b,option_c,option_d,correct_answer,language,created_at
    ins = skipped = err = 0
    for r in rows:
        try:
            topic = r[1] or ""
            slug  = TOPIC_TO_SLUG.get(topic)
            if not slug:
                log_err("pyq_questions", r[0], f"unmapped topic: {topic}")
                err += 1; continue

            subject_id = slug_to_id.get(slug)
            if not subject_id:
                err += 1; continue

            correct = (r[10] or "A").strip().upper()
            # PYQ correct_answer is uppercase A-D; lowercase for v3
            correct = correct.lower()
            if correct not in ("a","b","c","d","e"):
                correct = "a"

            opts_en = {}
            for k, v in zip("abcd", [r[6], r[7], r[8], r[9]]):
                if v: opts_en[k] = v

            q_text = r[5] or ""
            q_hash = md5q(f"pyq:{r[0]}:{q_text[:80]}")
            _, created = upsert_question(
                cur, q_hash, subject_id, None, "pyq",
                q_text, None, opts_en, {}, correct, "M",
                None, None,
                pyq_year=str(r[2]) if r[2] else None,
                pyq_paper=str(r[3]) if r[3] else None
            )
            if created: ins += 1
            else: skipped += 1
        except Exception as e:
            log_err("pyq_questions", r[0], str(e))
            err += 1
    print(f"  inserted: {ins}, skipped(dup): {skipped}, errors: {err}")
    return ins


# ── Step 6: HTML notes → chapters + notes ────────────────────────
def slugify(s):
    return re.sub(r"[^a-z0-9]+", "_", (s or "").lower()).strip("_")

def html_title_from_filename(fname):
    """ch01_location_area.html -> 'Location Area' """
    stem = Path(fname).stem  # e.g. ch01_location_area
    stem = re.sub(r"^(ch|polity_ch)\d+[a-z]?_?", "", stem)
    stem = stem.replace("_notes","").replace("_"," ").strip().title()
    return stem or Path(fname).stem

def chapter_num_from_filename(fname):
    """Extract number from ch01_... or polity_ch17_... etc."""
    m = re.search(r"(?:polity_ch|ch)(\d+)", Path(fname).stem)
    return int(m.group(1)) if m else None

def step_html_notes(cur, slug_to_id):
    print("\n=== STEP 6: HTML notes → chapters + notes ===")
    ch_created = note_created = page_created = 0

    # Walk _legacy/static/notes/<Subject>/...
    for subj_dir in sorted(LEGACY_NOTES.iterdir()):
        if not subj_dir.is_dir():
            continue
        slug = HTML_DIR_TO_SLUG.get(subj_dir.name)
        if not slug:
            print(f"  skip (no slug): {subj_dir.name}")
            continue
        subject_id = slug_to_id.get(slug)
        if not subject_id:
            continue

        # Only process Chapters/ subdirs for structured notes
        for sub in sorted(subj_dir.iterdir()):
            if not sub.is_dir():
                continue
            if sub.name not in ("Chapters", "Divisions", "Study_Notes"):
                continue
            for html_file in sorted(sub.glob("*.html")):
                ch_num = chapter_num_from_filename(html_file.name)
                if ch_num is None:
                    continue
                title_en = html_title_from_filename(html_file.name)
                try:
                    body = html_file.read_text(encoding="utf-8", errors="replace")
                except Exception as e:
                    log_err("html_notes", str(html_file), str(e))
                    continue

                ch_id = get_or_create_chapter(cur, subject_id, ch_num, title_en)
                ch_created += 1

                # Store entire HTML as section 1 body_en
                cur.execute(
                    "INSERT OR IGNORE INTO notes"
                    " (chapter_id, section_num, heading_en, heading_te, body_en, body_te)"
                    " VALUES (?,?,?,?,?,?)",
                    (ch_id, 1, title_en, "", body, "")
                )
                if cur.rowcount:
                    note_created += 1

    # ── Orphan HTML files at _legacy/*.html ──────────────────────
    orphan_map = {
        "AP_HC_Constitution_Bilingual.html": ("indian_constitution", "AP HC Constitution Bilingual"),
        "ap_geo_ch1_notes.html": ("ap_geography",        "AP Geography Chapter 1"),
        "ap_geo_ch2_notes.html": ("ap_geography",        "AP Geography Chapter 2"),
        "ap_geo_ch3_notes.html": ("ap_geography",        "AP Geography Chapter 3"),
        "ap_geo_ch4_notes.html": ("ap_geography",        "AP Geography Chapter 4"),
        "ap_geo_ch5_notes.html": ("ap_geography",        "AP Geography Chapter 5"),
        "medieval_india_telugu.html":  ("indian_history", "Medieval India (Telugu)"),
        "modern_india_telugu.html":    ("indian_history", "Modern India (Telugu)"),
        "india_current_affairs_telugu_2025_26.html": (None, "India Current Affairs 2025-26"),
        "MIDDLE_EAST_WAR_2024_2026_COMPLETE_NOTES_ENGLISH.html": (None, "Middle East War Notes"),
    }
    for fname, (slug, title) in orphan_map.items():
        fpath = LEGACY_DIR / fname
        if not fpath.exists():
            continue
        try:
            body = fpath.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue

        if slug and slug in slug_to_id:
            # Add as chapter note
            subject_id = slug_to_id[slug]
            cur.execute("SELECT COALESCE(MAX(chapter_num),0) FROM chapters WHERE subject_id=?",
                        (subject_id,))
            next_num = cur.fetchone()[0] + 1
            ch_id = get_or_create_chapter(cur, subject_id, next_num, title)
            cur.execute(
                "INSERT OR IGNORE INTO notes"
                " (chapter_id, section_num, heading_en, heading_te, body_en, body_te)"
                " VALUES (?,?,?,?,?,?)",
                (ch_id, 1, title, "", body, "")
            )
            ch_created += 1
            if cur.rowcount: note_created += 1
        else:
            # Store as page
            page_slug = slugify(title)[:120]
            cur.execute(
                "INSERT OR IGNORE INTO pages"
                " (slug, title_en, title_te, body_en, page_type, visible, created_at, updated_at)"
                " VALUES (?,?,?,?,'page',1,?,?)",
                (page_slug, title, "", body,
                 datetime.utcnow().isoformat(), datetime.utcnow().isoformat())
            )
            if cur.rowcount: page_created += 1

    print(f"  chapters upserted: {ch_created}, notes created: {note_created}, pages: {page_created}")
    return ch_created, note_created


# ── Step 7: Migrate exam_sessions ────────────────────────────────
def step_exam_sessions(src, cur):
    print("\n=== STEP 7: exam_sessions ===")
    rows = src.execute("SELECT * FROM exam_sessions").fetchall()
    # cols: id, config, questions, answers, started_at, submitted_at, score, total
    ins = skipped = 0
    for r in rows:
        sid = str(r[0])
        cur.execute("SELECT id FROM exam_sessions WHERE id=?", (sid,))
        if cur.fetchone():
            skipped += 1; continue
        cur.execute(
            """INSERT INTO exam_sessions
               (id, device_id, config, question_ids, answers, started_at, submitted_at, score, total)
               VALUES (?,?,?,?,?,?,?,?,?)""",
            (sid, "legacy",
             r[1] or "{}",   # config
             r[2] or "[]",   # questions -> question_ids
             r[3] or "{}",   # answers
             r[4], r[5], r[6], r[7])
        )
        ins += 1
    print(f"  inserted: {ins}, skipped(dup): {skipped}")
    return ins

# ── Main ──────────────────────────────────────────────────────────
def main():
    db_url = os.environ.get("DATABASE_URL", "")
    if db_url.startswith("sqlite:///"):
        new_db_path = db_url.replace("sqlite:///", "")
    elif db_url.startswith("sqlite:////"):
        new_db_path = db_url.replace("sqlite:////", "/")
    else:
        new_db_path = "/tmp/app_v3_migrated.db"

    print(f"Migration target: {new_db_path}")
    print(f"Legacy source:    {LEGACY_DB}")

    if not LEGACY_DB.exists():
        print(f"ERROR: legacy DB not found at {LEGACY_DB}")
        sys.exit(1)

    src = sqlite3.connect(str(LEGACY_DB))
    src.row_factory = sqlite3.Row

    dst = sqlite3.connect(new_db_path)
    dst.execute("PRAGMA journal_mode=WAL")
    dst.execute("PRAGMA foreign_keys=OFF")  # allow migration without FK ordering
    cur = dst.cursor()
    init_db(cur)
    dst.commit()

    # Run all steps
    slug_to_id   = step_subjects(cur);         dst.commit()
    sn_to_ch     = step_study_notes(src, cur, slug_to_id); dst.commit()
    q_cm         = step_chapter_mcqs(src, cur, slug_to_id, sn_to_ch); dst.commit()
    q_gk, arc    = step_questions(src, cur, slug_to_id);   dst.commit()
    q_pyq        = step_pyq(src, cur, slug_to_id);         dst.commit()
    step_html_notes(cur, slug_to_id);         dst.commit()
    step_exam_sessions(src, cur);             dst.commit()

    # ── Summary ───────────────────────────────────────────────────
    total_q = cur.execute("SELECT COUNT(*) FROM questions").fetchone()[0]
    total_ch = cur.execute("SELECT COUNT(*) FROM chapters").fetchone()[0]
    total_notes = cur.execute("SELECT COUNT(*) FROM notes").fetchone()[0]

    # AP economy check
    ap_eco_id = slug_to_id.get("ap_economy")
    ap_eco_q  = cur.execute("SELECT COUNT(*) FROM questions WHERE subject_id=?",
                             (ap_eco_id,)).fetchone()[0] if ap_eco_id else 0

    print(f"""
=== MIGRATION SUMMARY ===
  Questions migrated : {total_q}
    chapter_mcqs     : {q_cm}
    questions (GK)   : {q_gk}
    pyq_questions    : {q_pyq}
  Archived (dropped) : {arc}
  AP Economy Q       : {ap_eco_q}
  Chapters           : {total_ch}
  Notes              : {total_notes}
  Errors logged      : {len(errors)}
""")

    # Write error log
    if errors:
        with open(ERRORS_FILE, "w", encoding="utf-8") as f:
            json.dump(errors, f, ensure_ascii=False, indent=2)
        print(f"  Error log: {ERRORS_FILE}")
    else:
        print("  No errors.")

    src.close(); dst.close()
    return total_q

if __name__ == "__main__":
    main()
