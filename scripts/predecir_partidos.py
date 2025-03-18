import pandas as pd
import joblib

# Cargar el modelo entrenado
modelo = joblib.load("modelo_laliga.pkl")

# Simular nuevos partidos
nuevos_partidos = [
    ["Real Madrid", "Barcelona", 3, 1, 55.3, 14],
    ["Atlético de Madrid", "Sevilla", 1, 2, 48.2, 10],
    ["Real Sociedad", "Real Madrid", 2, 2, 52.7, 12],
    ["Barcelona", "Atlético de Madrid", 1, 0, 60.1, 16],
    ["Sevilla", "Real Sociedad", 0, 1, 49.9, 8]
]

df_nuevos = pd.DataFrame(nuevos_partidos, columns=["Local", "Visitante", "Goles_Local", "Goles_Visitante", "Posesión_Local", "Tiros_Local"])

# Hacer predicciones
predicciones = modelo.predict(df_nuevos[["Goles_Local", "Goles_Visitante", "Posesión_Local", "Tiros_Local"]])

# Mostrar resultados
for i, partido in enumerate(nuevos_partidos):
    resultado = "Gana el Local" if predicciones[i] == 1 else "Gana el Visitante o Empate"
    print(f"🔹 {partido[0]} vs {partido[1]} → {resultado}")
