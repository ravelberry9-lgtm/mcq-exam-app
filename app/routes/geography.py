"""Geography textbook, filtered PYQ practice and contextual chapter reader."""
import html
import json
import re
from pathlib import Path
from urllib.parse import urlsplit, unquote
from flask import Blueprint, abort, current_app, make_response, redirect, render_template, request, url_for, send_file
from ..services import geography_pyqs as pyqs
from ..services import geography_book_pyqs as book_pyqs
from ..services import solar_practice as solar
from ..services import geography_original as original
from ..services import solar_bilingual as bilingual
from ..services import chapter01_bilingual as maps_bilingual
from ..services import world_geography as world

bp = Blueprint("geography", __name__, url_prefix="/learn/geography")


def _question_language():
    value=request.args.get('qlang','').strip()
    if value not in ('','te','en'):abort(400,'Choose Telugu or English')
    return value


def _bilingual_page(q,filters,result,choice,position,total,previous,following,mode,chapter_url,related_urls=(),record=None):
    lang=filters.get('qlang','te');historical=record is not None
    cid=q.get('chapter','03')
    catalogue=maps_bilingual.payload(cid) if mode=='original' and cid in ('01','02') else None
    if catalogue:
        entry=catalogue['questions'][q['id']]
    elif mode=='original' and q.get('options_en') and q.get('options_te'):
        entry={'section':q['section'],'held':False,'variants':{
            'te':{'question':q['question_te'],'options':q['options_te'],'explanation':q['explanation_te'],
                  'option_explanations':q.get('option_explanations_te',q['option_explanations']),
                  'heading':q.get('heading','పాఠంలోని సంబంధిత అంశం'),'chapter_excerpt':q['source_paragraph']},
            'en':{'question':q['question_en'],'options':q['options_en'],'explanation':q['explanation_en'],
                  'option_explanations':q.get('option_explanations_en',[q['explanation_en']]*4),
                  'heading':f"Printed page {q.get('source_page','')} · Landform concept",
                  'chapter_excerpt':q['explanation_en']}}}
    else:
        entry=bilingual.payload()['historical' if historical else 'original'][q['id']]
    t=entry['variants'][lang]
    endpoint={'original':'geography.original_question','solar':'geography.solar_question','historical':'geography.pyq'}[mode]
    answer_endpoint={'original':'geography.original_answer','solar':'geography.solar_answer','historical':'geography.pyq_answer'}[mode]
    args={'chapter_id':cid} if mode=='original' else {}
    def target(qid,extra=None):return url_for(endpoint,question_id=qid,**args,**(extra if extra is not None else filters))
    review={'review':'1',**({'choice':str(choice)} if choice else {})} if result else {}
    switches={language:target(q['id'],{**filters,**review,'qlang':language})+('#answer-result' if result else '') for language in ('te','en')}
    filter_url=url_for('geography.original_index',chapter=cid,**filters) if mode=='original' else url_for('geography.solar_index' if mode=='solar' else 'geography.pyq_index',**filters)
    return render_template('ds/solar_bilingual_question.html',q=q,t=t,question_language=lang,practice_mode=mode,historical=historical,source_record=record,
        difficulty=original.difficulty(q) if mode=='original' else {},visual=catalogue['visuals'].get(entry.get('visual_id')) if catalogue else None,literal_excerpt=q.get('source_paragraph') if catalogue else None,
        scorable=bool(pyqs.accepted_options(record)) if record else not entry.get('held',False),result=result,choice=choice,position=position,total=total,filters=filters,
        switch_urls=switches,filter_url=filter_url,answer_url=url_for(answer_endpoint,question_id=q['id'],**args,**filters),
        previous_url=target(previous) if previous else None,next_url=target(following) if following else None,
        chapter_url=chapter_url,section_url=chapter_url+'#'+entry['section'],related_urls=related_urls)


def _root():
    return Path(current_app.static_folder) / "textbooks" / "geography"


def _catalogue():
    return json.loads((_root() / "catalogue.json").read_text(encoding="utf-8"))


def _world_lesson_ids():
    ids = set()
    for chapter in world.index()["chapters"]:
        legacy = chapter.get("legacy_lesson_ids", [])
        if isinstance(legacy, list):
            ids.update(str(value) for value in legacy)
    return ids


