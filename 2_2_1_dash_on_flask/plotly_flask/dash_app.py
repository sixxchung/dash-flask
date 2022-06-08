"""Instantiate a Dash app."""
from dash.dependencies import Input, Output
from dash import Dash, dcc, html

import pandas as pd

def create_dash_app(server):
    app_dash = Dash(
        server=server,
        routes_pathname_prefix="/dash/",
    )

    app_dash.layout = html.Div(id="dash-container", 
        children=[
            html.H1('Stock Tickers'),
            dcc.Dropdown(
                id='my-dropdown',
                options=[
                    {'label': 'Tesla', 'value': 'TSLA'},
                    {'label': 'Apple', 'value': 'AAPL'},
                    {'label': 'Coke', 'value': 'COKE'}
                ],
                value='TSLA'
            ),
            dcc.Graph(id='my-graph')
        ],
    )
    df = pd.read_csv(
        'https://raw.githubusercontent.com/plotly/datasets/master/hello-world-stock.csv')

    @app_dash.callback(Output('my-graph', 'figure'),
                       [Input('my-dropdown', 'value')])
    def update_graph(selected_dropdown_value):
        dff = df[df['Stock'] == selected_dropdown_value]
        return {
            'data': [{ 'x': dff.Date, 'y': dff.Close,
                'line': {'width': 3, 'shape': 'spline'}
            }],
            'layout': {
                'margin': {'l': 30,'r': 20, 'b': 30, 't': 20 }
            }
        }
    return app_dash.server
