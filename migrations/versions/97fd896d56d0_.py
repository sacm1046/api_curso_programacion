"""empty message

Revision ID: 97fd896d56d0
Revises: fae810e8e752
Create Date: 2020-08-02 00:43:36.425404

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '97fd896d56d0'
down_revision = 'fae810e8e752'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('image', sa.String(length=50), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('posts', 'image')
    # ### end Alembic commands ###
