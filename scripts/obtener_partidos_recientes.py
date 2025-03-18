import requests
import pandas as pd
from datetime import datetime

# Tu clave de API (mantenla segura)
API_KEY = "0bd6b60e01214f7aac2f1055dce9f67a"

# Establecer la URL base de la API para la liga española (LaLiga)
BASE_URL = "https://api.football-data.org/v4/competitions/PD/matches"

# Función para obtener los partidos de la temporada 2023-2024 hasta la fecha actual
def obtener_partidos_2023_2024(fecha_fin):
    # Definir la fecha de inicio para la temporada 2023-2024
    fecha_inicio = "2023-08-01"  # La temporada 2023-2024 comenzó el 1 de agosto de 2023

    # Construir la URL con el rango de fechas
    url = f"{BASE_URL}?dateFrom={fecha_inicio}&dateTo={fecha_fin}"
    
    # Cabeceras para la autenticación
    headers = {"X-Auth-Token": API_KEY}

    # Realizar la solicitud GET
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        return data['matches']
    else:
        print(f"Error {response.status_code}: No se pudo obtener la información.")
        print(f"Contenido de la respuesta: {response.text}")  # Ver el cuerpo de la respuesta para detalles adicionales.
        return []

# Función para agregar los partidos a un archivo CSV
def agregar_partidos_a_csv(partidos, archivo="resultados_desde_2023-2024.csv"):
    # Crear una lista de diccionarios con los datos que nos interesa
    partidos_datos = []
    for partido in partidos:
        partido_datos = {
            "fecha": partido["utcDate"],
            "local": partido["homeTeam"]["name"],
            "visitante": partido["awayTeam"]["name"],
            "goles_local": partido["score"]["fullTime"]["home"],
            "goles_visitante": partido["score"]["fullTime"]["away"],
        }
        partidos_datos.append(partido_datos)
    
    # Convertir los datos a un DataFrame
    df = pd.DataFrame(partidos_datos)
    
    # Si el archivo ya existe, agregar a los datos existentes, si no, crear uno nuevo
    try:
        df_existente = pd.read_csv(archivo)
        df_total = pd.concat([df_existente, df], ignore_index=True)
        df_total.to_csv(archivo, index=False)
    except FileNotFoundError:
        df.to_csv(archivo, index=False)

# Obtener los partidos de la temporada 2023-2024 hasta la fecha actual
fecha_actual = datetime.today().strftime('%Y-%m-%d')  # Obtener la fecha actual

# Obtener los partidos
partidos = obtener_partidos_2023_2024(fecha_actual)

# Agregar los partidos obtenidos al CSV
agregar_partidos_a_csv(partidos)

# Imprimir un mensaje para indicar que el proceso ha terminado
print(f"Partidos desde la temporada 2023-2024 hasta hoy añadidos al archivo.")

