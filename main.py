from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from api import ws

app = FastAPI()
app.include_router(ws.router)


# check ws route is healthy or not
@app.get("/health_check")
async def health_check():
    print(f"app.routes: {app.routes}")
    # check if contains "/ws"
    for route in app.routes:
        # match '/ws'
        if getattr(route, 'path') == '/ws':
            return {"status": "healthy"}
    return {"status": "unhealthy"}

# main page for loading chat frame
@app.get("/")
async def root():
    # read html of ws's main page
    html_path = Path("./templates/index.html")
    return HTMLResponse(html_path.read_text(encoding="UTF-8"))

# test api for http get
@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
