"""Separate, pinned Telugu and English study presentations for solar MCQs.

The historical corpus, answer keys and scoring holds remain owned by geography_pyqs.
This catalogue supplies wording only and never decides scoring eligibility.
"""
from functools import lru_cache
from pathlib import Path
import hashlib,json,re
from bs4 import BeautifulSoup
from flask import current_app

_ALLOWED_TE={'A','B','C','D','I','II','III','IV','AU','km','kg','m','s','g','cm','K','N','CO','UTC','LVM','M','PSLV','UB','S','T','a','h','P'}

def validate_variant(t,lang):
    if not all(isinstance(t.get(k),str) and t[k].strip() for k in ('question','explanation','heading','chapter_excerpt')):
        raise ValueError('Missing bilingual text')
    for key in ('options','option_explanations'):
        if not isinstance(t.get(key),list) or len(t[key])!=4 or not all(isinstance(x,str) and x.strip() for x in t[key]):
            raise ValueError('Incomplete bilingual options or explanations')
    if len(set(t['options']))!=4:raise ValueError('Duplicate translated options')
    texts=[t[k] for k in ('question','explanation','heading','chapter_excerpt')]+t['options']+t['option_explanations']
    if 'matching_lists' in t:
        lists=t['matching_lists']
        if set(lists)!= {'left','right'} or any(len(lists[k])!=4 or len(set(lists[k]))!=4 for k in lists):
            raise ValueError('Invalid translated matching lists')
        texts+=lists['left']+lists['right']
    joined=' '.join(texts)
    if lang=='en' and re.search('[\u0c00-\u0c7f]',joined):raise ValueError('Telugu leaked into English version')
    if lang=='te' and (set(re.findall('[A-Za-z]+',joined))-_ALLOWED_TE):raise ValueError('English prose leaked into Telugu version')

@lru_cache(maxsize=4)
def _load(path,mtime,pin,bookpath,booktime,bankpath,banktime,pyqpath,pyqtime):
    raw=Path(path).read_bytes()
    if hashlib.sha256(raw).hexdigest()!=pin:raise ValueError('Bilingual catalogue fingerprint mismatch')
    d=json.loads(raw);book=Path(bookpath).read_bytes()
    if d.get('format')!='solar-bilingual-mcqs-v1' or hashlib.sha256(book).hexdigest()!=d.get('chapter_sha256'):
        raise ValueError('Bilingual chapter fingerprint mismatch')
    originals={q['id']:q for q in json.loads(Path(bankpath).read_text(encoding='utf-8'))['questions']}
    historic={q['source']['id']:q['source'] for q in json.loads(Path(pyqpath).read_text(encoding='utf-8'))['records']}
    if set(d['original'])!=set(originals) or len(d['historical'])!=7:raise ValueError('Incomplete solar bilingual coverage')
    soup=BeautifulSoup(book,'html.parser')
    for group in ('original','historical'):
        for qid,entry in d[group].items():
            source=originals[qid] if group=='original' else historic[qid]
            key=source['answer'] if group=='original' else source['answer_index']
            if entry['answer']!=key or type(entry['answer']) is not int:raise ValueError('Translated answer order differs')
            if group=='original' and entry['section']!=source['section']:raise ValueError('Translated chapter destination differs')
            if not soup.find(id=entry['section']) or set(entry['variants'])!={'te','en'}:raise ValueError('Missing bilingual section or language')
            for lang,t in entry['variants'].items():
                validate_variant(t,lang)
                if source.get('matching_lists') and t.get('options')!=source['options']:raise ValueError('Matching permutations changed')
    return d

def payload():
    root=Path(current_app.root_path).parent;folder=root/'content/geography'
    p=folder/'solar_bilingual.json';book=root/'static/textbooks/geography/lessons/03_Earth_in_the_Solar_System_Bilingual_Foundation.html'
    bank=folder/'original_practice/03.json';pyqs=folder/'pyqs.json'
    pin=json.loads((folder/'solar_bilingual_manifest.json').read_text(encoding='utf-8'))['sha256']
    return _load(str(p),p.stat().st_mtime_ns,pin,str(book),book.stat().st_mtime_ns,str(bank),bank.stat().st_mtime_ns,str(pyqs),pyqs.stat().st_mtime_ns)

def question(qid,language='te',historical=False):
    if language not in ('te','en'):raise ValueError('Unsupported question language')
    q=payload()['historical' if historical else 'original'].get(qid)
    return q['variants'][language] if q else None
