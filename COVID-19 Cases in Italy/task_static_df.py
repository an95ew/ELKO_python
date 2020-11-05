import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "key.json"

import plotly.graph_objects as go
from plotly.offline import plot

from bq_helper import BigQueryHelper


client = BigQueryHelper('bigquery-public-data', 'covid19_italy')


query = """ select 
                    * 
            from bigquery-public-data.covid19_italy.data_by_region 
        """

df = client.query_to_pandas(query)

# 3.1 BAR >><<
df_for_bar = df[['date','hospitalized_patients_symptoms']][df.region_name=='Toscana']

bar = go.Bar(x=df.date, y=df.hospitalized_patients_symptoms)

bar_layout = go.Layout(
    title='Toscana',
    xaxis=dict(title='Date'),
    yaxis=dict(title='Amount')
)

fig_bar = go.Figure(
    data=[bar],
    layout=bar_layout
)

plot(fig_bar,
     filename='bar_file')

# 3.2 Pie >>><<<
df_for_pie = df[['region_name', 'hospitalized_patients_symptoms']].groupby(['region_name']).sum()

pie = go.Pie(
    # labels=df_for_pie.index,
    labels=list(df_for_pie.index),
    # values=df_for_pie.values
    values=df_for_pie.hospitalized_patients_symptoms
)

fig_pie = go.Figure(data=[pie])
plot(fig_pie,
     filename='pie_file')

# 3.3 Scatter

df_for_scatter = df[['date', 'total_hospitalized_patients']].groupby(['date']).mean()

scatter = go.Scatter(
    x=list(df_for_scatter.index),
    y=df_for_scatter.total_hospitalized_patients,
    mode="lines"
)

scatter_layout = go.Layout(title='Italy COVID-19 Dynamics')

scatter_fig = go.Figure(
    data=[scatter],
    layout=scatter_layout
)

plot(scatter_fig,
     filename='scatter_file')


