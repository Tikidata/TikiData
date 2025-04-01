import time
import requests

def obtener_estadisticas_detalladas():
    # URL de la API para obtener los partidos con estadísticas detalladas
    url = 'https://api.football-data.org/v4/matches'  # Ajusta la URL si es necesario
    headers = {'X-Auth-Token': '0bd6b60e01214f7aac2f1055dce9f67a'}  # Aquí va tu token

    for i in range(5):  # Intentamos 5 veces
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()  # Lanza un error si la solicitud no es exitosa
            return response.json()  # Devuelve la respuesta en formato JSON si la solicitud fue exitosa
        except requests.exceptions.HTTPError as err:
            print(f"Error HTTP: {err}")
            print(f"Respuesta completa: {response.text}")  # Muestra el cuerpo completo del error
            if response.status_code == 429:  # Si hay error 429 (limite de solicitudes alcanzado)
                print("Límite de solicitudes alcanzado. Esperando...")
                time.sleep(60)  # Espera 1 minuto antes de reintentar
            else:
                break  # Detiene el ciclo si el error no es 429
    return None  # Si no se obtiene respuesta después de 5 intentos

# Llamada a la función para obtener las estadísticas
estadisticas = obtener_estadisticas_detalladas()

# Mostrar los resultados si la respuesta es exitosa
if estadisticas:
    for partido in estadisticas['matches']:  # Itera sobre los partidos obtenidos
        print(f"Partido: {partido['homeTeam']['name']} vs {partido['awayTeam']['name']}")
        print(f"Fecha: {partido['utcDate']}")
        print(f"Marcador final: {partido['score']['fullTime']['homeTeam']} - {partido['score']['fullTime']['awayTeam']}")
        
        # Imprime estadísticas detalladas (possesión, tiros a puerta, córners, ocasiones de gol)
        if 'statistics' in partido:  # Asegúrate de que las estadísticas existan
            for stat in partido['statistics']:
                if stat['name'] == 'Possession':
                    print(f"Posesión: {stat['homeTeam']}% - {stat['awayTeam']}%")
                elif stat['name'] == 'Shots on Target':
                    print(f"Tiros a puerta: {stat['homeTeam']} - {stat['awayTeam']}")
                elif stat['name'] == 'Corners':
                    print(f"Córners: {stat['homeTeam']} - {stat['awayTeam']}")
                elif stat['name'] == 'Goal Attempts':
                    print(f"Ocasiones de gol: {stat['homeTeam']} - {stat['awayTeam']}")
        print('---')
else:
    print("No se pudo obtener las estadísticas de los partidos.")

