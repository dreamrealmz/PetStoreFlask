"""empty message

Revision ID: 5af1b62c29ad
Revises: 2f74ffa3921a
Create Date: 2022-07-21 19:07:49.292984

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5af1b62c29ad'
down_revision = '2f74ffa3921a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('breeds',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('pets', sa.Column('breed_id', sa.Integer(), nullable=False))
    op.alter_column('pets', 'name',
               existing_type=sa.VARCHAR(length=200),
               nullable=False)
    op.create_foreign_key(None, 'pets', 'breeds', ['breed_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'pets', type_='foreignkey')
    op.alter_column('pets', 'name',
               existing_type=sa.VARCHAR(length=200),
               nullable=True)
    op.drop_column('pets', 'breed_id')
    op.drop_table('breeds')
    # ### end Alembic commands ###