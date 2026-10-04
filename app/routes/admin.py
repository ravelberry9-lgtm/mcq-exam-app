"""
app/routes/admin.py
Minimal admin CMS — PIN gate + paste-HTML notes editor.

Phase 3 scope: paste-HTML + save only.
PIN: 1234 (change via ADMIN_PIN env var).
Not production-grade — cookie-based session token.
"""
import hashlib, hmac, secrets, subprocess, sys, os, time
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
    "*":   ["class", "id"],   # no inline style: there is no CSS sanitiser
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
        protocols=["http", "https", "mailto"],
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


# ── CSRF (session token; checked on every admin POST) ─────────────

def csrf_token() -> str:
    tok = session.get("_csrf")
    if not tok:
        tok = secrets.token_urlsafe(32)
        session["_csrf"] = tok
    return tok


@bp.app_template_global("csrf_token")
def _csrf_template_global():
    return csrf_token()


@bp.before_request
def _csrf_protect():
    if request.method in ("POST", "PUT", "PATCH", "DELETE"):
        sent = request.form.get("csrf_token") or request.headers.get("X-CSRF-Token") or ""
        expected = session.get("_csrf") or ""
        if not expected or not hmac.compare_digest(sent, expected):
            from flask import abort
            abort(400, "Missing or invalid CSRF token")


# ── login throttle (in memory; resets on restart / per worker) ─────
_FAILS: dict = {}


def _client_key() -> str:
    return request.remote_addr or "unknown"


def _locked_for(key: str) -> int:
    rec = _FAILS.get(key)
    if rec and rec["until"] > time.time():
        return int(rec["until"] - time.time()) + 1
    return 0


def _register_failure(key: str) -> None:
    rec = _FAILS.setdefault(key, {"n": 0, "until": 0})
    rec["n"] += 1
    if rec["n"] >= current_app.config.get("ADMIN_MAX_FAILURES", 5):
        rec["until"] = time.time() + current_app.config.get("ADMIN_LOCKOUT_SECONDS", 300)
        rec["n"] = 0


def _safe_next(target: str):
    """Only same-site absolute paths; rejects //host, scheme:, backslashes."""
    if target and target.startswith("/") and not target.startswith("//") and "\\" not in target and "\n" not in target and "\r" not in target:
        return target
    return None


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
        key = _client_key()
        wait = _locked_for(key)
        if wait:
            return render_template("admin/login.html", error=f"Too many attempts. Try again in {wait} seconds."), 429
        if hmac.compare_digest(pin.encode(), str(current_app.config["ADMIN_PIN"]).encode()):
            _FAILS.pop(key, None)
            csrf = session.get("_csrf")
            session.clear()                      # new session on login (no fixation)
            if csrf:
                session["_csrf"] = csrf
            session["admin_token"] = _make_token(pin)
            session.permanent = True
            return redirect(_safe_next(request.args.get("next", "")) or url_for("admin.index"))
        _register_failure(key)
        error = "Incorrect PIN. Try again."
    return render_template("admin/login.html", error=error)


@bp.route("/logout", methods=["POST"])
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

    # Get or create section 1 note
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


# ── One-time seed runner ──────────────────────────────────────────

@bp.route("/seed", methods=["GET", "POST"])
def seed():
    """Run seed_exam_group2.py against the live DB and stream output."""
    guard = _require_auth()
    if guard:
        return guard

    if request.method == "GET":
        return render_template("admin/seed.html")

    # POST — stream the script output back as plain text
    scripts_dir = os.path.join(
        os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
        "scripts",
    )
    script = os.path.join(scripts_dir, "seed_exam_group2.py")

    def generate():
        yield "Running seed_exam_group2.py ...\n\n"
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
            yield f"\n\nExit code: {proc.returncode}\n"
            if proc.returncode == 0:
                yield "DONE: Seed completed successfully.\n"
            else:
                yield "ERROR: Seed exited with errors - see output above.\n"
        except Exception as exc:
            yield f"ERROR: {exc}\n"

    return Response(generate(), mimetype="text/plain")


@bp.route("/load-content", methods=["GET", "POST"])
def load_content():
    """Run scripts/load_content.py — bulk-loads data/content.db into production DB."""
    guard = _require_auth()
    if guard:
        return guard

    if request.method == "GET":
        return render_template("admin/load_content.html")

    scripts_dir = os.path.join(
        os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
        "scripts",
    )
    script = os.path.join(scripts_dir, "load_content.py")

    def generate():
        yield "Running load_content.py ...\n\n"
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
            yield f"\n\nExit code: {proc.returncode}\n"
            if proc.returncode == 0:
                yield "DONE: Content loaded successfully.\n"
            else:
                yield "ERROR: load_content.py exited with errors — see above.\n"
        except Exception as exc:
            yield f"ERROR: {exc}\n"

    return Response(generate(), mimetype="text/plain")




@bp.route("/parse-ap-history", methods=["GET", "POST"])
def parse_ap_history():
    """
    Re-parse AP History HTML chapter files from static/notes/AP_History/Chapters/
    and reload into the live database.

    Use this whenever the HTML chapter files have been updated and deployed —
    it replaces all ap_history chapters + notes with freshly parsed content.
    """
    guard = _require_auth()
    if guard:
        return guard

    if request.method == "GET":
        return render_template("admin/parse_ap_history.html")

    scripts_dir = os.path.join(
        os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
        "scripts",
    )
    script = os.path.join(scripts_dir, "parse_ap_history_notes.py")

    def generate():
        yield "Running parse_ap_history_notes.py --postgres ...\n\n"
        try:
            proc = subprocess.Popen(
                [sys.executable, script, "--postgres"],
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                env={**os.environ},
            )
            for line in proc.stdout:
                yield line
            proc.wait()
            yield f"\n\nExit code: {proc.returncode}\n"
            if proc.returncode == 0:
                yield "DONE: AP History notes parsed and loaded successfully.\n"
            else:
                yield "ERROR: parse_ap_history_notes.py exited with errors — see above.\n"
        except Exception as exc:
            yield f"ERROR: {exc}\n"

    return Response(generate(), mimetype="text/plain")
