"""Complete Unit 6 learner entry point backed by immutable authored records."""
import os,random,uuid
from pathlib import Path
from datetime import datetime,timedelta
from flask import Blueprint,abort,current_app,redirect,render_template,request,url_for,make_response
from ..db import db
from ..polity_models import PolityUnit6State,PolityUnit6Progress,PolityUnit6Exam
from ..services.device import device_id
from .polity_maps import CONTENT,read,records,catalog
from ..services.polity_sections import section_links,directory
from ..services import polity_cards as _cards
from ..services import article_cards as _artcards
from ..services import recall_decks as _recall
import re,re as _re
from functools import lru_cache
_JARGON=_re.compile(r'(fact register|bank key|authenticated pairing|tests separately|untested|source[- ]bank|content team|GBK paragraph|Laxmikanth paragraph)',_re.I)
_IDS=_re.compile(r'\s*[\(\[]?\b(?:POL|APPSC|BK|GBK\d*|PYQ)-[A-Za-z0-9._-]+\b[\)\]]?')
def clean_text(t):
    if not t:return t
    t=_IDS.sub('',t)
    parts=_re.split(r'(?<=[.!?।])\s+',t)
    kept=[x for x in parts if not _JARGON.search(x)]
    return ' '.join(kept) if kept else t

bp=Blueprint('polity_unit6',__name__,url_prefix='/learn/polity/unit6')
def unit6_stats():
    corpus=records()
    mcq=sum(1 for q in corpus.values() if q['_kind']=='bank' and visible(q))
    pyq=sum(1 for q in corpus.values() if q['_kind'] in ('pyq','primary_pyq') and visible(q))
    return dict(chapters=len(chapters()),mcq=mcq,pyq=pyq,total=mcq+pyq,desc=len(descriptive_items()))
@bp.app_context_processor
def _cards_ctx():
    return {'unit6_cards_for':lambda q,n=3:_cards.cards_for_question(q,n),'unit6_chapter_cards':lambda c:_cards.chapter_cards(_cards.chapter_key(c)),'unit6_chapter_key':_cards.chapter_key}
@bp.get('/cards/<chapter_id>')
def concept_cards(chapter_id):
    key=_cards.chapter_key(chapter_id);cards=_cards.chapter_cards(key)
    if not cards:abort(404)
    c=chapter_or_404(chapter_id)
    hl=[x for x in request.args.get('hl','').split(',') if x]
    qid=request.args.get('item_id') or request.args.get('q');q=records().get(qid) if qid else None
    if q and q['_chapter']!=chapter_id:q=None
    lang=language();qkeep={'item_id':q['id']} if q else {}
    choice=request.args.get('choice',type=int);review=bool(q) and request.args.get('review')=='1' and choice in (1,2,3,4)
    if review:qkeep.update(review='1',choice=choice)
    target=None
    if q:
        args={**filters(chapter_id),'qlang':lang}
        if review:args.update(review='1',choice=choice)
        target=url_for('.practice',item_id=q['id'],**args)+'#answer-result'
    lax=[l for l in (c.get('laxmikanth') or []) if (LAX_DIR/f"chapter-{int(l['chapter']):03d}.html").is_file()]
    tabs=dict(show=False)
    toolbar=render_template('ds/polity_note_toolbar.html',chapter_url=url_for('.chapter',chapter_id=chapter_id),question_url=target,tabs=tabs)
    f=Path(__file__).resolve().parents[2]/'content'/'polity'/'g2'/'concept_pages'/f'{key}.html'
    if not f.is_file():
        return render_template('ds/polity_cards.html',cards=cards,key=key,hl=hl,lang=lang,chapter=c,chapter_id=chapter_id,toolbar=toolbar,qkeep=qkeep)
    hl_css=''.join(f'[id="{h}"]{{background:#fff8e1!important;border-color:#ffb300!important;box-shadow:0 0 0 3px #ffe082}}[id="{h}"] .ch::after{{content:" ◀ related";font-size:11px;color:#8d6e00;background:#ffecb3;border-radius:8px;padding:1px 7px;margin-left:6px}}' for h in hl if _re.fullmatch(r'CC-[0-9.]+-\d+',h))
    page=f.read_text(encoding='utf-8');scroll=''
    rf=f.parents[1]/'concept_recaps'/f'{key}.html'
    recap=rf.read_text(encoding='utf-8') if rf.is_file() else ''
    if recap:
        nav=('<nav class="rc-nav"><a href="#recap">⚡ Recap / సంక్షిప్త నోట్స్</a><a href="#full-details">📚 Full details / పూర్తి వివరాలు</a></nav>')
        divider=('<div id="full-details" class="rc-divider"><b>📚 Full details — all concept cards</b><span>పూర్తి వివరాలు — అన్ని కాన్సెప్ట్ కార్డులు</span></div>')
        ids=[h for h in hl if _re.fullmatch(r'CC-[0-9.]+-\d+',h)]
        scroll=('<script>window.addEventListener("load",function(){var e=document.getElementById("'+ids[0]+'");if(e)e.scrollIntoView({block:"start",behavior:"instant"})})</script>') if ids else ''
        recap_css_i=recap.find('</style>')+8
        m=_re.match(r'\s*<style>.*?</style>',page,flags=_re.S);base=m.group(0) if m else '';page=page[len(base):]
        page=base+recap[:recap_css_i]+nav+recap[recap_css_i:]+divider+page
    doc=('<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Concept cards '+key+' · Unit 6</title>'
        +'<style>:root{--acc:'+_accent(chapter_id)+'}'+CARDS_CSS+hl_css+'</style></head><body>'+toolbar+page+(scroll if recap else '')+'</body></html>')
    response=make_response(doc);response.headers['Content-Type']='text/html; charset=utf-8'
    return response
