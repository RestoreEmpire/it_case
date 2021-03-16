"""empty message

Revision ID: b5df6504fef7
Revises: c603ef23cee4
Create Date: 2021-03-13 11:39:31.538414

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'b5df6504fef7'
down_revision = 'c603ef23cee4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('positions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('position', sa.String(length=64), nullable=True),
    sa.Column('duty', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_positions_duty'), 'positions', ['duty'], unique=False)
    op.create_index(op.f('ix_positions_position'), 'positions', ['position'], unique=False)
    op.drop_column('users', 'position')
    op.drop_column('users', 'role')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('role', mysql.VARCHAR(length=20), nullable=True))
    op.add_column('users', sa.Column('position', mysql.VARCHAR(length=64), nullable=True))
    op.drop_index(op.f('ix_positions_position'), table_name='positions')
    op.drop_index(op.f('ix_positions_duty'), table_name='positions')
    op.drop_table('positions')
    # ### end Alembic commands ###
