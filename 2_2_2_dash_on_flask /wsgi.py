"""Application entry point."""
from plotly_flask import create_flask_app

app = create_flask_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8050, debug=True)