CARDS_CSS="""body{background:#e0f4f1}.page{width:auto!important;max-width:1040px!important;min-height:0!important;margin:0 auto 12px!important;padding:12px 14px!important;overflow-wrap:anywhere}
.secl{font-size:11.5px;color:#546e7a;margin-top:2px}.fact em.en{font-style:italic;color:#37474f;font-size:13.5px}.fact.flag{background:#fff3e0;border-radius:5px;padding:1px 4px}
.asof{font-size:11px;font-style:normal;color:#00695c;background:#d7ece6;border-radius:8px;padding:1px 6px;white-space:nowrap}.warn{font-size:11px;font-style:normal;font-weight:700;color:#b45309}
table{display:block;overflow-x:auto;max-width:100%}
.rc-nav{position:sticky;top:0;z-index:5;display:flex;gap:8px;justify-content:center;flex-wrap:wrap;padding:8px;background:#e0f4f1}.rc-nav a{background:#fff;border:1.5px solid var(--acc,#0f766e);color:var(--acc,#0f766e);font-weight:700;font-size:14px;border-radius:18px;padding:5px 14px;text-decoration:none}
.rc-divider{max-width:1040px;margin:18px auto 12px;padding:12px 14px;border-radius:10px;background:var(--acc,#0f766e);color:#fff;display:flex;flex-direction:column;gap:2px;font-size:16px}.rc-divider span{font-size:13.5px;opacity:.9}
html{scroll-behavior:smooth;scroll-padding-top:52px}
@media(max-width:480px){.rc-nav{gap:5px;padding:6px}.rc-nav a{font-size:12px;padding:4px 9px}}
@media(max-width:700px){.g2,.g3,.g4,.wgrid{grid-template-columns:1fr!important}.page{padding:10px 8px!important}.header{flex-wrap:wrap}.hmeta{margin-left:0!important;text-align:left!important}}"""
@bp.app_context_processor
def _stats_ctx():
    return {'unit6_enabled':enabled(),'unit6_stats':unit6_stats}
# Chapter accents: (fill, ink). fill = light-mode colour (white text on it, tinted tiles); ink = light text for dark mode.
# Kept away (CIEDE2000 >= 10) from the reserved meanings: known green, revise red, trap amber, PYQ blue.
ACCENTS={'6.1':('#0F766E','#5EEAD4'),'6.2':('#4338CA','#A5B4FC'),'6.3':('#A21CAF','#F0ABFC'),'6.4':('#7C2D12','#FDBA74'),'6.5':('#0E7490','#67E8F9'),
         '6.6':('#BE185D','#F9A8D4'),'6.7':('#334155','#CBD5E1'),'6.8':('#6B21A8','#D8B4FE'),'6.9':('#854D0E','#FDE68A')}
def _acc_pair(cid):return ACCENTS.get('.'.join(str(cid).split('.')[:2]),ACCENTS['6.1'])
@bp.app_template_filter('drop_brackets')
def drop_brackets(t):
    import re as _r
    return _r.sub(r'\s*\([^)]*\)','',t or '')
@bp.app_template_filter('xl')
def _xl(t,own=None):return _recall.autolink(t,own)
@bp.app_template_filter('accent')
def _accent(cid):return _acc_pair(cid)[0]
@bp.app_template_filter('accent_ink')
def _accent_ink(cid):return _acc_pair(cid)[1]
TE_TITLES={'6.1.1':'ప్రాథమిక భావనలు, పదజాలం','6.1.2':'రాజ్యాంగ భావన, వర్గీకరణ','6.1.3':'రాజ్యాంగ పరిణామం','6.1.4':'రాజ్యాంగ రచన','6.2.1':'భారత రాజ్యాంగ ముఖ్య లక్షణాలు','6.3.1':'ప్రవేశిక, రాజ్యాంగ తత్వం','6.4.1':'ప్రాథమిక హక్కులు','6.5.1':'ఆదేశిక సూత్రాలు','6.5.2':'ప్రాథమిక హక్కులు–ఆదేశిక సూత్రాల సంబంధం','6.6.1':'ప్రాథమిక విధులు','6.7.1':'రాజ్యాంగ సవరణ','6.8.1':'ప్రాథమిక స్వరూప సిద్ధాంతం','6.9.1':'భారత భూభాగం, యూనియన్','6.9.2':'పౌరసత్వం'}
@bp.app_template_filter('chapter_te')
def _chapter_te(cid):return TE_TITLES.get(cid,'')
from markupsafe import Markup,escape
_ITEM=_re.compile(r'^\s*(\(?)([1-9]|[A-Ea-e]|i{1,3}|iv|v)([.)])\s+(.*\S)\s*$')
def _kind(m):
    t=m.group(2)
    return 'num' if t.isdigit() else 'roman' if t in('i','ii','iii','iv','v') else 'upper' if t.isupper() else 'lower'
