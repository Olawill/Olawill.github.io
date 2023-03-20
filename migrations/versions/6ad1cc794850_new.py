"""New

Revision ID: 6ad1cc794850
Revises: 2c141f6f88bf
Create Date: 2023-03-17 16:39:53.518864

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6ad1cc794850'
down_revision = '2c141f6f88bf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('cart_item', sa.Column('price', sa.Integer(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('cart_item', 'price')
    # ### end Alembic commands ###
