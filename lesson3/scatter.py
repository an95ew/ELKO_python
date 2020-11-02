import plotly.graph_objects as go
from plotly.offline import plot

trace1 = go.Scatter(x=[1, 2, 3, 4], y=[1, 4, 9, 16], mode="lines")

trace2 = go.Scatter(x=[1, 2, 3, 4], y=[19, 41, 34, 12])

layout = go.Layout(title="Scatter")

fig = go.Figure(data=[trace1, trace2], layout=layout)
plot(fig)