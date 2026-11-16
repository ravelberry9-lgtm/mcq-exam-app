"""Complete Unit 6 learner entry point backed by immutable authored records."""
import os,random,uuid
from pathlib import Path
from datetime import datetime,timedelta
from flask import Blueprint,abort,current_app,redirect,render_template,request,url_for,make_response,jsonify,session
from ..db import db
from ..polity_models import PolityUnit6State,PolityUnit6Progress,PolityUnit6Exam
from ..services.device import device_id
from .polity_maps import CONTENT,read,records,catalog
from ..services.polity_sections import section_links,directory
from ..services import polity_cards as _cards
from ..services import article_cards as _artcards
from ..services import recall_decks as _recall
from ..services import pyq_metrics as _pm
from ..services import concepts as _cg
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
def unit_of(cid):return int(str(cid).split('.')[0])
def unit6_stats(unit=None):
    """Counts for one syllabus unit (6-10), or for all units when unit is None."""
    corpus=[q for q in records().values() if unit is None or unit_of(q['_chapter'])==unit]
    mcq=sum(1 for q in corpus if q['_kind']=='bank' and visible(q))
    pyq=sum(1 for q in corpus if q['_kind'] in ('pyq','primary_pyq') and visible(q))
    desc=sum(1 for x in descriptive_items() if unit is None or unit_of(x['chapter'])==unit)
    return dict(chapters=len(chapters(unit)),mcq=mcq,pyq=pyq,total=mcq+pyq,desc=desc)
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
    page=f.read_text(encoding='utf-8')+_pyq_cards_html(cards,hl);scroll=''
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
PYQ_HEAD='APPSC PYQ additions — facts asked in APPSC papers, not covered in GBK / Laxmikanth · APPSC ప్రశ్నల్లో అడిగినవి, GBK / లక్ష్మీకాంత్‌లో లేనివి'
def _pyq_cards_html(cards,hl):
    from markupsafe import escape as e
    lst=[c for c in cards if c.get('pyq_addition')]
    if not lst:return ''
    out=['<div class="page"><div class="sh">'+str(e(PYQ_HEAD))+'</div><div class="g2">']
    for c in lst:
        out.append('<div class="card ncard'+(' hl' if c['id'] in hl else '')+'" id="'+str(e(c['id']))+'"><div class="ch">'+str(e(c['title_te']))+' · '+str(e(c['title_en']))+'</div>')
        for it in c['items']:
            out.append('<div class="fact"><span lang="te">'+str(e(it['te']))+'</span><br><em class="en" lang="en">'+str(e(it['en']))+'</em>'+(' <em class="asof">as of '+str(e(it['as_of']))+'</em>' if it.get('as_of') else '')+'</div>')
        out.append('</div>')
    out.append('</div></div>');return ''.join(out)
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
TE_TITLES.update({'7.1.1':'ప్రభుత్వ అంగాలు','7.2.1':'ఏకసభ, ద్విసభ శాసనసభలు','7.2.2':'పార్లమెంటు','7.2.3':'రాష్ట్ర శాసనసభ','7.2.4':'శాసనసభ కమిటీలు','7.3.1':'పార్లమెంటరీ వ్యవస్థ','7.3.2':'రాష్ట్రపతి','7.3.3':'ఉపరాష్ట్రపతి','7.3.4':'ప్రధానమంత్రి, కేంద్ర మంత్రిమండలి','7.3.5':'గవర్నర్','7.3.6':'ముఖ్యమంత్రి, రాష్ట్ర మంత్రిమండలి','7.4.1':'సుప్రీంకోర్టు','7.4.2':'హైకోర్టులు','7.4.3':'దిగువ న్యాయస్థానాలు','7.4.4':'ట్రిబ్యునళ్లు, న్యాయ సహాయం','7.5.1':'న్యాయ సమీక్ష','7.6.1':'న్యాయ క్రియాశీలత, న్యాయ నిగ్రహం','7.6.2':'ప్రజా ప్రయోజన వ్యాజ్యం'})
@bp.app_template_filter('chapter_te')
def _chapter_te(cid):return TE_TITLES.get(cid,'')
from markupsafe import Markup,escape
_ITEM=_re.compile(r'^\s*(\(?)([1-9]|[A-Ea-e]|i{1,3}|iv|v)([.)])\s+(.*\S)\s*$')
def _kind(m):
    t=m.group(2)
    return 'num' if t.isdigit() else 'roman' if t in('i','ii','iii','iv','v') else 'upper' if t.isupper() else 'lower'
_LHDR=_re.compile(r'^\s*((?:List|LIST)[- ]?(?:I{1,2}|1|2|A|B)\b[^:：]*|జాబితా[- ]?(?:I{1,2}|1|2|A|B)\b[^:：]*|Categories|వర్గాలు|Codes?|కోడ్‌?లు?)\s*[:：]?\s*(.*)$')
_SEQS=[['I','II','III','IV','V','VI'],[c for c in 'ABCDEFG'],[c for c in 'abcdefg'],[str(i) for i in range(1,10)],['i','ii','iii','iv','v','vi']]
def _split_seq(line):
    """'A. x  B. y  C. z' -> ['A. x','B. y','C. z'] following the label sequence, so names like 'B. R. Ambedkar' inside an item are safe."""
    m=_re.match(r'\s*\(?([A-Ga-g]|[1-9]|I{1,3}|IV|i{1,3}|iv|vi?)[.)](?:\s+|(?=[^\W\d_]))',line)
    if not m:return [line]
    first=m.group(1);seq=next((q for q in _SEQS if first in q and q.index(first)==0),None)
    if not seq:return [line]
    parts=[];pos=0;idx=1
    while idx<len(seq):
        mm=_re.compile(r'(?:\s|,|;|\|)\s*\(?'+_re.escape(seq[idx])+r'[.)](?:\s+|(?=[^\W\d_]))').search(line,pos+2)
        if not mm:break
        parts.append(line[pos:mm.start()].strip(' ,;|'));pos=mm.start()+len(mm.group(0))-len(mm.group(0).lstrip(' ,;|'));idx+=1
    parts.append(line[pos:].strip(' ,;|'))
    return parts if len(parts)>1 else [line]
