"""Read-only geography textbook: 16 units and 83 canonical chapters."""
import json
from pathlib import Path
from flask import Blueprint, abort, current_app, render_template, send_file, request, url_for

from ..services import geography_pyqs as pyqs

bp = Blueprint("geography", __name__, url_prefix="/learn/geography")


def _root():
    return Path(current_app.static_folder) / "textbooks" / "geography"


def _catalogue():
    return json.loads((_root() / "catalogue.json").read_text(encoding="utf-8"))


@bp.get("/")
def index():
    return render_template("ds/geography.html", catalogue=_catalogue(), unit=None, pyq_summary=pyqs.summary())


@bp.get("/unit/<int:unit_id>")
def unit(unit_id):
    catalogue = _catalogue()
    selected = next((u for u in catalogue["units"] if u["id"] == unit_id), None)
    if selected is None:
        abort(404)
    return render_template("ds/geography.html", catalogue=catalogue, unit=selected, pyq_summary=pyqs.summary(pyqs.filtered(unit=str(unit_id))))


@bp.get("/lesson/<lesson_id>")
def lesson(lesson_id):
    selected = next((l for u in _catalogue()["units"] for l in u["lessons"]
                     if l["id"] == lesson_id), None)
    if selected is None:
        abort(404)
    return send_file(_root() / "lessons" / selected["file"], mimetype="text/html")


def _pyq_filters(catalogue):
    filters = {key: request.args.get(key, "").strip()[:200] for key in
               ("unit", "lesson", "exam", "year", "mode", "search")}
    if filters["unit"] and filters["unit"] not in {str(u["id"]) for u in catalogue["units"]}:
        abort(404)
    if filters["lesson"] and filters["lesson"] not in {l["id"] for u in catalogue["units"] for l in u["lessons"]}:
        abort(404)
    if filters["mode"] not in {"", "held", "scored"}:
        abort(400)
    return {key: value for key, value in filters.items() if value}


@bp.get("/pyqs")
def pyq_index():
    catalogue = _catalogue()
    filters = _pyq_filters(catalogue)
    selected = pyqs.filtered(**filters)
    try:
        page = max(1, int(request.args.get("page", "1")))
    except ValueError:
        page = 1
    page_size = 20
    pages = max(1, (len(selected) + page_size - 1) // page_size)
    page = min(page, pages)
    items = selected[(page-1)*page_size:page*page_size]
    return render_template("ds/geography_pyqs.html", catalogue=catalogue, filters=filters,
                           summary=pyqs.summary(selected), total_summary=pyqs.summary(),
                           records=items, page=page, pages=pages,
                           exams=sorted({r["source"]["exam"] for r in pyqs.records()}),
                           years=sorted({str(r["source"]["year"]) for r in pyqs.records()}, reverse=True))


def _pyq_page(question_id, answered=False):
    record = pyqs.question(question_id) or abort(404)
    view = pyqs.display(record)
    result = None
    choice = None
    if answered:
        raw = request.form.get("choice", "")
        try:
            choice = int(raw) if raw else None
            result = pyqs.grade(record, choice)
        except ValueError:
            abort(400, "Choose an option from 1 to 4")
    filters = _pyq_filters(_catalogue())
    all_records = pyqs.filtered(**filters)
    index = next((i for i, r in enumerate(all_records) if r["source"]["id"] == question_id), None)
    if index is None:
        abort(404)
    return render_template("ds/geography_pyq.html", q=view, result=result, choice=choice,
                           position=index+1, total=len(all_records), filters=filters,
                           previous=all_records[index-1]["source"]["id"] if index else None,
                           following=all_records[index+1]["source"]["id"] if index+1 < len(all_records) else None)


@bp.get("/pyq/<question_id>")
def pyq(question_id):
    return _pyq_page(question_id)


@bp.post("/pyq/<question_id>/answer")
def pyq_answer(question_id):
    return _pyq_page(question_id, answered=True)
