"""create equipos table

Revision ID: de4912cac39c
Revises: 
Create Date: 2023-06-16 11:48:28.160787

"""
from alembic import op
import sqlalchemy as sa
from datetime import datetime

# revision identifiers, used by Alembic.
revision = 'de4912cac39c'
down_revision = None
branch_labels = None
depends_on = None

#Change this model according to your needs

def upgrade() -> None:
    op.create_table('mymodels',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('created_at', sa.DateTime, default=datetime.now())
    )

def downgrade() -> None:
    op.drop_table('mymodels')
