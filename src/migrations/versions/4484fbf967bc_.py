"""empty message

Revision ID: 4484fbf967bc
Revises: 
Create Date: 2022-03-13 12:26:07.489434

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4484fbf967bc'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'user', ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user', type_='unique')
    # ### end Alembic commands ###