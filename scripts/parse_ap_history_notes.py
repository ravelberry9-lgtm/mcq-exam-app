#!/usr/bin/env python3
"""
scripts/parse_ap_history_notes.py
Parses AP History HTML chapter files from static/notes/AP_History/Chapters/
and imports them as Note records.

Usage (local SQLite):
    python scripts/parse_ap_history_notes.py

Usage (production PostgreSQL â via admin endpoint or directly):
    python scripts/parse_ap_history_notes.py --postgres

The script:
  1. Reads ch01_prehistoric_cultures.html â¦ ch12_vijayanagara.html
  2. Extracts <section class="section"> blocks â one Note per section
  3. Replaces all ap_history chapters + notes in the target database
  4. Re-creates 12 chapters with correct titles
"""

import os
import re
import sys
import sqlite3

from bs4 import BeautifulSoup

# ââ Chapter file â metadata mapping ââââââââââââââââââââââââââââ
# (filename, chapter_num, title_te, title_en, est_min)
CHAPTER_FILES = [
    ("ch01_prehistoric_cultures.html",          1, "à°ªà±à°°à°¾à°à±à°¨ à°¸à°à°¸à±à°à±à°¤à±à°²à±",              "Prehistoric Cultures of AP",        45),
    ("ch02_andhrula_parichayam_aadharalu.html", 2, "à°à°à°§à±à°°à±à°² à°ªà°°à°¿à°à°¯à° â à°à°§à°¾à°°à°¾à°²à±",       "Introduction to Andhras & Sources",  35),
    ("ch03_pre_satavahana_andhra.html",         3, "à°¶à°¾à°¤à°µà°¾à°¹à°¨ à°ªà±à°°à±à°µ à°à°à°§à±à°°à°¦à±à°¶à°",         "Pre-Satavahana Andhra",              30),
    ("ch04_dynasties_overview.html",            4, "à°à°à°§à±à°° à°°à°¾à°à°µà°à°¶à°¾à°² à°¸à°®à°à±à°° à°ªà°°à°¿à°à°¯à°",     "Overview of Andhra Dynasties",       30),
    ("ch05_satavahanas.html",                   5, "à°¶à°¾à°¤à°µà°¾à°¹à°¨ à°°à°¾à°à°µà°à°¶à°",                 "Satavahana Dynasty",                 40),
    ("ch06_ikshvakus.html",                     6, "à°à°à±à°·à±à°µà°¾à°à±à°²à± (à°µà°¿à°à°¯à°ªà±à°°à°¿)",           "Ikshvakus (Vijayapuri)",             35),
    ("ch07_minor_dynasties.html",               7, "à°à°¿à°¨à±à°¨ à°°à°¾à°à°µà°à°¶à°¾à°²à±",                  "Minor Dynasties of AP",              30),
    ("ch08_vishnukundins.html",                 8, "à°µà°¿à°·à±à°£à±à°à±à°à°¡à°¿à°¨ à°°à°¾à°à°µà°à°¶à°",             "Vishnukundin Dynasty",               30),
    ("ch09_eastern_chalukyas.html",             9, "à°¤à±à°°à±à°ªà± à°à°¾à°³à±à°à±à°¯à±à°²à± (à°µà±à°à°à°¿)",        "Eastern Chalukyas (Vengi)",          35),
    ("ch10_kakatiyas.html",                    10, "à°à°¾à°à°¤à±à°¯à±à°²à± (à°µà°°à°à°à°²à±)",               "Kakatiyas (Warangal)",               40),
    ("ch11_reddy_kingdoms.html",               11, "à°°à±à°¡à±à°¡à°¿ à°°à°¾à°à±à°²à± + à°®à±à°¨à±à°¸à±à°°à°¿ à°¨à°¾à°¯à°à±à°²à±", "Reddy Kingdoms & Musunuri Nayakas",  35),
    ("ch12_vijayanagara.html",                 12, "à°µà°¿à°à°¯à°¨à°à°° à°¸à°¾à°®à±à°°à°¾à°à±à°¯à°",              "Vijayanagara Empire",                45),
]

