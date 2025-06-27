
## ¿Cómo selecciono un subconjunto de un DataFrame?

**Para seleccionar una columna utilizamos `[]` con el nombre de la columna que queremos**

```python
# Cargar el DataFrame del Titanic
titanic = pd.read_csv("https://raw.githubusercontent.com/pandas-dev/pandas/main/doc/data/titanic.csv")

# Seleccionar una sola columna
ages = titanic["Age"]
print(ages.head())
```

```text
0    22.0
1    38.0
2    26.0
3    35.0
4    35.0
Name: Age, dtype: float64
```

**Cada columna de un DataFrame es una Series. Al seleccionar una sola columna, el objeto devuelto es un pandas Series. Podemos verificar esto comprobando el tipo de salida:**

```python
print(type(titanic["Age"]))
# Salida : <class 'pandas.core.series.Series'>
```

---

## DataFrame.shape

**Es un atributo de un pandas `Series` que contiene el número de filas y columnas. Una Series de pandas es unidimensional y solo devuelve el número de filas**

```python
titanic["Age"].shape
# Salida : (891,)
```

---

## Seleccionar múltiples columnas

```python
age_sex = titanic[["Age", "Sex"]]
print(age_sex.head())
```

**Salida:**

```text
    Age     Sex
0  22.0    male
1  38.0  female
2  26.0  female
3  35.0  female
4  35.0    male
```

---

## Seleccionando por fila o columna con `.iloc` y `.loc`

**Supongamos que queremos solo la fila 3 del dataset. Usamos `.iloc`. Esto nos devuelve una Series**

```python
titanic.iloc[3]
```

```text
PassengerId                                               4
Survived                                                  1
Pclass                                                    1
Name           Futrelle, Mrs. Jacques Heath (Lily May Peel)
Sex                                                  female
Age                                                    35.0
SibSp                                                     1
Parch                                                     0
Ticket                                               113803
Fare                                                   53.1
Cabin                                                  C123
Embarked                                                  S
Name: 3, dtype: object
```

---

**Ahora si queremos seleccionar por columnas del dataset usamos `.loc`, por ejemplo, mayores de 70 años:**

```python
mayores_de_70 = titanic.loc[titanic["Age"] > 70]
print(mayores_de_70)
```

**O solo ver los nombres y edades de las personas mayores de 70:**

```python
# Esto es como decir: buscame en el dataset la columna "Age", luego filtrá solo las que son mayores de 70 y luego dame los nombres y las edades
print(titanic.loc[titanic["Age"] > 70, ["Name", "Age"]])
```
