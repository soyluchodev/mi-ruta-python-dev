import pandas as pd

titanic = pd.read_csv("https://raw.githubusercontent.com/pandas-dev/pandas/main/doc/data/titanic.csv")

print(titanic)

print(titanic.head(8))
print(titanic.tail(8))
print(titanic.dtypes)

titanic.to_csv("titanic_filtrado.csv", columns=["Name", "Sex", "Age"], index=False)

primeras_10 = titanic.head(10)
primeras_10.to_csv("titanic_10filas.csv", columns=["Name", "Sex", "Age"], index=False)