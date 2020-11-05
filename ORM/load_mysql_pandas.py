import pandas as pd
import mysql.connector as sql
import plotly.graph_objects as go
from plotly.offline import plot

connection = sql.connect(
    host='10.10.64.201',
    database='elko',
    user='elko',
    password='elko'
)
cursor = connection.cursor()

query = """
        select
            cust_id,
            cust_name,
            cust_email,
            cust_country
        
        from 
            customers
        """

cursor.execute(query)

rows = cursor.fetchall()

df = pd.DataFrame(rows)
df.columns = ['id', 'name', 'email', 'country']

result = df.groupby(by='country').count()
# result = df[['country', 'id']].groupby(by='country').count() Верно, но затратно

#(list(map(lambda row: row[0], result.values)))

bar = go.Bar(x=result.index, y=list(map(lambda row: row[0], result.values)))
plot(go.Figure(data=[bar]))
print(result)