_AR_A=_re.compile(r'(Assertion\s*(?:\(A\)|A)?|(?:ప్రతిపాదన|ప్రకటన|వాదన|ధృవీకరణ|వక్కాణింపు|నిశ్చితాభిప్రాయం|నిశ్చిత వాక్యం|నిశ్చితం|అభిప్రాయం)\s*\(A\))\s*[:：]\s*')
_AR_R=_re.compile(r'(Reason\s*(?:\(R\)|R)?|కారణం\s*\(R\))\s*[:：]\s*')
_AR_TAIL=_re.compile(r'\s*(?:\n|(?<=[.?])\s+)(?=(?:In the context|Choose|Select|Which (?:one )?of the following|సరైన|పై రెండు|కింది వాటిలో))')
def _format_ar(text):
    a=_AR_A.search(text);r=_AR_R.search(text,a.end()) if a else None
    if not(a and r):return None
    intro=text[:a.start()].strip();A=text[a.end():r.start()].strip();rest=text[r.end():]
    t=_AR_TAIL.search(rest);R=(rest[:t.start()] if t else rest).strip();tail=(rest[t.end():] if t else '').strip()
    te=bool(_re.search(r'[ఀ-౿]',text))
    la,lr=('ప్రతిపాదన (A)','కారణం (R)') if te else ('Assertion (A)','Reason (R)')
    out=['<div class="u6-stem">']
    if intro:out.append('<p class="u6-intro">'+str(escape(intro))+'</p>')
    out.append('<div class="u6-ar"><p><b>'+la+'</b><span>'+str(escape(A))+'</span></p><p><b>'+lr+'</b><span>'+str(escape(R))+'</span></p></div>')
    if tail:out.append('<p class="u6-tail">'+str(escape(tail))+'</p>')
    out.append('</div>');return Markup(''.join(out))
_PAIR=_re.compile(r'^\s*\(?([A-Ga-g])[.)]\s*(.+?)\s+\(?([1-9]|i{1,3}|iv|v)[.)]\s+(.+)$')
def _normalize_lists(text):
    raw=[l.strip().strip('|').strip() for l in str(text).replace('\r','').split('\n') if not _re.match(r'^\s*\|?\s*-{3,}',l)]
    raw=[_re.sub(r'\s*\|\s*','  ',l) if _re.match(r'^\(?[A-Ga-g][.)]\s',l) else l for l in raw]
    pairs=[_PAIR.match(l) for l in raw]
    if sum(1 for p in pairs if p)>=2:
        L=[f'{p.group(1)}. {p.group(2)}' for p in pairs if p];R=[f'{p.group(3)}. {p.group(4)}' for p in pairs if p]
        first=next(i for i,p in enumerate(pairs) if p);last=max(i for i,p in enumerate(pairs) if p)
        text='\n'.join(raw[:first]+L+R+raw[last+1:])
    out=[]
    for line in str(text).replace('\r','').replace(' | ','\n').split('\n'):
        h=_LHDR.match(line)
        if h:
            out.append('§HDR§'+h.group(1).strip());line=h.group(2)
            if not line.strip():continue
        lead=_re.match(r'^(.*?[:：])\s*(?=\(?(?:A|a|1|i|I)[.)](?:\s|[^\W\d_]))',line)
        if lead and not _re.match(r'\s*\(?(?:[A-Ga-g]|[1-9]|i{1,3}|iv)[.)]\s',line):
            out.append(lead.group(1).strip());line=line[lead.end():]
        out.extend(_split_seq(line))
    return out
def format_stem(text):
    """Match-the-following and numbered statements get a tidy layout; wording is untouched."""
    if not text:return Markup('')
    ar=_format_ar(str(text))
    if ar is not None:return ar
    lines=_normalize_lists(text)
    items=[];intro=[];tail=[];state='intro';heads=[]
    for l in lines:
        if l.startswith('§HDR§'):
            heads.append(l[5:])
            if state=='intro' and not items:continue
            if state=='items':continue
            continue
        m=_ITEM.match(l)
        if m and state in('intro','items'):
            items.append((_kind(m),m.group(2),m.group(4)));state='items'
        elif state=='items' and l.strip():
            # a statement wrapped onto the next line (no closing punctuation yet): join it back
            if items and _re.match(r'[a-z(]',l.strip()) and not items[-1][2].rstrip().endswith(('.','?','!',':',';')) or items and items[-1][2].rstrip().endswith('\u0c4d') and not l.strip().endswith((':','?','：')):
                k0,lb0,b0=items[-1];items[-1]=(k0,lb0,b0.rstrip()+('' if b0.rstrip().endswith('\u0c4d') else ' ')+l.strip())
            elif items:tail.append(l.strip());state='tail'
        elif state=='intro' and l.strip():intro.append(l.strip())
        elif state=='tail' and l.strip():tail.append(l.strip())
    if not items:return Markup('<span class="u6-plain">'+str(escape(text))+'</span>')
    kinds=list(dict.fromkeys(k for k,_,_ in items))
    if len(kinds)==2:items=sorted(items,key=lambda it:kinds.index(it[0]))
    groups=[];
    for k,label,body in items:
        if groups and groups[-1][0]==k:groups[-1][1].append((label,body))
        else:groups.append([k,[(label,body)]])
    out=['<div class="u6-stem">']
    if intro:out.append('<p class="u6-intro">'+str(escape(' '.join(intro)))+'</p>')
    if len(groups)==2 and all(len(g[1])>=2 for g in groups):
        a,b=groups[0][1],groups[1][1]
        out.append('<div class="u6-match">')
        h1,h2=(heads+['',''])[:2] if len(heads)>=2 else ('','')
        for col,head in ((a,h1 or 'List I / జాబితా I'),(b,h2 or 'List II / జాబితా II')):
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
# Telugu initials and titles ("డా. బి. ఆర్. అంబేద్కర్"): one letter (+vowel sign, +conjunct ending in virama) or డా/శ్రీ/శ్రీమతి.
_ABBR_TE=re.compile(r"(?:^|\s)(?:డా|శ్రీ|శ్రీమతి|[\u0C05-\u0C14\u0C15-\u0C39][\u0C3E-\u0C4C\u0C02]?(?:[\u0C15-\u0C39]\u0C4D)?)\.$")
def _sentences(par):
    parts=re.split(r"(?<=[.!?])\s+",par.strip());out=[]
    for x in parts:
        if out and (_ABBR.search(out[-1]) or _ABBR_TE.search(out[-1])):out[-1]+=' '+x
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
from ..services import student_text as _st
@bp.app_template_filter('student')
def _student(t):return _st.strip_meta(t)
@bp.app_template_global('explain_parts')
def _explain_parts(t,options=(),answer=None):return _st.explain_parts(clean_text(t or ''),options,answer)
@bp.app_template_global('options_te_usable')
def _otu(q):return _st.options_te_usable(q)
@bp.app_template_filter('clean_expl')
def _clean_expl(t):return clean_text(t)

def enabled():return current_app.config.get('POLITY_UNIT6_ENABLED',os.environ.get('POLITY_UNIT6_ENABLED','0')=='1')
@bp.before_request
def availability():
    if not enabled():abort(404)

