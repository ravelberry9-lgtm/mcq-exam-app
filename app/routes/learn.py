"""Design-system journey (Stage 1-2): Learn -> Section -> Topic -> Notes -> Practice -> Explanation.

New blueprint under /learn. The old routes (/subjects, /subject/<slug>, /practice/<slug>,
/notes/..., /exam/...) are untouched and keep working until the new journey replaces them.
"""
import re
from flask import Blueprint, abort, jsonify, render_template, request, url_for

from ..db import db
from ..models import Chapter, ChapterProgress, ExamSection, Note, Subject
from ..services import learn as svc
from ..services import syllabus_view as syl
from ..services import expanded_view as xv
from ..services.ui_text import UI, t, tl

bp = Blueprint("learn", __name__, url_prefix="/learn")


def _device_id():
    from ..services.device import device_id
    return device_id()


bp.add_app_template_global(t, "t")
bp.add_app_template_global(tl, "tl")


@bp.route("/")
def hub():
    data = svc.hub()
    return render_template("ds/learn.html", data=data, resume=svc.resume_for(_device_id()))


@bp.route("/section/<int:section_id>")
def section(section_id):
    sec = db.session.get(ExamSection, section_id) or abort(404)
    groups = svc.with_banks(svc.topics_for_section(sec))
    groups = svc.attach_status(groups, _device_id())
    return render_template("ds/section.html", title_en=sec.name_en, title_te=sec.name_te,
                           groups=groups)


@bp.route("/ap-history")
def ap_history():
    data = syl.outline()
    return render_template("ds/syllabus.html", data=data)


@bp.route("/ap-history/<slug>")
def ap_history_chapter(slug):
    data = syl.chapter_detail(slug) or abort(404)
    return render_template("ds/syllabus_chapter.html", d=data)


@bp.route("/ap-history/<slug>/notes")
def expanded_index(slug):
    ch = xv.chapter_by_slug(slug) or abort(404)
    return render_template("ds/expanded_index.html", d=xv.index(ch), ch=ch)


@bp.route("/ap-history/<slug>/notes/<anchor_id>")
def expanded_note(slug, anchor_id):
    ch = xv.chapter_by_slug(slug) or abort(404)
    d = xv.page(ch, anchor_id) or abort(404)
    return render_template("ds/expanded_note.html", d=d, ch=ch, anchor_id=anchor_id)


@bp.route("/ap-history/<slug>/practice")
def canonical_practice(slug):
    """Practice for the questions imported through ap-history-import-v1 (only author-reviewed, learner-visible ones)."""
    ch = xv.chapter_by_slug(slug) or abort(404)
    sub = request.args.get("subtopic") or None
    qs = xv.native_questions(ch, sub)
    if qs is None:
        abort(404)
    total = len(qs)
    i = request.args.get("i", 1, type=int)
    extra = {"subtopic": sub} if sub else {}
    ctx = dict(chapter=None, subject=db.session.get(Subject, ch.subject_id), title_en=ch.title_en, title_te=ch.title_te, note_count=0,
               mcq_count=total, scope=f"c-{ch.slug}" + (f"-{sub}" if sub else ""),
               back_url=url_for("learn.ap_history_chapter", slug=slug), back_label="prac.back_chapter",
               restart_url=url_for("learn.canonical_practice", slug=slug, i=1, new=1, **extra))
    if total == 0:
        return render_template("ds/practice.html", **ctx, total=0, q=None, summary=False, i=1)
    if i > total:
        return render_template("ds/practice.html", **ctx, total=total, q=None, summary=True, i=i)
    i = max(1, i)
    return render_template("ds/practice.html", **ctx, total=total, q=svc.question_view(qs[i - 1]), summary=False, i=i,
                           next_url=url_for("learn.canonical_practice", slug=slug, i=i + 1, **extra), is_last=(i == total),
                           fresh=bool(request.args.get("new")))


@bp.route("/subject/<slug>")
def subject(slug):
    sub = Subject.query.filter_by(slug=slug).first_or_404()
    groups = svc.with_banks(svc.topics_for_subject(sub), [sub])
    groups = svc.attach_status(groups, _device_id())
    return render_template("ds/section.html", title_en=sub.name_en, title_te=sub.name_te,
                           marks=None, groups=groups,
                           canonical_url=url_for("learn.ap_history") if sub.slug == syl.SUBJECT_SLUG and syl.is_loaded() else None)


