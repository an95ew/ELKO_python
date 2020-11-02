import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "key.json"


from google.cloud import bigquery

client = bigquery.Client()

dataset_refference = client.dataset('stackoverflow', project='bigquery-public-data')

print(type(dataset_refference))

datawarehouse_refference = client.get_dataset(dataset_refference)

for table in client.list_tables(datawarehouse_refference):
    print(table.table_id)


table_refference  = client.get_table( datawarehouse_refference.table('users')  )

print(table_refference.schema)