UNITS=(6,7,8,9,10)
def units():
    return [u for u in read(CONTENT/'MASTER-INDEX.json')['units'] if u['unit'] in UNITS]
def chapters(unit=None):
    """Syllabus chapters of units 6-10 (or of one unit), in MASTER-INDEX order."""
    return [c for u in units() if unit is None or u['unit']==unit for s in u['sections'] for c in s['chapters']]
def unit_or_404(n):
    return next((u for u in units() if u['unit']==n),None) or abort(404)
def chapter_or_404(cid):
    return next((c for c in chapters() if c['id']==cid),None) or abort(404)
VISIBLE_KINDS=('bank','pyq','primary_pyq')
def visible(q):return q['_kind'] in VISIBLE_KINDS and q['_answer'] in (1,2,3,4) and not q.get('hold_reason')
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
    if request.endpoint in ('polity_unit6.home','polity_unit6.recall_hub','polity_unit6.recall_deck','polity_unit6.recall_card','polity_unit6.articles','polity_unit6.unit','polity_unit6.recall_trees','polity_unit6.recall_trees_chains'):_recall.refresh()
@bp.get('/')
def home():
    units=read(CONTENT/'MASTER-INDEX.json')['units']
    decks=[d for d in _recall.all_decks() if d['count']] if enabled() else []
    allq=[q for q in records().values() if visible(q)] if enabled() else []
    pt={'bank':sum(q['_kind']=='bank' for q in allq),'pyq':sum(q['_kind']!='bank' for q in allq)}
    return render_template('ds/polity_subject.html',practice_totals=lambda:pt,units=units,decks=decks,pm=_pm.metrics() if decks else None,trees=_recall.trees()['counts'] if decks else None)

def _recall_page(deck_id):
    d=_recall.deck(deck_id)
    if not d:abort(404)
    cards=_recall.items(deck_id)
    if not cards:abort(404)
    ch=request.args.get('chapter') or None
    if ch and ch not in {c['chapter'] for c in cards}:abort(404)
    _open=request.args.get('open') or ''
    _back=None;bk=request.args.get('back') or ''
    if bk.startswith('trees'):
        tab=bk.split(':',1)[1] if ':' in bk else ''
        _back={'id':'','deck':'trees','en':'Timeline trees','te':'కాలక్రమ వృక్షాలు (Trees)','url':url_for('polity_unit6.recall_trees')+('#'+tab if tab in ('am','case','both','lines') else '')}
    elif ':' in bk:
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
                           open_id=_open if _open in {c['id'] for c in cards} else '',back=_back,for_=_for,
                           pyq_cards=sum(1 for c in cards if c.get('pyq_count')),om_cards=sum(1 for c in cards if c.get('omitted')))
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
    return render_template('ds/polity_recall_hub.html',decks=[d for d in _recall.all_decks() if d['count']],lang=language(),pm=_pm.metrics(),trees=_recall.trees()['counts'])
@bp.get('/recall/trees')
def recall_trees():
    t=_recall.trees();light={k:t[k] for k in ('v','nodes','themes','parts','counts')}
    import json as _j  # raw UTF-8 (tojson's \\u escapes double the Telugu bytes); '<' escaped so the script tag cannot close early
    blob=_j.dumps(light,ensure_ascii=False,separators=(',',':')).replace('<','\\u003c').replace('>','\\u003e').replace('&','\\u0026')
    return render_template('ds/polity_trees.html',light=light,blob=blob,lang=language())
@bp.get('/recall/trees/chains.json')
def recall_trees_chains():
    r=jsonify(_recall.trees()['chains']);r.headers['Cache-Control']='public, max-age=600';return r
@bp.get('/recall/<deck_id>')
def recall_deck(deck_id):return _recall_page(deck_id)
# Short chapter names for the article-card chips (number, English, Telugu).
ARTCARD_CHAPTERS={'6.1':('Nature and development','స్వభావం, పరిణామం'),'6.2':('Salient features','ముఖ్య లక్షణాలు'),
    '6.3':('Preamble','ప్రవేశిక'),'6.4':('Fundamental Rights','ప్రాథమిక హక్కులు'),'6.5':('Directive Principles','ఆదేశిక సూత్రాలు'),
    '6.6':('Fundamental Duties','ప్రాథమిక విధులు'),'6.7':('Amendment','రాజ్యాంగ సవరణ'),'6.8':('Basic structure','ప్రాథమిక స్వరూపం'),
    '6.9':('Territory and citizenship','భూభాగం, పౌరసత్వం')}
@bp.get('/unit',defaults={'n':6})
@bp.get('/unit/<int:n>')
def unit(n):
    u=unit_or_404(n);corpus=records();rows=[]
    progress={p.chapter_id:p for p in PolityUnit6Progress.query.filter_by(device_id=device_id())}
    for c in chapters(n):
        own=[q for q in corpus.values() if q['_chapter']==c['id'] and visible(q)]
        rows.append(dict(chapter=c,desc=sum(1 for x in descriptive_items() if x['chapter']==c['id']),total=len(own),mcq=sum(q['_kind']=='bank' for q in own),pyq=sum(q['_kind'] in ('pyq','primary_pyq') for q in own),unscored=sum(not q['_scored'] for q in own),completed=bool(progress.get(c['id']) and progress[c['id']].completed)))
    return render_template('ds/polity_browse.html',mode='unit',rows=rows,stats=unit6_stats(n),unit=u,unit_no=n)

@bp.get('/chapters/<chapter_id>')
def chapter(chapter_id):
    c=chapter_or_404(chapter_id)
    own=[q for q in records().values() if q['_chapter']==chapter_id and visible(q)]
    progress=db.session.get(PolityUnit6Progress,(device_id(),chapter_id))
    return render_template('ds/polity_browse.html',mode='chapter',chapter=c,unit_no=unit_of(chapter_id),has_notes=(directory(chapter_id)/'Notes.html').is_file(),desc=sum(1 for x in descriptive_items() if x['chapter']==c['id']),mcq=sum(q['_kind']=='bank' for q in own),pyq=sum(q['_kind'] in ('pyq','primary_pyq') for q in own),total=len(own),unscored=sum(not q['_scored'] for q in own),progress=progress)

EXAM_GROUPS=[('upsc','UPSC'),('g2','APPSC Group 2'),('g1','APPSC Group 1'),('tspsc','TSPSC / TGPSC'),('appsc','APPSC other'),('other','Other')]
def exam_group(exam):
    e=(exam or '').upper()
    if e.startswith('UPSC'):return 'upsc'
    if 'TSPSC' in e or 'TGPSC' in e:return 'tspsc'
    if re.match(r'APPSC GROUP[- ]?(II|2)\b',e):return 'g2'
    if re.match(r'APPSC GROUP[- ]?(I|1)\b',e):return 'g1'
    if e.startswith('APPSC'):return 'appsc'
    return 'other'
