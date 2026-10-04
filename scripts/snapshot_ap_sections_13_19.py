"""Snapshot the section structure of the local AP History chapter files 13-19 (not tracked in git) for the mapping draft.

    python scripts/snapshot_ap_sections_13_19.py [--src PATH_TO_Chapters_FOLDER]

Reads the HTML files read-only and writes scripts/ap_source_sections_13_19.json: for every section its number, headings, text length and
a sha256 of its text, plus the sha256 of each source file, so the mapping stays traceable to the exact files it was drafted from.
Source files are never modified.
"""
import argparse
import hashlib
import html
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
from app.services.ap_history_parse import parse_chapter_file  # noqa: E402

FILES = {13: "ch13_qutb_shahis.html", 14: "ch14_asaf_jahis.html", 15: "ch15_british_coastal_andhra.html",
         16: "ch16_freedom_movement.html", 17: "ch17_ap_formation.html", 18: "ch18_modern_ap.html", 19: "ch19_REBUILT.html"}


def _text(h):
    h = re.sub(r"<(script|style)\b.*?</\1>", "", h or "", flags=re.S | re.I)
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", h))).strip()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--src", default=str(ROOT / "static" / "notes" / "AP_History" / "Chapters"))
    args = ap.parse_args()
    out = {}
    for num, name in FILES.items():
        path = Path(args.src) / name
        soup, sections = parse_chapter_file(str(path))
        h1 = soup.find("h1")
        out[str(num)] = {
            "file": name, "file_sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
            "title": re.sub(r"\s+", " ", h1.get_text(" ", strip=True)) if h1 else "",
            "sections": [{"section_num": s["section_num"], "heading_en": s["heading_en"], "heading_te": s["heading_te"],
                          "text_chars": len(_text(s["body_te"])), "text_sha256": hashlib.sha256(_text(s["body_te"]).encode()).hexdigest()}
                         for s in sections],
        }
    (ROOT / "scripts" / "ap_source_sections_13_19.json").write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print({k: len(v["sections"]) for k, v in out.items()})


if __name__ == "__main__":
    main()
