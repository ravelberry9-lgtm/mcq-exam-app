"""Concept cards for Unit 6 (audited against Laxmikanth/GBK; see content/polity/g2/concept_cards).

Cards are matched to a question lexically (article numbers, shared rare words), so an
admin-added MCQ is linked the same way as the audited ones.
"""
import json,math,re
from functools import lru_cache
from pathlib import Path

DIR=Path(__file__).resolve().parents[2]/'content'/'polity'/'g2'/'concept_cards'
_ART=re.compile(r'(?:article|articles|art\.?|ప్రకరణ|ప్రకరణలు)\s*(\d{1,3}[A-Z]{0,2})',re.I)
_WORD=re.compile(r'[A-Za-z]{4,}|\d{2,4}|[ఀ-౿]{3,}')
_STOP=set('this that with from which what whose their there these those under shall about also into than then have been were will would could should only other such when where while after before between within without being both each more most some many article articles india indian constitution state states union government'.split())

def chapter_key(qchapter):
    p=str(qchapter or '').split('.')
    return '.'.join(p[:2])

def _tokens(text):
    out=set()
    for w in _WORD.findall(text or ''):
        w=w.lower()
        if w in _STOP: continue
        out.add(w[:6] if w.isascii() and w.isalpha() and len(w)>6 else w)
    return out

def _arts(text):
    return {m.group(1).upper() for m in _ART.finditer(text or '')}

@lru_cache(maxsize=1)
def _load():
    cards={}
    for f in sorted(DIR.glob('cards_*.json')):
        for c in json.loads(f.read_text(encoding='utf-8')):
            c['_text']=' '.join([c.get('title_en',''),c.get('title_te','')]+c.get('keywords',[])+[i.get(k,'') for i in c['items'] for k in ('en','te')])
            c['_tok']=_tokens(c['_text']);c['_art']=_arts(c['_text'])
            cards.setdefault(c['chapter'],[]).append(c)
    for ch in cards: cards[ch].sort(key=lambda c:c['order'])
    idf={}
    for ch,lst in cards.items():
        df={}
        for c in lst:
            for t in c['_tok']: df[t]=df.get(t,0)+1
        idf[ch]={t:math.log(1+len(lst)/n) for t,n in df.items()}
    return cards,idf

def chapter_cards(ch):
    return _load()[0].get(ch,[])

def all_chapters():
    return sorted(_load()[0])

def cards_for_question(q,limit=3):
    ch=chapter_key(q.get('_chapter'))
    cards,idf=_load();lst=cards.get(ch,[])
    if not lst: return []
    text=' '.join([q.get('question_en',''),q.get('question_te','')]+list(q.get('options_en') or [])+list(q.get('options_te') or [])+[q.get('_en',''),q.get('_te','')])
    qt=_tokens(text);qa=_arts(text);w=idf[ch]
    scored=[]
    for c in lst:
        s=sum(w[t] for t in qt&c['_tok'])+4.0*len(qa&c['_art'])
        title=_tokens(c.get('title_en','')+' '+c.get('title_te',''))
        s+=1.5*sum(w.get(t,0) for t in qt&title)
        scored.append((s,c))
    scored.sort(key=lambda x:-x[0])
    if not scored or scored[0][0]<4.0: return []
    top=scored[0][0]
    return [c for s,c in scored[:limit] if s>=max(4.0,0.45*top)]