_ART=re.compile(r'\bArt(?:icle)?s?\.?\s*(\d{1,3}[A-Z]{0,2}(?:\s*\(\d+\))?(?:\s*(?:,|and|&|or)\s*\d{1,3}[A-Z]{0,2}(?:\s*\(\d+\))?)*)')
_AMD=re.compile(r'\b(\d{1,3})(?:st|nd|rd|th)\s+(?:Constitutional\s+|Constitution\s+)?\(?Amendment',re.I)
_AMD2=re.compile(r'Constitution\s*\((\d{1,3})(?:st|nd|rd|th)\s+Amendment',re.I)
_CA=re.compile(r'\b(recent(ly)?|in (the )?news|current(ly)?)\b|(?<!\()\b20(2[2-6])\b(?!\))',re.I)
@lru_cache(maxsize=1)
def _case_keys():
    out=[]
    for c in _recall.items('cases') or []:
        name=re.sub(r'\s+case$','',c.get('front_en') or '',flags=re.I).strip()
        if len(name)>=4:out.append((c['id'],name,[k for k in {name,(c.get('short_en') or '').strip()} if len(k)>=5]))
    return out
_TAGS={}
def q_tags(q):
    key=(q['id'],q.get('question_en'),tuple(q.get('options_en') or ()),q.get('exam'))
    t=_TAGS.get(key)
    if t is not None:return t
    txt=' '.join([q.get('question_en') or '']+list(q.get('options_en') or []))
    arts=set()
    for m in _ART.finditer(txt):
        for n in re.findall(r'\d{1,3}[A-Z]{0,2}',re.sub(r'\(\d+\)','',m.group(1))):
            if 1<=int(re.match(r'\d+',n).group())<=395:arts.add(n)
    amds={m.group(1) for r in (_AMD,_AMD2) for m in r.finditer(txt) if 1<=int(m.group(1))<=106}
    low=txt.casefold();cases={cid for cid,_,keys in _case_keys() if any(k.casefold() in low for k in keys)}
    stem=q.get('question_en') or ''
    t={'exam':exam_group(q.get('exam')) if q['_kind'] in ('pyq','primary_pyq') else '','art':arts,'amd':amds,'case':cases,'ca':bool(q.get('_ca') or _CA.search(stem))}
    _TAGS[key]=t;return t
def _artkey(a):m=re.match(r'(\d+)(.*)',a);return (int(m.group(1)),m.group(2))
def facet_options(qs):
    """Values (with counts) for the article / amendment / case dropdowns of a question set."""
    from collections import Counter
    a=Counter();m=Counter();c=Counter()
    for q in qs:
        t=q_tags(q);a.update(t['art']);m.update(t['amd']);c.update(t['case'])
    names={cid:n for cid,n,_ in _case_keys()}
    return {'art':[(k,'Article '+k,a[k]) for k in sorted(a,key=_artkey)],
            'amd':[(k,k+_ordinal(int(k))+' Amendment',m[k]) for k in sorted(m,key=int)],
            'case':sorted(((k,names[k],c[k]) for k in c),key=lambda x:x[1].casefold())}
def _ordinal(n):return 'th' if 10<=n%100<=20 else {1:'st',2:'nd',3:'rd'}.get(n%10,'th')
FACETS=('exam','art','amd','case','ca','cg')

def filters(default_chapter=''):
    values={k:request.args.get(k,'').strip() for k in ('chapter','kind','q','view','map','unit','cat')+FACETS}
    if values['exam'] and values['exam'] not in dict(EXAM_GROUPS):abort(404)
    if values['ca'] not in ('','1'):abort(404)
    if values['unit'] and (not values['unit'].isdigit() or int(values['unit']) not in UNITS):abort(404)
    if values['map'] and values['map'] not in catalog():abort(404)
    if not any(k in request.args for k in values):values['chapter']=default_chapter
    if any(values[k] for k in FACETS) and not any(k in request.args for k in ('chapter','unit')):values['chapter']=''
    if values['chapter']:chapter_or_404(values['chapter'])
    return values

def selection(values):
    chapter,kind,query,view=(values[k] for k in ('chapter','kind','q','view'))
    if values.get('map'):
        corpus=records();qs=[corpus[l['item_id']] for l in catalog()[values['map']]['links'] if l['item_id'] in corpus and visible(corpus[l['item_id']])]
        return list({q['id']:q for q in qs}.values())
    qs=test_records(chapter) if kind=='chaptertest' and chapter else list(records().values())
    if chapter:qs=[q for q in qs if q['_chapter']==chapter]
    elif values.get('unit'):qs=[q for q in qs if str(q['_chapter']).split('.')[0]==values['unit']]
    if kind and kind!='chaptertest':qs=[q for q in qs if q['_kind']==kind or kind=='pyq' and q['_kind']=='primary_pyq']
    if kind=='chaptertest' and not chapter:qs=[q for c in chapters() for q in test_records(c['id'])]
    if kind!='chaptertest':qs=[q for q in qs if visible(q)]
    else:qs=[q for q in qs if q.get('hold_reason')!='retired, no key']
    if values.get('exam'):qs=[q for q in qs if q_tags(q)['exam']==values['exam']]
    for k in ('art','amd','case'):
        if values.get(k):qs=[q for q in qs if values[k] in q_tags(q)[k]]
    if values.get('ca'):qs=[q for q in qs if q_tags(q)['ca']]
    if values.get('cat'):qs=[q for q in qs if q.get('ca_topic')==values['cat'] or values['cat'] in ('all','recent','earlier','apra') and q.get('_ca') and (values['cat']=='all' and q.get('ca_period') in ('recent','earlier') or q.get('ca_period')==values['cat'])]
    if values.get('cg'):qs=[q for q in qs if any(_cg.topic_of(x)==values['cg'] for x in _cg.index()['qmap'].get(q['id'],[]))]
    if query:qs=[q for q in qs if query.casefold() in (q.get('question_en','')+' '+q.get('question_te','')+' '+q['id']).casefold()]
    if view in ('saved','mistakes'):
        states=PolityUnit6State.query.filter_by(device_id=device_id()).all()
        ids={s.item_id for s in states if s.saved} if view=='saved' else {s.item_id for s in states if s.wrong_count>0}
        qs=[q for q in qs if q['id'] in ids]
    return list({q['id']:q for q in qs}.values())

