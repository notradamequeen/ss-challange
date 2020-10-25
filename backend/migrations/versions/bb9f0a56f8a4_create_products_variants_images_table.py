"""create products-variants-images table

Revision ID: bb9f0a56f8a4
Revises: 9194e59d14d9
Create Date: 2020-10-25 12:57:55.068488

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'bb9f0a56f8a4'
down_revision = '9194e59d14d9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('variants',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('size', sa.String(length=100), nullable=True),
    sa.Column('color', sa.String(length=25), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('variant_images',
    sa.Column('image_id', sa.Integer(), nullable=False),
    sa.Column('variant_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['image_id'], ['images.id'], ),
    sa.ForeignKeyConstraint(['variant_id'], ['variants.id'], ),
    sa.PrimaryKeyConstraint('image_id', 'variant_id')
    )
    op.drop_index('email', table_name='user')
    op.drop_index('username', table_name='user')
    op.drop_table('user')
    op.add_column('products', sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True))
    op.add_column('products', sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True))
    op.drop_column('products', 'updated_on')
    op.drop_column('products', 'created_on')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('products', sa.Column('created_on', mysql.DATETIME(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True))
    op.add_column('products', sa.Column('updated_on', mysql.DATETIME(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True))
    op.drop_column('products', 'updated_at')
    op.drop_column('products', 'created_at')
    op.create_table('user',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('email', mysql.VARCHAR(length=50), nullable=False),
    sa.Column('admin', mysql.TINYINT(display_width=1), autoincrement=False, nullable=False),
    sa.Column('username', mysql.VARCHAR(length=50), nullable=True),
    sa.Column('password_hash', mysql.VARCHAR(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='latin1',
    mysql_engine='InnoDB'
    )
    op.create_index('username', 'user', ['username'], unique=True)
    op.create_index('email', 'user', ['email'], unique=True)
    op.drop_table('variant_images')
    op.drop_table('variants')
    # ### end Alembic commands ###
