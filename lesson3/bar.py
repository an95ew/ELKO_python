import plotly.graph_objects as go
from plotly.offline import plot

bar = go.Bar(x=['Bob', 'John', 'Wayne'], y=[21, 12, 19])

layout = go.Layout(title='Ages', xaxis=dict(title='students'), yaxis=dict(title='ages'))

figure = go.Figure(data=[bar], layout=layout)
plot(figure)