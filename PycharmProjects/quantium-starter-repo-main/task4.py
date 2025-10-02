import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

# Load sales data
df = pd.read_csv("processed_sales.csv")  # Ensure columns: 'Sales', 'date', 'region'

# Convert 'date' to datetime
df['date'] = pd.to_datetime(df['date'])

app = dash.Dash(__name__)

# Layout
app.layout = html.Div([
    html.H1("Pink Morsels Sales Dashboard", className='app-header'),

    html.Div([
        html.Label("Select Region:", className='radio-label'),
        dcc.RadioItems(
            id='region-selector',
            options=[
                {'label': 'North', 'value': 'north'},
                {'label': 'East', 'value': 'east'},
                {'label': 'South', 'value': 'south'},
                {'label': 'West', 'value': 'west'},
                {'label': 'All', 'value': 'all'}
            ],
            value='all',
            labelStyle={'display': 'inline-block', 'margin-right': '20px'},
            inputStyle={"margin-right": "5px"}
        )
    ], className='radio-container'),

    dcc.Graph(id='sales-line-chart', className='line-chart')
], className='app-container')


# Callback for filtering chart
@app.callback(
    Output('sales-line-chart', 'figure'),
    Input('region-selector', 'value')
)
def update_chart(selected_region):
    if selected_region == 'all':
        filtered_df = df
    else:
        filtered_df = df[df['region'] == selected_region]

    fig = px.line(
        filtered_df,
        x='date',
        y='Sales',
        color='region',
        title=f"Sales Trend: {selected_region.capitalize()}",
        markers=True
    )

    fig.update_layout(
        plot_bgcolor='#ffffff',
        paper_bgcolor='#f0f8ff',
        font=dict(family="Verdana", size=12, color="#333"),
        title_font=dict(size=20, color="#ff1493")
    )

    return fig


if __name__ == '__main__':
    app.run(debug=True)
