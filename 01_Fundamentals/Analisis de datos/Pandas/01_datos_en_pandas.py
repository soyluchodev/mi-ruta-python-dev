import pandas as pd

data = {
    "Nombre": ["Ana", "Juan", "Laura"],
    "Edad": [23, 34, 29],
    "Ciudad": ["Madrid", "Barcelona", "Sevilla"]
}

#Usamos pd.DataFrame(...) para convertir el diccionario en un DataFrame, que es una tabla de Pandas.

df = pd.DataFrame(data)

print(df)
print(df["Edad"])
print(df[df["Edad"] > 25])
#primero agregamos columna (que modifica la el dataframe al principio) y luego imprimimos
df["MayorEdad"] = df["Edad"] > 30
print(df)
#aca le decimos. Toma df convertilo a un archivo csv que se llame "personas.csv" y no incluyas los indices (0, 1, 2 etc)
df.to_csv("personas.csv", index=False)