def format_stem(text):
    """Match-the-following and numbered statements get a tidy layout; wording is untouched."""
    if not text:return Markup('')
    lines=[l for l in str(text).replace('\r','').split('\n')]
    items=[];intro=[];tail=[];state='intro'
    for l in lines:
        m=_ITEM.match(l)
        if m and state in('intro','items'):
            items.append((_kind(m),m.group(2),m.group(4)));state='items'
        elif state=='items' and l.strip():
            if items:tail.append(l.strip());state='tail'
        elif state=='intro' and l.strip():intro.append(l.strip())
        elif state=='tail' and l.strip():tail.append(l.strip())
    if not items:return Markup('<span class="u6-plain">'+str(escape(text))+'</span>')
    groups=[];
    for k,label,body in items:
        if groups and groups[-1][0]==k:groups[-1][1].append((label,body))
        else:groups.append([k,[(label,body)]])
    out=['<div class="u6-stem">']
    if intro:out.append('<p class="u6-intro">'+str(escape(' '.join(intro)))+'</p>')
    if len(groups)==2 and all(len(g[1])>=2 for g in groups):
        a,b=groups[0][1],groups[1][1]
        out.append('<div class="u6-match">')
        for col,head in ((a,'List I / జాబితా I'),(b,'List II / జాబితా II')):
            out.append('<div class="mcol"><div class="mh">'+head+'</div>')
            for label,body in col:out.append('<div class="mc"><b>'+str(escape(label.upper() if col is a else label))+'</b><span>'+str(escape(body))+'</span></div>')
            out.append('</div>')
        out.append('</div>')
    else:
        out.append('<ol class="u6-stmts">')
        for k,label,body in items:out.append('<li><b>'+str(escape(label))+'</b><span>'+str(escape(body))+'</span></li>')
        out.append('</ol>')
    if tail:out.append('<p class="u6-tail">'+str(escape(' '.join(tail)))+'</p>')
    out.append('</div>')
    return Markup(''.join(out))
@bp.app_template_filter('fmt_stem')
def _fmt_stem(t):return format_stem(t)
@bp.app_template_filter('pyq_label')
def _pyq_label(q):
    """Attribution exactly as recorded in the question bank; nothing is inferred."""
    if q.get('_kind') not in ('pyq','primary_pyq'):return None
    exam=(q.get('exam') or '').replace('Other credible examinations - ','').strip()
    year=str(q.get('year') or '').strip()
    stage=(q.get('stage') or '').strip();stage=stage[:1].upper()+stage[1:] if stage else ''
    paper=(q.get('paper') or '').strip()
    if paper.lower().startswith('subject-indexed'):paper=''
    elif paper and not paper.lower().startswith('paper') and len(paper)<=4:paper='Paper '+paper
    series=(q.get('series_set') or '').strip()
    if series and series.lower() not in ('a','b','c','d') :pass
    detail=' · '.join(x for x in (stage,paper,series,('Q'+str(q['question_number'])) if q.get('question_number') else '') if x)
    return dict(title=' · '.join(x for x in (exam,year) if x),detail=detail)

_ABBR=re.compile(r"(?:\b(?:Ch|No|Nos|Art|Arts|Sec|Cl|Sch|Vol|vs|v|Dr|Mr|Shri|Smt|Pt|St|etc|viz|cf|ed|Pr|Fig|Sl)|\b[A-Z])\.$")
def _sentences(par):
    parts=re.split(r"(?<=[.!?])\s+",par.strip());out=[]
    for x in parts:
        if out and _ABBR.search(out[-1]):out[-1]+=' '+x
        else:out.append(x)
    return [x for x in out if x]
def format_expl(t):
    t=clean_text(t or '').strip()
    if not t:return Markup('')
    pars=[x for x in re.split(r"\n+",t) if x.strip()]
    sents=[x for par in pars for x in _sentences(par)]
    if len(sents)<=1:return Markup('<p class="lead">'+str(escape(sents[0] if sents else t))+'</p>')
    out=['<p class="lead">'+str(escape(sents[0]))+'</p><ul class="pts">']
    for x in sents[1:]:
        clauses=[c.strip() for c in re.split(r";\s+",x) if c.strip()]
        if len(x)>170 and len(clauses)>1:
            out.append('<li>'+str(escape(clauses[0]))+'<ul>'+''.join('<li>'+str(escape(c))+'</li>' for c in clauses[1:])+'</ul></li>')
        else:out.append('<li>'+str(escape(x))+'</li>')
    out.append('</ul>')
    return Markup(''.join(out))
@bp.app_template_filter('fmt_expl')
def _fmt_expl(t):return format_expl(t)
@bp.app_template_filter('clean_expl')
def _clean_expl(t):return clean_text(t)

def enabled():return current_app.config.get('POLITY_UNIT6_ENABLED',os.environ.get('POLITY_UNIT6_ENABLED','0')=='1')
@bp.before_request
def availability():
    if not enabled():abort(404)

