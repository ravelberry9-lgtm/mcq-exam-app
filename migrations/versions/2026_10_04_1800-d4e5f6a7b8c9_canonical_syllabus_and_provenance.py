"""canonical syllabus hierarchy + question provenance (additive only)

Adds: syllabus_units, syllabus_chapters, syllabus_subtopics, chapter_source_map, and nullable provenance /
canonical-identity columns on questions with a unique (source, source_qid) index.
Nothing existing is changed, moved, backfilled or deleted: every new questions column is NULL for existing rows.

Revision ID: d4e5f6a7b8c9
Revises: c3d4e5f6a7b8
Create Date: 2026-10-04 18:00:00+00:00
"""
from alembic import op
import sqlalchemy as sa

revision = "d4e5f6a7b8c9"
down_revision = "c3d4e5f6a7b8"
branch_labels = None
depends_on = None

NEW_Q_COLS = [
    ("syllabus_chapter_id", sa.Integer()), ("subtopic_id", sa.Integer()), ("secondary_tags", sa.JSON()),
    ("source", sa.String(24)), ("source_file", sa.String(256)), ("source_qid", sa.String(128)),
    ("source_chapter", sa.String(64)), ("qtype", sa.String(24)), ("review_status", sa.String(24)),
    ("batch_id", sa.String(64)), ("content_hash", sa.String(32)),
]


def _ix(insp, table):
    return {i["name"] for i in insp.get_indexes(table)}


def upgrade() -> None:
    bind = op.get_bind()
    insp = sa.inspect(bind)

    if not insp.has_table("syllabus_units"):
        op.create_table(
            "syllabus_units",
            sa.Column("id", sa.Integer(), nullable=False),
            sa.Column("subject_id", sa.Integer(), nullable=False),
            sa.Column("unit_num", sa.Integer(), nullable=False),
            sa.Column("slug", sa.String(64), nullable=False),
            sa.Column("title_en", sa.String(256), nullable=False),
            sa.Column("title_te", sa.String(256), nullable=False),
            sa.Column("sort_order", sa.Integer(), nullable=True),
            sa.ForeignKeyConstraint(["subject_id"], ["subjects.id"], ondelete="CASCADE"),
            sa.PrimaryKeyConstraint("id"),
            sa.UniqueConstraint("slug"),
            sa.UniqueConstraint("subject_id", "unit_num"),
        )
        op.create_index("ix_syllabus_units_subject_id", "syllabus_units", ["subject_id"])

    if not insp.has_table("syllabus_chapters"):
        op.create_table(
            "syllabus_chapters",
            sa.Column("id", sa.Integer(), nullable=False),
            sa.Column("subject_id", sa.Integer(), nullable=False),
            sa.Column("unit_id", sa.Integer(), nullable=True),
            sa.Column("chapter_num", sa.Integer(), nullable=True),
            sa.Column("slug", sa.String(96), nullable=False),
            sa.Column("title_en", sa.String(256), nullable=False),
            sa.Column("title_te", sa.String(256), nullable=False),
            sa.Column("classification", sa.String(16), nullable=False),
            sa.Column("supplementary_type", sa.String(48), nullable=True),
            sa.Column("sort_order", sa.Integer(), nullable=True),
            sa.ForeignKeyConstraint(["subject_id"], ["subjects.id"], ondelete="CASCADE"),
            sa.ForeignKeyConstraint(["unit_id"], ["syllabus_units.id"], ondelete="CASCADE"),
            sa.PrimaryKeyConstraint("id"),
            sa.UniqueConstraint("slug"),
            sa.UniqueConstraint("subject_id", "chapter_num"),
            sa.CheckConstraint("classification IN ('direct','bridge','thematic','supplementary')", name="ck_syllabus_chapters_classification"),
            sa.CheckConstraint(
                "(classification = 'supplementary' AND supplementary_type IS NOT NULL AND unit_id IS NULL AND chapter_num IS NULL) OR "
                "(classification <> 'supplementary' AND supplementary_type IS NULL AND unit_id IS NOT NULL AND chapter_num IS NOT NULL)",
                name="ck_syllabus_chapters_core_vs_supplementary"),
        )
        op.create_index("ix_syllabus_chapters_subject_id", "syllabus_chapters", ["subject_id"])
        op.create_index("ix_syllabus_chapters_unit_id", "syllabus_chapters", ["unit_id"])

    if not insp.has_table("syllabus_subtopics"):
        op.create_table(
            "syllabus_subtopics",
            sa.Column("id", sa.Integer(), nullable=False),
            sa.Column("chapter_id", sa.Integer(), nullable=False),
            sa.Column("slug", sa.String(128), nullable=False),
            sa.Column("subtopic_en", sa.String(256), nullable=False),
            sa.Column("subtopic_te", sa.String(256), nullable=False),
            sa.Column("sort_order", sa.Integer(), nullable=True),
            sa.ForeignKeyConstraint(["chapter_id"], ["syllabus_chapters.id"], ondelete="CASCADE"),
            sa.PrimaryKeyConstraint("id"),
            sa.UniqueConstraint("slug"),
        )
        op.create_index("ix_syllabus_subtopics_chapter_id", "syllabus_subtopics", ["chapter_id"])

    if not insp.has_table("chapter_source_map"):
        op.create_table(
            "chapter_source_map",
            sa.Column("id", sa.Integer(), nullable=False),
            sa.Column("subject_id", sa.Integer(), nullable=False),
            sa.Column("source_chapter_num", sa.Integer(), nullable=False),
            sa.Column("section_num", sa.Integer(), nullable=True),
            sa.Column("syllabus_chapter_id", sa.Integer(), nullable=False),
            sa.Column("subtopic_id", sa.Integer(), nullable=True),
            sa.Column("relation", sa.String(12), nullable=False),
            sa.Column("mapping_kind", sa.String(24), nullable=True),
            sa.Column("confidence", sa.String(8), nullable=True),
            sa.Column("reason", sa.String(512), nullable=True),
            sa.Column("status", sa.String(12), nullable=False),
            sa.ForeignKeyConstraint(["subject_id"], ["subjects.id"], ondelete="CASCADE"),
            sa.ForeignKeyConstraint(["syllabus_chapter_id"], ["syllabus_chapters.id"], ondelete="CASCADE"),
            sa.ForeignKeyConstraint(["subtopic_id"], ["syllabus_subtopics.id"], ondelete="SET NULL"),
            sa.PrimaryKeyConstraint("id"),
            sa.UniqueConstraint("subject_id", "source_chapter_num", "section_num", "syllabus_chapter_id", "relation"),
        )
        op.create_index("ix_chapter_source_map_subject_id", "chapter_source_map", ["subject_id"])
        op.create_index("ix_chapter_source_map_syllabus_chapter_id", "chapter_source_map", ["syllabus_chapter_id"])

    # questions: nullable columns only. Existing rows keep NULL in every one of them.
    have = {c["name"] for c in insp.get_columns("questions")}
    missing = [(n, t) for n, t in NEW_Q_COLS if n not in have]
    if missing:
        with op.batch_alter_table("questions") as batch:
            for name, typ in missing:
                batch.add_column(sa.Column(name, typ, nullable=True))
            if "syllabus_chapter_id" not in have:
                batch.create_foreign_key("fk_questions_syllabus_chapter_id", "syllabus_chapters", ["syllabus_chapter_id"], ["id"])
            if "subtopic_id" not in have:
                batch.create_foreign_key("fk_questions_subtopic_id", "syllabus_subtopics", ["subtopic_id"], ["id"])
    ix = _ix(sa.inspect(bind), "questions")
    for name, cols, uniq in [
        ("ix_questions_syllabus_chapter_id", ["syllabus_chapter_id"], False),
        ("ix_questions_subtopic_id", ["subtopic_id"], False),
        ("ix_questions_content_hash", ["content_hash"], False),
        ("uq_questions_source_qid", ["source", "source_qid"], True),
    ]:
        if name not in ix:
            op.create_index(name, "questions", cols, unique=uniq)


