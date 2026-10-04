"""questions.subject_id guard (replaces the old startup schema patch)

Older databases were created before ``questions.subject_id`` existed; ``_patch_schema()`` used to add it
on every application start. That logic now lives here, runs once, and works on SQLite and PostgreSQL.

Revision ID: a1b2c3d4e5f6
Revises: c68decc8a6c3
Create Date: 2026-10-04 12:00:00+00:00
"""
from alembic import op
import sqlalchemy as sa

revision = "a1b2c3d4e5f6"
down_revision = "c68decc8a6c3"
branch_labels = None
depends_on = None


def upgrade() -> None:
    bind = op.get_bind()
    insp = sa.inspect(bind)
    if not insp.has_table("questions"):
        return
    cols = {c["name"] for c in insp.get_columns("questions")}
    if "subject_id" not in cols:
        # nullable first: existing rows have no value yet
        op.add_column("questions", sa.Column("subject_id", sa.Integer(), nullable=True))
        # chapter questions inherit the subject of their chapter; rows with no chapter stay NULL and
        # must be assigned by the content loader (nothing is guessed here)
        op.execute(sa.text(
            "UPDATE questions SET subject_id = "
            "(SELECT chapters.subject_id FROM chapters WHERE chapters.id = questions.chapter_id) "
            "WHERE chapter_id IS NOT NULL"))
        if bind.dialect.name == "postgresql":
            op.create_foreign_key("fk_questions_subject_id", "questions", "subjects", ["subject_id"], ["id"])
            nulls = bind.execute(sa.text("SELECT COUNT(*) FROM questions WHERE subject_id IS NULL")).scalar()
            if not nulls:
                op.alter_column("questions", "subject_id", nullable=False)
    indexes = {ix["name"] for ix in sa.inspect(bind).get_indexes("questions")}
    if "ix_questions_subject_id" not in indexes:
        op.create_index("ix_questions_subject_id", "questions", ["subject_id"], unique=False)


def downgrade() -> None:
    # The column is part of the baseline schema; nothing to undo.
    pass
