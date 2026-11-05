import html
from flask import abort, make_response, render_template, request, url_for
from .geography import bp
from ..services import geo_g2 as g2

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
    q=request.args.get('question');toolbar='<nav class="geo-note-return"><a href="'+html.escape(back,quote=True)+'">‹ పాఠం · Lesson</a>'
    if q:
        ret=url_for('geography.g2_question',number=number,qid=q,qlang=request.args.get('qlang','te'),**({'review':'1','choice':request.args['choice']} if request.args.get('review') else {}))
        toolbar+='<a href="'+html.escape(ret,quote=True)+'#answer-result">‹ ప్రశ్నకు తిరిగి · Back to question</a>'
    toolbar+='</nav>'
    css='<style>.geo-note-return{position:sticky;top:0;z-index:30;background:#fff;border-bottom:1px solid #dbe5dc;display:flex;justify-content:space-between;gap:16px;padding:12px 18px;font:600 15px/1.5 system-ui}[id]{scroll-margin-top:90px}</style>'
    page=page.replace('</head>',css+'</head>',1).replace('<body>','<body>'+toolbar,1)
    r=make_response(page);r.headers['Content-Type']='text/html; charset=utf-8';return r

@bp.get('/g2/<int:number>/practice')
def g2_practice(number):
    ch=g2.chapter(number) or abort(404);rows=g2.questions(number)
    return render_template('ds/g2_practice.html',number=number,ch=ch,questions=rows)

def _g2_question(number,qid,answered=False):
    ch=g2.chapter(number) or abort(404);rows=g2.questions(number)
    q=g2.question(number,qid) or abort(404);pos=next(i for i,x in enumerate(rows) if x['id']==qid)
    lang=request.args.get('qlang','te')
    if lang not in ('te','en'):abort(400)
    choice=result=None
    if answered or request.args.get('review')=='1':
        raw=request.form.get('choice','') if answered else request.args.get('choice','')
        if raw not in ('1','2','3','4'):abort(400)
        choice=int(raw);result={'correct':choice==q['answer']}
    na={'question':qid,'qlang':lang}
    if result:na.update({'review':'1','choice':choice})
    notes_url=url_for('geography.g2_notes',number=number,**na)
    return render_template('ds/g2_question.html',number=number,ch=ch,q=q,lang=lang,options=q['options_'+lang],explanation=q['explanation_'+lang],option_explanations=q['option_explanations_'+lang],result=result,choice=choice,position=pos+1,total=len(rows),previous=rows[pos-1]['id'] if pos else None,following=rows[pos+1]['id'] if pos+1<len(rows) else None,notes_url=notes_url,section_url=notes_url+'#'+q['section'])

@bp.get('/g2/<int:number>/practice/<qid>')
def g2_question(number,qid):return _g2_question(number,qid)

@bp.post('/g2/<int:number>/practice/<qid>/answer')
def g2_answer(number,qid):return _g2_question(number,qid,True)