def language():
    lang=request.args.get('qlang','en')
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
                    q_en=it.get('question_en') or it.get('prompt_en') or '',q_te=it.get('question_te') or it.get('prompt_te') or '',
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
    if pos is None:
        # The question left a saved/mistakes view (unbookmarked, or answered right) or is outside the
        # filter: keep Previous/Next by placing it where it sits in the unfiltered chapter order, so the
        # learner can always move on (never a dead end with only "Finish").
        base=selection({**values,'view':''}) if values.get('view') else []
        order={r['id']:i for i,r in enumerate(base)}
        if q['id'] in order:
            k=order[q['id']];before=[r for r in qs if order.get(r['id'],-1)<k];after=[r for r in qs if order.get(r['id'],-1)>k]
            qs=before+[q]+after;pos=len(before)
        else:qs=[q]+list(qs);pos=0
    lang=language();feedback=None
    if review:feedback='correct' if choice==q['_answer'] else 'incorrect'
    context={**values,'qlang':lang}
    review_args={'review':'1','choice':choice} if review and choice in (1,2,3,4) else {}
    notes=url_for('.notes',chapter_id=q['_chapter'],item_id=q['id'],**context,**review_args)
    locators=section_links(q)
    links=[dict(url=notes+'#'+l['anchor'],basis=l['basis'],title=l.get('title','')) for l in locators]
    rl=read_links().get(q['id'])
    if rl:
        if rl['src']=='lax':
            ex={'also':','.join(rl['also'])} if rl.get('also') else {}
            u=url_for('.notes',chapter_id=q['_chapter'],item_id=q['id'],src='lax',lx=rl['lx'],**context,**review_args,**ex)+'#'+rl['pid']
            links=[dict(url=u,basis='exact',title='Laxmikanth')]+[l for l in links if l['basis']=='heading'][:1]
        else:links=[dict(url=(url_for('.notes',chapter_id=q['_chapter'],item_id=q['id'],also=','.join(rl['also']),**context,**review_args) if rl.get('also') else notes)+'#'+rl['pid'],basis='exact',title='GBK notes')]+[l for l in links if l['basis']=='heading'][:1]
    has_notes=(directory(q['_chapter'])/'Notes.html').is_file()
    if not links and has_notes:links=[dict(url=notes+'#question-explanation',basis='explanation')]
    if not has_notes:notes=None
    return render_template('ds/polity_question.html',run=_run(),concept_subs=lambda i:_cg.subs_for(i),question=q,choice=choice,feedback=feedback,lang=lang,context=context,
        state=db.session.get(PolityUnit6State,(device_id(),q['id'])),position=pos+1,total=len(qs),
        previous=qs[pos-1]['id'] if pos else None,following=qs[pos+1]['id'] if pos+1<len(qs) else None,
        notes_url=notes,section_links=links,review_args=review_args)

from functools import lru_cache
@lru_cache(maxsize=1)
def read_links():
    f=CONTENT/'_shared'/'Read-Links.json'
    if not f.is_file():return {}
    import json as _j;return _j.loads(f.read_text(encoding='utf-8')).get('links',{})
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
from app.services import para_anchors as _pa
LAX_DIR=CONTENT/'references'/'laxmikanth'
LAX_CSS='''<style>body{background:#f4f6f8!important;font-size:16px!important;overflow-wrap:anywhere}.page{width:auto!important;max-width:900px!important;min-height:0!important;margin:0 auto!important;padding:14px 14px 30px!important;box-shadow:none!important;background:#fff!important}body>nav[style]{display:none!important}img,svg{max-width:100%;height:auto}table{display:block;max-width:100%;overflow-x:auto;-webkit-overflow-scrolling:touch}h1{font-size:1.35rem!important;line-height:1.4}.ptitle{display:block!important}@media(max-width:640px){body{font-size:15.5px!important}.page{padding:10px 10px 26px!important}[style*="columns"],[style*="column-count"]{column-count:1!important;columns:1!important}td,th{min-width:84px}ul{margin-left:16px!important}}</style>'''
@bp.get('/chapters/<chapter_id>/notes')
def notes(chapter_id):
    chapter_or_404(chapter_id)
    if not (directory(chapter_id)/'Notes.html').is_file():abort(404)
    item_id=request.args.get('item_id');q=records().get(item_id) if item_id else None
    if item_id and (not q or q['_chapter']!=chapter_id):abort(404)
    c=chapter_or_404(chapter_id)
    lax=[l for l in (c.get('laxmikanth') or []) if (LAX_DIR/f"chapter-{int(l['chapter']):03d}.html").is_file()]
    lx=request.args.get('lx',type=int)
    if not lax and q and lx and (LAX_DIR/f"chapter-{lx:03d}.html").is_file():lax=[dict(chapter=lx,title='')]
    src='lax' if request.args.get('src')=='lax' and lax else 'gbk'
    if src=='lax':
        if lx not in [l['chapter'] for l in lax]:
            if lx and (LAX_DIR/f"chapter-{lx:03d}.html").is_file() and q:lax=lax+[dict(chapter=lx,title='')]
            else:lx=lax[0]['chapter']
        content=(LAX_DIR/f"chapter-{lx:03d}.html").read_text(encoding='utf-8-sig')
        content=_re.sub(r'</head>',lambda m:LAX_CSS+m.group(0),content,count=1,flags=_re.I)
        content=_pa.add_ids(content,'lp')
    else:content=_pa.add_ids(numbered_notes(chapter_id),'gp')
    content=_pa.decorate(content)
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
    ids=[c['id'] for c in chapters(unit_of(chapter_id))];nxt=ids[ids.index(chapter_id)+1] if ids.index(chapter_id)+1<len(ids) else None
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
    if request.args.get('fresh')=='1':
        _run_reset();args={k:v for k,v in request.args.items() if k!='fresh'}
        return redirect(url_for('.practice',item_id=item_id,**args))
    choice=request.args.get('choice',type=int)
    _remember_last(item_id)
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
    _run_record(q['id'],feedback=='correct');_remember_last(q['id'])
    # Post/Redirect/Get: the result is shown on a GET page, so going to the notes and pressing
    # Back (or refreshing) never asks the browser to resubmit a form.
    args={**filters(q['_chapter']),'qlang':language(),'review':'1','choice':selected}
    return redirect(url_for('.practice',item_id=item_id,**args)+'#answer-result')

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
    un=request.form.get('unit','')
    qs=test_records(cid) if chapter_mode and cid else [q for q in records().values() if visible(q) and (not cid or q['_chapter']==cid) and (cid or not un or str(q['_chapter']).split('.')[0]==un)]
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
    return render_template('ds/polity_unit6.html',mode='exam',exam=e,lang=language(),seconds=max(0,int((e.deadline-now).total_seconds())))

