"""empty message

Revision ID: 4cb8b6830ab1
Revises: a34feacadab5
Create Date: 2017-06-27 10:30:58.005728

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '4cb8b6830ab1'
down_revision = 'a34feacadab5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('batches', sa.Column('sample_type', sa.SmallInteger(), nullable=True))
    op.drop_column('batches', 'type')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('batches', sa.Column('type', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True))
    op.drop_column('batches', 'sample_type')
    # ### end Alembic commands ###