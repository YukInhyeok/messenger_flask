"""empty message

Revision ID: e48db54ebc46
Revises: 4e8dee13584f
Create Date: 2024-06-13 12:52:47.023965

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e48db54ebc46'
down_revision = '4e8dee13584f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('chat', schema=None) as batch_op:
        batch_op.add_column(sa.Column('name', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('chat', schema=None) as batch_op:
        batch_op.drop_column('name')

    # ### end Alembic commands ###
