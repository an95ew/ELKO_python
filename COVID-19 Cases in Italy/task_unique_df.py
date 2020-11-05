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
query_for_bar = """ select 
                    date, hospitalized_patients_symptoms
            from bigquery-public-data.covid19_italy.data_by_region 
            where region_name="Toscana"
                    
        """
query_for_pie = """ select 
                    region_name, SUM(hospitalized_patients_symptoms) AS sick
            
                    from bigquery-public-data.covid19_italy.data_by_region 
            
                    group by region_name
                """
query_for_scatter = """ select 
                                date, AVG(total_hospitalized_patients) as hospitalized
                                
                        from bigquery-public-data.covid19_italy.data_by_region 
                        
                        group by 
                                date
                        order by
                                date
                    """

df = client.query_to_pandas(query)

# 3.1 BAR >><<
df_for_bar = client.query_to_pandas(query_for_bar)

bar = go.Bar(x=df_for_bar.date,
             y=df_for_bar.hospitalized_patients_symptoms)

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
df_for_pie = client.query_to_pandas(query_for_pie)


pie = go.Pie(
    labels=df_for_pie.region_name,
    values=df_for_pie.sick
)

fig_pie = go.Figure(data=[pie])
plot(fig_pie,
     filename='pie_file')

# 3.3 Scatter

df_for_scatter = client.query_to_pandas(query_for_scatter)
print(df_for_scatter)
scatter = go.Scatter(
    x=df_for_scatter.date,
    y=list(map(lambda num: num+1000 if num < 40 else num, df_for_scatter.hospitalized)),
    mode="lines"
)

scatter_layout = go.Layout(title='Italy COVID-19 Dynamics')

scatter_fig = go.Figure(
    data=[scatter],
    layout=scatter_layout
)

plot(scatter_fig,
     filename='scatter_file')


