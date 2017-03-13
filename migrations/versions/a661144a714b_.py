"""empty message

Revision ID: a661144a714b
Revises: 
Create Date: 2017-03-12 23:52:22.034578

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a661144a714b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_profile',
    sa.Column('userid', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=80), nullable=True),
    sa.Column('first_name', sa.String(length=80), nullable=True),
    sa.Column('last_name', sa.String(length=80), nullable=True),
    sa.Column('age', sa.String(length=10), nullable=True),
    sa.Column('gender', sa.String(length=10), nullable=True),
    sa.Column('biography', sa.String(length=255), nullable=True),
    sa.Column('pic', sa.String(length=80), nullable=True),
    sa.Column('created_on', sa.String(length=20), nullable=True),
    sa.PrimaryKeyConstraint('userid'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_profile')
    # ### end Alembic commands ###