# ââ Root detection âââââââââââââââââââââââââââââââââââââââââââââââ
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
APP_ROOT   = os.path.dirname(SCRIPT_DIR)
NOTES_DIR  = os.path.join(APP_ROOT, "static", "notes", "AP_History", "Chapters")
SQLITE_DB  = os.path.join(APP_ROOT, "data", "content.db")


# ââ HTML parsing helpers âââââââââââââââââââââââââââââââââââââââââ

def _clean_heading(h2_tag):
    """
    Extract (heading_te, heading_en) from a <h2> tag.
    heading_te = full text, cleaned of leading section numbers
    heading_en = content of .eng span or parenthetical at end
    """
    if h2_tag is None:
        return "", ""

    # Extract .eng span if present
    eng_span = h2_tag.find("span", class_="eng")
    heading_en = ""
    if eng_span:
        heading_en = eng_span.get_text(" ", strip=True).strip("()")
        eng_span.decompose()

    heading_te = h2_tag.get_text(" ", strip=True)

    # If no .eng span, try to pull English from trailing parentheses
    if not heading_en:
        m = re.search(r'\(([A-Za-z][^)]{2,})\)\s*$', heading_te)
        if m:
            heading_en = m.group(1).strip()
            heading_te = heading_te[:m.start()].strip(" ââ")

    # Strip leading section number like "1. " or "01. "
    heading_te = re.sub(r'^\d+\.\s*', '', heading_te).strip()

    return heading_te, heading_en


def parse_chapter_file(filepath):
    """
    Return list of dicts:
        {section_num, heading_te, heading_en, body_te}
    body_te = inner HTML of the section (minus the <h2> heading).
    """
    with open(filepath, encoding="utf-8") as fh:
        soup = BeautifulSoup(fh.read(), "html.parser")

    sections = soup.find_all(["section", "div"], class_="section")
    notes = []
    for i, sec in enumerate(sections, start=1):
        h2 = sec.find("h2", recursive=False)
        if h2 is None:
            # try any h2 at first level
            h2 = sec.find("h2")

        heading_te, heading_en = _clean_heading(h2)

        # Remove h2 from section before capturing body
        if h2:
            h2.decompose()

        body_te = sec.decode_contents().strip()

        notes.append({
            "section_num": i,
            "heading_te":  heading_te,
            "heading_en":  heading_en,
            "body_te":     body_te,
            "body_en":     "",      # rich content is all in body_te
        })
    return notes


# ââ SQLite (local content.db) import ââââââââââââââââââââââââââââ

