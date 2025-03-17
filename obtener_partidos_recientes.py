import requests
from datetime import datetime, timedelta

# Tu clave de API (mantenla segura y no la compartas públicamente)
API_KEY = "0bd6b60e01214f7aac2f1055dce9f67a"

# Fecha actual y fecha de hace 7 días
fecha_actual = datetime.now().strftime('%Y-%m-%d')
fecha_hace_7_dias = (datetime.now() - timedelta(days=7)).strftime('%Y-%m-%d')

# URL de la API para obtener partidos de LaLiga en el intervalo de fechas
URL = f"https://api.football-data.org/v4/competitions/PD/matches?dateFrom={fecha_hace_7_dias}&dateTo={fecha_actual}"

# Encabezados de la solicitud
headers = {"X-Auth-Token": API_KEY}

# Realizar la solicitud GET
response = requests.get(URL, headers=headers)

# Verificar si la solicitud fue exitosa
if response.status_code == 200:
    data = response.json()
    matches = data.get("matches", [])

    if matches:
        print(f"Partidos de LaLiga desde {fecha_hace_7_dias} hasta {fecha_actual}:\n")
        for match in matches:
            home_team = match["homeTeam"]["name"]
            away_team = match["awayTeam"]["name"]
            date = match["utcDate"]
            score_home = match["score"]["fullTime"]["home"]
            score_away = match["score"]["fullTime"]["away"]
            print(f"{date}: {home_team} {score_home} - {score_away} {away_team}")
    else:
        print(f"No se encontraron partidos de LaLiga entre {fecha_hace_7_dias} y {fecha_actual}.")
else:
    print(f"Error {response.status_code}: No se pudo obtener la información.")
