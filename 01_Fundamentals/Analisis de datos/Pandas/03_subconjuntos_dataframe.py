import pandas as pd

# Cargar el DataFrame del Titanic
titanic = pd.read_csv("https://raw.githubusercontent.com/pandas-dev/pandas/main/doc/data/titanic.csv")

# Seleccionar una sola columna
ages = titanic["Age"]
print(ages.head())

#verigicando el tipo de salida

print(type(titanic["Age"]))
print(titanic["Age"].shape)

age_sex = titanic[["Age", "Sex"]]
print(age_sex.head())

print(titanic.iloc[3])

mayores_de_70 = titanic.loc[titanic["Age"] > 70]
print(mayores_de_70)

print(titanic.loc[titanic["Age"] > 70, ["Name", "Age"]] )