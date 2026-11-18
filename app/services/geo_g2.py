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

# ---- Cross-lesson index (hub, practice setup, library, revise, tests) ----
import html as _html
import re as _re
PYQ_BASE=BASE.parent/"g2_pyq"
GROUPS=[("world","ప్రపంచ భూగోళశాస్త్రం","World Geography","Lessons 1–11",[("","","",1,11)]),
        ("india","భారతదేశం–ఆంధ్రప్రదేశ్ భూగోళశాస్త్రం","India and Andhra Pradesh Geography","Lessons 12–34",
         [("physical","భౌతిక, విపత్తులు","Physical and disasters",12,20),("economic","ఆర్థిక","Economic",21,30),("human","మానవ","Human",31,34)])]
def is_pyq(q):return "PYQ" in q["id"] or "pyq" in (q.get("kind") or "")
@lru_cache(maxsize=1)
def pyq_meta():
    out={}
    for f in sorted(PYQ_BASE.glob("L*.json")):
        for r in json.loads(f.read_text(encoding="utf-8")).get("records",[]):
            out[r["pid"]]=r.get("source") or {}
    return out
def exam_group(exam):
    from ..routes.polity_unit6 import exam_group as _eg   # same grouping as Polity
    return _eg(exam)
@lru_cache(maxsize=1)
def records():
    """Every lesson question in lesson order, tagged for filtering."""
    meta=pyq_meta();out=[]
    for c in index()["chapters"]:
        n=c["display_chapter"]
        for q in questions(n):
            p=is_pyq(q);src=meta.get(q["id"]) if p else None
            out.append({**q,"_lesson":n,"_kind":"pyq" if p else "bank","_src":src,
                        "_exam":exam_group((src or {}).get("exam") or q.get("pyq_source") or "") if p else "",
                        "_year":(src or {}).get("year")})
    return out
@lru_cache(maxsize=1)
def by_id():return {q["id"]:q for q in records()}
def lesson_records(n):return [q for q in records() if q["_lesson"]==int(n)]
def pyq_label(q):
    """'exam · year' and 'paper · Q n' exactly as recorded in the PYQ metadata; nothing inferred."""
    if q.get("_kind")!="pyq":return None
    s=q.get("_src") or {}
    if not s:return {"title":q.get("pyq_source") or "PYQ","detail":""}
    return {"title":" · ".join(str(x) for x in (s.get("exam"),s.get("year")) if x),
            "detail":" · ".join(x for x in (s.get("paper") or "",("Q"+str(s["qno"])) if s.get("qno") else "") if x)}
@lru_cache(maxsize=40)
def sections(n):
    """[(id, heading)] for every heading with an id in the lesson notes, in page order."""
    p=notes_path(n)
    if not p.is_file():return []
    out=[]
    for m in _re.finditer(r'<h([1-4])\b[^>]*\bid="([^"]+)"[^>]*>(.*?)</h\1>',p.read_text(encoding="utf-8-sig"),_re.S):
        out.append((m.group(2),_re.sub(r"\s+"," ",_html.unescape(_re.sub(r"<[^>]+>","",m.group(3)))).strip()))
    return out
def section_title(n,sid):return dict(sections(n)).get(sid)
def lesson_sections(n):
    """Sections that have questions, in notes order (unknown ids last), with counts."""
    from collections import Counter
    cnt=Counter(q.get("section") or "" for q in lesson_records(n));titles=dict(sections(n));order=[s for s,_ in sections(n)]
    keys=sorted(cnt,key=lambda s:(order.index(s) if s in order else 10**6,s))
    return [(s,titles.get(s) or s or "Other",cnt[s]) for s in keys]
def lesson_images(n):
    d=images(n);return [{"stem":k,**v} for k,v in d.get("images",{}).items()]
