"""Admin overrides and plain-text submissions for Unit 6."""
from alembic import op
import sqlalchemy as sa
revision='u6_20261110'
down_revision='u6_20261109'
branch_labels=None
depends_on=None
def upgrade():
    existing=set(sa.inspect(op.get_bind()).get_table_names())
    if 'polity_unit6_override' not in existing:op.create_table('polity_unit6_override',sa.Column('item_id',sa.String(128),primary_key=True),sa.Column('deleted',sa.Boolean(),nullable=False,server_default=sa.false()),sa.Column('data',sa.JSON(),nullable=False),sa.Column('updated_at',sa.DateTime(),nullable=False))
    if 'polity_unit6_submission' not in existing:op.create_table('polity_unit6_submission',sa.Column('id',sa.Integer(),primary_key=True,autoincrement=True),sa.Column('chapter_id',sa.String(32),nullable=False,server_default=''),sa.Column('text',sa.Text(),nullable=False),sa.Column('status',sa.String(16),nullable=False,server_default='new'),sa.Column('created_at',sa.DateTime(),nullable=False))
def downgrade():
    op.drop_table('polity_unit6_submission')
    op.drop_table('polity_unit6_override')
