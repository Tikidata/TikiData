from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

# Crear una aplicación FastAPI
app = FastAPI()

# Configurar Jinja2
templates = Jinja2Templates(directory="app/templates")

# Servir archivos estáticos
app.mount("/static", StaticFiles(directory="app/static"), name="static")

@app.get("/")
def read_root(request: Request):
    # Renderizar la plantilla (en este caso solo un título)
    return templates.TemplateResponse("index.html", {"request": request})
