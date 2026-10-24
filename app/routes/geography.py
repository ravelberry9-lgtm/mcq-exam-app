"""Read-only geography textbook: 16 units and 83 canonical chapters."""
import json
from pathlib import Path
from flask import Blueprint, abort, current_app, render_template, send_file

bp = Blueprint("geography", __name__, url_prefix="/learn/geography")


def _root():
    return Path(current_app.static_folder) / "textbooks" / "geography"


def _catalogue():
    return json.loads((_root() / "catalogue.json").read_text(encoding="utf-8"))


@bp.get("/")
def index():
    return render_template("ds/geography.html", catalogue=_catalogue(), unit=None)


@bp.get("/unit/<int:unit_id>")
def unit(unit_id):
    catalogue = _catalogue()
    selected = next((u for u in catalogue["units"] if u["id"] == unit_id), None)
    if selected is None:
        abort(404)
    return render_template("ds/geography.html", catalogue=catalogue, unit=selected)


@bp.get("/lesson/<lesson_id>")
def lesson(lesson_id):
    selected = next((l for u in _catalogue()["units"] for l in u["lessons"]
                     if l["id"] == lesson_id), None)
    if selected is None:
        abort(404)
    return send_file(_root() / "lessons" / selected["file"], mimetype="text/html")
