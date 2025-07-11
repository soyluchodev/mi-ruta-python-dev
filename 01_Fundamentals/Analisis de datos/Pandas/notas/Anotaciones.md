﻿## 📒📚Anotaciones importantes


**Este código, tal cual, solo imprime las listas ciudades y los valores booleanos (como está en el libro). La cuestión es que no imprime la serie creada con numeros porque crea la serie pero no la muestra. Al usar un archivo Jupyter, solo muestra la primera y la última línea, aunque la línea del medio está igual que numeros. Se imprime porque es la última línea del recuadro.**
```python
#Ejercicio 1 Series
ciudades = ['Madrid', 'Londres', 'Nueva York', 'Tokio']
print(ciudades)
ciudades_serie = pd.Series(ciudades)
print(ciudades_serie)

numeros = [1, 2, 3, 4, 5]
pd.Series(numeros)



booleanos = [True, False, False, True, True]
pd.Series(booleanos)
````

**También se puede poner solo el nombre de la variable para mostrarla (siempre y cuando sea la última línea evaluada):**

```python
colores = pd.Series(["Azul", "Verde", "Rojo", "Amarillo", "Negro"])
colores

#Salida
0        Azul
1       Verde
2        Rojo
3    Amarillo
4       Negro
dtype: object
```

## Import Pandas

**No hace falta importar pandas en cada recuadro de texto del notebook jupyter. Si se pone al principio. siempre y cuando no se reinicie el kernel o se cierre vs code. El kernel es el que almacena las variables importaciones y todo, asi que con hacerlo una vez al principio se puede trabajar**

## Head ()

```python
#Ejercicio 5 de Series
numeros = pd.Series([23,35,2,78,54,98,17,69,48])
numeros
numeros.head()  # Muestra los primeros 5 elementos de la serie 'numeros'
numeros.head(3) #especificamos valor para el parametro. osea nos da los primeros 3
```


## tail()

```python
#Ejercicio 5 de Series
numeros = pd.Series([23,35,2,78,54,98,17,69,48])
numeros.tail()   # Muestra los últimos 5 elementos de la serie 'numeros'
numeros.tail(3)  # Muestra los últimos 3 elementos de la serie 'numeros'
```

## serie.sort_values

```python
#Ejercicio 5 de Series
numeros = pd.Series([23,35,2,78,54,98,17,69,48])
numeros.sort_values()  # Ordena la serie 'numeros' de menor a mayor
numeros.sort_values(ascending=False)  # Ordena la serie 'numeros' de mayor a menor
numeros.sort_values(ascending=True)  # Ordena la serie 'numeros' de menor a mayor (equivalente a sort_values())
```

