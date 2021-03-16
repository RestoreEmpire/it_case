"""empty message

Revision ID: c603ef23cee4
Revises: ffc1aac56a46
Create Date: 2021-03-12 21:12:36.218818

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c603ef23cee4'
down_revision = 'ffc1aac56a46'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('first_name', sa.String(length=32), nullable=True))
    op.add_column('users', sa.Column('last_name', sa.String(length=32), nullable=True))
    op.add_column('users', sa.Column('patronym', sa.String(length=32), nullable=True))
    op.add_column('users', sa.Column('position', sa.String(length=64), nullable=True))
    op.add_column('users', sa.Column('role', sa.String(length=20), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'role')
    op.drop_column('users', 'position')
    op.drop_column('users', 'patronym')
    op.drop_column('users', 'last_name')
    op.drop_column('users', 'first_name')
    # ### end Alembic commands ###