def chapters():
    return [c for u in read(CONTENT/'MASTER-INDEX.json')['units'] if u['unit']==6 for s in u['sections'] for c in s['chapters']]
def chapter_or_404(cid):
    return next((c for c in chapters() if c['id']==cid),None) or abort(404)
VISIBLE_KINDS=('bank','pyq','primary_pyq')
def visible(q):return q['_kind'] in VISIBLE_KINDS and q['_answer'] in (1,2,3,4)
def scoreable(q):
    return q['_answer'] in (1,2,3,4)
def state_for(item_id):
    key=(device_id(),item_id);state=db.session.get(PolityUnit6State,key)
    if state is None:
        state=PolityUnit6State(device_id=key[0],item_id=item_id,saved=False,seen_count=0,wrong_count=0);db.session.add(state)
    return state
def test_records(cid):
    chapter_or_404(cid);p=CONTENT/'.'.join(cid.split('.')[:2])/cid/'Chapter-Test.json'
    if not p.is_file():return []
    d=read(p);ids=[q['id'] for q in d.get('questions',[])]+d.get('question_ids',[])
    corpus=records();return [corpus[i] for i in dict.fromkeys(ids) if i in corpus]

@bp.before_request
def _recall_fresh():
    if request.endpoint in ('polity_unit6.home','polity_unit6.recall_hub','polity_unit6.recall_deck','polity_unit6.recall_card','polity_unit6.articles','polity_unit6.unit'):_recall.refresh()
@bp.get('/')
def home():
    units=read(CONTENT/'MASTER-INDEX.json')['units']
    return render_template('ds/polity_subject.html',units=units,decks=[d for d in _recall.all_decks() if d['count']] if enabled() else [])

def _recall_page(deck_id):
    d=_recall.deck(deck_id)
    if not d:abort(404)
    cards=_recall.items(deck_id)
    if not cards:abort(404)
    ch=request.args.get('chapter') or None
    if ch and ch not in {c['chapter'] for c in cards}:abort(404)
    _open=request.args.get('open') or ''
    _back=None;bk=request.args.get('back') or ''
    if ':' in bk:
        bd,bid=bk.split(':',1);bc=_recall.index()['cards'].get(bid) if _recall.deck_of(bid)==bd else None;lb=bc and (bc['front_en'],bc.get('front_te') or bc['front_en'])
        if lb:_back={'id':bid,'deck':bd,'en':lb[0],'te':lb[1],'url':_recall.card_url(bid)}
    # ?for=<card id>: a matrix of exactly the cards of this deck linked to that card (from its Related row)
    _for=None;fid=request.args.get('for') or ''
    if fid:
        fc=_recall.index()['cards'].get(fid)
        if not fc:abort(404)
        have={c['id'] for c in cards};fids=[r['id'] for r in _recall.related(fc).get(deck_id,[]) if r['id'] in have]
        _for={'id':fid,'ids':fids,'en':fc['front_en'],'te':fc.get('front_te') or fc['front_en']}
        if not _back:_back={'id':fid,'deck':_recall.deck_of(fid),'en':_for['en'],'te':_for['te'],'url':_recall.card_url(fid)}
    light={'v':_recall.data_version(),'cards':[_recall.light(c,d) for c in cards],'themes':_recall.light_themes(deck_id),
           'parts':{P[0]:[P[1],P[2],P[4],P[5]] for P in _recall.PARTS}}
    for x in light['cards']:
        if 'acc' not in x:x['acc'],x['ink']=_acc_pair(x['ch'])
    return render_template('ds/polity_recall.html',d=d,total=len(cards),chapter=ch,names=ARTCARD_CHAPTERS,lang=language(),lang_set='qlang' in request.args,
                           parts=_recall.part_counts(cards),units=_recall.UNITS,ucounts=_recall.unit_counts(cards),light=light,
                           open_id=_open if _open in {c['id'] for c in cards} else '',back=_back,for_=_for)
@bp.get('/recall/<deck_id>/card/<card_id>')
def recall_card(deck_id,card_id):
    """One card's full detail markup (<article class="ac-src">), fetched lazily when the card is opened. Cached by data version."""
    d=_recall.deck(deck_id)
    if not d:abort(404)
    cards=_recall.items(deck_id);c=next((x for x in cards if x['id']==card_id),None);t=None
    if not c:
        t=next((x for x in _recall.themes(deck_id) if x['id']==card_id),None)
        if not t:abort(404)
    etag='"%s-%s-%s"'%(_recall.data_version(),deck_id,card_id)
    if request.if_none_match and etag.strip('"') in request.if_none_match:
        r=make_response('',304)
    else:
        r=make_response(render_template('ds/polity_recall_card.html',d=d,card=c,t=t,cards=cards,names=ARTCARD_CHAPTERS,themes=_recall.themes(deck_id),
                        chains=_recall.chains(),card_chains=_recall.card_chains,ref_url=_recall.ref_url,art_ref=_recall.art_ref,exam_label=_recall.exam_label,related=_recall.related))
        r.headers['Content-Type']='text/html; charset=utf-8'
    r.headers['ETag']=etag;r.headers['Cache-Control']='public, max-age=604800' if request.args.get('v') else 'no-cache'
    r.headers['Vary']='Accept-Encoding'
    return r
