import json
from functools import lru_cache
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "content" / "geography" / "world_chapters"

@lru_cache(maxsize=1)
def index():
    data = json.loads((BASE / "manifest.json").read_text(encoding="utf-8-sig"))
    if data.get("display_range") != "01-29":
        raise ValueError("World Geography canonical index is not release-ready")
    return data

@lru_cache(maxsize=32)
def chapter(number):
    number = int(number)
    if number not in range(1, 30):
        return None
    data = json.loads((BASE / str(number) / "manifest.json").read_text(encoding="utf-8-sig"))
    if data.get("display_chapter") != number or data.get("railway_deployed") is not False:
        raise ValueError("Invalid World Geography chapter manifest")
    return data

@lru_cache(maxsize=16)
def questions(number):
    data = chapter(number)
    rel = data.get("questions_file") if data else None
    if not rel:
        return []
    payload = json.loads((BASE / str(number) / Path(rel).name).read_text(encoding="utf-8-sig"))
    rows = payload.get("questions", payload if isinstance(payload, list) else [])
    if len(rows) != data["question_count"]:
        raise ValueError("World Geography question count mismatch")
    return rows

def question(number, qid):
    return next((q for q in questions(number) if q.get("id") == qid), None)

def notes_path(number):
    data = chapter(number)
    rel = data.get("notes_file") if data else None
    return BASE / str(number) / Path(rel).name if rel else None
