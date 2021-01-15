"""empty message

Revision ID: 6314551fe3a7
Revises: a3fb59fea6c2
Create Date: 2021-01-15 22:29:59.208250

"""

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


# revision identifiers, used by Alembic.
revision = '6314551fe3a7'
down_revision = 'a3fb59fea6c2'


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('ticket_holders', sa.Column('accept_video_recording', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('ticket_holders', 'accept_video_recording')
    # ### end Alembic commands ###