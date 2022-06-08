import uvicorn

from fastapi import FastAPI
from fastapi.middleware.wsgi import WSGIMiddleware
from fastapi.responses import RedirectResponse

from app_dash import create_dash_app
#from routers import model_get

urlPath_dash = '/dash'
port_dash = 8050

#------------------
app = FastAPI()
dash_app = create_dash_app(requests_pathname_prefix="/dash/")
app.mount(urlPath_dash, WSGIMiddleware(dash_app.server))
#app.include_router(model_get.router)

@app.get("/")
def redirect_root():
    url = "http://0.0.0.0:"+ str(port_dash) + urlPath_dash 
    response = RedirectResponse(url)
    return response

@app.get("/status")
def get_status():
    return {"status": "ok"}

if __name__ == "__main__":
    uvicorn.run(app, port=port_dash)