@bp.get('/articles')
def articles():return _recall_page('articles')
@bp.get('/recall')
def recall_hub():
    return render_template('ds/polity_recall_hub.html',decks=[d for d in _recall.all_decks() if d['count']],lang=language())
@bp.get('/recall/<deck_id>')
def recall_deck(deck_id):return _recall_page(deck_id)
# Short chapter names for the article-card chips (number, English, Telugu).
ARTCARD_CHAPTERS={'6.1':('Nature and development','స్వభావం, పరిణామం'),'6.2':('Salient features','ముఖ్య లక్షణాలు'),
    '6.3':('Preamble','ప్రవేశిక'),'6.4':('Fundamental Rights','ప్రాథమిక హక్కులు'),'6.5':('Directive Principles','ఆదేశిక సూత్రాలు'),
    '6.6':('Fundamental Duties','ప్రాథమిక విధులు'),'6.7':('Amendment','రాజ్యాంగ సవరణ'),'6.8':('Basic structure','ప్రాథమిక స్వరూపం'),
    '6.9':('Territory and citizenship','భూభాగం, పౌరసత్వం')}
@bp.get('/unit')
def unit():
    corpus=records();rows=[]
    progress={p.chapter_id:p for p in PolityUnit6Progress.query.filter_by(device_id=device_id())}
    for c in chapters():
        own=[q for q in corpus.values() if q['_chapter']==c['id'] and visible(q)]
        rows.append(dict(chapter=c,desc=sum(1 for x in descriptive_items() if x['chapter']==c['id']),total=len(own),mcq=sum(q['_kind']=='bank' for q in own),pyq=sum(q['_kind'] in ('pyq','primary_pyq') for q in own),unscored=sum(not q['_scored'] for q in own),completed=bool(progress.get(c['id']) and progress[c['id']].completed)))
    return render_template('ds/polity_browse.html',mode='unit',rows=rows,stats=unit6_stats())

@bp.get('/chapters/<chapter_id>')
def chapter(chapter_id):
    c=chapter_or_404(chapter_id)
    own=[q for q in records().values() if q['_chapter']==chapter_id and visible(q)]
    progress=db.session.get(PolityUnit6Progress,(device_id(),chapter_id))
    return render_template('ds/polity_browse.html',mode='chapter',chapter=c,desc=sum(1 for x in descriptive_items() if x['chapter']==c['id']),mcq=sum(q['_kind']=='bank' for q in own),pyq=sum(q['_kind'] in ('pyq','primary_pyq') for q in own),total=len(own),unscored=sum(not q['_scored'] for q in own),progress=progress)

def filters(default_chapter=''):
    values={k:request.args.get(k,'').strip() for k in ('chapter','kind','q','view','map')}
    if values['map'] and values['map'] not in catalog():abort(404)
    if not any(k in request.args for k in values):values['chapter']=default_chapter
    if values['chapter']:chapter_or_404(values['chapter'])
    return values

def selection(values):
    chapter,kind,query,view=(values[k] for k in ('chapter','kind','q','view'))
    if values.get('map'):
        corpus=records();qs=[corpus[l['item_id']] for l in catalog()[values['map']]['links'] if l['item_id'] in corpus and visible(corpus[l['item_id']])]
        return list({q['id']:q for q in qs}.values())
    qs=test_records(chapter) if kind=='chaptertest' and chapter else list(records().values())
    if chapter:qs=[q for q in qs if q['_chapter']==chapter]
    if kind and kind!='chaptertest':qs=[q for q in qs if q['_kind']==kind or kind=='pyq' and q['_kind']=='primary_pyq']
    if kind=='chaptertest' and not chapter:qs=[q for c in chapters() for q in test_records(c['id'])]
    if kind!='chaptertest':qs=[q for q in qs if visible(q)]
    if query:qs=[q for q in qs if query.casefold() in (q.get('question_en','')+' '+q.get('question_te','')+' '+q['id']).casefold()]
    if view in ('saved','mistakes'):
        states=PolityUnit6State.query.filter_by(device_id=device_id()).all()
        ids={s.item_id for s in states if s.saved} if view=='saved' else {s.item_id for s in states if s.wrong_count>0}
        qs=[q for q in qs if q['id'] in ids]
    return list({q['id']:q for q in qs}.values())

def language():
    lang=request.args.get('qlang','te')
    if lang not in ('te','en','both'):abort(400)
    return lang

def _lang_pick(d,key,lang):
    return d.get(key+'_'+lang) if (key+'_'+lang) in d else d.get(lang)
def struct_flat(s,lang):
    """Plain text of a structured answer (used by the AI teacher and as a fallback)."""
    out=[]
    if s.get('intro',{}).get(lang):out.append(s['intro'][lang])
    for v in s.get('visuals',[]):
        t=_lang_pick(v,'title',lang)
        if v.get('type')=='table':
            cols=_lang_pick(v,'columns',lang) or []
            out.append((t or '')+': '+' | '.join(cols))
            for r in v.get('rows',[]):out.append(' | '.join(r.get(lang,[])))
        elif v.get('type')=='flow':
            out.append((t or '')+': '+' -> '.join(x.get(lang,'') for x in v.get('steps',[])))
        elif v.get('type')=='box':
            out.append((t or '')+': '+'; '.join(x.get(lang,'') for x in v.get('items',[])))
    for sec in s.get('sections',[]):
        out.append(_lang_pick(sec,'heading',lang) or '')
        out+= ['- '+p.get(lang,'') for p in sec.get('points',[])]
    c=s.get('conclusion') or {}
    if c.get(lang):out.append((c.get('label_'+lang) or '')+': '+c[lang])
    return [x for x in out if x]
