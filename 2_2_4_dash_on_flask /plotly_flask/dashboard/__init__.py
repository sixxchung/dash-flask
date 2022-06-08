"""Instantiate a Dash app."""
#from dash import dash_table
from dash.dependencies import Input, Output
from dash import Dash, dcc, html

#from .data import create_dataframe
#from .layout import html_layout

import pandas as pd

def init_dashboard(server):
    """Create a Plotly Dash dashboard."""
    dash_app = Dash(
        server=server,
        routes_pathname_prefix="/dashapp/",
        external_stylesheets=[
            "/static/dist/css/styles.css",
            "https://fonts.googleapis.com/css?family=Lato",
        ],
    )

    # Load DataFrame
    #df = create_dataframe()
    df = pd.read_csv(
        'https://raw.githubusercontent.com/plotly/datasets/master/hello-world-stock.csv')
    # Custom HTML layout
    # dash_app.index_string = html_layout

    # Create Layout
    dash_app.layout = html.Div(id="dash-container", 
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
            # dcc.Graph(
            #     id="histogram-graph",
            #     figure={
            #         "data": [
            #             {
            #                 "x": df["complaint_type"],
            #                 "text": df["complaint_type"],
            #                 "customdata": df["key"],
            #                 "name": "311 Calls by region.",
            #                 "type": "histogram",
            #             }
            #         ],
            #         "layout": {
            #             "title": "NYC 311 Calls category.",
            #             "height": 500,
            #             "padding": 150,
            #         },
            #     },
            # ),

            # create_data_table(df),
        ],
    )

    @dash_app.callback(Output('my-graph', 'figure'),
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
    return dash_app.server


# def create_data_table(df):
#     """Create Dash datatable from Pandas DataFrame."""
#     table = dash_table.DataTable(
#         id="database-table",
#         columns=[{"name": i, "id": i} for i in df.columns],
#         data=df.to_dict("records"),
#         sort_action="native",
#         sort_mode="native",
#         page_size=300,
#     )
#     return table
