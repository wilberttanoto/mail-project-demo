from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
mail_mail = Table('mail_mail', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('email', VARCHAR(length=120)),
    Column('body', VARCHAR(length=140)),
    Column('timestamp', DATETIME),
)

mail_mail = Table('mail_mail', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('email', Text),
    Column('email_body', String(length=140)),
    Column('email_subject', String(length=140)),
    Column('timestamp', DateTime),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['mail_mail'].columns['body'].drop()
    post_meta.tables['mail_mail'].columns['email_body'].create()
    post_meta.tables['mail_mail'].columns['email_subject'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['mail_mail'].columns['body'].create()
    post_meta.tables['mail_mail'].columns['email_body'].drop()
    post_meta.tables['mail_mail'].columns['email_subject'].drop()
