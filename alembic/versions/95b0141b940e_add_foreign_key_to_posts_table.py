"""add foreign key to posts table

Revision ID: 95b0141b940e
Revises: 2c568fefa97d
Create Date: 2021-12-20 17:33:14.648816

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '95b0141b940e'
down_revision = '2c568fefa97d'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('posts_users_fk', source_table='posts', referent_table='users',
                          local_cols=['owner_id'], remote_cols=['id'], ondelete='CASCADE')
    pass


def downgrade():
    op.drop_constraint('posts_users_fk', table_name='posts')
    op.drop_column('posts', 'owner_id')
    pass
