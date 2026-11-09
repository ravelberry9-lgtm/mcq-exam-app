"""Add Unit 6 state without modifying legacy content or learner state."""
from alembic import op
import sqlalchemy as sa
revision='u6_20261109'
down_revision='t6o7p8q9r0s1'
branch_labels=None
depends_on=None
def upgrade():
    op.create_table('polity_unit6_state',sa.Column('device_id',sa.String(64),primary_key=True),sa.Column('item_id',sa.String(128),primary_key=True),sa.Column('saved',sa.Boolean(),nullable=False,server_default=sa.false()),sa.Column('seen_count',sa.Integer(),nullable=False,server_default='0'),sa.Column('wrong_count',sa.Integer(),nullable=False,server_default='0'),sa.Column('last_seen_at',sa.DateTime()))
    op.create_table('polity_unit6_progress',sa.Column('device_id',sa.String(64),primary_key=True),sa.Column('chapter_id',sa.String(32),primary_key=True),sa.Column('completed',sa.Boolean(),nullable=False,server_default=sa.false()),sa.Column('updated_at',sa.DateTime(),nullable=False))
    op.create_table('polity_unit6_exam',sa.Column('id',sa.String(36),primary_key=True),sa.Column('device_id',sa.String(64),nullable=False),sa.Column('questions',sa.JSON(),nullable=False),sa.Column('answers',sa.JSON(),nullable=False),sa.Column('started_at',sa.DateTime(),nullable=False),sa.Column('deadline',sa.DateTime(),nullable=False),sa.Column('submitted_at',sa.DateTime()),sa.Column('score',sa.Integer()))
    op.create_index('ix_polity_unit6_exam_device_id','polity_unit6_exam',['device_id'])
def downgrade():
    # Retain learner state on application rollback; these additive tables are harmless.
    pass