def render_struct(s,lang):
    e=lambda x:str(escape(x or ''))
    h=['<div class="d-struct" lang="%s">'%lang]
    if s.get('intro',{}).get(lang):h.append('<p class="d-intro">'+e(s['intro'][lang])+'</p>')
    for v in s.get('visuals',[]):
        t=_lang_pick(v,'title',lang)
        if v.get('type')=='table':
            cols=_lang_pick(v,'columns',lang) or []
            h.append('<div class="d-tablewrap"><table class="d-table">'+('<caption>'+e(t)+'</caption>' if t else '')+'<thead><tr>'+''.join('<th>'+e(c)+'</th>' for c in cols)+'</tr></thead><tbody>')
            for r in v.get('rows',[]):
                cells=r.get(lang,[]);h.append('<tr>'+''.join('<td data-label="%s">%s</td>'%(e(cols[i] if i<len(cols) else ''),e(c)) for i,c in enumerate(cells))+'</tr>')
            h.append('</tbody></table></div>')
        elif v.get('type')=='flow':
            h.append('<div class="d-flow">'+('<b>'+e(t)+'</b>' if t else '')+'<ol>'+''.join('<li>'+e(x.get(lang,''))+'</li>' for x in v.get('steps',[]))+'</ol></div>')
        elif v.get('type')=='box':
            h.append('<aside class="d-box">'+('<b>'+e(t)+'</b>' if t else '')+'<ul>'+''.join('<li>'+e(x.get(lang,''))+'</li>' for x in v.get('items',[]))+'</ul></aside>')
    for sec in s.get('sections',[]):
        hd=_lang_pick(sec,'heading',lang)
        if hd:h.append('<h3>'+e(hd)+'</h3>')
        h.append('<ul class="d-pts">'+''.join('<li>'+e(p.get(lang,''))+'</li>' for p in sec.get('points',[]))+'</ul>')
    c=s.get('conclusion') or {}
    if c.get(lang):h.append('<div class="d-concl"><b>'+e(c.get('label_'+lang) or '')+'</b> '+e(c[lang])+'</div>')
    h.append('</div>');return Markup(''.join(h))
@bp.app_template_filter('fmt_struct')
def _fmt_struct(s,lang):return render_struct(s,lang)

@lru_cache(maxsize=1)
def descriptive_items():
    out=[]
    for c in chapters():
        f=CONTENT/c['id'].rsplit('.',1)[0]/c['id']/'Group-I.json'
        if not f.is_file():continue
        d=read(f)
        sf=f.with_name('Descriptive-structured.json');structured=(read(sf).get('items') or {}) if sf.is_file() else {}
        for key in ('items','answers'):
            for it in (d.get(key) if isinstance(d.get(key),list) else []):
                def paras(v):
                    if isinstance(v,list):return [str(x).strip() for x in v if str(x).strip()]
                    return [x.strip() for x in str(v or '').split('\n') if x.strip()]
                kind=str(it.get('kind') or '')
                exam=str(it.get('exam') or it.get('source') or '').split(' \u2014 ')[0].strip() if 'PYQ' in kind or it.get('exam') else ''
                exam=exam if re.match(r'APPSC',exam) and 'style' not in exam.lower() else ''
                st=structured.get(it.get('id'))
                out.append(dict(id=it.get('id'),chapter=c['id'],s=st,exam=exam,marks=it.get('marks'),
                    q_en=it.get('question_en') or '',q_te=it.get('question_te') or '',
                    a_en=paras(it.get('answer_en') or it.get('model_answer_en')),a_te=paras(it.get('answer_te') or it.get('model_answer_te'))))
    for x in out:
        if x.get('s'):x['a_en']=struct_flat(x['s'],'en');x['a_te']=struct_flat(x['s'],'te')
    return [x for x in out if x['id'] and (x['a_en'] or x['a_te'])]
@bp.app_context_processor
def _desc_ctx():return {'unit6_desc_count':lambda:len(descriptive_items()) if enabled() else 0}

@bp.get('/descriptive')
def descriptive():
    cid=request.args.get('chapter','')
    if cid:chapter_or_404(cid)
    items=[x for x in descriptive_items() if not cid or x['chapter']==cid]
    return render_template('ds/polity_descriptive.html',items=items,chapter=cid,lang=language(),total=len(descriptive_items()),
        chs=[(c,sum(1 for x in descriptive_items() if x['chapter']==c['id'])) for c in chapters()])

@bp.get('/library')
def library():
    values=filters();qs=selection(values)
    page=max(1,request.args.get('page',1,type=int));total=len(qs)
    return render_template('ds/polity_browse.html',mode='library',questions=qs[(page-1)*40:page*40],total=total,page=page,filters=values,lang=language(),start=qs[0]['id'] if qs else None)

