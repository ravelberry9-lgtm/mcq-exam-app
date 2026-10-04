"""questions.subject_id guard (replaces the old startup schema patch)

Older databases were created before ``questions.subject_id`` existed; ``_patch_schema()`` used to add it
on every application start. That logic now lives here, runs once, and works on SQLite and PostgreSQL.

Policy for rows that cannot be assigned a subject: **nothing is guessed**. Chapter questions inherit their
chapter's subject. If any question is still without a subject afterwards the migration stops with a clear
message (PostgreSQL rolls everything back; SQLite leaves the harmless new nullable column, and re-running
repeats the same check). Assign those rows yourself, then run the upgrade again, e.g.::

    UPDATE questions SET subject_id = (SELECT id FROM subjects WHERE slug = 'your_subject') WHERE subject_id IS NULL;

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
        op.add_column("questions", sa.Column("subject_id", sa.Integer(), nullable=True))
    if insp.has_table("chapters"):
        op.execute(sa.text(
            "UPDATE questions SET subject_id = "
            "(SELECT chapters.subject_id FROM chapters WHERE chapters.id = questions.chapter_id) "
            "WHERE subject_id IS NULL AND chapter_id IS NOT NULL"))
    nulls = bind.execute(sa.text("SELECT COUNT(*) FROM questions WHERE subject_id IS NULL")).scalar()
    if nulls:
        raise RuntimeError(
            f"{nulls} question(s) have no subject_id and no chapter to inherit one from. Assign them explicitly, "
            "then re-run the upgrade (see the docstring of migration a1b2c3d4e5f6). Nothing was guessed.")
    if bind.dialect.name == "postgresql":
        fks = [fk for fk in sa.inspect(bind).get_foreign_keys("questions") if fk["constrained_columns"] == ["subject_id"]]
        if not fks:
            op.create_foreign_key("fk_questions_subject_id", "questions", "subjects", ["subject_id"], ["id"])
        col = next(c for c in sa.inspect(bind).get_columns("questions") if c["name"] == "subject_id")
        if col["nullable"]:
            op.alter_column("questions", "subject_id", nullable=False)
    indexes = {ix["name"] for ix in sa.inspect(bind).get_indexes("questions")}
    if "ix_questions_subject_id" not in indexes:
        op.create_index("ix_questions_subject_id", "questions", ["subject_id"], unique=False)


def downgrade() -> None:
    # The column is part of the baseline schema; nothing to undo.
    pass
