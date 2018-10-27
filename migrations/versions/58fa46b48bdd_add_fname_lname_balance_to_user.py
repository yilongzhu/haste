"""Add fname, lname, balance to User

Revision ID: 58fa46b48bdd
Revises: 4379ab396176
Create Date: 2018-10-27 19:02:47.650333

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '58fa46b48bdd'
down_revision = '4379ab396176'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('balance', sa.Float(), nullable=True))
    op.add_column('user', sa.Column('first_name', sa.String(length=48), nullable=True))
    op.add_column('user', sa.Column('last_name', sa.String(length=48), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'last_name')
    op.drop_column('user', 'first_name')
    op.drop_column('user', 'balance')
    # ### end Alembic commands ###
