import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "key.json"


from google.cloud import bigquery

client = bigquery.Client()

dataset_reffence = client.dataset('stackoverflow', project='bigquery-public-data')

print(type(dataset_reffence))