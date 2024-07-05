"""empty message

Revision ID: 6170f85603b2
Revises: e41cac53ee20
Create Date: 2024-07-05 12:24:07.438575

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6170f85603b2'
down_revision = 'e41cac53ee20'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('recipes', schema=None) as batch_op:
        batch_op.alter_column('minutes_to_complete',
               existing_type=sa.INTEGER(),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('recipes', schema=None) as batch_op:
        batch_op.alter_column('minutes_to_complete',
               existing_type=sa.INTEGER(),
               nullable=True)

    # ### end Alembic commands ###