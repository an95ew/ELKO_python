from sqlalchemy import create_engine, MetaData, Table, Column, text, bindparam, String, Integer, Float, select, and_, \
    between

engine = create_engine("mysql+pymysql://elko:elko@10.10.64.201/elko", echo=True)

query = """
        SELECT 
            prod_name
        FROM 
            products
        WHERE
            trim(vend_id) = trim(:vendor_id)
            AND prod_price > :product_price
        """

products = Table(
    'products', MetaData(),
    Column('vend_id', String(10)),
    Column('prod_name', String(50)),
    Column('prod_price', Float)
)

# METHOD #1: how to execute pure SQL raw string (with binding parameters or w\o)
with engine.connect() as connection:
    prepared_query = text(query)
    prepared_query = prepared_query.bindparams(
        bindparam('vendor_id', type_=String),
        bindparam('product_price', type_=Float)
    )

    cursor = connection.execute(prepared_query, {
        'vendor_id': 'BRS01',
        'product_price': 8
    })
    #
    # for row in cursor.fetchall():
    #     print(row)

# VS

# METHOD #2: how to use MAPPED table structure and make Query via sqlalchemy.select
with engine.connect() as connection:
    prepared_query = select([products.c.prod_name]).where(
                                                            and_(products.c.vend_id == 'BRS01',
                                                                 between(products.c.prod_price, 8, 12))
    )

    cursor = connection.execute(prepared_query)
    # print(cursor.fetchall())

