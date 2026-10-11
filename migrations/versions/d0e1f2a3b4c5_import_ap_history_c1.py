"""Import approved AP History Chapter 1 notes and questions (additive, idempotent).

Revision ID: d0e1f2a3b4c5
Revises: c9d0e1f2a3b4
"""
from datetime import datetime
import hashlib
import json
import re
from pathlib import Path

from alembic import op
import sqlalchemy as sa


revision = "d0e1f2a3b4c5"
down_revision = "c9d0e1f2a3b4"
branch_labels = None
depends_on = None

COLLECTION = "ap-history-fresh-v1"
PACKAGES = (
    "aph-u1-c01-final-researched-20261010",
    "aph-u1-c01-final-hr-20261010",
)
ROOT = Path(__file__).resolve().parents[2]
PACKAGE_ROOT = ROOT / "content" / "ap_history_import" / "chapter1"


def _norm(value):
    return re.sub(r"\s+", " ", (value or "").strip()).lower()


def _content_hash(record):
    parts = [record.get("question_en"), record.get("question_te")]
    for key in ("a", "b", "c", "d"):
        option = (record.get("options") or {}).get(key) or {}
        parts.extend((option.get("en"), option.get("te")))
    return hashlib.md5("␟".join(_norm(part) for part in parts).encode("utf-8")).hexdigest()


def _q_hash(record):
    options = record["options"]
    text = "|".join([
        _norm(record["question_en"]),
        *(_norm(options[key]["en"]) for key in ("a", "b", "c", "d")),
    ])
    return hashlib.md5(text.encode("utf-8")).hexdigest()


def _trace(record, manifest):
    old = dict(record.get("source_trace") or {})
    return {
        **old,
        "format_version": manifest["format_version"],
        "taxonomy_version": manifest["taxonomy_version"],
        "package_questions_sha256": manifest["questions_sha256"],
        "content_approval_note": manifest["approval_note"],
        "approval_basis": record.get("approval_basis"),
        "H": record.get("H", ""),
        "coverage_scope": record.get("coverage_scope"),
        "difficulty_original": record.get("difficulty"),
        "difficulty_calibration": record.get("difficulty_calibration"),
        "sources": record.get("sources") or [],
        "expanded_note": record.get("expanded_note"),
        "reconciliation": record.get("reconciliation"),
        "quality_adjudication": record.get("quality_adjudication"),
        "source_proposition_audit": record.get("source_proposition_audit"),
    }


def _load_package(name):
    package = PACKAGE_ROOT / name
    manifest = json.loads((package / "manifest.json").read_text(encoding="utf-8"))
    raw = (package / "questions.jsonl").read_bytes()
    # Git checks out text with platform-native line endings.  Hash the
    # canonical LF representation so the same reviewed package validates on
    # Windows audit machines and Linux production containers.
    canonical_raw = raw.replace(b"\r\n", b"\n").replace(b"\r", b"\n")
    if hashlib.sha256(canonical_raw).hexdigest() != manifest["questions_sha256"]:
        raise RuntimeError(f"checksum mismatch in {name}")
    records = [json.loads(line) for line in raw.decode("utf-8").splitlines() if line.strip()]
    if len(records) != manifest["question_count"]:
        raise RuntimeError(f"record count mismatch in {name}")
    return package, manifest, records


