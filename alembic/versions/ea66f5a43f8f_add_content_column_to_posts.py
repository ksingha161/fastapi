"""add content column to posts

Revision ID: ea66f5a43f8f
Revises: 8762edb82d28
Create Date: 2021-12-19 20:58:48.513284

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ea66f5a43f8f'
down_revision = '8762edb82d28'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