@bp.route("/subject/<slug>/<any(practice,pyq):bank>")
def bank(slug, bank):
    """Subject-level question banks: Practice (questions not tied to a chapter) and Previous papers."""
    sub = Subject.query.filter_by(slug=slug).first_or_404()
    qs = svc.bank_questions(sub.id, bank)
    total = len(qs)
    i = request.args.get("i", 1, type=int)
    label_en, label_te = UI["bank." + bank]
    ctx = dict(chapter=None, subject=sub, title_en=f"{sub.name_en} · {label_en}", title_te=f"{sub.name_te} · {label_te}",
               note_count=0, mcq_count=total, scope=f"s-{slug}-{bank}",
               back_url=url_for("learn.subject", slug=slug), back_label="prac.back_subject",
               restart_url=url_for("learn.bank", slug=slug, bank=bank, i=1, new=1))
    if total == 0:
        return render_template("ds/practice.html", **ctx, total=0, q=None, summary=False, i=1)
    if i > total:
        return render_template("ds/practice.html", **ctx, total=total, q=None, summary=True, i=i)
    i = max(1, i)
    return render_template("ds/practice.html", **ctx, total=total, q=svc.question_view(qs[i - 1]), summary=False, i=i,
                           next_url=url_for("learn.bank", slug=slug, bank=bank, i=i + 1), is_last=(i == total),
                           fresh=bool(request.args.get("new")))


@bp.route("/topic/<int:chapter_id>")
def topic(chapter_id):
    ch = db.session.get(Chapter, chapter_id) or abort(404)
    ctx = svc.topic_context(ch)
    prog = ChapterProgress.query.filter_by(device_id=_device_id(), chapter_id=ch.id).first()
    # only same-app section/subject pages are accepted as a return target (no open redirect)
    back = request.args.get("back", "")
    back_url = back if re.fullmatch(r"/learn/(section/\d+|subject/[\w-]+)", back) else None
    return render_template("ds/topic.html", **ctx, back_url=back_url,
                           status=prog.status if prog else "not_started")


@bp.route("/topic/<int:chapter_id>/notes")
def notes(chapter_id):
    ch = db.session.get(Chapter, chapter_id) or abort(404)
    ctx = svc.topic_context(ch)
    sections = Note.query.filter_by(chapter_id=ch.id).order_by(Note.section_num).all()
    if not sections:
        return render_template("ds/notes.html", **ctx, note=None, sections=[], pos=0, prev_n=None, next_n=None)
    wanted = request.args.get("section", type=int)
    nums = [n.section_num for n in sections]
    if wanted is None:
        prog = ChapterProgress.query.filter_by(device_id=_device_id(), chapter_id=ch.id).first()
        wanted = prog.current_section if prog and prog.current_section in nums else nums[0]
    if wanted not in nums:
        abort(404)
    pos = nums.index(wanted)
    note = sections[pos]
    keep_class = ctx["subject"].slug == "ap_history"
    body_en = svc.render_note_html(note.body_en, keep_class) if (note.body_en or "").strip() else ""
    body_te = svc.render_note_html(note.body_te, keep_class) if (note.body_te or "").strip() else ""
    return render_template(
        "ds/notes.html", **ctx, note=note, sections=sections, pos=pos,
        prev_n=nums[pos - 1] if pos > 0 else None,
        next_n=nums[pos + 1] if pos < len(nums) - 1 else None,
        body_en=body_en, body_te=body_te,
    )


@bp.route("/topic/<int:chapter_id>/practice")
def practice(chapter_id):
    ch = db.session.get(Chapter, chapter_id) or abort(404)
    ctx = svc.topic_context(ch)
    ctx.update(scope=str(ch.id), back_url=url_for("learn.topic", chapter_id=ch.id), back_label="prac.back_topic",
               restart_url=url_for("learn.practice", chapter_id=ch.id, i=1, new=1))
    qs = svc.chapter_questions(ch.id)
    total = len(qs)
    i = request.args.get("i", 1, type=int)
    if total == 0:
        return render_template("ds/practice.html", **ctx, total=0, q=None, summary=False, i=1)
    if i > total:
        return render_template("ds/practice.html", **ctx, total=total, q=None, summary=True, i=i)
    i = max(1, i)
    q = svc.question_view(qs[i - 1])
    nxt = url_for("learn.practice", chapter_id=ch.id, i=i + 1)
    return render_template("ds/practice.html", **ctx, total=total, q=q, summary=False, i=i,
                           next_url=nxt, is_last=(i == total), fresh=bool(request.args.get("new")))


@bp.route("/api/topic/<int:chapter_id>/section", methods=["POST"])
def api_section(chapter_id):
    """Remember which note section a device is reading (drives Resume)."""
    ch = db.session.get(Chapter, chapter_id) or abort(404)
    payload = request.get_json(silent=True) or {}
    num = payload.get("section")
    if not isinstance(num, int) or not Note.query.filter_by(chapter_id=ch.id, section_num=num).first():
        return jsonify({"error": "invalid section"}), 400
    prog = svc.record_section(_device_id(), ch.id, num)
    return jsonify({"status": prog.status, "current_section": prog.current_section})
