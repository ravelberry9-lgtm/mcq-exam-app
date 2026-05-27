"""
app/routes/admin.py
Minimal admin CMS — PIN gate + paste-HTML notes editor.

Phase 3 scope: paste-HTML + save only.
PIN: 1234 (change via ADMIN_PIN env var).
Not production-grade — cookie-based session token.
"""
import hashlib, secrets, subprocess, sys, os
from flask import (
    Blueprint, render_template, request, redirect,
    url_for, session, flash, current_app, Response
)
import bleach

from ..db import db
from ..models import Subject, Chapter, Note

bp = Blueprint("admin", __name__, url_prefix="/admin")

# ── HTML tag allowlist (educational bilingual notes) ──────────────
ALLOWED_TAGS = [
    "p", "br", "hr",
    "h1", "h2", "h3", "h4", "h5", "h6",
    "ul", "ol", "li",
    "strong", "b", "em", "i", "u", "s",
    "span", "div",
    "table", "thead", "tbody", "tr", "th", "td",
    "blockquote", "pre", "code",
    "a",
    "img",
    "sup", "sub",
]
ALLOWED_ATTRS = {
    "*":   ["class", "id", "style"],
    "a":   ["href", "title", "target", "rel"],
    "img": ["src", "alt", "width", "height"],
    "td":  ["colspan", "rowspan"],
    "th":  ["colspan", "rowspan"],
}


def _sanitize(html: str) -> str:
    """Bleach-clean HTML with the educational tag allowlist."""
    return bleach.clean(
        html or "",
        tags=ALLOWED_TAGS,
        attributes=ALLOWED_ATTRS,
        strip=True,
    )


# ── PIN gate helpers ──────────────────────────────────────────────

def _is_authed() -> bool:
    token = session.get("admin_token")
    if not token:
        return False
    expected = _make_token(current_app.config["ADMIN_PIN"])
    return secrets.compare_digest(token, expected)


def _make_token(pin: str) -> str:
    return hashlib.sha256(f"admin:{pin}".encode()).hexdigest()


def _require_auth():
    """Return redirect to login if not authed, else None."""
    if not _is_authed():
        return redirect(url_for("admin.login", next=request.path))
    return None


# ── Routes ────────────────────────────────────────────────────────

@bp.route("/", methods=["GET"])
def index():
    guard = _require_auth()
    if guard:
        return guard
    subjects = Subject.query.order_by(Subject.sort_order).all()
    return render_template("admin/index.html", subjects=subjects)


@bp.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        pin = request.form.get("pin", "")
        if pin == current_app.config["ADMIN_PIN"]:
            session["admin_token"] = _make_token(pin)
            session.permanent = True
            return redirect(request.args.get("next") or url_for("admin.index"))
        error = "Incorrect PIN. Try again."
    return render_template("admin/login.html", error=error)


@bp.route("/logout")
def logout():
    session.pop("admin_token", None)
    return redirect(url_for("admin.login"))


@bp.route("/notes", methods=["GET"])
def notes_list():
    guard = _require_auth()
    if guard:
        return guard
    subjects = (
        Subject.query
        .order_by(Subject.sort_order)
        .all()
    )
    chapters_by_subject = {}
    for subj in subjects:
        chs = (
            Chapter.query
            .filter_by(subject_id=subj.id)
            .order_by(Chapter.chapter_num)
            .all()
        )
        chapters_by_subject[subj.id] = chs
    return render_template(
        "admin/notes_list.html",
        subjects=subjects,
        chapters_by_subject=chapters_by_subject,
    )


@bp.route("/notes/<int:chapter_id>/edit", methods=["GET", "POST"])
def notes_edit(chapter_id: int):
    guard = _require_auth()
    if guard:
        return guard

    chapter = Chapter.query.get_or_404(chapter_id)
    subject = Subject.query.get(chapter.subject_id)

    note = Note.query.filter_by(chapter_id=chapter_id, section_num=1).first()
    if note is None:
        note = Note(
            chapter_id=chapter_id,
            section_num=1,
            heading_en=chapter.title_en,
            heading_te=chapter.title_te,
            body_en="",
            body_te="",
        )
        db.session.add(note)
        db.session.commit()

    if request.method == "POST":
        body_en = _sanitize(request.form.get("body_en", ""))
        body_te = _sanitize(request.form.get("body_te", ""))
        heading_en = request.form.get("heading_en", note.heading_en or "").strip()[:256]
        heading_te = request.form.get("heading_te", note.heading_te or "").strip()[:256]

        note.body_en = body_en
        note.body_te = body_te
        note.heading_en = heading_en
        note.heading_te = heading_te
        db.session.commit()
        flash(f"Saved '{chapter.title_en}' notes.", "success")
        return redirect(url_for("admin.notes_edit", chapter_id=chapter_id))

    return render_template(
        "admin/notes_edit.html",
        chapter=chapter,
        subject=subject,
        note=note,
    )


# ── One-time seed runner ──────────────────────────────────────────────

def _run_script(script_path):
    """Run a script and yield its output lines."""
    yield f"--- Running {os.path.basename(script_path)} ---\n"
    try:
        proc = subprocess.Popen(
            [sys.executable, script_path],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            env={**os.environ},
        )
        for line in proc.stdout:
            yield line
        proc.wait()
        yield f"Exit code: {proc.returncode}\n\n"
        return proc.returncode
    except Exception as exc:
        yield f"ERROR: {exc}\n"
        return 1


@bp.route("/seed", methods=["GET", "POST"])
def seed():
    """Run seed_dev.py then seed_exam_group2.py against the live DB."""
    guard = _require_auth()
    if guard:
        return guard

    if request.method == "GET":
        return render_template("admin/seed.html")

    scripts_dir = os.path.join(
        os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
        "scripts",
    )

    def generate():
        rc = 0
        for script_name in ["seed_dev.py", "seed_exam_group2.py"]:
            script = os.path.join(scripts_dir, script_name)
            last_rc = 0
            yield f"--- Running {script_name} ---\n"
            try:
                proc = subprocess.Popen(
                    [sys.executable, script],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.STDOUT,
                    text=True,
                    env={**os.environ},
                )
                for line in proc.stdout:
                    yield line
                proc.wait()
                last_rc = proc.returncode
                yield f"Exit code: {last_rc}\n\n"
            except Exception as exc:
                yield f"ERROR launching {script_name}: {exc}\n\n"
                last_rc = 1
            if last_rc != 0:
                rc = last_rc
        if rc == 0:
            yield "ALL DONE: Both seed scripts completed successfully.\n"
        else:
            yield "FINISHED WITH ERRORS: check output above.\n"

    return Response(generate(), mimetype="text/plain")
