"""explicit collection id + per-chapter learner collection switch (additive only)

Adds nullable ``collection_id`` to ``questions`` and ``expanded_notes`` (existing rows stay NULL = legacy) and two small tables:
``chapter_collection_setting`` (which collection learners see per canonical chapter; no row = legacy) and
``chapter_collection_log`` (append-only audit of every switch). No row of any existing table is changed, moved or deleted.

Revision ID: c9d0e1f2a3b4
Revises: b8c9d0e1f2a3
Create Date: 2026-10-09 12:00:00+00:00
"""
from alembic import op
import sqlalchemy as sa

revision = "c9d0e1f2a3b4"
down_revision = "b8c9d0e1f2a3"
branch_labels = None
depends_on = None


def _has_col(insp, table, col):
    return any(c["name"] == col for c in insp.get_columns(table))


def upgrade() -> None:
    insp = sa.inspect(op.get_bind())
    for table in ("questions", "expanded_notes"):
        if not _has_col(insp, table, "collection_id"):
            op.add_column(table, sa.Column("collection_id", sa.String(64), nullable=True))
            op.create_index(f"ix_{table}_collection_id", table, ["collection_id"])
    if not insp.has_table("chapter_collection_setting"):
        op.create_table(
            "chapter_collection_setting",
            sa.Column("id", sa.Integer(), nullable=False),
            sa.Column("syllabus_chapter_id", sa.Integer(), nullable=False),
            sa.Column("active_collection", sa.String(64), nullable=True),
            sa.Column("updated_by", sa.String(80), nullable=True),
            sa.Column("updated_at", sa.DateTime(), nullable=True),
            sa.ForeignKeyConstraint(["syllabus_chapter_id"], ["syllabus_chapters.id"], ondelete="CASCADE"),
            sa.PrimaryKeyConstraint("id"),
            sa.UniqueConstraint("syllabus_chapter_id", name="uq_chapter_collection_setting_chapter"),
        )
    if not insp.has_table("chapter_collection_log"):
        op.create_table(
            "chapter_collection_log",
            sa.Column("id", sa.Integer(), nullable=False),
            sa.Column("syllabus_chapter_id", sa.Integer(), nullable=False),
            sa.Column("chapter_slug", sa.String(96), nullable=False),
            sa.Column("from_collection", sa.String(64), nullable=True),
            sa.Column("to_collection", sa.String(64), nullable=True),
            sa.Column("actor", sa.String(80), nullable=False),
            sa.Column("remote_addr", sa.String(64), nullable=True),
            sa.Column("changed_at", sa.DateTime(), nullable=False),
            sa.Column("readiness", sa.JSON(), nullable=True),
            sa.Column("reason", sa.String(300), nullable=True),
            sa.ForeignKeyConstraint(["syllabus_chapter_id"], ["syllabus_chapters.id"], ondelete="CASCADE"),
            sa.PrimaryKeyConstraint("id"),
        )
        op.create_index("ix_chapter_collection_log_syllabus_chapter_id", "chapter_collection_log", ["syllabus_chapter_id"])


def downgrade() -> None:
    """Refuses while any setting/log row or any collection-tagged row exists, so no switch history or membership is lost."""
    bind = op.get_bind()
    insp = sa.inspect(bind)
    held = []
    for t in ("chapter_collection_setting", "chapter_collection_log"):
        if insp.has_table(t) and bind.execute(sa.text(f"SELECT COUNT(*) FROM {t}")).scalar():
            held.append(t)
    for t in ("questions", "expanded_notes"):
        if bind.execute(sa.text(f"SELECT COUNT(*) FROM {t} WHERE collection_id IS NOT NULL")).scalar():
            held.append(f"{t}.collection_id")
    if held:
        raise RuntimeError(f"refusing to downgrade: {', '.join(held)} hold data. Nothing was changed.")
    op.drop_table("chapter_collection_log")
    op.drop_table("chapter_collection_setting")
    for table in ("expanded_notes", "questions"):
        op.drop_index(f"ix_{table}_collection_id", table_name=table)
        op.drop_column(table, "collection_id")
