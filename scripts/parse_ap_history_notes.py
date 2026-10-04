#!/usr/bin/env python3
"""
scripts/parse_ap_history_notes.py
Parses AP History HTML chapter files from static/notes/AP_History/Chapters/
and imports them as Note records.

Usage (local SQLite):
    python scripts/parse_ap_history_notes.py

Usage (production PostgreSQL — via admin endpoint or directly):
    python scripts/parse_ap_history_notes.py --postgres

The script:
  1. Reads ch01_prehistoric_cultures.html … ch12_vijayanagara.html
  2. Extracts <section class="section"> blocks → one Note per section
  3. Replaces all ap_history chapters + notes in the target database
  4. Re-creates 12 chapters with correct titles
"""

import os
import re
import sys
import sqlite3

from bs4 import BeautifulSoup

# ── Chapter file → metadata mapping ────────────────────────────
# (filename, chapter_num, title_te, title_en, est_min)
CHAPTER_FILES = [
    ("ch01_prehistoric_cultures.html",          1, "ప్రాచీన సంస్కృతులు",              "Prehistoric Cultures of AP",        45),
    ("ch02_andhrula_parichayam_aadharalu.html", 2, "ఆంధ్రుల పరిచయం — ఆధారాలు",       "Introduction to Andhras & Sources",  35),
    ("ch03_pre_satavahana_andhra.html",         3, "శాతవాహన పూర్వ ఆంధ్రదేశం",         "Pre-Satavahana Andhra",              30),
    ("ch04_dynasties_overview.html",            4, "ఆంధ్ర రాజవంశాల సమగ్ర పరిచయం",     "Overview of Andhra Dynasties",       30),
    ("ch05_satavahanas.html",                   5, "శాతవాహన రాజవంశం",                 "Satavahana Dynasty",                 40),
    ("ch06_ikshvakus.html",                     6, "ఇక్ష్వాకులు (విజయపురి)",           "Ikshvakus (Vijayapuri)",             35),
    ("ch07_minor_dynasties.html",               7, "చిన్న రాజవంశాలు",                  "Minor Dynasties of AP",              30),
    ("ch08_vishnukundins.html",                 8, "విష్ణుకుండిన రాజవంశం",             "Vishnukundin Dynasty",               30),
    ("ch09_eastern_chalukyas.html",             9, "తూర్పు చాళుక్యులు (వెంగి)",        "Eastern Chalukyas (Vengi)",          35),
    ("ch10_kakatiyas.html",                    10, "కాకతీయులు (వరంగల్)",               "Kakatiyas (Warangal)",               40),
    ("ch11_reddy_kingdoms.html",               11, "రెడ్డి రాజులు + మునుసూరి నాయకులు", "Reddy Kingdoms & Musunuri Nayakas",  35),
    ("ch12_vijayanagara.html",                 12, "విజయనగర సామ్రాజ్యం",              "Vijayanagara Empire",                45),
]

# ── Root detection ───────────────────────────────────────────────
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
APP_ROOT   = os.path.dirname(SCRIPT_DIR)
NOTES_DIR  = os.path.join(APP_ROOT, "static", "notes", "AP_History", "Chapters")
SQLITE_DB  = os.path.join(APP_ROOT, "data", "content.db")


# ── HTML parsing helpers ─────────────────────────────────────────

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
            heading_te = heading_te[:m.start()].strip(" —–")

    # Strip leading section number like "1. " or "01. "
    heading_te = re.sub(r'^\d+\.\s*', '', heading_te).strip()

    return heading_te, heading_en


def extract_chapter_title_te(soup, fallback_title_te):
    """
    Extract chapter title_te from the HTML file's <h1> or <title> element.
    Returns a BeautifulSoup-parsed Unicode string (correct encoding).
    Falls back to the provided string if nothing found.
    """
    # Try <h1>: strip leading emoji/ASCII prefix before the Telugu text
    h1 = soup.find("h1")
    if h1:
        text = h1.get_text(" ", strip=True)
        # Split on em-dash variants and take the last chunk (the chapter name)
        import re as _re
        parts = _re.split(r"[—–\-]\s*", text)
        te_part = parts[-1].strip() if len(parts) > 1 else text
        # Remove leading/trailing non-Telugu punctuation
        te_part = te_part.strip(" 🏺📚")
        if te_part:
            return te_part
    # Try <title> tag: extract part after last colon and before |
    title_tag = soup.find("title")
    if title_tag:
        text = title_tag.get_text()
        if ":" in text:
            text = text.split(":")[-1]
        if "|" in text:
            text = text.split("|")[0]
        text = text.strip()
        if text:
            return text
    return fallback_title_te


def parse_chapter_file(filepath):
    """
    Return (chapter_title_te, list of section dicts).
    Each section dict: {section_num, heading_te, heading_en, body_te, body_en}
    body_te = inner HTML of the section (minus the <h2> heading).
    """
    with open(filepath, encoding="utf-8") as fh:
        soup = BeautifulSoup(fh.read(), "html.parser")

    # Also get the chapter title from the HTML (ensures correct Unicode via BS4)
    chapter_title_te = None  # filled below after we know fallback

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
    return soup, notes


# ── SQLite (local content.db) import ────────────────────────────

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

        # Parse file first so we can extract title_te from HTML (avoids encoding issues)
        soup, sections = parse_chapter_file(filepath)
        html_title_te = extract_chapter_title_te(soup, title_te)

        # Insert chapter
        cur.execute(
            "INSERT INTO chapters (subject_id, chapter_num, title_en, title_te, est_read_minutes) "
            "VALUES (?,?,?,?,?)",
            (subject_id, ch_num, title_en, html_title_te, est_min),
        )
        chapter_id = cur.lastrowid

        # Insert sections
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


# ── PostgreSQL (production) import ──────────────────────────────

def import_to_postgres():
    """Direct PostgreSQL import — used by the admin endpoint on Railway."""
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
        print(f"  Deleting {len(old_chapters)} old chapters…")
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

            # Parse file first so we can extract title_te from HTML (avoids encoding issues)
            soup, sections = parse_chapter_file(filepath)
            html_title_te = extract_chapter_title_te(soup, title_te)

            ch = Chapter(
                subject_id=subj.id,
                chapter_num=ch_num,
                title_en=title_en,
                title_te=html_title_te,
                est_read_minutes=est_min,
            )
            db.session.add(ch)
            db.session.flush()   # get ch.id

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


# ── Entry point ──────────────────────────────────────────────────

if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "--sqlite"
    if mode == "--postgres":
        print("Mode: PostgreSQL (production)")
        import_to_postgres()
    else:
        print("Mode: SQLite (local content.db)")
        import_to_sqlite()
