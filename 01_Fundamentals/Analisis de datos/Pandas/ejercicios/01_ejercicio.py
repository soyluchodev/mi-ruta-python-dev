# 🧪 Ejercicio práctico
# Carga el dataset del Titanic desde la URL proporcionada anteriormente.
# Selecciona las columnas 'Age' y 'Fare'.
# Crea un gráfico de dispersión (scatter) para visualizar la relación entre la edad y la tarifa.
# Personaliza el gráfico agregando títulos y etiquetas a los ejes.

import pandas as pd
import matplotlib.pyplot as plt

#Cargamos el dataset desde la web
titanic = pd.read_csv("https://raw.githubusercontent.com/pandas-dev/pandas/main/doc/data/titanic.csv")

#seleccionamos columnas edad y tarifa
age_fare = titanic[["Age", "Fare"]]
print(age_fare)

#generamos un grafico de dispersion y lo personalizamos con etiquetas
titanic.plot.scatter(x="Age", y="Fare")
plt.title("Relación entre Edad y Tarifa")
plt.xlabel("Edad")
plt.ylabel("Tarifa")
plt.show()