@bp.post('/tests/<exam_id>/save')
def save_exam_answer(exam_id):
    e=PolityUnit6Exam.query.filter_by(id=exam_id,device_id=device_id()).with_for_update().first_or_404()
    if e.submitted_at or datetime.utcnow()>=e.deadline:abort(409)
    item_id=request.form.get('item_id');answer=request.form.get('answer',type=int)
    if item_id not in {q['id'] for q in e.questions} or answer not in (1,2,3,4):abort(400)
    e.answers={**(e.answers or {}),item_id:answer};db.session.commit()
    return {'saved':True}


def _hub_values():
    v={k:request.args.get(k,'').strip() for k in ('kind','chapter')+FACETS}
    v['cat']=request.args.get('cat','').strip()
    if v['cat'] not in ('','all','recent','earlier','apra'):v['cat']=''
    if v['cat'] and v['kind']=='pyq':v['cat']=''
    if v['kind'] not in ('','bank','pyq'):abort(404)
    if v['exam'] and v['exam'] not in dict(EXAM_GROUPS):abort(404)
    if v['chapter']:chapter_or_404(v['chapter'])
    if v['kind']=='bank':
        for k in FACETS:
            if k!='cg':v[k]=''
    if v['kind']=='':v['exam']=''
    if v['cg'] and v['cg'] not in _cg.index()['by_id']:abort(404)
    return v
def _hub_select(v):return selection({'q':'','view':'','map':'','unit':'',**v})
@bp.get('/practice')
def practice_hub():
    v=_hub_values();qs=_hub_select(v)
    base=_hub_select({**v,'chapter':''});fbase=_hub_select({**v,'art':'','amd':'','case':'','ca':''})
    allq=[q for q in records().values() if visible(q)]
    ex={g:sum(1 for q in allq if q['_kind']!='bank' and q_tags(q)['exam']==g) for g,_ in EXAM_GROUPS}
    chs=[(c,sum(1 for q in base if q['_chapter']==c['id'])) for c in chapters()]
    lang=language()
    start=url_for('.practice',item_id=qs[0]['id'],qlang=lang,**{k:x for k,x in v.items() if x}) if qs else None
    return render_template('ds/polity_practice_hub.html',v=v,count=len(qs),start=start,groups=EXAM_GROUPS,exam_counts=ex,
        chapters=[c for c in chs if c[1]],facets=facet_options(fbase),
        totals={'bank':sum(q['_kind']=='bank' for q in allq),'pyq':sum(q['_kind']!='bank' for q in allq)},ca_counts={p:sum(1 for q in allq if q.get('_ca') and (p=='all' and q.get('ca_period') in ('recent','earlier') or q.get('ca_period')==p)) for p in ('all','recent','earlier','apra')},
        list_url=url_for('.library',**{k:x for k,x in v.items() if x}),resume=_resume_for(v,qs,lang),**_wrong_entry(lang))
def _concept_url(ref,**kw):
    t,sub=_cg.link_target(ref)
    if not t:return None
    return url_for('.concept_card',tid=t,**({'sub':sub} if sub else {}),**kw)+('#'+sub if sub else '')
def _concept_qcount():
    vis={q['id'] for q in records().values() if visible(q)};c={}
    for qid,lst in _cg.index()['qmap'].items():
        if qid in vis:
            for t in {_cg.topic_of(x) for x in lst}:
                if t:c[t]=c.get(t,0)+1
    return c
@bp.get('/concepts')
def concepts_hub():
    ts=[t for t in _cg.topics() if _cg.topic(t['id'])]
    return render_template('ds/polity_concepts.html',topics=ts,counts=_concept_qcount())
@bp.get('/concepts/<tid>')
def concept_card(tid):
    t=_cg.topic(tid) or abort(404)
    sub=request.args.get('sub','')
    ids=[s['id'] for s in t['subcards']]
    open_sub=sub if sub in ids else (ids[0] if ids else '')
    back=request.args.get('back','');back_url=back if back.startswith('/learn/polity/') else None
    n=_concept_qcount().get(tid,0)
    return render_template('ds/polity_concept_card.html',ca_for_concept=ca_for_concept,pilot=request.args.get('plain')!='1',t=t,n=n,open_sub=open_sub,back_url=back_url,
        practice_url=url_for('.practice_hub',kind='',cg=tid),xl=_xl,link_url=_concept_url)

@bp.get('/pick.json')
def pick():
    """Section chooser for MCQ/PYQ practice: 'All' for the unit plus one entry per chapter, each with a start link."""
    from flask import jsonify
    kind=request.args.get('kind','bank')
    if kind not in ('bank','pyq'):abort(400)
    n=request.args.get('unit',type=int)
    if n not in UNITS:abort(404)
    lang=request.args.get('qlang','en') if request.args.get('qlang') in ('te','en','both') else 'en'
    def entry(label,vals):
        qs=selection({'chapter':'','kind':kind,'q':'','view':'','map':'','unit':'',**vals})
        return dict(label=label,count=len(qs),url=url_for('.practice',item_id=qs[0]['id'],qlang=lang,kind=kind,**vals) if qs else None)
    items=[entry('All of Unit %d'%n,{'unit':str(n)})]
    for c in chapters(n):
        items.append(entry(c['id']+'  '+c['title'],{'chapter':c['id']}))
    return jsonify(kind=kind,unit=n,items=[i for i in items if i['count']],
                   list_url=url_for('.library',kind=kind,unit=n,qlang=lang))

# ---- Topic-wise revision list: every PYQ/MCQ in Laxmikanth chapter order, answers hidden until tapped ----
@lru_cache(maxsize=1)
def _revise_order():
    f=CONTENT/'revise'/'order.json'
    if not f.is_file():return []
    import json as _j;return _j.loads(f.read_text(encoding='utf-8'))['chapters']
_REV_KINDS={'pyq':'PYQs','bank':'MCQs','both':'PYQs + MCQs'}
def _rev_kind():
    k=request.args.get('kind','pyq');return k if k in _REV_KINDS else 'pyq'
def _rev_match(q,kind):return q is not None and visible(q) and (kind=='both' or (q['_kind']=='bank')==(kind=='bank'))
def _rev_chapters(kind):
    recs=records();out=[];n=0
    for c in _revise_order():
        groups=[]
        for g in c['groups']:
            ids=[i for i in g['ids'] if _rev_match(recs.get(i),kind)]
            if ids:groups.append({**g,'ids':ids})
        cnt=sum(len(g['ids']) for g in groups)
        if cnt:out.append({**c,'groups':groups,'count':cnt,'start':n+1});n+=cnt
    return out,n
