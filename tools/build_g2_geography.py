"""Build content/geography/g2 (Group 2 Geography, lessons 1-34) from content/geography/_claude_rebuild.
Questions get options shuffled with a fixed seed (answer remapped; correct text never changes)."""
import json, re, random, shutil, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]/"content"/"geography"
SRC=ROOT/"_claude_rebuild"; OUT=ROOT/"g2"
def J(p): return json.loads(Path(p).read_text(encoding="utf-8-sig"))
def ok(v): return bool(v) and str(v)!="None"
def sec(v): return str(v).split("#")[-1] if ok(v) else None
def flat(q,sect):
    """normalise any of the source formats to the flat bilingual schema"""
    if "variants" in q:
        te,en=q["variants"].get("te",{}),q["variants"].get("en",{})
        r={"id":q["id"],"question_te":te.get("question"),"question_en":en.get("question"),
           "options_te":te.get("options"),"options_en":en.get("options"),
           "option_explanations_te":te.get("option_explanations"),"option_explanations_en":en.get("option_explanations"),
           "explanation_te":te.get("explanation"),"explanation_en":en.get("explanation"),"answer":q["answer"]}
    else:
        r={k:q.get(k) for k in ("id","question_te","question_en","options_te","options_en","option_explanations_te","option_explanations_en","explanation_te","explanation_en","answer")}
        if not r["options_en"] and q.get("options"): r["options_en"]=q["options"]
        if not r["option_explanations_en"] and q.get("option_explanations"): r["option_explanations_en"]=q["option_explanations"]
    for a,b in (("question_te","question_en"),("options_te","options_en"),("option_explanations_te","option_explanations_en"),("explanation_te","explanation_en")):
        if not r[a]: r[a]=r[b]
        if not r[b]: r[b]=r[a]
    r["section"]=sect; r["kind"]=q.get("kind","")
    return r
FIXED=re.compile(r"(\bonly\b|\bboth\b|\bneither\b|\bnone of\b|\ball of\b|\babove\b|\bboth\b|పైవన్నీ|పైవేవీ|మాత్రమే|రెండూ|కావు|^[A-Da-d]\s*[–-]\s*\d|^\d(\s*,\s*\d)*(\s*(and|&)\s*\d)?$)",re.I)
POS=re.compile(r"\b(option|options)\s*[1-4A-D]\b|ఎంపిక\s*[1-4]|\b[1-4]\s*(వ|వది)\s*ఎంపిక",re.I)
def shuffle(r):
    n=len(r["options_en"] or [])
    if n<2 or r["answer"] not in range(1,n+1): return r,False
    texts=" ".join(r["options_en"]+r["options_te"])
    if any(FIXED.search(o) for o in r["options_en"]+r["options_te"]): return r,False
    if POS.search(" ".join(filter(None,[r["explanation_en"],r["explanation_te"]]+(r["option_explanations_en"] or [])+(r["option_explanations_te"] or [])))): return r,False
    if any(len(x or [])!=n for x in (r["options_te"],r["option_explanations_en"],r["option_explanations_te"])): return r,False
    perm=list(range(n)); random.Random("g2-"+r["id"]).shuffle(perm)
    r=dict(r)
    for k in ("options_en","options_te","option_explanations_en","option_explanations_te"): r[k]=[r[k][i] for i in perm]
    r["answer"]=perm.index(r["answer"]-1)+1
    return r,True
def shown(n):
    NN=f"{n:02d}"; out=[]
    if n<=3:
        d=SRC/f"ch{NN}"/"mcq"; links=J(d/"links.json")
        b=J(d/("solar_bilingual.patched.json" if n==3 else f"chapter{NN}_bilingual.patched.json"))
        pool={}
        for k in ("questions","original","historical"):
            if isinstance(b.get(k),dict): pool.update(b[k])
        for qid,l in links.items():
            if ok(l) and qid in pool and not pool[qid].get("held"):
                q=dict(pool[qid]); q["id"]=qid; out.append(flat(q,sec(l)))
        nq=J(d/"new_questions.json"); nq=nq.get("questions",nq)
        for qid,q in nq.items():
            if q.get("held"): continue
            q=dict(q); q["id"]=qid; out.append(flat(q,sec(q.get("link") or q["section"])))
    else:
        d=SRC/f"lesson{NN}"/"mcq"
        files=[d/"04.patched.json"] if n==4 else [d/f"lesson{NN}_questions.json"]
        files+= [d/"new_questions.json"]
        for f in files:
            if f.exists():
                x=J(f); x=x.get("questions",x) if isinstance(x,dict) else x
                for q in x:
                    s=q.get(f"lesson{NN}_section")
                    if ok(s) and not q.get("retire_suggest"): out.append(flat(q,sec(s)))
    if n in (1,2,3,5):
        f=SRC/{1:"ch01",2:"ch02",3:"ch03",5:"lesson05"}[n]/"mcq"/f"lesson{NN}_moved_in.json"
        if f.exists():
            x=J(f); x=x.get("questions",x)
            for q in x:
                s=q.get(f"lesson{NN}_section")
                if ok(s) and not q.get("retire_suggest"): out.append(flat(q,sec(s)))
    seen=set(); res=[]
    for q in out:
        if q["id"] in seen or not q["options_en"] or q["answer"] is None: continue
        seen.add(q["id"]); res.append(q)
    return res
def main():
    lm=J(SRC/"lesson_map.json"); titles={}
    for g in lm["groups"]:
        for l in g["lessons"]: titles[l["lesson"]]=(g["id"],l["title"])
    if OUT.exists(): shutil.rmtree(OUT)
    OUT.mkdir(parents=True); chapters=[]; tot=sh=0
    for n in range(1,35):
        NN=f"{n:02d}"; ddir={1:"ch01",2:"ch02",3:"ch03"}.get(n,f"lesson{NN}")
        html=SRC/ddir/(f"lesson_{NN}_trimmed.html" if n<=3 else f"lesson_{NN}_rebuilt.html")
        page=html.read_text(encoding="utf-8-sig")
        page=re.sub(r'href="lesson_(\d\d)_(?:rebuilt|trimmed)\.html(#[^"]*)?"',lambda m:f'href="/learn/geography/g2/{int(m[1])}/notes{m[2] or ""}"',page)
        qs=[]
        for q in shown(n):
            q,s=shuffle(q); sh+=s; qs.append(q)
        d=OUT/str(n); d.mkdir()
        (d/"Notes.html").write_text(page,encoding="utf-8")
        (d/"Questions.json").write_text(json.dumps({"questions":qs},ensure_ascii=False),encoding="utf-8")
        m={"display_chapter":n,"group":titles[n][0],"title":titles[n][1],"question_count":len(qs),"notes_file":"Notes.html","questions_file":"Questions.json"}
        (d/"manifest.json").write_text(json.dumps(m,ensure_ascii=False,indent=1),encoding="utf-8")
        chapters.append(m); tot+=len(qs)
    (OUT/"manifest.json").write_text(json.dumps({"format":"g2-geography-v1","built":"2026-11-05","question_count":tot,"chapters":chapters},ensure_ascii=False,indent=1),encoding="utf-8")
    print("lessons",len(chapters),"questions",tot,"shuffled",sh)
main()
