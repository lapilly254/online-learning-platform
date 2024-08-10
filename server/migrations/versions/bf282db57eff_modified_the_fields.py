"""Modified the fields

Revision ID: bf282db57eff
Revises: 
Create Date: 2024-08-09 12:24:13.287215

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bf282db57eff'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('courses',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=200), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.Column('rating', sa.Float(), nullable=True),
    sa.Column('price', sa.Float(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('username', sa.String(length=10), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('phone', sa.String(length=10), nullable=True),
    sa.Column('password', sa.String(length=128), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('discussions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('topic', sa.Text(), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('comment', sa.Text(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('course_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['course_id'], ['courses.id'], name=op.f('fk_discussions_course_id_courses')),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name=op.f('fk_discussions_user_id_users')),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('enrollment',
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('course_id', sa.Integer(), nullable=False),
    sa.Column('enrolled_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['course_id'], ['courses.id'], name=op.f('fk_enrollment_course_id_courses')),
    sa.ForeignKeyConstraint(['name'], ['users.name'], name=op.f('fk_enrollment_name_users')),
    sa.PrimaryKeyConstraint('name', 'course_id')
    )
    op.create_table('lessons',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('topic', sa.Text(), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('video_url', sa.String(length=255), nullable=True),
    sa.Column('course_id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['course_id'], ['courses.id'], name=op.f('fk_lessons_course_id_courses')),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('payments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('amount', sa.Float(), nullable=False),
    sa.Column('payment_date', sa.DateTime(), nullable=True),
    sa.Column('course_id', sa.Integer(), nullable=False),
    sa.Column('method_of_payment', sa.String(length=10), nullable=False),
    sa.Column('card_number', sa.String(length=16), nullable=True),
    sa.Column('expiry_date', sa.String(length=5), nullable=True),
    sa.Column('cvv', sa.String(length=3), nullable=True),
    sa.Column('phone_number', sa.String(length=10), nullable=True),
    sa.Column('mpesa_reference', sa.String(length=20), nullable=True),
    sa.ForeignKeyConstraint(['course_id'], ['courses.id'], name=op.f('fk_payments_course_id_courses')),
    sa.ForeignKeyConstraint(['name'], ['users.name'], name=op.f('fk_payments_name_users')),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name=op.f('fk_payments_user_id_users')),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('payments')
    op.drop_table('lessons')
    op.drop_table('enrollment')
    op.drop_table('discussions')
    op.drop_table('users')
    op.drop_table('courses')
    # ### end Alembic commands ###