@bp.get('/revise')
def revise():
    kind=_rev_kind();lang=language();chs,total=_rev_chapters(kind)
    return render_template('ds/polity_revise.html',kind=kind,kinds=_REV_KINDS,lang=lang,chapters=chs,total=total,
        open_ch=request.args.get('ch',''))
@bp.get('/revise/part')
def revise_part():
    kind=_rev_kind();lang=language();chs,_=_rev_chapters(kind)
    c=next((x for x in chs if x['key']==request.args.get('ch')),None) or abort(404)
    recs=records();back=url_for('.revise',kind=kind,qlang=lang,ch=c['key'])
    return render_template('ds/polity_revise_part.html',c=c,recs=recs,lang=lang,kind=kind,back=back)
_RV_ASK=re.compile(r'\b(which|who|whom|when|what|name|in which|under which)\b',re.I)
_RV_THING=re.compile(r'\b(articles?|case|cases|act|enactment|amendment|year|committee|commission|provision|schedule|part|person|court|body|state|chair\w*|first|president|minister|judge|session|list|entry|writ|doctrine|report|day|date|number|how many|minimum|maximum|age|term|tenure|founder|known as|called|term used)\b',re.I)
_RV_NEED=re.compile(r'following|statement|match|list[- ]?i\b|assertion|reason|\bnot\b|incorrect|correct|\btrue\b|false|pairs?\b|arrange|chronolog|\bcodes?\b|best|propos|follows?\b|most (accurate|appropriate|likely|valid)|consider|except|odd one|wrong|valid|invalid|implication|outcome|result|effect|reflects|accurately|describes|options?\b',re.I)
@bp.app_template_global('rv_direct')
def rv_direct(q):
    """True when a question can be asked without its options (pure recall, e.g. 'Which Article…?')."""
    st=q.get('question_en') or ''
    if len(st)>220 or '\n' in st.strip() or _RV_NEED.search(st):return False
    return bool(_RV_ASK.search(st) and (_RV_THING.search(st) or len(st)<140))
@lru_cache(maxsize=1)
def _cell_layout():
    f=CONTENT/'concepts'/'layout.json'
    if not f.is_file():return {}
    import json as _j;return _j.loads(f.read_text(encoding='utf-8'))
@bp.app_template_global('cell_parts')
def cell_parts(text):
    """Hand-checked layout for a dense table cell (lead + points); same words, only shown as bullets."""
    v=_cell_layout().get(str(text or '').strip())
    if not v:return None
    return {'lead':v.get('lead',''),'items':[i if isinstance(i,dict) else {'text':i} for i in v.get('items',[])]}
def _book_chapters():
    subs={s['id']:(t['id'],s) for t in [_cg.topic(x['id']) for x in _cg.topics()] if t for s in t['subcards']}
    from ..routes.polity_unit6 import _revise_order as _ro
    import json as _j
    # chapter -> sub-cards, in the Laxmikanth order used by the revision list (includes cards with no questions)
    out=[]
    for c in _ro():
        ids=list(dict.fromkeys(g['sub'] for g in c['groups'] if g['sub'] in subs))
        if ids:out.append({**c,'subs':[subs[i] for i in ids]})
    return out
@bp.get('/facts')
def quick_facts():
    """Concept book: every concept card, chapter by chapter in Laxmikanth order, in one scroll (cards themselves unchanged)."""
    chs=_book_chapters()
    return render_template('ds/polity_facts.html',chapters=chs,nsubs=sum(len(c['subs']) for c in chs))
@bp.get('/facts/part')
def quick_facts_part():
    sid=request.args.get('sub','')
    hit=[ts for c in _book_chapters() for ts in c['subs'] if ts[1]['id']==sid] or abort(404)
    return render_template('ds/polity_facts_part.html',subs=hit[:1],xl=_xl,link_url=_concept_url,pilot=True)


# ---- Practice score: marks for the current practice run (kept in the browser session) ----
def _run():
    r=session.get('u6run') or {}
    return {'n':r.get('n',0),'ok':r.get('ok',0),'wrong':r.get('wrong',[]),'seen':r.get('seen',[])}
def _run_reset():session['u6run']={'n':0,'ok':0,'wrong':[],'seen':[]}
def _run_record(item_id,correct):
    r=_run()
    if item_id in r['seen']:return            # first attempt only counts for marks
    r['seen']=(r['seen']+[item_id])[-150:];r['n']+=1
    if correct:r['ok']+=1
    else:r['wrong']=(r['wrong']+[item_id])[-100:]
    session['u6run']=r
@bp.get('/practice/result')
def practice_result():
    r=_run();lang=language();recs=records()
    wrong=[recs[i] for i in r['wrong'] if i in recs]
    pending={s.item_id for s in PolityUnit6State.query.filter_by(device_id=device_id()).all() if s.wrong_count>0}
    allwrong=[q for q in recs.values() if q['id'] in pending and visible(q)]
    return render_template('ds/polity_result.html',run=r,wrong=wrong,lang=lang,total_wrong=len(allwrong),
        retry=url_for('.practice',item_id=allwrong[0]['id'],view='mistakes',chapter='',qlang=lang,fresh='1') if allwrong else None)
def _wrong_entry(lang):
    ids={s.item_id for s in PolityUnit6State.query.filter_by(device_id=device_id()).all() if s.wrong_count>0}
    qs=[q for q in records().values() if q['id'] in ids and visible(q)]
    return {'wrong_n':len(qs),'wrong_start':url_for('.practice',item_id=qs[0]['id'],view='mistakes',chapter='',qlang=lang,fresh='1') if qs else None}
@bp.get('/practice-start')
def practice_start():
    """Indian Polity from the Practice tab: practise, or practise only my wrong answers."""
    lang=language()
    return render_template('ds/polity_practice_start.html',lang=lang,**_wrong_entry(lang))

# ---- Resume: remember the last question opened for each practice selection ----
def _sel_sig(args):
    return '&'.join(f'{k}={args.get(k)}' for k in ('kind','chapter')+tuple(FACETS) if args.get(k))
def _remember_last(item_id):
    if request.args.get('view') or request.args.get('review')=='1':return
    d=dict(session.get('u6last') or {});sig=_sel_sig(request.args)
    d.pop(sig,None);d[sig]=item_id
    while len(d)>25:d.pop(next(iter(d)))
    session['u6last']=d
def _resume_for(v,qs,lang):
    item=(session.get('u6last') or {}).get(_sel_sig(v))
    pos=next((i for i,q in enumerate(qs) if q['id']==item),None)
    if pos is None or pos==0:return None
    return {'pos':pos+1,'url':url_for('.practice',item_id=item,qlang=lang,**{k:x for k,x in v.items() if x})}

