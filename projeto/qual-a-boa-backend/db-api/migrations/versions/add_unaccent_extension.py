"""add unaccent extension

Revision ID: add_unaccent_extension
Revises: 
Create Date: 2024-04-05 22:15:00.000000

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'add_unaccent_extension'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    op.execute('CREATE EXTENSION IF NOT EXISTS unaccent')

def downgrade():
    op.execute('DROP EXTENSION IF EXISTS unaccent') 