def _india_ap_catalogue():
    """Return the legacy catalogue after moving World chapters to their umbrella."""
    data = _catalogue()
    world_ids = _world_lesson_ids()
    units = []
    for unit in data["units"]:
        lessons = [lesson for lesson in unit["lessons"] if lesson["id"] not in world_ids]
        if lessons:
            units.append({**unit, "lessons": lessons})
    return {**data, "units": units}


def _scope_pyqs(records, umbrella):
    if not umbrella:
        return records
    world_ids = _world_lesson_ids()
    allowed = world_ids if umbrella == "world" else {
        lesson["id"] for unit in _india_ap_catalogue()["units"] for lesson in unit["lessons"]
    }
    return [record for record in records if any(route.get("lesson_id") in allowed for route in record["routes"])]


def _pyq_filters(catalogue):
    filters = {key: request.args.get(key, "").strip()[:200] for key in
               ("unit", "lesson", "exam", "year", "paper", "mode", "search", "umbrella")}
    if filters["unit"] and filters["unit"] not in {str(u["id"]) for u in catalogue["units"]}:
        abort(404)
    if filters["lesson"] and filters["lesson"] not in {l["id"] for u in catalogue["units"] for l in u["lessons"]}:
        abort(404)
    if filters["mode"] not in {"", "held", "scored"}:
        abort(400)
    if filters["umbrella"] not in {"", "world", "india-ap"}:
        abort(400)
    if _question_language():filters["qlang"]=_question_language()
    return {key: value for key, value in filters.items() if value}


@bp.get("/")
def index():
    world_rows = _scope_pyqs(pyqs.records(), "world")
    india_rows = _scope_pyqs(pyqs.records(), "india-ap")
    return render_template("ds/geography_hub.html", world=world.index(),
                           world_pyqs=pyqs.summary(world_rows), india_pyqs=pyqs.summary(india_rows),
                           india_chapters=sum(len(unit["lessons"]) for unit in _india_ap_catalogue()["units"]))


@bp.get("/india-ap")
def india_ap_index():
    catalogue = _india_ap_catalogue()
    return render_template("ds/geography.html", catalogue=catalogue, unit=None,
                           pyq_summary=pyqs.summary(_scope_pyqs(pyqs.records(), "india-ap")))


@bp.get("/unit/<int:unit_id>")
def unit(unit_id):
    catalogue = _india_ap_catalogue()
    selected = next((u for u in catalogue["units"] if u["id"] == unit_id), None)
    if selected is None:
        abort(404)
    return render_template("ds/geography.html", catalogue=catalogue, unit=selected,
                           pyq_summary=pyqs.summary(pyqs.filtered(unit=str(unit_id))))


