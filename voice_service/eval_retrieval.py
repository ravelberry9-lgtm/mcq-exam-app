"""Does notes search route a real exam question to the right chapter?  python eval_retrieval.py <sqlite path>"""
import random, sys
from sqlalchemy import create_engine, text
from content import NotesIndex, make_chunks, load_note_rows

path = sys.argv[1]
eng = create_engine(f"sqlite:///{path}")
rows = load_note_rows(eng)
print("note sections:", len(rows))
with eng.connect() as c:
    qs = [dict(r._mapping) for r in c.execute(text("""
        SELECT q.id, q.chapter_id, q.question_te, q.options_te, q.correct_answer
        FROM questions q JOIN subjects s ON s.id=q.subject_id
        WHERE s.slug='ap_history' AND q.chapter_id IS NOT NULL AND q.question_te IS NOT NULL AND q.question_te<>''"""))]
have = {r["chapter_id"] for r in rows}
qs = [q for q in qs if q["chapter_id"] in have]
random.seed(7); random.shuffle(qs); qs = qs[:400]
print("questions tested:", len(qs), "| chapters with notes:", len(have))
for n in (3, 4):
    idx = NotesIndex(make_chunks(rows), ngram=n)
    h1 = h3 = 0
    for q in qs:
        top = idx.search(q["question_te"], k=3, subject="ap_history")
        ch = [c.chapter_id for c, _ in top]
        h1 += bool(ch and ch[0] == q["chapter_id"]); h3 += q["chapter_id"] in ch
    print(f"n-gram={n}: chunks={len(idx.chunks)}  chapter hit@1={h1/len(qs):.0%}  hit@3={h3/len(qs):.0%}")