def import_to_sqlite():
    if not os.path.exists(SQLITE_DB):
        print(f"ERROR: {SQLITE_DB} not found", file=sys.stderr)
        sys.exit(1)

    conn = sqlite3.connect(SQLITE_DB)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    # Find ap_history subject
    row = cur.execute(
        "SELECT id FROM subjects WHERE slug = 'ap_history'"
    ).fetchone()
    if row is None:
        print("ERROR: subject 'ap_history' not found in content.db", file=sys.stderr)
        sys.exit(1)
    subject_id = row["id"]
    print(f"Subject ap_history id={subject_id}")

    # Delete existing chapters (cascade: notes deleted too if FK, else manual)
    existing_ch_ids = [r[0] for r in cur.execute(
        "SELECT id FROM chapters WHERE subject_id=?", (subject_id,)
    ).fetchall()]
    if existing_ch_ids:
        placeholders = ",".join("?" * len(existing_ch_ids))
        cur.execute(f"DELETE FROM notes WHERE chapter_id IN ({placeholders})", existing_ch_ids)
        cur.execute("DELETE FROM chapters WHERE subject_id=?", (subject_id,))
        print(f"  Deleted {len(existing_ch_ids)} old chapters and their notes.")

    total_notes = 0
    for (filename, ch_num, title_te, title_en, est_min) in CHAPTER_FILES:
        filepath = os.path.join(NOTES_DIR, filename)
        if not os.path.exists(filepath):
            print(f"  WARNING: {filename} not found, skipping ch{ch_num}")
            continue

        # Insert chapter
        cur.execute(
            "INSERT INTO chapters (subject_id, chapter_num, title_en, title_te, est_read_minutes) "
            "VALUES (?,?,?,?,?)",
            (subject_id, ch_num, title_en, title_te, est_min),
        )
        chapter_id = cur.lastrowid

        # Parse and insert sections
        sections = parse_chapter_file(filepath)
        for sec in sections:
            cur.execute(
                "INSERT INTO notes (chapter_id, section_num, heading_en, heading_te, body_en, body_te) "
                "VALUES (?,?,?,?,?,?)",
                (chapter_id, sec["section_num"], sec["heading_en"],
                 sec["heading_te"], sec["body_en"], sec["body_te"]),
            )
        total_notes += len(sections)
        print(f"  ch{ch_num:02d} {title_en}: {len(sections)} sections imported (db_id={chapter_id})")

    conn.commit()
    conn.close()
    print(f"\nDone. Total notes inserted: {total_notes}")


# ââ PostgreSQL (production) import ââââââââââââââââââââââââââââââ

def import_to_postgres():
    """Direct PostgreSQL import â used by the admin endpoint on Railway."""
    # Flask app context is required for db access; we use SQLAlchemy models.
    # This function must be called from within the Flask app context.
    import os
    # Bootstrap Flask app
    sys.path.insert(0, APP_ROOT)
    from app import create_app
    from app.db import db
    from app.models import Subject, Chapter, Note

    flask_app = create_app()
    with flask_app.app_context():
        subj = Subject.query.filter_by(slug="ap_history").first()
        if not subj:
            print("ERROR: subject 'ap_history' not found in DB", file=sys.stderr)
            sys.exit(1)
        print(f"Subject ap_history id={subj.id}")

        # Delete existing chapters + notes
        old_chapters = Chapter.query.filter_by(subject_id=subj.id).all()
        print(f"  Deleting {len(old_chapters)} old chaptersâ¦")
        for ch in old_chapters:
            Note.query.filter_by(chapter_id=ch.id).delete()
            db.session.delete(ch)
        db.session.flush()

        total_notes = 0
        for (filename, ch_num, title_te, title_en, est_min) in CHAPTER_FILES:
            filepath = os.path.join(NOTES_DIR, filename)
            if not os.path.exists(filepath):
                print(f"  WARNING: {filename} not found, skipping ch{ch_num}")
                continue

            ch = Chapter(
                subject_id=subj.id,
                chapter_num=ch_num,
                title_en=title_en,
                title_te=title_te,
                est_read_minutes=est_min,
            )
            db.session.add(ch)
            db.session.flush()   # get ch.id

            sections = parse_chapter_file(filepath)
            for sec in sections:
                n = Note(
                    chapter_id=ch.id,
                    section_num=sec["section_num"],
                    heading_en=sec["heading_en"],
                    heading_te=sec["heading_te"],
                    body_en=sec["body_en"],
                    body_te=sec["body_te"],
                )
                db.session.add(n)
            total_notes += len(sections)
            print(f"  ch{ch_num:02d} {title_en}: {len(sections)} sections (db_id={ch.id})")

        db.session.commit()
        print(f"\nDone. Total notes inserted: {total_notes}")


# ââ Entry point ââââââââââââââââââââââââââââââââââââââââââââââââââ

if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "--sqlite"
    if mode == "--postgres":
        print("Mode: PostgreSQL (production)")
        import_to_postgres()
    else:
        print("Mode: SQLite (local content.db)")
        import_to_sqlite()
