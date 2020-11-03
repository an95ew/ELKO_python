import os
import pandas as pd
import plotly.graph_objects as go
from plotly.offline import plot

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "key.json"

from bq_helper import BigQueryHelper

client = BigQueryHelper('bigquery-public-data', 'stackoverflow')

query = """ select
                    *
            from bigquery-public-data.stackoverflow.stackoverflow_posts 
            limit 1000
        """

df = client.query_to_pandas(query)
df_filter = df[['id', 'title', 'comment_count', 'answer_count']][ (df.comment_count>=2) & (df.answer_count>=1) ]

print(df_filter.comment_count.mean())

#
# trace = go.Scatter(x=df.creation_date, y=df.count_of_posts)
# # VS
# trace_dict = {
#     "x": df.creation_date,
#     "y": df.count_of_posts,
#     "type": "scatter"
# }
#
# fig = go.Figure(data=[])
# # VS
# fig_dict = {
#     "data": [
#         {
#             "x": df.creation_date,
#             "y": df.count_of_posts,
#             "type": "scatter"
#         }
#     ],
#     "layout": {
#         "title": "Information"
#     }
# }
# plot(fig_dict)
