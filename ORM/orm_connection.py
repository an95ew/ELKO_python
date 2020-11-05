from sqlalchemy import create_engine
from sqlalchemy import Integer, String, MetaData, Table, Column

engine = create_engine("mysql+pymysql://elko:elko@10.10.64.201/elko", echo=True)

meta = MetaData()

shops = Table(
    'shops',
    meta,
    Column('shop_id', Integer, primary_key=True),
    Column('shop_name', String(100))
)

# INSERT
rows = [
    {
        'shop_id': 117,
        'shop_name': 'ELKO shop'
    },
    {
        'shop_id': 118,
        'shop_name': 'ELKO shop '
    },
    {
        'shop_id': 119,
        'shop_name': 'ELKO shop'
    }
]

with engine.connect() as connection:
    # connection.execute(shops.insert(), rows)
    pass

# SELECT
with engine.connect() as connection:
    rows = connection.execute(shops.select())

    for row in rows:
        print(row)

# SELECT WHERE
with engine.connect() as connection:
    rows = connection.execute(shops.select().where(shops.c.shop_id < 100))

    for row in rows:
        print(row)

# UPDATE WHERE
with engine.connect() as connection:
    rows = connection.execute(shops.update().where(shops.c.shop_id==314).values(shop_name="UPDATED"))

# DELETE
with engine.connect() as connection:
    rows = connection.delete(shops.delete().where(shops.c.shop_id==314))
