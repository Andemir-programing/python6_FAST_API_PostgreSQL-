"""add tables

Revision ID: d042be684057
Revises: 
Create Date: 2023-05-31 19:02:30.919746

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd042be684057'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('keys',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('code', sa.String(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_keys_id'), 'keys', ['id'], unique=False)
    op.create_table('person',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('firstname', sa.String(length=32), nullable=False),
    sa.Column('lastname', sa.String(length=32), nullable=False),
    sa.Column('spouse_id', sa.Integer(), nullable=True),
    sa.Column('kids_ids', sa.ARRAY(sa.Integer()), nullable=True),
    sa.Column('is_married', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_person_id'), 'person', ['id'], unique=False)
    op.create_table('products',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=32), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_products_id'), 'products', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_products_id'), table_name='products')
    op.drop_table('products')
    op.drop_index(op.f('ix_person_id'), table_name='person')
    op.drop_table('person')
    op.drop_index(op.f('ix_keys_id'), table_name='keys')
    op.drop_table('keys')
    # ### end Alembic commands ###
