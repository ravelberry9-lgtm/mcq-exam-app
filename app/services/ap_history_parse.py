"""Parse the AP History HTML chapter files into an import *source* for ``content_import``.

The parsing helpers below are the ones that used to live in ``scripts/parse_ap_history_notes.py`` (unchanged). What changed
is what happens with the result: it is no longer written over the live chapters and notes. ``build_source`` packs the parsed
chapters into a temporary read-only SQLite source, and the generic preview → scoped, transactional, backed-up apply →
restore flow in ``content_import`` decides what to do with it.
"""
import hashlib
import json
import os
import re
import sqlite3
import tempfile
from pathlib import Path

from bs4 import BeautifulSoup

from ..models import Subject
from .content_import import ContentImportError, Source

APP_ROOT = str(Path(__file__).resolve().parent.parent.parent)
NOTES_DIR = os.path.join(APP_ROOT, "static", "notes", "AP_History", "Chapters")
SUBJECT_SLUG = "ap_history"

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


_SCHEMA = """
CREATE TABLE subjects(id INTEGER PRIMARY KEY, slug TEXT, name_en TEXT, name_te TEXT, sort_order INT);
CREATE TABLE chapters(id INTEGER PRIMARY KEY, subject_id INT, chapter_num INT, title_en TEXT, title_te TEXT, est_read_minutes INT);
CREATE TABLE notes(id INTEGER PRIMARY KEY, chapter_id INT, section_num INT, heading_en TEXT, heading_te TEXT, body_en TEXT, body_te TEXT);
CREATE TABLE questions(id INTEGER PRIMARY KEY, subject_id INT, chapter_id INT, source_type TEXT, difficulty TEXT,
  question_en TEXT, question_te TEXT, options_en TEXT, options_te TEXT, correct_answer TEXT,
  explanation_en TEXT, explanation_te TEXT, pyq_year TEXT, pyq_paper TEXT);
"""


def build_source(notes_dir=None):
    """Parse the chapter files and return a ``Source``. The ``ap_history`` subject must already exist live (its names are
    reused); missing chapter files are reported as warnings, not silently skipped."""
    notes_dir = notes_dir or NOTES_DIR
    subj = Subject.query.filter_by(slug=SUBJECT_SLUG).first()
    if subj is None:
        raise ContentImportError("Subject 'ap_history' does not exist in the live database. "
                                 "Import it from Load Content first. Nothing was changed.")
    tmp = tempfile.mkdtemp(prefix="ap_history_src_")
    conn = sqlite3.connect(os.path.join(tmp, "ap_history.db"))
    try:
        conn.executescript(_SCHEMA)
        conn.execute("INSERT INTO subjects VALUES(1,?,?,?,?)", (SUBJECT_SLUG, subj.name_en, subj.name_te, subj.sort_order or 0))
        digest, warnings = hashlib.sha256(), []
        for (filename, ch_num, title_te, title_en, est_min) in CHAPTER_FILES:
            path = os.path.join(notes_dir, filename)
            if not os.path.exists(path):
                warnings.append(f"{filename} not found; chapter {ch_num} is not part of this import.")
                continue
            with open(path, "rb") as fh:
                digest.update(filename.encode()); digest.update(fh.read())
            soup, sections = parse_chapter_file(path)
            cur = conn.execute("INSERT INTO chapters(subject_id, chapter_num, title_en, title_te, est_read_minutes) VALUES(1,?,?,?,?)",
                               (ch_num, title_en, extract_chapter_title_te(soup, title_te), est_min))
            for sec in sections:
                conn.execute("INSERT INTO notes(chapter_id, section_num, heading_en, heading_te, body_en, body_te) VALUES(?,?,?,?,?,?)",
                             (cur.lastrowid, sec["section_num"], sec["heading_en"], sec["heading_te"], sec["body_en"], sec["body_te"]))
        conn.commit()
        conn.close()
        ro = sqlite3.connect(f"file:{Path(tmp, 'ap_history.db').as_posix()}?mode=ro", uri=True)
        ro.row_factory = sqlite3.Row
        digest.update(json.dumps(CHAPTER_FILES, ensure_ascii=False).encode())
        return Source(ro, digest.hexdigest(), tmp, warnings)
    except BaseException:
        conn.close()
        import shutil
        shutil.rmtree(tmp, ignore_errors=True)
        raise
