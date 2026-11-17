"""Group 2 Geography (lessons 1-34): same question design as Polity (explain panel, option table,
named notes links, bookmark, running score, swipe navigation)."""
import html
import re
from datetime import datetime
from functools import lru_cache
from flask import abort, make_response, redirect, render_template, request, session, url_for
from .geography import bp
from ..db import db
from ..services import geo_g2 as g2
from ..services.device import device_id

LANGS=('te','en','both')

@bp.get('/g2')
def g2_index():
    return render_template('ds/g2_geography.html',data=g2.index())

@bp.get('/g2/<int:number>')
def g2_chapter(number):
    ch=g2.chapter(number) or abort(404)
    return render_template('ds/g2_chapter.html',ch=ch)

@bp.get('/g2/<int:number>/notes')
def g2_notes(number):
    g2.chapter(number) or abort(404);path=g2.notes_path(number)
    if not path.is_file():abort(404)
    page=path.read_text(encoding='utf-8-sig')
    back=url_for('geography.g2_chapter',number=number)
    q=request.args.get('question')
    toolbar='<nav class="u6-reader-nav" aria-label="Return to practice"><a href="'+html.escape(back,quote=True)+'">‹ పాఠం · Lesson</a>'
    if q:
        ret=url_for('geography.g2_question',number=number,qid=q,qlang=request.args.get('qlang','te'),**({'review':'1','choice':request.args['choice']} if request.args.get('review') else {}))
        toolbar+='<a data-return-question href="'+html.escape(ret,quote=True)+'#answer-result">Back to question / ప్రశ్నకు తిరిగి వెళ్ళండి →</a>'
    toolbar+='</nav>'
    css=('<style>.u6-reader-nav{position:sticky;top:0;z-index:10000;display:flex;flex-wrap:wrap;gap:12px;justify-content:space-between;align-items:center;'
         'padding:12px;background:#fff;border-bottom:1px solid #dce5df;font:600 16px/1.6 system-ui,sans-serif}.u6-reader-nav a{color:#195f52;padding:6px;text-decoration:underline}'
         'html{scroll-padding-top:110px}body [id]{scroll-margin-top:110px}:target{background:#fff8e1;box-shadow:0 0 0 4px #ffe082;border-radius:6px}</style>')
    page=page.replace('</head>',css+'</head>',1).replace('<body>','<body>'+toolbar,1)
    r=make_response(page);r.headers['Content-Type']='text/html; charset=utf-8';return r

@bp.get('/g2/<int:number>/practice')
def g2_practice(number):
    ch=g2.chapter(number) or abort(404);rows=g2.questions(number)
    from ..polity_models import PolityUnit6State
    ids={q['id'] for q in rows};saved=wrong=[];seen=0
    try:
        st=[s for s in PolityUnit6State.query.filter_by(device_id=device_id()).all() if s.item_id in ids]
        order={q['id']:i for i,q in enumerate(rows)}
        saved=sorted((s.item_id for s in st if s.saved),key=order.get);wrong=sorted((s.item_id for s in st if s.wrong_count),key=order.get);seen=sum(1 for s in st if s.seen_count)
    except Exception:db.session.rollback()
    nxt=next((q['id'] for q in rows if q['id'] not in set(_run(number)['seen'])),rows[0]['id'] if rows else None)
    byid={q['id']:q for q in rows}
    return render_template('ds/g2_practice.html',number=number,ch=ch,questions=rows,saved=[byid[i] for i in saved],wrong=[byid[i] for i in wrong],seen=seen,next_id=nxt,run=_run(number))

@lru_cache(maxsize=40)
def _section_titles(number):
    """Heading text for every section id in the lesson notes (for named 'read notes' links)."""
    p=g2.notes_path(number)
    if not p.is_file():return {}
    out={}
    for m in re.finditer(r'<h([1-4])\b[^>]*\bid="([^"]+)"[^>]*>(.*?)</h\1>',p.read_text(encoding='utf-8-sig'),re.S):
        t=re.sub(r'\s+',' ',html.unescape(re.sub(r'<[^>]+>','',m.group(3)))).strip()
        out[m.group(2)]=t
    return out

def _view(q):
    """Question in the shape the shared Polity explain panel expects."""
    v=dict(q);a=q['answer'];v['_answer']=a
    v['_te']=q.get('explanation_te') or '';v['_en']=q.get('explanation_en') or ''
    for lang,lbl in (('te',('ఎంపిక','ఎందుకు','సరైనదా?')),('en',('Option','Why','Correct?'))):
        why=q.get('option_explanations_'+lang) or [];opts=q.get('options_'+lang) or []
        if len(why)==len(opts)==4 and any(why):
            v['explain_table_'+lang if lang=='te' else 'explain_table']=dict(head=list(lbl),rows=[[f'{i+1}. {opts[i]}',why[i],'✓' if i+1==a else '✗'] for i in range(4)])
    v['_is_pyq']='PYQ' in q['id'] or 'pyq' in (q.get('kind') or '')
    return v