def question_page(q,choice=None,review=False,qs=None):
    values=filters(q['_chapter']);qs=selection(values) if qs is None else qs
    pos=next((i for i,r in enumerate(qs) if r['id']==q['id']),None)
    # A bookmarked question may disappear from the filter after an action; keep it
    # visible without silently switching to the full bank.
    if pos is None:qs=[q];pos=0
    lang=language();feedback=None
    if review:feedback='correct' if choice==q['_answer'] else 'incorrect'
    context={**values,'qlang':lang}
    review_args={'review':'1','choice':choice} if review and choice in (1,2,3,4) else {}
    notes=url_for('.notes',chapter_id=q['_chapter'],item_id=q['id'],**context,**review_args)
    locators=section_links(q)
    links=[dict(url=notes+'#'+l['anchor'],basis=l['basis'],title=l.get('title','')) for l in locators]
    if not links:links=[dict(url=notes+'#question-explanation',basis='explanation')]
    return render_template('ds/polity_question.html',question=q,choice=choice,feedback=feedback,lang=lang,context=context,
        state=db.session.get(PolityUnit6State,(device_id(),q['id'])),position=pos+1,total=len(qs),
        previous=qs[pos-1]['id'] if pos else None,following=qs[pos+1]['id'] if pos+1<len(qs) else None,
        notes_url=notes,section_links=links,review_args=review_args)

from functools import lru_cache
@lru_cache(maxsize=16)
def numbered_notes(chapter_id):
    """Stored notes HTML is untouched on disk; headings get stable ids at response time."""
    html=(directory(chapter_id)/'Notes.html').read_text(encoding='utf-8-sig')
    counter=[0]
    def add(m):
        i=counter[0];counter[0]+=1
        return f'<a id="u6s-{i}"></a>'+m.group(0) if ' id=' in m.group(0) else m.group(0)[:-1]+f' id="u6s-{i}">'
    return _re.sub(r'<h[1-4]\b[^>]*>',add,html)

from pathlib import Path as _P
LAX_DIR=CONTENT/'references'/'laxmikanth'
LAX_CSS='''<style>body{background:#f4f6f8!important;font-size:16px!important;overflow-wrap:anywhere}.page{width:auto!important;max-width:900px!important;min-height:0!important;margin:0 auto!important;padding:14px 14px 30px!important;box-shadow:none!important;background:#fff!important}body>nav[style]{display:none!important}img,svg{max-width:100%;height:auto}table{display:block;max-width:100%;overflow-x:auto;-webkit-overflow-scrolling:touch}h1{font-size:1.35rem!important;line-height:1.4}.ptitle{display:block!important}@media(max-width:640px){body{font-size:15.5px!important}.page{padding:10px 10px 26px!important}[style*="columns"],[style*="column-count"]{column-count:1!important;columns:1!important}td,th{min-width:84px}ul{margin-left:16px!important}}</style>'''
@bp.get('/chapters/<chapter_id>/notes')
def notes(chapter_id):
    chapter_or_404(chapter_id);item_id=request.args.get('item_id');q=records().get(item_id) if item_id else None
    if item_id and (not q or q['_chapter']!=chapter_id):abort(404)
    c=chapter_or_404(chapter_id)
    lax=[l for l in (c.get('laxmikanth') or []) if (LAX_DIR/f"chapter-{int(l['chapter']):03d}.html").is_file()]
    src='lax' if request.args.get('src')=='lax' and lax else 'gbk'
    lx=request.args.get('lx',type=int)
    if src=='lax':
        if lx not in [l['chapter'] for l in lax]:lx=lax[0]['chapter']
        content=(LAX_DIR/f"chapter-{lx:03d}.html").read_text(encoding='utf-8-sig')
        content=_re.sub(r'</head>',lambda m:LAX_CSS+m.group(0),content,count=1,flags=_re.I)
    else:content=numbered_notes(chapter_id)
    keep={k:v for k,v in request.args.items() if k not in ('src','lx')}
    tabs=dict(show=bool(lax),src=src,lx=lx,lax=[dict(n=l['chapter'],title=l.get('title',''),url=url_for('.notes',chapter_id=chapter_id,src='lax',lx=l['chapter'],**keep)) for l in lax],
        gbk=url_for('.notes',chapter_id=chapter_id,**keep),laxurl=url_for('.notes',chapter_id=chapter_id,src='lax',lx=lax[0]['chapter'],**keep) if lax else '')
    back=url_for('.chapter',chapter_id=chapter_id)
    target=None
    if q:
        args={**filters(chapter_id),'qlang':language()}
        choice=request.args.get('choice',type=int)
        if request.args.get('review')=='1' and choice in (1,2,3,4):args.update(review='1',choice=choice)
        target=url_for('.practice',item_id=q['id'],**args)+'#answer-result'
    ids=[c['id'] for c in chapters()];nxt=ids[ids.index(chapter_id)+1] if ids.index(chapter_id)+1<len(ids) else None
    toolbar=render_template('ds/polity_note_toolbar.html',chapter_url=back,question_url=target,tabs=tabs)
    footer=render_template('ds/polity_note_footer.html',chapter_id=chapter_id,next_id=nxt)
    import re
    content=re.sub(r'(<body\b[^>]*>)',lambda m:m.group(1)+toolbar,content,count=1,flags=re.I)
    content=re.sub(r'</body>',lambda m:footer+m.group(0),content,count=1,flags=re.I)
    if q and src=='gbk' and not section_links(q):
        appendix=render_template('ds/polity_note_explanation.html',question=q,lang=language())
        content=re.sub(r'</body>',lambda m:appendix+m.group(0),content,count=1,flags=re.I)
    response=make_response(content);response.headers['Content-Type']='text/html; charset=utf-8'
    return response

