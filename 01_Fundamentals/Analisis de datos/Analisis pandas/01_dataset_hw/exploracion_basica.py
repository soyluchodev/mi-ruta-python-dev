#importamos pandas
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Cargamos el archivo
df = pd.read_csv("hw_200.csv")

#ver las primeras filas

print("Primeras filas:")
print(df.head())

#vemos la forma de los datos

print("\nForma del dataset (filas, columnas): ")
print(df.shape)

#vemos los nombres de las columnas

print("\nColumnas:")
print(df.columns)

#Estadisticas generales
print("Estadisticas generales:")
print(df.describe())

#verificamos datos nulos
print("\nDatos nulos por columnas:")
print(df.isnull().sum())


# ¿Cuántos registros y columnas hay?
#Hay 200 registros y 3 columnas

# ¿Qué columnas existen?
#index, heigth y weight

# ¿Hay datos nulos?
#No hay datos nulos 

# ¿Qué ves en las estadísticas (promedio, mínimo, máximo)?

# Las estadísticas muestran que la altura promedio es de aproximadamente 66.5 pulgadas, con un mínimo de 60 y un máximo de 75.
# En cuanto al peso, el promedio es de 160.3 libras, con un mínimo de 100.2 y un máximo de 210.
# Ambas variables tienen una distribución razonable para personas adultas. No hay valores extremos ni fuera de lo normal.