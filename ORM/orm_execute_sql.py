from sqlalchemy import create_engine, String, bindparam
from sqlalchemy import text  # for prepared query


engine = create_engine("mysql+pymysql://elko:elko@10.10.64.201/elko", echo=True)

connection = engine.connect()

query = """
            select 
                cust_name
            from
                customers
            where
                trim(cust_contact) = trim(:contact) 
                and trim(cust_country) = trim(:country)
        """
# query (str) => prepared query (oject)
cursor = connection.execute(text(query), contact="   John Smith        ", country="USA")

for row in cursor.fetchall():
    print(row)

# VS Parameters Binding
prepared_query = text(query)
prepared_query = prepared_query.bindparams(
    bindparam('contact', type_=String),
    bindparam('country', type_=String)
)

cursor = connection.execute(prepared_query, {
    'contact': '   John Smith        ',
    'country': 'USA'
})

for row in cursor.fetchall():
    print(row)