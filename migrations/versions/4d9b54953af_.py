"""Create address table

Revision ID: 4d9b54953af
Revises: 3c73596c56d
Create Date: 2018-04-29 12:43:35.033923

"""

# revision identifiers, used by Alembic.
revision = '4d9b54953af'
down_revision = '3c73596c56d'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table('address',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('street', sa.String(length=120), nullable=True),
                    sa.Column('postal_code', sa.String(
                        length=120), nullable=True),
                    sa.Column('city', sa.String(length=120), nullable=True),
                    sa.Column('country', sa.String(length=120), nullable=True),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.add_column('supermarket', sa.Column(
        'address_id', sa.Integer(), nullable=False))
    op.alter_column('supermarket', 'name',
                    existing_type=sa.VARCHAR(length=120),
                    nullable=False)
    op.drop_constraint('supermarket_name_key', 'supermarket', type_='unique')


def downgrade():
    op.create_unique_constraint(
        'supermarket_name_key', 'supermarket', ['name'])
    op.alter_column('supermarket', 'name',
                    existing_type=sa.VARCHAR(length=120),
                    nullable=True)
    op.drop_column('supermarket', 'address_id')
    op.drop_table('address')
