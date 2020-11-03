import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "key.json"

import pandas as pd
from bq_helper import BigQueryHelper

client = BigQueryHelper('bigquery-public-data', 'stackoverflow')

query = "SELECT " \
        "title, answer_count " \
        "FROM " \
        "bigquery-public-data.stackoverflow.stackoverflow_posts " \
        "ORDER BY " \
        "answer_count DESC " \
        "LIMIT 2"

df = client.query_to_pandas(query)
print(df)
