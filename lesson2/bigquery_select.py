import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "key.json"


from google.cloud import bigquery

client = bigquery.Client()

query = "select * from bigquery-public-data.stackoverflow.tags LIMIT 3"

query_job = client.query(query)

for row in query_job:
    print(row)