def _reader(filename, lesson=None):
    catalogue = _catalogue()
    if "lessons/" + filename not in catalogue["files"]:
        abort(404)
    filters = _pyq_filters(catalogue)
    question_id = request.args.get("question", "")[:120]
    question = pyqs.question(question_id) if question_id else None
    context = {}
    practice_id = request.args.get("practice", "")[:80]
    practice = solar.question(practice_id) if practice_id else None
    original_id=request.args.get("original", "")[:120]
    original_q=original.question(lesson['id'],original_id) if lesson and original_id else None
    book_id=request.args.get('book_pyq','')[:120]
    book_q=book_pyqs.question(book_id) if book_id else None
    if book_q and lesson and book_q['chapter']==lesson['id']:
        context={**_book_filters(), 'book_pyq':book_id}
        if request.args.get('review')=='1':context['review']='1'
        if request.args.get('choice') in ('1','2','3','4'):context['choice']=request.args['choice']
        back=url_for('geography.book_pyq',question_id=book_id,**{k:v for k,v in context.items() if k!='book_pyq'})
        if context.get('review'):back+='#answer-result'
        label='‹ ప్రశ్నకు తిరిగి · Back to question'
    elif original_q:
        selection=_original_filters()
        context={**selection,"original":original_id}
        if request.args.get("review")=="1":context["review"]="1"
        if request.args.get("choice") in {"1","2","3","4"}:context["choice"]=request.args["choice"]
        back=url_for("geography.original_question",chapter_id=lesson['id'],question_id=original_id,**{k:v for k,v in context.items() if k!="original"})
        if context.get("review"):back+="#answer-result"
        label="‹ ప్రశ్నకు తిరిగి · Back to question"
    elif practice:
        selection = _solar_filters()
        context = {**selection, "practice": practice_id}
        if request.args.get("review") == "1":
            context["review"] = "1"
        if request.args.get("choice") in {"1", "2", "3", "4"}:
            context["choice"] = request.args["choice"]
        back = url_for("geography.solar_question", question_id=practice_id,
                       **{k: v for k, v in context.items() if k != "practice"})
        if context.get("review"):
            back += "#answer-result"
        label = "‹ ప్రశ్నకు తిరిగి · Back to question"
    elif question:
        context = {**filters, "question": question_id}
        if request.args.get("review") == "1":
            context["review"] = "1"
        if request.args.get("choice") in {"1", "2", "3", "4"}:
            context["choice"] = request.args["choice"]
        back = url_for("geography.pyq", question_id=question_id,
                       **{k: v for k, v in context.items() if k != "question"})
        if context.get("review"):
            back += "#answer-result"
        label = "‹ ప్రశ్నకు తిరిగి · Back to question"
    else:
        back = url_for("geography.unit", unit_id=lesson["unit"]) if lesson else url_for("geography.index")
        label = "‹ యూనిట్‌కు తిరిగి · Back to unit" if lesson else "‹ భూగోళశాస్త్రం · Geography"
    books = {l["file"]: l for u in catalogue["units"] for l in u["lessons"]}
    page = (_root() / "lessons" / filename).read_text(encoding="utf-8")
    def rebase(match):
        href = html.unescape(match[1]);parsed = urlsplit(href)
        if parsed.scheme or parsed.netloc:
            return match[0]
        if parsed.path.startswith("/learn/geography/lesson/"):
            other = parsed.path.rsplit("/", 1)[-1]
            if other in {l["id"] for l in books.values()}:
                target = url_for("geography.lesson", lesson_id=other, **context)
            else:
                return match[0]
        elif parsed.path.startswith("/static/textbooks/geography/lessons/"):
            file = unquote(parsed.path.rsplit("/", 1)[-1])
            if "lessons/"+file not in catalogue["files"]:
                return match[0]
            target = url_for("geography.lesson", lesson_id=books[file]["id"], **context) if file in books else url_for("geography.reference", name=file, **context)
        else:
            return match[0]
        if parsed.fragment:
            target += "#" + parsed.fragment
        return 'href="' + html.escape(target, quote=True) + '"'
    page = re.sub(r'href="([^"]+)"', rebase, page)
    page = re.sub(r'(<article(?:\s[^>]*)?>)', r'\1<span id="chapter-overview"></span>', page, count=1)
    toolbar = '<nav class="geo-note-return" aria-label="Return to practice"><a data-note-back href="'+html.escape(back,quote=True)+'">'+label+'</a><a href="'+url_for("geography.index")+'">అన్ని యూనిట్లు · All units</a></nav>'
    css = '<style>.geo-note-return{position:sticky;top:0;z-index:30;background:#fff;border-bottom:1px solid #dbe5dc;display:flex;justify-content:space-between;gap:15px;padding:14px max(18px,calc((100vw - 1040px)/2));font:600 15px/1.5 system-ui,"Nirmala UI",sans-serif}.geo-note-return a{display:inline-flex;align-items:center;min-height:32px}article [id],h2[id],h3[id],#chapter-overview{scroll-margin-top:135px}#chapter-overview{display:block}@media(max-width:600px){.geo-note-return{font-size:13px;padding:10px 14px;flex-wrap:wrap;gap:4px 14px}}</style>'
    page = page.replace("</head>",css+"</head>",1).replace("<body>","<body>"+toolbar,1)
    response = make_response(page)
    response.headers["Content-Type"] = "text/html; charset=utf-8"
    response.headers["Cache-Control"] = "private, no-store"
    return response


@bp.get("/lesson/<lesson_id>")
def lesson(lesson_id):
    selected = next((l for u in _catalogue()["units"] for l in u["lessons"] if l["id"] == lesson_id), None)
    if selected is None:
        abort(404)
    return _reader(selected["file"], selected)


@bp.get("/reference/<name>")
def reference(name):
    return _reader(name)


