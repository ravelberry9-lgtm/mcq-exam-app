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
def explanations(n):
    """Explanations are stored separately (Explanations.json, keyed by explanation_id), as in Polity."""
    p=BASE/str(int(n))/"Explanations.json"
    return json.loads(p.read_text(encoding="utf-8")).get("questions",{}) if p.is_file() else {}
@lru_cache(maxsize=40)
def questions(n):
    rows=json.loads((BASE/str(int(n))/"Questions.json").read_text(encoding="utf-8"))["questions"]
    ex=explanations(n);out=[]
    for q in rows:
        e=ex.get(q.get("explanation_id",q["id"]))
        if e:
            q={**q,"explanation_te":e.get("te",""),"explanation_en":e.get("en",""),
               "option_explanations_te":e.get("options_te") or [],"option_explanations_en":e.get("options_en") or []}
        out.append(q)
    return out
def question(n,qid):
    return next((q for q in questions(n) if q["id"]==qid),None)
def notes_path(n):
    return BASE/str(int(n))/"Notes.html"
@lru_cache(maxsize=40)
def images(n):
    """Infographics for a lesson (Images.json): image metadata plus question -> image stems."""
    p=BASE/str(int(n))/"Images.json"
    return json.loads(p.read_text(encoding="utf-8")) if p.is_file() else {"images":{},"questions":{}}
def question_images(n,qid):
    d=images(n);out=[]
    for stem in d.get("questions",{}).get(qid,[]):
        m=d.get("images",{}).get(stem)
        if m:out.append(m)
    return out
