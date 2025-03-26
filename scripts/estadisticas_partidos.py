import requests
import pandas as pd
from datetime import datetime

# Tu clave de API
API_KEY = "0bd6b60e01214f7aac2f1055dce9f67a"

# URL base de la API
BASE_URL = "https://api.football-data.org/v4/competitions/PD/matches"

# Función para obtener las estadísticas de los partidos
def obtener_estadisticas_partidos(temporada_inicio, fecha_fin):
    fecha_inicio = f"{temporada_inicio}-08-01"  # LaLiga suele empezar en agosto
    
    url = f"{BASE_URL}?dateFrom={fecha_inicio}&dateTo={fecha_fin}"
    headers = {"X-Auth-Token": API_KEY}
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        return data.get("matches", [])  # Si no hay partidos, devuelve lista vacía
    else:
        print(f"Error {response.status_code}: No se pudo obtener la información.")
        return []

# Función para procesar y guardar las estadísticas
def guardar_estadisticas(partidos, archivo="estadisticas_partidos.csv"):
    estadisticas_datos = []
    
    for partido in partidos:
        if "statistics" in partido:
            estadisticas_datos.append({
                "fecha": partido["utcDate"],
                "equipo_local": partido["homeTeam"]["name"],
                "equipo_visitante": partido["awayTeam"]["name"],
                "posesion_local": partido["statistics"][0]["value"] if len(partido["statistics"]) > 0 else "N/A",
                "posesion_visitante": partido["statistics"][1]["value"] if len(partido["statistics"]) > 1 else "N/A",
                "tiros_local": partido["statistics"][2]["value"] if len(partido["statistics"]) > 2 else "N/A",
                "tiros_visitante": partido["statistics"][3]["value"] if len(partido["statistics"]) > 3 else "N/A",
                "tiros_a_puerta_local": partido["statistics"][4]["value"] if len(partido["statistics"]) > 4 else "N/A",
                "tiros_a_puerta_visitante": partido["statistics"][5]["value"] if len(partido["statistics"]) > 5 else "N/A",
                "ocasiones_local": partido["statistics"][6]["value"] if len(partido["statistics"]) > 6 else "N/A",
                "ocasiones_visitante": partido["statistics"][7]["value"] if len(partido["statistics"]) > 7 else "N/A"
            })
    
    df = pd.DataFrame(estadisticas_datos)
    
    try:
        df_existente = pd.read_csv(archivo)
        df_total = pd.concat([df_existente, df], ignore_index=True)
        df_total.to_csv(archivo, index=False)
    except FileNotFoundError:
        df.to_csv(archivo, index=False)

# Obtener estadísticas de la temporada 2023-2024 hasta la fecha actual
temporada_inicio = 2023
fecha_actual = datetime.today().strftime('%Y-%m-%d')

# Obtener y guardar estadísticas
partidos = obtener_estadisticas_partidos(temporada_inicio, fecha_actual)
guardar_estadisticas(partidos)

print(f"✅ Estadísticas de partidos desde la temporada {temporada_inicio}-2024 hasta hoy añadidas al archivo.")
