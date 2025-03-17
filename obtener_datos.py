import requests

# 📌 Usa tu API Key aquí (pero mejor guárdala en un archivo .env para mayor seguridad)
API_KEY = "0bd6b60e01214f7aac2f1055dce9f67a"

# URL para obtener los partidos de LaLiga (Competition Code: "PD" = Primera División de España)
URL = "https://api.football-data.org/v4/competitions/PD/matches"

# Encabezados con la API Key
headers = {"X-Auth-Token": API_KEY}

# Realizar la petición GET
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