def downgrade() -> None:
    bind = op.get_bind()
    insp = sa.inspect(bind)
    # Refuse to discard canonical data or provenance that has been written.
    for table in ("chapter_source_map", "syllabus_subtopics", "syllabus_chapters", "syllabus_units"):
        if insp.has_table(table) and bind.execute(sa.text(f"SELECT COUNT(*) FROM {table}")).scalar():
            raise RuntimeError(f"Refusing to drop {table}: it contains rows. Nothing was changed.")
    cols = {c["name"] for c in insp.get_columns("questions")}
    if "source" in cols and bind.execute(sa.text(
            "SELECT COUNT(*) FROM questions WHERE source IS NOT NULL OR syllabus_chapter_id IS NOT NULL OR subtopic_id IS NOT NULL")).scalar():
        raise RuntimeError("Refusing to drop provenance columns: questions carry provenance or canonical mapping. Nothing was changed.")
    ix = _ix(insp, "questions")
    for name in ("uq_questions_source_qid", "ix_questions_content_hash", "ix_questions_subtopic_id", "ix_questions_syllabus_chapter_id"):
        if name in ix:
            op.drop_index(name, table_name="questions")
    present = [n for n, _ in NEW_Q_COLS if n in cols]
    if present:
        with op.batch_alter_table("questions") as batch:
            for fk in ("fk_questions_syllabus_chapter_id", "fk_questions_subtopic_id"):
                try:
                    batch.drop_constraint(fk, type_="foreignkey")
                except Exception:
                    pass
            for name in present:
                batch.drop_column(name)
    for table in ("chapter_source_map", "syllabus_subtopics", "syllabus_chapters", "syllabus_units"):
        if sa.inspect(bind).has_table(table):
            op.drop_table(table)