def _state(item):
    from ..polity_models import PolityUnit6State
    key=(device_id(),item);s=db.session.get(PolityUnit6State,key)
    if s is None:s=PolityUnit6State(device_id=key[0],item_id=item,saved=False,seen_count=0,wrong_count=0);db.session.add(s)
    return s

def _run(number):
    r=(session.get('g2run') or {}).get(str(number)) or {}
    return {'n':r.get('n',0),'ok':r.get('ok',0),'wrong':r.get('wrong',[]),'seen':r.get('seen',[])}
def _run_record(number,qid,correct):
    r=_run(number)
    if qid in r['seen']:return
    r['seen']=(r['seen']+[qid])[-400:];r['n']+=1
    if correct:r['ok']+=1
    else:r['wrong']=(r['wrong']+[qid])[-300:]
    allr=dict(session.get('g2run') or {});allr[str(number)]=r;session['g2run']=allr

def _lang():
    lang=request.args.get('qlang','te')
    if lang not in LANGS:abort(400)
    return lang

@bp.get('/g2/<int:number>/practice/<qid>')
def g2_question(number,qid):
    ch=g2.chapter(number) or abort(404);rows=g2.questions(number)
    q=g2.question(number,qid) or abort(404);pos=next(i for i,x in enumerate(rows) if x['id']==qid)
    lang=_lang();choice=feedback=None
    if request.args.get('review')=='1':
        raw=request.args.get('choice','')
        if raw not in ('1','2','3','4'):abort(400)
        choice=int(raw);feedback='correct' if choice==q['answer'] else 'incorrect'
    na={'question':qid,'qlang':lang}
    if feedback:na.update({'review':'1','choice':choice})
    notes_url=url_for('geography.g2_notes',number=number,**na)
    title=_section_titles(number).get(q['section'])
    from ..polity_models import PolityUnit6State
    try:state=db.session.get(PolityUnit6State,(device_id(),qid))
    except Exception:db.session.rollback();state=None
    return render_template('ds/g2_question.html',number=number,ch=ch,q=_view(q),lang=lang,choice=choice,feedback=feedback,
        position=pos+1,total=len(rows),previous=rows[pos-1]['id'] if pos else None,following=rows[pos+1]['id'] if pos+1<len(rows) else None,
        notes_url=notes_url,section_url=notes_url+'#'+q['section'],section_title=title,state=state,run=_run(number),
        images=g2.question_images(number,qid) if feedback else [])

@bp.post('/g2/<int:number>/practice/<qid>/answer')
def g2_answer(number,qid):
    g2.chapter(number) or abort(404);q=g2.question(number,qid) or abort(404);lang=_lang()
    state=_state(qid)
    if request.form.get('action')=='bookmark':
        state.saved=not state.saved;db.session.commit()
        args={'qlang':lang}
        if request.args.get('review')=='1' and request.args.get('choice') in ('1','2','3','4'):args.update(review='1',choice=request.args['choice'])
        return redirect(url_for('geography.g2_question',number=number,qid=qid,**args))
    raw=request.form.get('answer') or request.form.get('choice') or ''
    if raw not in ('1','2','3','4'):abort(400)
    choice=int(raw);correct=choice==q['answer']
    state.seen_count+=1;state.last_seen_at=datetime.utcnow();state.wrong_count=0 if correct else state.wrong_count+1
    db.session.commit();_run_record(number,qid,correct)
    # Post/Redirect/Get, as in Polity: refresh or Back never resubmits.
    return redirect(url_for('geography.g2_question',number=number,qid=qid,qlang=lang,review='1',choice=choice)+'#answer-result')

@bp.get('/g2/<int:number>/result')
def g2_result(number):
    ch=g2.chapter(number) or abort(404);r=_run(number);lang=_lang()
    wrong=[g2.question(number,i) for i in r['wrong']];wrong=[w for w in wrong if w]
    if request.args.get('reset')=='1':
        allr=dict(session.get('g2run') or {});allr.pop(str(number),None);session['g2run']=allr
        return redirect(url_for('geography.g2_practice',number=number))
    return render_template('ds/g2_result.html',number=number,ch=ch,run=r,wrong=wrong,lang=lang)
