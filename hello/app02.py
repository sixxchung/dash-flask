from dash import Dash, html, dcc

from flask import Flask

import pandas as pd
import numpy as np
import plotly.express as px

server = Flask(__name__)

app = Dash(
    __name__,
    server=server,
    #url_base_pathname='/dash'
)

df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

app.layout = html.Div(id='dash-container', children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for your data.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

# @server.route("/dash")
# def my_dash_app():
#     return app.index()


if __name__ == '__main__':
    app.run_server(debug=True)