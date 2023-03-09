"""kyle table

Revision ID: 0d6d7b150f41
Revises: 
Create Date: 2023-03-06 15:32:43.028720

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0d6d7b150f41'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    conn = op.get_bind()
    if not conn.dialect.has_table(conn, 'kyle_items'):
        op.create_table('kyle_items',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('first_name', sa.String(), nullable=True),
        sa.Column('last_name', sa.String(), nullable=True),
        sa.PrimaryKeyConstraint('id')
        )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('kyle_items')
    # ### end Alembic commands ###
