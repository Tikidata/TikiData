import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# Cargar datos
df = pd.read_csv("laliga_simulada.csv")

# Crear variable objetivo: 1 si gana el local, 0 si no
df["Gana_Local"] = (df["Goles_Local"] > df["Goles_Visitante"]).astype(int)

# Definir variables de entrada
X = df[["Goles_Local", "Goles_Visitante", "Posesión_Local", "Tiros_Local"]]
y = df["Gana_Local"]

# Separar datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entrenar el modelo
modelo = RandomForestClassifier(n_estimators=100, random_state=42)
modelo.fit(X_train, y_train)

# Guardar el modelo
joblib.dump(modelo, "modelo_laliga.pkl")

print("✅ Modelo entrenado y guardado.")
