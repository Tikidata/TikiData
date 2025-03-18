# obtener_datos.py

import pandas as pd
import requests
from dotenv import load_dotenv
import os

# Cargar las variables del archivo .env
load_dotenv()

# Cargar la API Key desde el archivo .env
API_KEY = os.getenv('API_KEY')

# Función para obtener partidos desde el archivo CSV
def obtener_partidos():
    df = pd.read_csv("laliga_simulada.csv")  # Asegúrate de que el CSV está en la carpeta correcta
    return df.to_dict(orient="records")  # Convertimos a lista de diccionarios

# URL para obtener los partidos de LaLiga (Competition Code: "PD" = Primera División de España)
URL = "https://api.football-data.org/v4/competitions/PD/matches"

# Encabezados con la API Key
headers = {"X-Auth-Token": API_KEY}

# Realizar la petición GET
def obtener_partidos_api():
    response = requests.get(URL, headers=headers)

    if response.status_code == 200:
        data = response.json()

        print("\n📌 Últimos 5 partidos de LaLiga:")
        for match in data["matches"][:5]:  # Mostramos solo los primeros 5 partidos
            home_team = match["homeTeam"]["name"]
            away_team = match["awayTeam"]["name"]
            score = match["score"]["fullTime"]
            print(f"{home_team} vs {away_team} - Resultado: {score}")
    else:
        print(f"❌ Error {response.status_code}: No se pudo obtener la información.")
