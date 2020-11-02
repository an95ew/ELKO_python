import plotly.graph_objects as go
from plotly.offline import plot

pie = go.Pie(labels=["Bob", "john", "Nick"], values=[1000,2000,120])
figure = go.Figure(data=pie)
plot(figure)