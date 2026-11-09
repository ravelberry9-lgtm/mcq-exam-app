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

FLOOR=26.0

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

_ARTLIST=re.compile(r'(?:articles?|art\.?|ప్రకరణ(?:లు)?)\s*((?:\d{1,3}[A-Z]{0,2}(?:\([^)]{1,6}\))*\s*(?:,|&|and|to|-|\u2013|/|మరియు)?\s*)+)',re.I)
_NUM=re.compile(r'(\d{1,3})([A-Z]{0,2})')
_ORD={'first':1,'second':2,'third':3,'fourth':4,'fifth':5,'sixth':6,'seventh':7,'eighth':8,'ninth':9,'tenth':10}
_AMD=re.compile(r'\b(\d{1,3})(?:st|nd|rd|th)?\s+(?:constitution\s+)?\(?amendment|\b(first|second|third|fourth|fifth|sixth|seventh|eighth|ninth|tenth)\s+amendment',re.I)

def _arts(text):
    out=set()
    for m in _ARTLIST.finditer(text or ''):
        body=re.sub(r'\([^)]*\)','',m.group(1))
        nums=[(int(a),b) for a,b in _NUM.findall(body)]
        for k,(n,suf) in enumerate(nums):
            out.add(f'{n}{suf.upper()}')
        for k in range(len(nums)-1):
            a,b=nums[k][0],nums[k+1][0]
            if re.search(r'\b'+str(a)+r'\w*\s*(?:to|-|\u2013)\s*'+str(b)+r'\b',body) and 0<b-a<=15:
                out.update(str(x) for x in range(a,b+1))
    return out

def _amds(text):
    out=set()
    for m in _AMD.finditer(text or ''):
        v=m.group(1) or str(_ORD[m.group(2).lower()]);out.add(int(v))
    return out

@lru_cache(maxsize=1)
def _load():
    cards={}
    for f in sorted(DIR.glob('cards_*.json')):
        for c in json.loads(f.read_text(encoding='utf-8')):
            c['_text']=' '.join([c.get('title_en',''),c.get('title_te','')]+c.get('keywords',[])+[i.get(k,'') for i in c['items'] for k in ('en','te')])
            c['_tok']=_tokens(c['_text']);c['_art']=_arts(c['_text']);c['_amd']=_amds(c['_text']);c['_kw']=[k.lower() for k in c.get('keywords',[]) if len(k)>=6]
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
    ans=q.get('_answer');opts_en=list(q.get('options_en') or []);opts_te=list(q.get('options_te') or [])
    right=' '.join(o[ans-1] for o in (opts_en,opts_te) if ans in (1,2,3,4) and len(o)>=ans)
    wrong=' '.join(o[i] for o in (opts_en,opts_te) for i in range(len(o)) if ans!=i+1)
    stem=' '.join([q.get('question_en',''),q.get('question_te','')])
    expl=' '.join([q.get('_en',''),q.get('_te','')])
    parts=[(_tokens(stem),1.0),(_tokens(right),1.0),(_tokens(expl),0.7),(_tokens(wrong),0.2)]
    key_text=(stem+' '+right).lower()
    qa=_arts(stem+' '+right)|(_arts(expl)&_arts(stem+' '+right+' '+wrong) if False else set())
    qa_all=qa|_arts(expl)
    qd=_amds(stem+' '+right+' '+expl)
    w=idf[ch];scored=[]
    for c in lst:
        s_=0.0;hit=set()
        for toks,wt in parts:
            for t in toks&c['_tok']:
                if t not in hit: hit.add(t)
                s_+=wt*w[t]
        title=_tokens(c.get('title_en','')+' '+c.get('title_te',''))
        s_+=1.5*sum(w.get(t,0) for t in _tokens(stem+' '+right)&title)
        a_hit=qa&c['_art'] or (qa_all&c['_art'] if not qa else set())
        s_+=4.0*len(a_hit)
        if qd&c['_amd']: s_+=4.0
        s_+=3.0*sum(1 for k in c['_kw'] if k in key_text)
        if qa and c['_art'] and not (qa&c['_art']): s_*=0.6
        ok=bool(a_hit) or bool(qd&c['_amd']) or len(hit)>=2
        scored.append((s_ if ok else 0.0,c))
    scored.sort(key=lambda x:-x[0])
    if not scored or scored[0][0]<FLOOR: return []
    top=scored[0][0]
    return [c for s_,c in scored[:limit] if s_>=max(FLOOR,0.65*top)]
