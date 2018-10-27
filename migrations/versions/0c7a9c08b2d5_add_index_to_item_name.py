"""Add index to Item.name

Revision ID: 0c7a9c08b2d5
Revises: 35ec7d78b091
Create Date: 2018-10-27 13:07:51.545441

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0c7a9c08b2d5'
down_revision = '35ec7d78b091'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(op.f('ix_item_name'), 'item', ['name'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_item_name'), table_name='item')
    # ### end Alembic commands ###
