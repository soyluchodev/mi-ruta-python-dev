## 📋💹Introducción a pandas / Primeros pasos

**Pandas es un paquete de Python que proporciona estructuras de datos rápidas, flexibles y expresivas para que trabajar con datos relacionales o etiquetados en sea fácil e intuitivo.**


## 1. 🧰Instalacion

Instalacion con pip. 👉

```bash
pip install pandas
```
- Esto carga la biblioteca pandas, que usaremos para trabajar con datos en forma de tablas.
- Se importa como pd por convención, así podemos escribir pd.DataFrame(...) en lugar de pandas.DataFrame(...).

## 2. 🧱Creamos un diccionario en python

```Python
data = {
    "Nombre": ["Ana", "Juan", "Laura"],
    "Edad": [23, 34, 29],
    "Ciudad": ["Madrid", "Barcelona", "Sevilla"]
}
```

- Creamos un diccionario de Python con tres claves: "Nombre", "Edad" y "Ciudad".
- Cada clave tiene como valor una lista con datos.
- Este diccionario representa una pequeña tabla con tres columnas y tres filas.


## 📊 3. Crear un DataFrame

```Python
df = pd.DataFrame(data)
```

- Usamos pd.DataFrame(...) para convertir el diccionario en un DataFrame, que es una tabla de Pandas.
- df ahora contiene los datos organizados como si fueran una hoja de cálculo.

## 👀 4. Ver los datos

```Python
print(df)
```

- Mostramos el contenido de la tabla df en pantalla.

Resultado 👉

```nginx
    Nombre  Edad     Ciudad
0    Ana    23     Madrid
1   Juan    34  Barcelona
2  Laura    29    Sevilla
```

- Cada fila tiene un número (índice) automáticamente asignado: 0, 1, 2.

## 🔎 5. Acceder a una columna específica


```python
df["Edad"]
```
- Esto devuelve solo la columna "Edad" como un objeto ```Series```.

```yaml
0    23
1    34
2    29
Name: Edad, dtype: int64
```
- Sirve para analizar una sola variable, como las edades.

 6. Filtrar filas según una condición

 ```python
df[df["Edad"] > 25]
 ```

 - Esto devuelve solo las filas donde la edad es mayor a 25.

 ```nginx
   Nombre  Edad     Ciudad
1   Juan     34  Barcelona
2  Laura     29    Sevilla
 ```

 - Es una forma rápida de hacer filtros sobre los datos, como si aplicáramos un “filtro” en Excel.

## 7. Agregar una nueva columna
**Esta es genial**

```python
df["MayorEdad"] = df["Edad"] >= 30
```
- Crea una nueva columna llamada "MayorEdad".
- Cada fila tendrá True si la edad es 30 o más, y False si no.

```graphql
  Nombre  Edad     Ciudad  MayorEdad
0   Ana     23     Madrid      False
1  Juan     34  Barcelona       True
2 Laura     29    Sevilla      False
```
- Esto es útil para agregar etiquetas o clasificaciones.

## 💾 8. Guardar los datos en un archivo CSV

```python
df.to_csv("personas.csv", index=False)
```

- Guarda el contenido del DataFrame en un archivo llamado personas.csv.
- index=False indica que no queremos guardar la columna de índices (0, 1, 2).

## ✅ Conclusión
**Hoy aprendi:**

- Crear un DataFrame desde un diccionario
- Leer y visualizar columnas
- Filtrar por condiciones
- Agregar nuevas columnas
- Guardar los datos como archivo CSV

