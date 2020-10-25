"""create products-variants-images table

Revision ID: 2a76aeba34c9
Revises: bb9f0a56f8a4
Create Date: 2020-10-25 14:09:40.537316

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2a76aeba34c9'
down_revision = 'bb9f0a56f8a4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('variants', sa.Column('product_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'variants', 'products', ['product_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'variants', type_='foreignkey')
    op.drop_column('variants', 'product_id')
    # ### end Alembic commands ###