from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from obtener_datos import obtener_partidos, obtener_partidos_api
from obtener_datos import obtener_partidos

app = FastAPI()

# Configurar Jinja2
templates = Jinja2Templates(directory="templates")

# Servir archivos estáticos
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def read_root(request: Request):
    partidos = obtener_partidos()  # Obtener los datos de los partidos
    return templates.TemplateResponse("index.html", {"request": request, "partidos": partidos})

