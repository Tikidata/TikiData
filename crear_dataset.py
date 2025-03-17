import pandas as pd
import numpy as np

# Equipos de prueba
equipos = ["Real Madrid", "Barcelona", "Atlético de Madrid", "Sevilla", "Real Sociedad"]

# Generar datos simulados
np.random.seed(42)
partidos = []

for _ in range(20):  # 20 partidos aleatorios
    local, visitante = np.random.choice(equipos, size=2, replace=False)
    goles_local = np.random.randint(0, 5)
    goles_visitante = np.random.randint(0, 5)
    posesion_local = np.random.uniform(40, 60)
    tiros_local = np.random.randint(5, 20)

    partidos.append([local, visitante, goles_local, goles_visitante, posesion_local, tiros_local])

# Guardar en CSV
df = pd.DataFrame(partidos, columns=["Local", "Visitante", "Goles_Local", "Goles_Visitante", "Posesión_Local", "Tiros_Local"])
df.to_csv("laliga_simulada.csv", index=False)

print("✅ Dataset creado con éxito")
