from sqlalchemy import create_engine, text, bindparam, String, Integer, Float, and_, MetaData, Table, Column, or_, \
    select

engine = create_engine("mysql+pymysql://elko:elko@10.10.64.201/elko", echo=True)
connection = engine.connect()

query = """
        SELECT 
            prod_name
        FROM 
            products
        WHERE
            trim(vend_id) = 'BRS01'
            AND prod_price > 8
        """

meta = MetaData()

customers = Table(
    'customers', meta,
    Column('cust_id', String(10), primary_key=True),
    Column('cust_name', String(50)),
    Column('cust_contact', String(50)),
    Column('cust_country', String(50))
)
print(or_(
    and_(customers.c.cust_contact == 'John Smith', customers.c.cust_country == 'USA'),
    customers.c.cust_country == 'Germany'
))
prepared_query = select([customers.c.cust_name]).where(or_(
                                                and_(customers.c.cust_contact == 'John Smith', customers.c.cust_country == 'USA'),
                                                customers.c.cust_country == 'Germany'
))

cursor = connection.execute(prepared_query)
print(cursor.fetchall())
