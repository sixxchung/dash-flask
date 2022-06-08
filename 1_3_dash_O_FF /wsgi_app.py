from fastapi import FastAPI, Depends
from fastapi.middleware.wsgi import WSGIMiddleware
from fastapi.responses import RedirectResponse

from dash_app import create_dash_app
#from routers import model_get

urlPath_dash = '/dash'
port_dash = 8050

#------------------
app_fastapi = FastAPI()
app_dash = create_dash_app(requests_pathname_prefix=urlPath_dash)
app_fastapi.mount(urlPath_dash, WSGIMiddleware(app_dash.server))
#app.include_router(model_get.router)

@app_fastapi.get("/")
def redirect_root():
    url = "http://0.0.0.0:" + str(port_dash) + urlPath_dash
    response = RedirectResponse(url)
    return response


@app_fastapi.get("/status")
def get_status():
    return {"status": "ok"}