@bp.get('/practice/<item_id>')
def practice(item_id):
    q=records().get(item_id)
    if q is None:
        alias=next((r.get('canonical_question_id') for r in read(CONTENT/'_shared/Expected-Questions.json') if r['id']==item_id),None)
        if alias in records():return redirect(url_for('.practice',item_id=alias))
        abort(404)
    choice=request.args.get('choice',type=int)
    return question_page(q,choice,request.args.get('review')=='1' and choice in (1,2,3,4))

@bp.post('/practice/<item_id>')
def answer(item_id):
    q=records().get(item_id) or abort(404);state=state_for(item_id)
    if request.form.get('action')=='bookmark':
        state.saved=not state.saved;db.session.commit()
        args={**filters(q['_chapter']),'qlang':language()}
        choice=request.args.get('choice',type=int)
        if request.args.get('review')=='1' and choice in (1,2,3,4):args.update(review='1',choice=choice)
        return redirect(url_for('.practice',item_id=item_id,**args))
    selected=request.form.get('answer',type=int)
    if selected not in (1,2,3,4):abort(400)
    qs=selection(filters(q['_chapter']))
    state.seen_count+=1;state.last_seen_at=datetime.utcnow()
    feedback='correct' if selected==q['_answer'] else 'incorrect'
    if feedback=='incorrect':state.wrong_count+=1
    else:state.wrong_count=0
    db.session.commit()
    return question_page(q,selected,True,qs)

@bp.post('/progress/<chapter_id>')
def progress(chapter_id):
    chapter_or_404(chapter_id);key=(device_id(),chapter_id)
    p=db.session.get(PolityUnit6Progress,key)
    if p is None:p=PolityUnit6Progress(device_id=key[0],chapter_id=chapter_id);db.session.add(p)
    p.completed=request.form.get('completed')=='1';p.updated_at=datetime.utcnow();db.session.commit()
    return redirect(url_for('.chapter',chapter_id=chapter_id))

@bp.post('/tests')
def start_test():
    cid=request.form.get('chapter','');chapter_mode=request.form.get('kind')=='chaptertest'
    if cid:chapter_or_404(cid)
    qs=test_records(cid) if chapter_mode and cid else [q for q in records().values() if visible(q) and (not cid or q['_chapter']==cid)]
    qs=[q for q in qs if scoreable(q)]
    count=min(100,max(1,request.form.get('count',25,type=int)));minutes=min(180,max(1,request.form.get('minutes',30,type=int)))
    if not chapter_mode:random.SystemRandom().shuffle(qs)
    qs=qs[:count]
    if not qs:abort(400,description='No scored questions available for this selection.')
    now=datetime.utcnow();exam=PolityUnit6Exam(id=str(uuid.uuid4()),device_id=device_id(),questions=qs,answers={},started_at=now,deadline=now+timedelta(minutes=minutes))
    db.session.add(exam);db.session.commit();return redirect(url_for('.exam',exam_id=exam.id))

@bp.route('/tests/<exam_id>',methods=['GET','POST'])
def exam(exam_id):
    e=PolityUnit6Exam.query.filter_by(id=exam_id,device_id=device_id()).with_for_update().first_or_404()
    now=datetime.utcnow()
    if not e.submitted_at and (request.method=='POST' or now>=e.deadline):
        answers=dict(e.answers or {})
        # Never accept answers received after the server deadline.
        if now<e.deadline:
            for q in e.questions:
                a=request.form.get(q['id'],type=int)
                if a in (1,2,3,4):answers[q['id']]=a
        e.answers=answers;e.score=sum(answers.get(q['id'])==q['_answer'] for q in e.questions);e.submitted_at=now
        for q in e.questions:
            if q['id'] not in answers:continue
            s=state_for(q['id']);s.seen_count+=1;s.last_seen_at=now
            if answers[q['id']]!=q['_answer']:s.wrong_count+=1
            else:s.wrong_count=0
        db.session.commit()
    return render_template('ds/polity_unit6.html',mode='exam',exam=e,seconds=max(0,int((e.deadline-now).total_seconds())))

@bp.post('/tests/<exam_id>/save')
def save_exam_answer(exam_id):
    e=PolityUnit6Exam.query.filter_by(id=exam_id,device_id=device_id()).with_for_update().first_or_404()
    if e.submitted_at or datetime.utcnow()>=e.deadline:abort(409)
    item_id=request.form.get('item_id');answer=request.form.get('answer',type=int)
    if item_id not in {q['id'] for q in e.questions} or answer not in (1,2,3,4):abort(400)
    e.answers={**(e.answers or {}),item_id:answer};db.session.commit()
    return {'saved':True}
