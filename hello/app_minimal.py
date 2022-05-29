from dash import Dash, dcc, html


external_scripts = None

app = Dash(
    __name__,
    external_stylesheets=['/static/dist/css/style.css'],
    external_scripts=external_scripts,
    routes_pathname_prefix='/dash/'
)

app.layout = html.Div(id='example-div-element')


if __name__ == '__main__':
    app.run_server(debug=True)