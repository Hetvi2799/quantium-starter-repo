
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd

# Load your processed sales data
df = pd.read_csv('processed_sales.csv')

# Create a line chart using Plotly Express
fig = px.line(df, x='date', y='Sales', title='Sales Over Time')

# Initialize the Dash app with a Bootstrap theme
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Define the layout of the app
app.layout = dbc.Container([
    dbc.Row(dbc.Col(html.H1('Sales Visualizer', className='text-center'))),
    dbc.Row(dbc.Col(dcc.Graph(figure=fig))),
], fluid=True)

if __name__ == "__main__":
    app.run(debug=True)
