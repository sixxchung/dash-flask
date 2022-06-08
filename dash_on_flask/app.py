import uvicorn
from fastapi import FastAPI
from fastapi.middleware.wsgi import WSGIMiddleware

from dashapp import create_dash_app

app = FastAPI()

@app.get("/")
def read_main():
    return {
        "routes": [
            {"method": "GET", "path": "/", "summary": "Landing"},
            {"method": "GET", "path": "/status", "summary": "App status"},
            {"method": "GET", "path": "/dash", "summary": "Sub-mounted Dash application"},
        ]
    }


@app.get("/status")
def get_status():
    return {"status": "ok"}


# A bit odd, but the only way I've been able to get prefixing of the Dash app
# to work is by allowing the Dash/Flask app to prefix itself, then mounting
# it to root
#dash_app = create_dash_app(requests_pathname_prefix="/dash/")
#app.mount("/dash", WSGIMiddleware(dash_app.server))



from dashpage import init_app
flask_app = init_app()

#app.mount("/ddd", WSGIMiddleware(flask_app))
app.mount("/", WSGIMiddleware(flask_app))


# http://127.0.0.1:8000/ddd/
@flask_app.get('/')
def blog_page():
    return "llll form ...."

# http://127.0.0.1:8000/ddd/about
@flask_app.get('/about')
def blog_page2():
    return "llll form ...."



if __name__ == "__main__":
    uvicorn.run(app, port=8066)
