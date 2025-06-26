## 📋💹Introducción a pandas / Leer y escribir

**Pandas tiene la funcion ```read.csv``` para leer archivos almacenados en un csv como ```DataFrame``` tambien permite fuentes de datos diferentes de forma predeterminada (csv, excel, sql, json, parquet, …), cada uno de ellos con el prefijo read_**


## 📥 Leer datos – read_csv()
**En este ejemplo uso los datos del Titanic directamente desde la web**

https://raw.githubusercontent.com/pandas-dev/pandas/main/doc/data/titanic.csv

```python
titanic = pd.read_csv("https://raw.githubusercontent.com/pandas-dev/pandas/main/doc/data/titanic.csv")

print(titanic)
```
**la salida es 👉:** 
- pandas muestra las primeras y las ultimas 5 filas del ``DataFrame``

 ```nginx
     PassengerId  Survived  Pclass  ...     Fare Cabin  Embarked
0              1         0       3  ...   7.2500   NaN         S
1              2         1       1  ...  71.2833   C85         C
2              3         1       3  ...   7.9250   NaN         S
3              4         1       1  ...  53.1000  C123         S
4              5         0       3  ...   8.0500   NaN         S
..           ...       ...     ...  ...      ...   ...       ...
886          887         0       2  ...  13.0000   NaN         S
887          888         1       1  ...  30.0000   B42         S
888          889         0       3  ...  23.4500   NaN         S
889          890         1       1  ...  30.0000  C148         C
890          891         0       3  ...   7.7500   NaN         Q

[891 rows x 12 columns]
 ```

## 👀 Ver los primeros o últimos registros

**Para ver las primeras un numero X de un ``DataFrame`` usamos head()**
**de la misma manera tambien usamos tail() para que no devuelva las ultimas asi:**

```python
titanic.head(8)
print(titanic.head(8)) #imprimimos para ver en consola
titanic.tail(8)
print(titanic.tail(8))
```


## 🔎 Ver tipos de datos – .dtypes

**dtypes nos proporciona para cada columna el tipo de dato utilizado**

```python
print(titanic.dtypes)
```

 ```nginx
PassengerId      int64
Survived         int64
Pclass           int64  
Name            object  
Sex             object
Age            float64 #numeros flotantes
SibSp            int64 #numeros enteros
Parch            int64
Ticket          object #cadenas de texto
Fare           float64
Cabin           object
Embarked        object
dtype: object
 ```


## 💾 Filtrar columnas y guardar con to_csv()

**Si quisieramos por ejemplo guardar algunas columnas**

```python
# Del dataset titanic queremos guardar solo 'Name', 'Sex' y 'Age'
titanic.to_csv("titanic_filtrado.csv", columns=["Name", "Sex", "Age"], index=False)
```

**Si quisieramos esas columnas pero las primeras 10**
```python
#asignamos a una nueva variable
primeras_10 = titanic.head(10)
primeras_10.to_csv("titanic_10filas.csv", columns=["Name", "Sex", "Age"], index=False)
```