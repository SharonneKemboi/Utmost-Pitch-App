"""Initial Migration

Revision ID: 7c5a28c41ee9
Revises: c0b0c806924e
Create Date: 2022-05-09 21:14:29.543669

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7c5a28c41ee9'
down_revision = 'c0b0c806924e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('date', sa.String(), nullable=True))
    op.add_column('comments', sa.Column('time', sa.String(), nullable=True))
    op.add_column('pitches', sa.Column('date', sa.String(), nullable=True))
    op.add_column('pitches', sa.Column('time', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('pitches', 'time')
    op.drop_column('pitches', 'date')
    op.drop_column('comments', 'time')
    op.drop_column('comments', 'date')
    # ### end Alembic commands ###