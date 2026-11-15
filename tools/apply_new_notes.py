"""Install rewritten notes for lesson N: content/geography/g2_review/new_notes/LNN_Notes.html (+ LNN_questions_changes.json)."""
import json,shutil,sys,os
from pathlib import Path
G=Path(__file__).resolve().parents[1]/"content"/"geography"
for n in map(int,sys.argv[1:]):
    NN=f"{n:02d}"; src=G/"g2_review"/"new_notes"/f"L{NN}_Notes.html"
    d={1:"ch01",2:"ch02",3:"ch03"}.get(n,f"lesson{NN}")
    dst=G/"_claude_rebuild"/d/(f"lesson_{NN}_trimmed.html" if n<=3 else f"lesson_{NN}_rebuilt.html")
    bak=dst.with_name(dst.stem+".v1_2026-11-15.html")
    if not bak.exists(): shutil.copy(dst,bak)
    shutil.copy(src,dst)
    fx=G/"g2_fixes"/f"fixes_L{NN}.json"
    f=json.load(open(fx,encoding="utf-8")) if fx.exists() else {"lesson":n,"notes":[],"questions":{},"retire":[]}
    f["notes"]=[]
    qc=G/"g2_review"/"new_notes"/f"L{NN}_questions_changes.json"
    if qc.exists():
        c=json.load(open(qc,encoding="utf-8"))
        f["retire"]=sorted(set(f.get("retire",[]))|set(c.get("retire",[])))
        for i,v in c.get("reword",{}).items(): f.setdefault("questions",{}).setdefault(i,{}).update(v)
        for i,s in c.get("relink",{}).items(): f.setdefault("questions",{}).setdefault(i,{})["section"]=s
    json.dump(f,open(fx,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
    print("installed",NN)