def upgrade():
    # The production code already contains the reviewed parser used in the local rehearsal.
    from app.services.expanded_notes import parse_package_notes

    bind = op.get_bind()
    meta = sa.MetaData()
    subjects = sa.Table("subjects", meta, autoload_with=bind)
    chapters = sa.Table("syllabus_chapters", meta, autoload_with=bind)
    subtopics = sa.Table("syllabus_subtopics", meta, autoload_with=bind)
    expanded = sa.Table("expanded_notes", meta, autoload_with=bind)
    questions = sa.Table("questions", meta, autoload_with=bind)

    subject_id = bind.execute(
        sa.select(subjects.c.id).where(subjects.c.slug == "ap_history")
    ).scalar_one_or_none()
    chapter_id = bind.execute(
        sa.select(chapters.c.id).where(chapters.c.slug == "u1-c01-region-people-sources")
    ).scalar_one_or_none()
    # Alembic must remain valid for clean installations where application seed
    # data is intentionally loaded after the schema chain. Production already
    # has both prerequisites; an unseeded database safely receives the schema
    # revision and can load this additive package through the normal importer.
    if subject_id is None or chapter_id is None:
        return

    note_package, note_manifest, _ = _load_package(PACKAGES[0])
    note_rows, _anchors, problems, warnings = parse_package_notes(note_package)
    if problems or warnings:
        raise RuntimeError(f"Chapter 1 notes failed migration validation: {problems or warnings}")
    existing_notes = {
        row.anchor_id: row.content_hash
        for row in bind.execute(
            sa.select(expanded.c.anchor_id, expanded.c.content_hash).where(expanded.c.subject_id == subject_id)
        )
    }
    for index, row in enumerate(note_rows, 1):
        have = existing_notes.get(row["anchor_id"])
        if have is not None:
            if have != row["content_hash"]:
                raise RuntimeError(f"existing note anchor differs: {row['anchor_id']}")
            continue
        bind.execute(expanded.insert().values(
            subject_id=subject_id,
            syllabus_chapter_id=chapter_id,
            anchor_id=row["anchor_id"],
            kind=row["kind"],
            package_section=row.get("package_section"),
            sort_order=row.get("sort_order", index),
            heading_en=row["heading_en"],
            heading_te=row.get("heading_te"),
            body_en=row.get("body_en"),
            body_te=row.get("body_te"),
            sources=row.get("sources") or [],
            core_connections=row.get("core_connections") or [],
            package_batch_id=note_manifest["batch_id"],
            collection_id=COLLECTION,
            content_hash=row["content_hash"],
            created_at=datetime.utcnow(),
        ))

    loaded_anchors = {
        value for (value,) in bind.execute(
            sa.select(expanded.c.anchor_id).where(expanded.c.subject_id == subject_id)
        )
    }
    subtopic_ids = {
        row.slug: row.id for row in bind.execute(sa.select(subtopics.c.slug, subtopics.c.id))
    }
    existing_questions = {
        (row.source, row.source_qid): row.content_hash
        for row in bind.execute(sa.select(questions.c.source, questions.c.source_qid, questions.c.content_hash))
        if row.source and row.source_qid
    }
    display = {"easy": "E", "medium": "M", "tough": "H", "toughest": "H"}

    for package_name in PACKAGES:
        _package, manifest, records = _load_package(package_name)
        for record in records:
            # The reviewed collection is intentionally independent from the
            # legacy bank.  Some legacy rows use the same source identifiers
            # for older wording, so give the fresh row a stable,
            # collection-scoped database identity instead of overwriting it.
            identity_qid = f"{COLLECTION}:{record['source_qid']}"
            key = (record["source"], identity_qid)
            content_hash = _content_hash(record)
            if key in existing_questions:
                if existing_questions[key] != content_hash:
                    raise RuntimeError(f"existing question identity differs: {key}")
                continue
            anchors = (record.get("expanded_note") or {}).get("anchor_ids") or []
            missing = sorted(set(anchors) - loaded_anchors)
            if missing:
                raise RuntimeError(f"unresolved note anchors for {record['source_qid']}: {missing}")
            options = record["options"]
            subtopic_id = subtopic_ids.get(record.get("subtopic_slug"))
            if record.get("subtopic_slug") and subtopic_id is None:
                raise RuntimeError(f"unknown subtopic: {record['subtopic_slug']}")
            bind.execute(questions.insert().values(
                subject_id=subject_id,
                chapter_id=None,
                source_type="chapter",
                q_hash=_q_hash(record),
                difficulty=display[record["difficulty"]],
                question_en=record["question_en"].strip(),
                question_te=record["question_te"].strip(),
                options_en={key: options[key]["en"] for key in ("a", "b", "c", "d")},
                options_te={key: options[key]["te"] for key in ("a", "b", "c", "d")},
                correct_answer=record["correct_answer"],
                explanation_en=record["explanation_en"].strip(),
                explanation_te=record["explanation_te"].strip(),
                note_section_num=None,
                note_target_slug=record.get("subtopic_slug") or record["chapter_slug"],
                source_trace=_trace(record, manifest),
                import_ref=record["source_qid"],
                created_at=datetime.utcnow(),
                updated_at=datetime.utcnow(),
                syllabus_chapter_id=chapter_id,
                subtopic_id=subtopic_id,
                secondary_tags={
                    "chapters": record.get("secondary_chapters") or [],
                    "microtopics": record.get("microtopic_slugs") or [],
                    "coverage_scope": record["coverage_scope"],
                },
                source=record["source"],
                source_file=record.get("source_file"),
                source_qid=identity_qid,
                qtype=record["qtype"],
                review_status=record["review_status"],
                batch_id=record["batch_id"],
                content_hash=content_hash,
                collection_id=COLLECTION,
            ))


def downgrade():
    bind = op.get_bind()
    meta = sa.MetaData()
    questions = sa.Table("questions", meta, autoload_with=bind)
    expanded = sa.Table("expanded_notes", meta, autoload_with=bind)
    batches = tuple(PACKAGES)
    bind.execute(questions.delete().where(questions.c.batch_id.in_(batches)))
    bind.execute(expanded.delete().where(expanded.c.package_batch_id == PACKAGES[0]))