@bp.get("/pyqs")
def pyq_index():
    scope = request.args.get("umbrella", "").strip()
    catalogue = _india_ap_catalogue() if scope == "india-ap" else _catalogue();filters = _pyq_filters(catalogue)
    service_filters = {key: value for key, value in filters.items() if key != "umbrella"}
    all_records = _scope_pyqs(pyqs.records(), scope);selected = _scope_pyqs(pyqs.filtered(**service_filters), scope)
    if request.args.get("start") == "1" and selected:
        return redirect(url_for("geography.pyq", question_id=selected[0]["source"]["id"], **filters))
    try:
        page = max(1, int(request.args.get("page", "1")))
    except ValueError:
        page = 1
    pages = max(1, (len(selected)+19)//20);page = min(page,pages)
    chapter_counts = {l["id"]: sum(any(x["lesson_id"] == l["id"] for x in record["routes"]) for record in all_records) for u in catalogue["units"] for l in u["lessons"]}
    matrix = [{"exam":r["source"]["exam"],"year":str(r["source"]["year"]),"paper":r["source"].get("paper") or "__unknown__",
               "units":sorted({str(x["unit"]) for x in r["routes"] if x["unit"]}),"lessons":sorted({x["lesson_id"] for x in r["routes"] if x["lesson_id"]})} for r in all_records]
    return render_template("ds/geography_pyqs.html", catalogue=catalogue, filters=filters,
                           summary=pyqs.summary(selected), total_summary=pyqs.summary(all_records),
                           records=selected[(page-1)*20:page*20], page=page,pages=pages,
                           exams=sorted({r["source"]["exam"] for r in all_records}),
                           years=sorted({str(r["source"]["year"]) for r in all_records},reverse=True),
                           papers=sorted({r["source"].get("paper") or "__unknown__" for r in all_records}),
                           matrix=matrix, chapter_counts=chapter_counts, no_match=bool(request.args.get("start") and not selected))


def _pyq_page(question_id, answered=False):
    record = pyqs.question(question_id) or abort(404);view = pyqs.display(record)
    result = None;choice = None;filters = _pyq_filters(_catalogue())
    if answered or request.args.get("review") == "1":
        raw = request.form.get("choice", "") if answered else request.args.get("choice", "")
        try:
            choice = int(raw) if raw else None
            if answered or choice in (1,2,3,4) or not view["scorable"]:
                result = pyqs.grade(record, choice)
        except ValueError:
            abort(400,"Choose an option from 1 to 4")
    scope = filters.get("umbrella", "")
    service_filters = {key: value for key, value in filters.items() if key != "umbrella"}
    all_records = _scope_pyqs(pyqs.filtered(**service_filters), scope)
    index = next((i for i,r in enumerate(all_records) if r["source"]["id"] == question_id),None)
    if index is None:
        abort(404)
    context = {**filters,"question":question_id}
    if result:
        context["review"] = "1"
        if choice:
            context["choice"] = str(choice)
    chapter_links=[]
    for item in pyqs.chapter_context(record):
        target = url_for("geography.lesson",lesson_id=item["lesson_id"],**context) if item["lesson_id"] else url_for("geography.reference",name=item["file"],**context)
        chapter_links.append({**item,"chapter_url":target,"section_url":target+("#"+item["anchor"] if item["anchor"] else "")})
    if question_id in bilingual.payload()['historical']:
        source=record['source'];q={'id':question_id,'answer':source['answer_index'],'source_urls':[source[k] for k in ('source_url','official_key_url') if source.get(k)]}
        return _bilingual_page(q,filters,result,choice,index+1,len(all_records),all_records[index-1]['source']['id'] if index else None,all_records[index+1]['source']['id'] if index+1<len(all_records) else None,'historical',url_for('geography.lesson',lesson_id='03',**context),record=record)
    return render_template("ds/geography_pyq.html",q=view,result=result,choice=choice,position=index+1,total=len(all_records),filters=filters,
                           accepted=pyqs.accepted_options(record) if result else (),contexts=chapter_links,
                           previous=all_records[index-1]["source"]["id"] if index else None,
                           following=all_records[index+1]["source"]["id"] if index+1<len(all_records) else None)


@bp.get("/pyq/<question_id>")
def pyq(question_id):
    return _pyq_page(question_id)


@bp.post("/pyq/<question_id>/answer")
def pyq_answer(question_id):
    return _pyq_page(question_id,answered=True)


# Original practice has its own IDs, data and routes; historical PYQs remain separate.
def _solar_filters():
    filters = {k: request.args.get(k, "").strip()[:80] for k in ("topic", "kind")}
    data = solar.payload()
    if filters["topic"] and filters["topic"] not in {str(t["id"]) for t in data["topics"]}:
        abort(400)
    if filters["kind"] and filters["kind"] not in {q["kind"] for q in data["questions"]}:
        abort(400)
    if _question_language():filters["qlang"]=_question_language()
    return {k: v for k, v in filters.items() if v}


@bp.get("/solar-practice")
def solar_index():
    filters = _solar_filters()
    selected = solar.questions(**filters)
    if request.args.get("start") == "1" and selected:
        return redirect(url_for("geography.solar_question", question_id=selected[0]["id"], **filters))
    return render_template("ds/solar_practice.html", topics=solar.payload()["topics"],
                           kinds=sorted({q["kind"] for q in solar.questions()}), questions=selected,
                           filters=filters, no_match=not selected,bilingual_titles=bilingual.payload()["original"])


def _solar_page(question_id, answered=False):
    filters = _solar_filters()
    selected = solar.questions(**filters)
    index = next((i for i,q in enumerate(selected) if q["id"] == question_id), None)
    if index is None:
        abort(404)
    q = selected[index];choice = None;result = None
    if answered or request.args.get("review") == "1":
        raw = request.form.get("choice", "") if answered else request.args.get("choice", "")
        try:
            choice = int(raw)
            result = solar.grade(q, choice)
        except (ValueError, TypeError):
            abort(400, "Choose an option from 1 to 4")
    context = {**filters, "practice": question_id}
    if result:
        context.update(review="1", choice=str(choice))
    chapter_url = url_for("geography.lesson", lesson_id="03", **context)
    return _bilingual_page(q,filters,result,choice,index+1,len(selected),selected[index-1]['id'] if index else None,selected[index+1]['id'] if index+1<len(selected) else None,'solar',chapter_url)



@bp.get("/solar-practice/<question_id>")
def solar_question(question_id):
    return _solar_page(question_id)


@bp.post("/solar-practice/<question_id>/answer")
def solar_answer(question_id):
    return _solar_page(question_id, answered=True)


# Baseline original practice across all prepared chapters. Publishing remains held.
def _original_filters():
    kind=request.args.get('kind','').strip()[:80]
    filters={'kind':kind} if kind else {}
    scope=request.args.get('scope','').strip()
    page=request.args.get('page','').strip()
    if scope and scope not in ('book','baseline'):abort(400)
    if page and (not page.isdigit() or not 2 <= int(page) <= 176):
        abort(400)
    if scope:filters['scope']=scope
    if page:filters['page']=str(int(page))
    if _question_language():filters['qlang']=_question_language()
    difficulty=request.args.get('difficulty','').strip()
    if difficulty not in ('','easy','moderate','hard'):abort(400)
    if difficulty:filters['difficulty']=difficulty
    return filters

def _original_book_question(q):
    return q.get('origin') in ('book-audit-original','chapter-audit-original','printed-atom-audit-original')

def _original_printed_page(q):
    return str(q.get('source_page',q.get('printed_page_reference','')))

def _select_original(data,filters):
    return [q for q in data['questions'] if (not filters.get('kind') or q['kind']==filters['kind']) and (not filters.get('scope') or _original_book_question(q)==(filters['scope']=='book')) and (not filters.get('page') or _original_printed_page(q)==filters['page']) and (not filters.get('difficulty') or original.difficulty(q).get('level')==filters['difficulty'])]

@bp.get('/original-practice')
def original_index():
    chapters=original.manifest()['chapters'];cid=request.args.get('chapter','')
    if cid and cid not in chapters:abort(404)
    data=original.chapter(cid) if cid else None;filters=_original_filters()
    if data and filters.get('kind') and filters['kind'] not in {q['kind'] for q in data['questions']}:abort(400)
    selected=_select_original(data,filters) if data else []
    if request.args.get('start')=='1' and selected:return redirect(url_for('geography.original_question',chapter_id=cid,question_id=selected[0]['id'],**filters))
    return render_template('ds/original_practice.html',chapters=chapters,data=data,questions=selected,filters=filters,bilingual_titles=maps_bilingual.payload(cid)['questions'] if data and cid in ('01','02') else bilingual.payload()['original'] if data and cid=='03' else {})

@bp.get('/original-practice/<chapter_id>/<question_id>')
def original_question(chapter_id,question_id):return _original_page(chapter_id,question_id)

@bp.post('/original-practice/<chapter_id>/<question_id>/answer')
def original_answer(chapter_id,question_id):return _original_page(chapter_id,question_id,True)

def _original_page(cid,qid,answered=False):
    data=original.chapter(cid)
    if not data:abort(404)
    filters=_original_filters()
    if filters.get('kind') and filters['kind'] not in {q['kind'] for q in data['questions']}:abort(400)
    selected=_select_original(data,filters)
    position=next((i for i,q in enumerate(selected) if q['id']==qid),None)
    if position is None:abort(404)
    q=selected[position];choice=None;result=None;context={**filters,'original':qid}
    if answered or request.args.get('review')=='1':
        try:
            raw=request.form.get('choice','') if answered else request.args.get('choice','')
            choice=int(raw) if raw else None
            if choice is not None and choice not in (1,2,3,4):raise ValueError('Invalid choice')
            result=original.grade(q,choice)
        except (ValueError,TypeError):abort(400,'Choose 1 to 4')
        context.update(review='1')
        if choice is not None:context['choice']=str(choice)
    chapter_url=url_for('geography.lesson',lesson_id=cid,**context)
    if cid in ('01','02','03') or (q.get('options_en') and q.get('options_te')):
        return _bilingual_page(q,filters,result,choice,position+1,len(selected),selected[position-1]['id'] if position else None,selected[position+1]['id'] if position+1<len(selected) else None,'original',chapter_url,[url_for('geography.lesson',lesson_id=cid,**context)+'#'+a for a in q.get('related_sections',[])])
    return render_template('ds/original_question.html',q=q,chapter_id=cid,result=result,choice=choice,filters=filters,position=position+1,total=len(selected),chapter_url=chapter_url,section_url=chapter_url+'#'+q['section'],previous=selected[position-1]['id'] if position else None,following=selected[position+1]['id'] if position+1<len(selected) else None,related_urls=[url_for('geography.lesson',lesson_id=cid,**context)+'#'+a for a in q.get('related_sections',[])])


def _book_filters():
    values={k:request.args.get(k,'').strip()[:120] for k in ('state','board','exam','year','difficulty','qlang')}
    values['qlang']=values['qlang'] or 'te'
    if values['qlang'] not in ('te','en'):abort(400)
    return {k:v for k,v in values.items() if v}


@bp.get('/book-pyqs')
def book_pyq_index():
    filters=_book_filters();rows=book_pyqs.records()
    fields={'state':'state','board':'board_as_printed','exam':'exam_as_printed','year':'year_as_printed','difficulty':'difficulty_editorial'}
    facets={k:sorted({str(r.get(field)) for r in rows if r.get(field) is not None}) for k,field in fields.items()}
    selected=[r for r in rows if all(not filters.get(k) or str(r.get(field,''))==filters[k] for k,field in fields.items())]
    return render_template('ds/geography_book_pyqs.html',rows=selected,filters=filters,facets=facets)


@bp.route('/book-pyqs/<question_id>',methods=['GET','POST'])
def book_pyq(question_id):
    row=book_pyqs.question(question_id) or abort(404)
    filters=_book_filters();lang=filters['qlang'];choice=None;result=None
    if request.method=='POST' or request.args.get('review')=='1':
        raw=request.form.get('choice','') if request.method=='POST' else request.args.get('choice','')
        if raw not in ('','1','2','3','4'):abort(400)
        choice=int(raw) if raw else None
        result=book_pyqs.grade(row,choice)
    translation=row['editorial_english_translation']
    question=row['question_te_draft'] if lang=='te' else translation['question']
    statements=row['statements_te_draft'] if lang=='te' else translation['statements']
    options=row['options_as_printed_draft'] if lang=='te' else translation['options']
    context={**filters,'book_pyq':question_id}
    review={'review':'1',**({'choice':str(choice)} if choice else {})} if result else {}
    context.update(review)
    links=[url_for('geography.lesson',lesson_id=row['chapter'],**context)+'#'+section for section in row['sections']]
    switches={l:url_for('geography.book_pyq',question_id=question_id,**{**filters,**review,'qlang':l}) for l in ('te','en')}
    return render_template('ds/geography_book_pyq.html',r=row,question=question,statements=statements,options=options,filters=filters,lang=lang,result=result,choice=choice,links=links,switches=switches)


@bp.get('/book-pyq-evidence/<question_id>')
def book_pyq_evidence(question_id):
    row=book_pyqs.question(question_id) or abort(404)
    try:path=book_pyqs.evidence(row)
    except (ValueError,OSError):abort(404)
    return send_file(path,conditional=True)


@bp.get('/world')
def world_index():
    return render_template('ds/world_geography.html', chapters=world.index()['chapters'])


def _world_resources(manifest):
    catalogue=_catalogue();lessons={l['id']:l for u in catalogue['units'] for l in u['lessons']}
    ids=manifest.get('legacy_lesson_ids',[])
    if isinstance(ids,str):ids=[]
    return [lessons[i] for i in ids if i in lessons]


@bp.get('/world/<int:number>')
def world_chapter(number):
    ch=world.chapter(number) or abort(404)
    return render_template('ds/world_chapter.html',ch=ch,native=bool(ch.get('notes_file')),resources=_world_resources(ch))


@bp.get('/world/<int:number>/notes')
def world_notes(number):
    ch=world.chapter(number) or abort(404);path=world.notes_path(number)
    if not path or not path.is_file():abort(404)
    page=path.read_text(encoding='utf-8-sig')
    back=url_for('geography.world_chapter',number=number)
    toolbar='<nav class="geo-note-return"><a href="'+html.escape(back,quote=True)+'">‹ World chapter</a><a href="'+url_for('geography.world_index')+'">All World Geography</a></nav>'
    css='<style>.geo-note-return{position:sticky;top:0;z-index:30;background:#fff;border-bottom:1px solid #dbe5dc;display:flex;justify-content:space-between;padding:12px 18px;font:600 15px/1.5 system-ui}.geo-note-return+* [id],article [id]{scroll-margin-top:90px}</style>'
    page=page.replace('</head>',css+'</head>',1).replace('<body>','<body>'+toolbar,1)
    response=make_response(page);response.headers['Content-Type']='text/html; charset=utf-8';return response


@bp.get('/world/<int:number>/practice')
def world_practice(number):
    ch=world.chapter(number) or abort(404);rows=world.questions(number)
    if not rows:abort(404)
    return render_template('ds/world_practice.html',number=number,ch=ch,questions=rows)


def _world_question_page(number,qid,answered=False):
    ch=world.chapter(number) or abort(404);rows=world.questions(number)
    q=world.question(number,qid) or abort(404);position=next(i for i,x in enumerate(rows) if x['id']==qid)
    lang=request.args.get('qlang','te');
    if lang not in ('te','en'):abort(400)
    choice=None;result=None
    if answered or request.args.get('review')=='1':
        raw=request.form.get('choice','') if answered else request.args.get('choice','')
        if raw not in ('1','2','3','4'):abort(400)
        choice=int(raw);result={'correct':choice==q['answer'],'score':int(choice==q['answer'])}
    options=q['options_te' if lang=='te' else 'options_en'];explanation=q['explanation_te' if lang=='te' else 'explanation_en'];whys=q['option_explanations_te' if lang=='te' else 'option_explanations_en']
    notes_url=url_for('geography.world_notes',number=number,**({'review':'1','choice':choice} if result else {}))
    return render_template('ds/world_question.html',number=number,ch=ch,q=q,lang=lang,options=options,explanation=explanation,option_explanations=whys,result=result,choice=choice,position=position+1,total=len(rows),previous=rows[position-1]['id'] if position else None,following=rows[position+1]['id'] if position+1<len(rows) else None,notes_url=notes_url,section_url=notes_url+'#'+q['section'])


@bp.get('/world/<int:number>/practice/<qid>')
def world_question(number,qid):return _world_question_page(number,qid)


@bp.post('/world/<int:number>/practice/<qid>/answer')
def world_answer(number,qid):return _world_question_page(number,qid,True)

