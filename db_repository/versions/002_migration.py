from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
premiere = Table('premiere', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String(length=255)),
    Column('description', String(length=255)),
    Column('trailer', String(length=255)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['premiere'].columns['trailer'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['premiere'].columns['trailer'].drop()