# ---- Current affairs (Indian & AP polity, Nov 2025 – Nov 2026): notes + MCQs ----
CA_SECTIONS=[('P','Parliament & Constitution amendments','పార్లమెంట్ & రాజ్యాంగ సవరణలు'),('J','Judiciary','న్యాయవ్యవస్థ'),('E','Elections','ఎన్నికలు'),('X','Executive & constitutional bodies','కార్యనిర్వాహక వర్గం & రాజ్యాంగ సంస్థలు'),('F','Federalism & rights','సమాఖ్య విధానం & హక్కులు'),('L','Local government & governance','స్థానిక ప్రభుత్వాలు & పాలన'),('A','Andhra Pradesh polity','ఆంధ్రప్రదేశ్ రాజకీయ వ్యవస్థ'),('R','Reports, indices & days','నివేదికలు, సూచీలు & దినోత్సవాలు'),('Z','AP Reorganisation Act, 2014','ఏపీ పునర్వ్యవస్థీకరణ చట్టం, 2014')]
@lru_cache(maxsize=1)
def ca_data():
    f=CONTENT/'current-affairs'/'topics.json'
    if not f.is_file():return {'topics':[],'asof':''}
    import json as _j;return _j.loads(f.read_text(encoding='utf-8'))
def ca_for_concept(sub_id):
    return [t for t in ca_data()['topics'] if sub_id in (t.get('concepts') or [])]
def _ca_first(cat,lang):
    qs=[q for q in records().values() if visible(q) and q.get('_ca') and (cat=='all' and q.get('ca_period') in ('recent','earlier') or q.get('ca_topic')==cat or q.get('ca_period')==cat)]
    return url_for('.practice',item_id=qs[0]['id'],cat=cat,chapter='',qlang=lang,fresh='1') if qs else None
@bp.get('/current-affairs')
def ca_home():
    lang=language();d=ca_data()
    periods=[('recent','Last 12 months','Nov 2025 – Nov 2026'),('earlier','2024 – 2025','Jun 2024 – Oct 2025')]
    have=[p for p in periods if any(t.get('period','recent')==p[0] for t in d['topics'])]
    per=request.args.get('p','recent')
    if per not in [p[0] for p in have]:per=have[0][0] if have else 'recent'
    ts=[t for t in d['topics'] if t.get('period','recent')==per]
    groups=[(k,en,te,[t for t in ts if t.get('section')==k]) for k,en,te in CA_SECTIONS]
    n=sum(len(t.get('mcqs',[])) for t in ts)
    return render_template('ds/polity_ca.html',groups=[g for g in groups if g[3]],lang=lang,periods=have,per=per,
        span=dict((p[0],p[2]) for p in periods)[per],ntopics=len(ts),nmcq=n,start_all=_ca_first(per,lang))
WHO_TABS=[('persons','Persons','వ్యక్తులు'),('days','Days','దినోత్సవాలు'),('books','Books & writers','పుస్తకాలు & రచయితలు'),('quotes','Quotes','సూక్తులు'),('present','Present office holders','ప్రస్తుత పదవుల్లో ఉన్నవారు'),('places','States, UTs & places','రాష్ట్రాలు, UTలు & ప్రదేశాలు'),('dates','Landmark dates','ముఖ్య తేదీలు'),('numbers','Numbers to remember','గుర్తుంచుకోవలసిన సంఖ్యలు'),('records','Highest, longest, first','అత్యధికం, సుదీర్ఘం, మొదటి'),('symbols','Symbols & languages','చిహ్నాలు & భాషలు'),('parties','Parties & alliances','పార్టీలు & కూటములు'),('quickmap','Quick map: Articles, Parts, cases','త్వరిత పటం: ప్రకరణలు, భాగాలు, కేసులు'),('lists','All office holders since 1950','1950 నుంచి పదవి చేపట్టినవారు')]
@lru_cache(maxsize=1)
def who_data():
    d={k:[] for k,_,_ in WHO_TABS};asof={}
    folder=CONTENT/'whoswho'
    if folder.exists():
        for f in sorted(folder.glob('*.json')):
            j=read(f);t=j.get('tab')
            if t in d:d[t]+=j.get('groups',[]);asof[t]=j.get('asof','')
    return d,asof
@bp.get('/whos-who')
def whos_who():
    lang=language();d,asof=who_data()
    tab=request.args.get('t','persons')
    if tab not in d:tab='persons'
    tabs=[(k,en,te,sum(len(g.get('items',[])) for g in d[k])) for k,en,te in WHO_TABS if d[k]]
    sets=[(t['id'],t['title_te'] if lang=='te' and t.get('title_te') else t['title_en'],len(t.get('mcqs',[])),_ca_first(t['id'],lang)) for t in ca_data()['topics'] if t.get('period')=='who' and t.get('wtab')==tab]
    return render_template('ds/polity_who.html',tabs=tabs,tab=tab,groups=d[tab],asof=asof.get(tab,''),lang=lang,sets=sets)
@bp.get('/ap-reorganisation-act')
def ap_reorg():
    lang=language();ts=[t for t in ca_data()['topics'] if t.get('period')=='apra']
    if not ts:abort(404)
    n=sum(len(t.get('mcqs',[])) for t in ts);npyq=sum(1 for t in ts for m in t.get('mcqs',[]) if m.get('pyq'))
    return render_template('ds/polity_ca.html',groups=[('Z','AP Reorganisation Act, 2014','ఏపీ పునర్వ్యవస్థీకరణ చట్టం, 2014',ts)],lang=lang,periods=[],per='apra',
        span=f'{npyq} PYQs included',ntopics=len(ts),nmcq=n,start_all=_ca_first('apra',lang),apra=True)
@bp.get('/current-affairs/<tid>')
def ca_topic(tid):
    lang=language();t=next((x for x in ca_data()['topics'] if x['id']==tid),None) or abort(404)
    subs={s['id']:(tp['id'],s['title']) for tp in [_cg.topic(x['id']) for x in _cg.topics()] if tp for s in tp['subcards']}
    links=[(subs[c][1],url_for('.concept_card',tid=subs[c][0],sub=c)+'#'+c) for c in t.get('concepts',[]) if c in subs]
    order=[x['id'] for x in ca_data()['topics'] if x.get('period','recent')==t.get('period','recent')];i=order.index(tid)
    return render_template('ds/polity_ca_topic.html',t=t,lang=lang,links=links,start=_ca_first(tid,lang),
        prev=order[i-1] if i else None,next=order[i+1] if i+1<len(order) else None,sections={k:(en,te) for k,en,te in CA_SECTIONS})
@bp.app_template_filter('ca_title')
def _ca_title(tid):
    t=next((x for x in ca_data()['topics'] if x['id']==tid),None)
    return t['title_en'] if t else ''
