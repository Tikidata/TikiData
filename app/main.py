from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path

app = FastAPI()

# Servir archivos estáticos (CSS, imágenes)
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Configurar Jinja2
templates = Jinja2Templates(directory="app/templates")

# Ruta para la página de inicio
@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
