"""Geography textbook, filtered PYQ practice and contextual chapter reader."""
import html
import json
import re
from pathlib import Path
from urllib.parse import urlsplit, unquote
from flask import Blueprint, abort, current_app, make_response, redirect, render_template, request, url_for
from ..services import geography_pyqs as pyqs
from ..services import solar_practice as solar

bp = Blueprint("geography", __name__, url_prefix="/learn/geography")


def _root():
    return Path(current_app.static_folder) / "textbooks" / "geography"


def _catalogue():
    return json.loads((_root() / "catalogue.json").read_text(encoding="utf-8"))


def _pyq_filters(catalogue):
    filters = {key: request.args.get(key, "").strip()[:200] for key in
               ("unit", "lesson", "exam", "year", "paper", "mode", "search")}
    if filters["unit"] and filters["unit"] not in {str(u["id"]) for u in catalogue["units"]}:
        abort(404)
    if filters["lesson"] and filters["lesson"] not in {l["id"] for u in catalogue["units"] for l in u["lessons"]}:
        abort(404)
    if filters["mode"] not in {"", "held", "scored"}:
        abort(400)
    return {key: value for key, value in filters.items() if value}


@bp.get("/")
def index():
    return render_template("ds/geography.html", catalogue=_catalogue(), unit=None, pyq_summary=pyqs.summary())


@bp.get("/unit/<int:unit_id>")
def unit(unit_id):
    catalogue = _catalogue()
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
    if practice:
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
    css = '<style>.geo-note-return{position:sticky;top:0;z-index:30;background:#fff;border-bottom:1px solid #dbe5dc;display:flex;justify-content:space-between;gap:15px;padding:14px max(18px,calc((100vw - 1040px)/2));font:600 15px/1.5 system-ui,"Nirmala UI",sans-serif}.geo-note-return a{display:inline-flex;align-items:center;min-height:32px}h2[id],h3[id],#chapter-overview{scroll-margin-top:135px}#chapter-overview{display:block}@media(max-width:600px){.geo-note-return{font-size:13px;padding:10px 14px;flex-wrap:wrap;gap:4px 14px}}</style>'
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
    catalogue = _catalogue();filters = _pyq_filters(catalogue)
    all_records = pyqs.records();selected = pyqs.filtered(**filters)
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
    all_records = pyqs.filtered(**filters)
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
    return {k: v for k, v in filters.items() if v}


@bp.get("/solar-practice")
def solar_index():
    filters = _solar_filters()
    selected = solar.questions(**filters)
    if request.args.get("start") == "1" and selected:
        return redirect(url_for("geography.solar_question", question_id=selected[0]["id"], **filters))
    return render_template("ds/solar_practice.html", topics=solar.payload()["topics"],
                           kinds=sorted({q["kind"] for q in solar.questions()}), questions=selected,
                           filters=filters, no_match=not selected)


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
    return render_template("ds/solar_question.html", q=q, result=result, choice=choice, filters=filters,
                           position=index+1,total=len(selected),chapter_url=chapter_url,
                           section_url=chapter_url+"#"+q["section"],
                           previous=selected[index-1]["id"] if index else None,
                           following=selected[index+1]["id"] if index+1<len(selected) else None)


@bp.get("/solar-practice/<question_id>")
def solar_question(question_id):
    return _solar_page(question_id)


@bp.post("/solar-practice/<question_id>/answer")
def solar_answer(question_id):
    return _solar_page(question_id, answered=True)
