import dash
from dash import dash_table
from dash.dependencies import Input, Output
from dash import dcc, html

from .data import create_dataframe
from .layout import html_layout


def init_dashboard(server):
    dash_app = dash.Dash(
        server = server,
        routes_pathname_prefix='/ddd/',
        external_stylesheets=[
            "/static/dist/css/styles.css",
            "https://fonts.googleapis.com/css?family=Lato",
        ],
    )

    df = create_dataframe()
    dash_app.index_string = html_layout
    dash_app.layout = html.Div([create_data_table(df)])
    return dash_app.server

def create_data_table(df):
    """Create Dash datatable from Pandas DataFrame."""
    table = dash_table.DataTable(
        id="database-table",
        columns=[{"name": i, "id": i} for i in df.columns],
        data=df.to_dict("records"),
        sort_action="native",
        sort_mode="native",
        page_size=300,
    )
    return table
