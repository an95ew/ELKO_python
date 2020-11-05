from sqlalchemy import create_engine, text, bindparam, String, Integer, Float, and_, MetaData, Table, Column, or_, \
    select, func, union

engine = create_engine("mysql+pymysql://elko:elko@10.10.64.201/elko", echo=True)
connection = engine.connect()

meta = MetaData()

products = Table(
    'products', MetaData(),
    Column('vend_id', String(10)),
    Column('prod_name', String(50)),
    Column('prod_price', Float)
)

prepared_query = select([func.max(products.c.prod_price)])

cursor = connection.execute(prepared_query)
print(cursor.fetchall())

