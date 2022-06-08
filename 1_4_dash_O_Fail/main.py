import uvicorn
from wsgi_app import app_fastapi

port_dash = 8050
reload_fastapi = True
#------------------

if __name__ == "__main__":
    uvicorn.run("main:app_fastapi", 
        host="0.0.0.0",
        port=port_dash,
        reload=reload_fastapi,
        workers=2
    )
