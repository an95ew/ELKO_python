from sqlalchemy import create_engine
from sqlalchemy import Integer, String, MetaData, Table, Column, ForeignKey

engine = create_engine("mysql+pymysql://elko:elko@10.10.64.201/elko", echo=True)

meta = MetaData()


parent = Table(
    'parent', meta,
    Column('parent_id', Integer, primary_key=True)
)

child = Table(
    'child',
    meta,
    Column('child_id', Integer, primary_key=True),
    Column('parent_fk', Integer, ForeignKey('parent.parent_id'))
)
meta.create_all(engine)

# my_range = range(400, 422)
# row = {
#     'parents': [{'parent_id': (i*4)} for i in my_range],
#     'childs': [{'child_id': (i*4)+1, 'parent_fk': (i*4)} for i in my_range],
# }
# with engine.connect() as connection:
#     connection.execute(parent.insert(), row['parents'])
#     connection.execute(child.insert(), row['childs'])

# with engine.connect() as connection:
#     for i in my_range:
#         connection.execute(child.delete().where(child.c.parent_fk == i))
    # connection.execute(parent.insert(), row['parents'])

