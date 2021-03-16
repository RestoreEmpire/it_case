"""empty message

Revision ID: a6f2a3f70604
Revises: a22adb6e6fd5
Create Date: 2021-03-14 00:43:21.435175

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a6f2a3f70604'
down_revision = 'a22adb6e6fd5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('mentors',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=32), nullable=True),
    sa.Column('last_name', sa.String(length=32), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('users', sa.Column('mentors_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'users', 'mentors', ['mentors_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='foreignkey')
    op.drop_column('users', 'mentors_id')
    op.drop_table('mentors')
    # ### end Alembic commands ###