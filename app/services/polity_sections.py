"""Links from existing authored locators only; never infer a page from question IDs."""
from functools import lru_cache
from bs4 import BeautifulSoup
from ..routes.polity_maps import CONTENT, read

def directory(chapter):
    return CONTENT/'.'.join(chapter.split('.')[:2])/chapter

@lru_cache(maxsize=20)
def chapter_locators(chapter):
    root=directory(chapter)
    ids={tag['id'] for tag in BeautifulSoup((root/'Notes.html').read_text(encoding='utf-8-sig'),'html.parser').select('[id]')}
    p=root/'Fact-register.json'
    facts=read(p).get('facts',[]) if p.is_file() else []
    return ids,{f['id']:f for f in facts if 'id' in f}

def pages(record):
    values=[record.get('source_page'),record.get('gbk_page')]
    sources=record.get('sources') or {}
    source=sources.get('gbk',{}) if isinstance(sources,dict) else {}
    if isinstance(source,dict):values.extend(source.get(k) for k in ('page','printed_page','pages'))
    out=[]
    for value in values:
        for v in value if isinstance(value,list) else [value]:
            if isinstance(v,int) and not isinstance(v,bool):out.append(v)
            elif isinstance(v,str) and v.isdigit():out.append(int(v))
    return out

@lru_cache(maxsize=1)
def heading_map():
    p=CONTENT/'_shared/Note-Section-Map.json'
    return read(p).get('items',{}) if p.is_file() else {}

def section_links(question):
    ids,facts=chapter_locators(question['_chapter'])
    result=[]
    hm=heading_map().get(question['id'])
    if hm and hm.get('chapter')==question['_chapter']:result.append(dict(anchor=f"u6s-{hm['heading_idx']}",basis='heading',title=hm.get('title_en','')))
    section=question.get('section')
    if section in ids:result.append(dict(anchor=section,basis='section'))
    for page in pages(question):
        anchor=f'gbk-page-{page}'
        if anchor in ids:result.append(dict(anchor=anchor,basis='source_page'))
    if not result:
        for fid in question.get('fact_ids',[]):
            for page in pages(facts.get(fid,{})):
                anchor=f'gbk-page-{page}'
                if anchor in ids:result.append(dict(anchor=anchor,basis='related_fact'))
    return list({r['anchor']:r for r in result}.values())[:2]
