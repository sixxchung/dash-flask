#import dash
from dash.dependencies import Input, Output
from dash import Dash, dcc, html
import pandas as pd

import flask
import os


def create_dash_app(app_flask, requests_pathname_prefix: str = None) -> Dash:
    #app_flask = flask.Flask(__name__)
    app_dash = Dash(
        # __name__, 
        server=app_flask,
        requests_pathname_prefix= requests_pathname_prefix
    )
    app_dash.scripts.config.serve_locally = False

    app_dash.layout = html.Div([
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
    ], className="container")

    df = pd.read_csv(
        'https://raw.githubusercontent.com/plotly/datasets/master/hello-world-stock.csv')

    @app_dash.callback(Output('my-graph', 'figure'),
                  [Input('my-dropdown', 'value')])
    def update_graph(selected_dropdown_value):
        dff = df[df['Stock'] == selected_dropdown_value]
        return {
            'data': [{
                'x': dff.Date,
                'y': dff.Close,
                'line': {
                    'width': 3,
                    'shape': 'spline'
                }
            }],
            'layout': {
                'margin': {
                    'l': 30,
                    'r': 20,
                    'b': 30,
                    't': 20
                }
            }
        }

    return app_dash
