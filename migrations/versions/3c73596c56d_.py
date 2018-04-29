"""Create supermarket model

Revision ID: 3c73596c56d
Revises: None
Create Date: 2018-04-29 11:49:02.746881

"""

# revision identifiers, used by Alembic.
revision = '3c73596c56d'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table(
        'supermarket',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(length=120), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('name')
    )


def downgrade():
    op.drop_table('supermarket')
