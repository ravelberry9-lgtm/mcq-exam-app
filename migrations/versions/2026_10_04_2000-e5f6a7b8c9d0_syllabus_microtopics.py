"""syllabus microtopics + taxonomy version columns (additive only)

Adds the syllabus_microtopics table and two nullable columns on syllabus_subtopics (search_key_te, taxonomy_version).
Nothing existing is changed, moved, backfilled or deleted.

Revision ID: e5f6a7b8c9d0
Revises: d4e5f6a7b8c9
Create Date: 2026-10-04 20:00:00+00:00
"""
from alembic import op
import sqlalchemy as sa

revision = "e5f6a7b8c9d0"
down_revision = "d4e5f6a7b8c9"
branch_labels = None
depends_on = None


def upgrade() -> None:
    bind = op.get_bind()
    insp = sa.inspect(bind)
    have = {c["name"] for c in insp.get_columns("syllabus_subtopics")}
    add = [(n, t) for n, t in (("search_key_te", sa.String(256)), ("taxonomy_version", sa.String(32))) if n not in have]
    if add:
        with op.batch_alter_table("syllabus_subtopics") as batch:
            for name, typ in add:
                batch.add_column(sa.Column(name, typ, nullable=True))
    if not insp.has_table("syllabus_microtopics"):
        op.create_table(
            "syllabus_microtopics",
            sa.Column("id", sa.Integer(), nullable=False),
            sa.Column("subtopic_id", sa.Integer(), nullable=False),
            sa.Column("slug", sa.String(128), nullable=False),
            sa.Column("micro_en", sa.String(256), nullable=False),
            sa.Column("micro_te", sa.String(256), nullable=False),
            sa.Column("search_key_te", sa.String(256), nullable=True),
            sa.Column("scope", sa.String(24), nullable=False),
            sa.Column("old_draft_slug", sa.String(128), nullable=True),
            sa.Column("taxonomy_version", sa.String(32), nullable=True),
            sa.Column("sort_order", sa.Integer(), nullable=True),
            sa.ForeignKeyConstraint(["subtopic_id"], ["syllabus_subtopics.id"], ondelete="CASCADE"),
            sa.PrimaryKeyConstraint("id"),
            sa.UniqueConstraint("slug"),
            sa.CheckConstraint("scope IN ('direct','supplementary_context')", name="ck_syllabus_microtopics_scope"),
        )
        op.create_index("ix_syllabus_microtopics_subtopic_id", "syllabus_microtopics", ["subtopic_id"])


def downgrade() -> None:
    bind = op.get_bind()
    insp = sa.inspect(bind)
    if insp.has_table("syllabus_microtopics"):
        if bind.execute(sa.text("SELECT COUNT(*) FROM syllabus_microtopics")).scalar():
            raise RuntimeError("Refusing to downgrade: syllabus_microtopics holds rows. Export them first; nothing was changed.")
        op.drop_index("ix_syllabus_microtopics_subtopic_id", table_name="syllabus_microtopics")
        op.drop_table("syllabus_microtopics")
    have = {c["name"] for c in sa.inspect(bind).get_columns("syllabus_subtopics")}
    drop = [n for n in ("search_key_te", "taxonomy_version") if n in have]
    if drop:
        if "taxonomy_version" in drop and bind.execute(sa.text("SELECT COUNT(*) FROM syllabus_subtopics WHERE taxonomy_version IS NOT NULL")).scalar():
            raise RuntimeError("Refusing to downgrade: syllabus_subtopics carries taxonomy versions. Nothing was changed.")
        with op.batch_alter_table("syllabus_subtopics") as batch:
            for n in drop:
                batch.drop_column(n)
