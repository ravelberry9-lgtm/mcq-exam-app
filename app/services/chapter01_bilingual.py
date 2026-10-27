from pathlib import Path
from functools import lru_cache
import hashlib,json
from bs4 import BeautifulSoup
from flask import current_app
from .solar_bilingual import validate_variant

@lru_cache(maxsize=8)
def _load(path,stamp,pin,bookpath,bookstamp,bankpath,bankstamp,asset_stamps):
 raw=Path(path).read_bytes()
 if hashlib.sha256(raw).hexdigest()!=pin:raise ValueError('Chapter bilingual fingerprint mismatch')
 d=json.loads(raw);book=Path(bookpath).read_bytes()
 if d.get('format')!='geography-chapter-bilingual-v1' or hashlib.sha256(book).hexdigest()!=d.get('chapter_sha256'):raise ValueError('Chapter bilingual notes fingerprint mismatch')
 source=json.loads(Path(bankpath).read_bytes())
 if d.get('chapter')!=source['chapter']:raise ValueError('Bilingual chapter identity differs')
 bank={q['id']:q for q in source['questions']};soup=BeautifulSoup(book,'html.parser')
 if set(d['questions'])!=set(bank) or len(bank)!=d['question_count']:raise ValueError('Incomplete bilingual coverage')
 for qid,e in d['questions'].items():
  q=bank[qid]
  if type(e['answer']) is not int or e['answer']!=q['answer'] or e['section']!=q['section']:raise ValueError('Bilingual answer or destination differs')
  if not soup.find(id=e['section']) or set(e['variants'])!={'te','en'}:raise ValueError('Missing bilingual anchor or language')
  if e['held']!=(qid in d['held_question_ids']):raise ValueError('Inconsistent scoring hold')
  for lang,t in e['variants'].items():
   validate_variant(t,lang)
   if q.get('matching_lists') and t['options']!=q['options']:raise ValueError('Matching permutation changed')
  if e.get('visual_id') and e['visual_id'] not in d['visuals']:raise ValueError('Missing question visual')
 for vid,v in d['visuals'].items():
  p=Path(bookpath).parents[3]/v['file'];fig=soup.find(id=vid)
  if hashlib.sha256(p.read_bytes()).hexdigest()!=v['sha256'] or not fig or not soup.find(id=v['section']):raise ValueError('Visual fingerprint or anchor mismatch')
 return d

def payload(chapter_id="01"):
 if chapter_id not in ("01","02"):raise ValueError("Unsupported chapter bilingual catalogue")
 root=Path(current_app.root_path).parent;folder=root/'content/geography';p=folder/f'chapter{chapter_id}_bilingual.json';bank=folder/'original_practice'/f'{chapter_id}.json';entry=json.loads((folder/'original_practice_manifest.json').read_bytes())['chapters'][chapter_id];book=root/'static/textbooks/geography/lessons'/entry['file']
 pin=json.loads((folder/f'chapter{chapter_id}_bilingual_manifest.json').read_bytes())['sha256']
 assets=tuple((x.name,x.stat().st_mtime_ns,x.stat().st_size) for x in sorted((root/f'static/textbooks/geography/visuals/ch{chapter_id}').glob('*.svg')))
 return _load(str(p),p.stat().st_mtime_ns,pin,str(book),book.stat().st_mtime_ns,str(bank),bank.stat().st_mtime_ns,assets)

def is_held(qid,chapter_id='01'):return qid in payload(chapter_id)['held_question_ids']
