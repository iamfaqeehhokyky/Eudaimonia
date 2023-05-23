"""empty message

Revision ID: 194a558753c0
Revises: 6006c6fad71f
Create Date: 2023-05-21 17:44:56.476820

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '194a558753c0'
down_revision = '6006c6fad71f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('stress_management_resource',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=255), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('user')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=50), nullable=True),
    sa.Column('email', sa.VARCHAR(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.drop_table('stress_management_resource')
    # ### end Alembic commands ###
