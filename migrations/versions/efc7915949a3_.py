"""empty message

Revision ID: efc7915949a3
Revises: 4cb8b6830ab1
Create Date: 2017-06-27 11:07:10.422665

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'efc7915949a3'
down_revision = '4cb8b6830ab1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('samples', sa.Column('amount_type', sa.SmallInteger(), nullable=True))
    op.drop_column('samples', 'type')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('samples', sa.Column('type', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True))
    op.drop_column('samples', 'amount_type')
    # ### end Alembic commands ###
