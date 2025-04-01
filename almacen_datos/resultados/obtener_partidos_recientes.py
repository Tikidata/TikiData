import time
import requests
import os

def obtener_estadisticas_detalladas():
    url = 'https://api.football-data.org/v4/matches'
    headers = {'X-Auth-Token': os.getenv('FOOTBALL_API_TOKEN')}  # Usa una variable de entorno

    for i in range(5):  # Reintentos
        try:
            response = requests.get(url, headers=headers)
            
            if response.status_code == 429:  # Límite de solicitudes
                print("Límite de solicitudes alcanzado. Esperando...")
                time.sleep(60)  # Espera 1 minuto
                continue  # Reintentar solicitud
            
            response.raise_for_status()  # Lanza error si el código no es 2xx
            
            return response.json()  # Devuelve JSON si la solicitud fue exitosa
        
        except requests.exceptions.RequestException as err:
            print(f"Error en la solicitud: {err}")
            return None  # Si hay error crítico, salir del bucle
    
    return None  # Si después de 5 intentos no hay respuesta, devolver None

# Llamada a la función
estadisticas = obtener_estadisticas_detalladas()

if estadisticas and 'matches' in estadisticas:
    for partido in estadisticas.get('matches', []):
        home_team = partido.get('homeTeam', {}).get('name', 'Desconocido')
        away_team = partido.get('awayTeam', {}).get('name', 'Desconocido')
        fecha = partido.get('utcDate', 'Fecha desconocida')
        score = partido.get('score', {}).get('fullTime', {})
        
        marcador_home = score.get('homeTeam', 'N/A')
        marcador_away = score.get('awayTeam', 'N/A')
        
        print(f"Partido: {home_team} vs {away_team}")
        print(f"Fecha: {fecha}")
        print(f"Marcador final: {marcador_home} - {marcador_away}")
        
        # Comprobamos si existen estadísticas
        if 'statistics' in partido:
            for stat in partido.get('statistics', []):
                stat_name = stat.get('name', '')
                home_value = stat.get('homeTeam', 'N/A')
                away_value = stat.get('awayTeam', 'N/A')

                if stat_name == 'Possession':
                    print(f"Posesión: {home_value}% - {away_value}%")
                elif stat_name == 'Shots on Target':
                    print(f"Tiros a puerta: {home_value} - {away_value}")
                elif stat_name == 'Corners':
                    print(f"Córners: {home_value} - {away_value}")
                elif stat_name == 'Goal Attempts':
                    print(f"Ocasiones de gol: {home_value} - {away_value}")
        print('---')
else:
    print("No se pudo obtener las estadísticas de los partidos.")

