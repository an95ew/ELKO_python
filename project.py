import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "lesson2/key.json"

from google.cloud import bigquery
import plotly.graph_objects as go
from plotly.offline import plot

client = bigquery.Client()

query = "select * from bigquery-public-data.stackoverflow.tags LIMIT 6"

query_job = client.query(query)

dataset = dict()
for row in query_job:
    dataset[row[0]] = row[1]

plot(go.Figure(data=[go.Pie(labels=list(dataset.keys()), values=list(dataset.values()))]))
