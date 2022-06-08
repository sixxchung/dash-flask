"""Initialize Flask app."""
from flask import Flask, render_template

def create_flask_app():
    app_flask = Flask(__name__, instance_relative_config=False)
    with app_flask.app_context():
        #from . import routes
        @app_flask.route("/")
        def home():
            """Landing page."""
            return render_template(
                "index.jinja2",
                title="Plotly Dash Flask Tutorial",
                description="Embed Plotly Dash into your Flask applications.",
                template="home-template",
                body="This is a homepage served with Flask.",
            )

        from .dashboard import create_dash_app
        app_dash = create_dash_app(app_flask)
        return app_dash
