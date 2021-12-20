"""create posts table

Revision ID: 8762edb82d28
Revises: 
Create Date: 2021-12-19 17:56:22.809467

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8762edb82d28'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
                    sa.Column('title', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_table('posts')
    pass
