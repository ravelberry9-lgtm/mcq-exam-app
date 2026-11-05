"""Loader for Group 2 Geography (lessons 1-34, content/geography/g2)."""
import json
from functools import lru_cache
from pathlib import Path
BASE=Path(__file__).resolve().parents[2]/"content"/"geography"/"g2"
@lru_cache(maxsize=1)
def index():
    return json.loads((BASE/"manifest.json").read_text(encoding="utf-8"))
def chapter(n):
    return next((c for c in index()["chapters"] if c["display_chapter"]==int(n)),None)
@lru_cache(maxsize=40)
def questions(n):
    return json.loads((BASE/str(int(n))/"Questions.json").read_text(encoding="utf-8"))["questions"]
def question(n,qid):
    return next((q for q in questions(n) if q["id"]==qid),None)
def notes_path(n):
    return BASE/str(int(n))/"Notes.html"
