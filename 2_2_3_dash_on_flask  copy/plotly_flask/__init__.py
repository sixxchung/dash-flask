"""Initialize Flask app."""
from flask import Flask
from flask_assets import Environment

def init_app():
    app = Flask(__name__, instance_relative_config=False)
    with app.app_context():
        from . import routes
        from .dashboard import init_dashboard
        app = init_dashboard(app)
        return app
