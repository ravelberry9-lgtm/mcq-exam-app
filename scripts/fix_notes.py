#!/usr/bin/env python3
"""
scripts/fix_notes.py
Rebuilds notes in data/content.db from the legacy database.

Fixes two bugs from the original migration:
 1. Double-encoded JSON in study_notes ids 51-54 (AP_Current_Affairs chapters 7-10)
    caused the parser to iterate character-by-character, producing ~5,601 garbage notes.
 2. Body content was too thin — only the short `sub` keyword was stored.
    This script now stores:
      body_en  = keywords formatted as <ul><li>…</li></ul>
      body_te  = audio lecture text formatted as <p>…</p> paragraphs (when available)

Usage:
    python scripts/fix_notes.py
"""
import sys, os, json, sqlite3, re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LEGACY_DB = ROOT / "_legacy" / "database.db"
DATA_DB   = ROOT / "data" / "content.db"


# ── HTML formatters ────────────────────────────────────────────────

def format_keywords_as_html(text: str) -> str:
    """
    Converts "Keyword1 · Keyword2 · Keyword3" into a <ul> list.
    Also handles plain paragraphs (no · separators).
    """
    if not text:
        return ""
    # Split on · or — bullet separators
    parts = [p.strip() for p in re.split(r'\s*[·•]\s*', text) if p.strip()]
    if len(parts) <= 1:
        # No bullets — wrap in a paragraph
        return f"<p>{text.strip()}</p>"
    items = "".join(f"<li>{p}</li>" for p in parts)
    return f"<ul>{items}</ul>"


def format_audio_as_html(audio: str) -> str:
    """
    Converts audio lecture text (Telugu sentences) into <p> paragraphs.
    Sentences are split on `. ` or `.\n`.
    """
    if not audio:
        return ""
    # Split into sentences on '. ' or '.\n'
    sentences = re.split(r'\.\s+', audio.strip())
    paragraphs = []
    current = []
    for s in sentences:
        s = s.strip()
        if not s:
            continue
        current.append(s)
        # Group ~3 sentences per paragraph for readability
        if len(current) >= 3:
            paragraphs.append(". ".join(current) + ".")
            current = []
    if current:
        paragraphs.append(". ".join(current) + ("." if not current[-1].endswith(".") else ""))
    if not paragraphs:
        return f"<p>{audio.strip()}</p>"
    return "".join(f"<p>{p}</p>" for p in paragraphs)


def parse_sections_json(raw: str):
    """
    Parse sections_json handling both normal and double-encoded JSON.
    Returns a list of dicts.
    """
    if not raw:
        return []
    try:
        parsed = json.loads(raw)
    except Exception:
        return []

    # If parsed is a string → double-encoded; parse again
    if isinstance(parsed, str):
        try:
            parsed = json.loads(parsed)
        except Exception:
            return []

    if not isinstance(parsed, list):
        return []

    # Ensure each item is a dict (handle double-encoded list items)
    result = []
    for item in parsed:
        if isinstance(item, str):
            try:
                item = json.loads(item)
            except Exception:
                continue
        if isinstance(item, dict):
            result.append(item)
    return result


def get_section_fields(sec: dict):
    """
    Extract (heading, body_en, body_te) from a section dict.
    Handles both formats:
      Format A: {title, sub, audio}    — most chapters
      Format B: {id, title, summary}   — newer AP_Current_Affairs chapters
    """
    heading = sec.get("title", "").strip()

    # Body English
    sub     = sec.get("sub", "").strip()
    summary = sec.get("summary", "").strip()
    body_src = summary if summary else sub
    body_en = format_keywords_as_html(body_src) if body_src else ""

    # Body Telugu (audio field — lecture text)
    audio   = sec.get("audio", "").strip()
    body_te = format_audio_as_html(audio) if audio else ""

    return heading, body_en, body_te


# ── Main ──────────────────────────────────────────────────────────

def main():
    if not LEGACY_DB.exists():
        print(f"ERROR: Legacy DB not found at {LEGACY_DB}")
        sys.exit(1)
    if not DATA_DB.exists():
        print(f"ERROR: content.db not found at {DATA_DB}. Run load_content.py first.")
        sys.exit(1)

    src = sqlite3.connect(LEGACY_DB)
    src.row_factory = sqlite3.Row
    dst = sqlite3.connect(DATA_DB)
    dst.row_factory = sqlite3.Row

    study_notes = src.execute(
        "SELECT * FROM study_notes ORDER BY topic, chapter_num, id"
    ).fetchall()
    print(f"Loaded {len(study_notes)} study_notes rows from legacy DB")

    # Build subject slug → subject_id map
    slug_to_id = {
        r["slug"]: r["id"]
        for r in dst.execute("SELECT id, slug FROM subjects").fetchall()
    }

    TOPIC_TO_SLUG = {
        "Indian_History":    "indian_history",
        "Indian_Polity":     "indian_constitution",
        "AP_Geography":      "ap_geography",
        "AP_Current_Affairs":"current_affairs",
    }

    total_deleted = 0
    total_inserted = 0
    chapters_fixed = 0

    for r in study_notes:
        topic = r["topic"]
        slug  = TOPIC_TO_SLUG.get(topic)
        if not slug:
            continue
        subject_id = slug_to_id.get(slug)
        if not subject_id:
            continue

        # Find the chapter in content.db
        ch = dst.execute(
            "SELECT id FROM chapters WHERE subject_id=? AND chapter_num=?",
            (subject_id, r["chapter_num"])
        ).fetchone()
        if not ch:
            continue
        chapter_id = ch["id"]

        sections = parse_sections_json(r["sections_json"])
        if not sections:
            continue

        # Delete existing notes for this chapter
        deleted = dst.execute(
            "DELETE FROM notes WHERE chapter_id=?", (chapter_id,)
        ).rowcount
        total_deleted += deleted

        # Re-insert with proper content
        inserted = 0
        for i, sec in enumerate(sections, 1):
            heading, body_en, body_te = get_section_fields(sec)
            if not heading and not body_en and not body_te:
                continue
            dst.execute(
                "INSERT OR REPLACE INTO notes "
                "(chapter_id, section_num, heading_en, heading_te, body_en, body_te) "
                "VALUES (?,?,?,?,?,?)",
                (chapter_id, i, heading, "", body_en, body_te)
            )
            inserted += 1
        total_inserted += inserted
        chapters_fixed += 1

    dst.commit()
    src.close()
    dst.close()

    print(f"\n✅ Done!")
    print(f"  Chapters processed : {chapters_fixed}")
    print(f"  Old notes deleted  : {total_deleted}")
    print(f"  New notes inserted : {total_inserted}")

    # Verify
    dst2 = sqlite3.connect(DATA_DB)
    total_notes = dst2.execute("SELECT COUNT(*) FROM notes").fetchone()[0]
    bad_notes   = dst2.execute(
        "SELECT COUNT(*) FROM notes WHERE length(heading_en) <= 1 AND (body_en='' OR body_en IS NULL)"
    ).fetchone()[0]
    dst2.close()
    print(f"  Total notes now    : {total_notes}")
    print(f"  Still-bad notes    : {bad_notes}")


if __name__ == "__main__":
    main()
