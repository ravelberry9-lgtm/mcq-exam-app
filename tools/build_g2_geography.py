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
    if "variants" in q:
        ml={"te":(q["variants"].get("te",{}) or {}).get("matching_lists"),"en":(q["variants"].get("en",{}) or {}).get("matching_lists")}
    else:
        ml={"te":q.get("matching_lists_te") or q.get("matching_lists"),"en":q.get("matching_lists_en") or q.get("matching_lists")}
    ml["te"]=ml["te"] or ml["en"]; ml["en"]=ml["en"] or ml["te"]
    if ml["te"]: r["matching_lists_te"],r["matching_lists_en"]=ml["te"],ml["en"]
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

import re as _re
_L2=_re.compile(r"(?:List\s*II|జాబితా\s*[-–]?\s*II|జాబితా\s*-?\s*2)\s*:")
_L1=_re.compile(r"(?:List\s*I|జాబితా\s*[-–]?\s*I|జాబితా\s*-?\s*1)\s*:")
def _items(t,pat):
    return [x.strip().rstrip(";.,").strip() for x in _re.split(pat," "+t)[1:]]
def sync_lists(q):
    """Make the List I/II grid follow the numbering printed in the stem, so answer codes match what is shown."""
    for lg in ("en","te"):
        ml=q.get("matching_lists_"+lg); st=q.get("question_"+lg) or ""
        if not ml: continue
        ml=q["matching_lists_"+lg]={k:list(v) if isinstance(v,list) else v for k,v in ml.items()}
        m2=_L2.search(st); m1=_L1.search(st)
        if not m2:
            # Stem lists "A. … D. …" then "1. … 4. …" without a "List II:" label.
            ds=[m.end() for m in _re.finditer(r"(?:^|\s)D\.\s",st)]
            one=_re.compile(r"(?:^|\s)1\.\s").search(st,ds[-1]) if ds else None
            if not one: continue
            right=_items(st[one.start():],r"(?:^|\s)\d\.\s")
            if len(right)==len(ml.get("right",[])) and all(right): ml["right"]=right
            a0=_re.search(r"(?:^|\s)A\.\s",st)
            if a0 and a0.start()<one.start():
                left=_items(st[a0.start():one.start()],r"(?:^|\s)[A-D]\.\s")
                if len(left)==len(ml.get("left",[])) and all(left): ml["left"]=left
            continue
        right=_items(st[m2.end():],r"(?:^|\s)\d\.\s")
        if len(right)==len(ml.get("right",[])) and all(right): ml["right"]=right
        if m1 and m1.end()<=m2.start():
            left=_items(st[m1.end():m2.start()],r"(?:^|\s)[A-D]\.\s")
            if len(left)==len(ml.get("left",[])) and all(left): ml["left"]=left

def main():
    lm=J(SRC/"lesson_map.json"); titles={}
    for g in lm["groups"]:
        for l in g["lessons"]: titles[l["lesson"]]=(g["id"],l["title"])
    OUT.mkdir(parents=True,exist_ok=True); chapters=[]; tot=sh=0
    for n in range(1,35):
        NN=f"{n:02d}"; ddir={1:"ch01",2:"ch02",3:"ch03"}.get(n,f"lesson{NN}")
        html=SRC/ddir/(f"lesson_{NN}_trimmed.html" if n<=3 else f"lesson_{NN}_rebuilt.html")
        page=html.read_text(encoding="utf-8-sig")
        page=re.sub(r'href="lesson_(\d\d)_(?:rebuilt|trimmed)\.html(#[^"]*)?"',lambda m:f'href="/learn/geography/g2/{int(m[1])}/notes{m[2] or ""}"',page)
        qs=[]
        for q in shown(n):
            q,s=shuffle(q); sh+=s; qs.append(q)
        fx=ROOT/"g2_fixes"/f"fixes_L{NN}.json"
        if fx.exists():
            f=J(fx)
            for x in f.get("notes",[]):
                if page.count(x["old"])!=1: raise SystemExit(f"L{NN}: notes old text not unique: {x['old'][:50]!r}")
                page=page.replace(x["old"],x["new"])
            byid={q["id"]:q for q in qs}
            for qid,d in f.get("questions",{}).items():
                q=byid[qid]
                for k,v in d.items():
                    assert k!="answer"
                    if k.startswith("options_"):
                        a=q["answer"]-1
                        assert len(v)==len(q[k]) and v[a]==q[k][a],f"{qid} {k} key moved"
                    q[k]=v
            dead=set(f.get("retire",[]))
            qs=[q for q in qs if q["id"] not in dead]
        # Manual APPSC-standard MCQ review (2026-11-16): fixes only, never retire.
        # Positions refer to the displayed (shuffled) order; the correct option stays at its index.
        rv=ROOT/"g2_mcq_review"/f"review_L{NN}.json"
        if rv.exists():
            byid={q["id"]:q for q in qs}
            for qid,d in J(rv).get("fix",{}).items():
                q=byid[qid]
                for k,v in d.items():
                    if k in ("reason",): continue
                    if k=="explanation_stale": q["explanation_stale"]=bool(v); continue
                    assert k!="answer",f"{qid}: answer index may not change"
                    if k.startswith("options_"): assert len(v)==len(q[k]),f"{qid} {k} option count changed"
                    q[k]=v
        for q in qs: sync_lists(q)
        d=OUT/str(n); d.mkdir(exist_ok=True)
        (d/"Notes.html").write_text(page,encoding="utf-8")
        # Polity design: explanations live in their own file, keyed by explanation_id.
        EXK=("explanation_te","explanation_en","option_explanations_te","option_explanations_en")
        ex={}
        for q in qs:
            q["explanation_id"]=q["id"]
            ex[q["id"]]={"te":q.pop("explanation_te",None) or "","en":q.pop("explanation_en",None) or "",
                         "options_te":q.pop("option_explanations_te",None) or [],"options_en":q.pop("option_explanations_en",None) or []}
            if q.pop("explanation_stale",False): ex[q["id"]]["stale"]=True
        (d/"Questions.json").write_text(json.dumps({"questions":qs},ensure_ascii=False),encoding="utf-8")
        (d/"Explanations.json").write_text(json.dumps({"chapter":n,"questions":ex},ensure_ascii=False),encoding="utf-8")
        m={"display_chapter":n,"group":titles[n][0],"title":titles[n][1],"question_count":len(qs),"notes_file":"Notes.html","questions_file":"Questions.json","explanations_file":"Explanations.json"}
        (d/"manifest.json").write_text(json.dumps(m,ensure_ascii=False,indent=1),encoding="utf-8")
        chapters.append(m); tot+=len(qs)
    (OUT/"manifest.json").write_text(json.dumps({"format":"g2-geography-v1","built":"2026-11-05","question_count":tot,"chapters":chapters},ensure_ascii=False,indent=1),encoding="utf-8")
    print("lessons",len(chapters),"questions",tot,"shuffled",sh)
main()
