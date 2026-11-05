"""Read-only loader for the consolidated India–AP Geography chapters."""
import json
from functools import lru_cache
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "content" / "geography" / "india_ap_chapters"
ACTIVE_CHAPTERS = tuple(range(1, 21))


@lru_cache(maxsize=1)
def index():
    """Return the complete reviewed India–AP consolidated sequence."""
    root = json.loads((BASE / "manifest.json").read_text(encoding="utf-8-sig"))
    if root.get("format") != "india-ap-consolidated-v1":
        raise ValueError("Invalid India–AP Geography index manifest")
    chapters = []
    for number in ACTIVE_CHAPTERS:
        item = chapter(number)
        if item is None:
            raise ValueError(f"Missing India–AP Geography chapter {number}")
        chapters.append(item)
    return {**root, "chapters": chapters}


@lru_cache(maxsize=32)
def chapter(number):
    number = int(number)
    path = BASE / str(number) / "manifest.json"
    if number < 1 or not path.is_file():
        return None
    data = json.loads(path.read_text(encoding="utf-8-sig"))
    if data.get("display_chapter") != number or data.get("railway_deployed") is not False:
        raise ValueError("Invalid India–AP Geography chapter manifest")
    return data


@lru_cache(maxsize=32)
def questions(number):
    data = chapter(number)
    rel = data.get("questions_file") if data else None
    if not rel:
        return []
    payload = json.loads((BASE / str(int(number)) / Path(rel).name).read_text(encoding="utf-8-sig"))
    rows = payload.get("questions", payload if isinstance(payload, list) else [])
    if len(rows) != data["question_count"]:
        raise ValueError("India–AP Geography question count mismatch")
    return rows


def question(number, qid):
    return next((q for q in questions(number) if q.get("id") == qid), None)


def notes_path(number):
    data = chapter(number)
    rel = data.get("notes_file") if data else None
    return BASE / str(int(number)) / Path(rel).name if rel else None
