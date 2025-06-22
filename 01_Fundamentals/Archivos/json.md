# Mini guía de JSON en Python 🐍📦

## ¿Qué es JSON?

JSON (JavaScript Object Notation) es un formato ligero para almacenar y transportar datos. Es muy usado para:
- Guardar configuraciones
- Intercambiar datos en APIs
- Almacenamiento simple de información

En Python, usamos el módulo `json` para convertir entre:
- Objetos Python (listas, diccionarios, números, strings)
- Texto con formato JSON

---

## Las 4 funciones básicas

### 1. `json.dumps()`

**Convierte un objeto Python → cadena JSON**

Uso típico:
- Enviar datos por red
- Mostrar en pantalla
- Almacenar en bases de datos

```python
import json

data = {"nombre": "Ana", "edad": 25, "activo": True}
json_str = json.dumps(data)
print(json_str)  # Salida: '{"nombre": "Ana", "edad": 25, "activo": true}'
```

### 2. `json.loads()`

**Convierte una cadena JSON a un objeto Python**

```python
json_str = '{"nombre": "Ana", "edad": 25, "activo": true}'

data = json.loads(json_str)
print(data["nombre"])  # Salida: Ana
print(type(data))      # Salida: <class 'dict'>
```


### 3. `json.dump()`

**Guarda un objeto Python en un archivo JSON**
**Para guardar datos en disco directamente**

```python
data = {"nombre": "Ana", "edad": 25, "activo": True}

with open("datos.json", "w") as f:
    json.dump(data, f, indent=4)  # indent=4 para formato legible
```

### 4. `json.load()`

**Lee un archivo JSON y lo convierte a un objeto Python**
**Para cargar datos guardados**


```python
with open("datos.json", "r") as f:
    data = json.load(f)

print(data["edad"])  # Salida: 25
```

## Parámetros útiles

- indent (en dump/dumps): Agrega sangría para formato legible
- sort_keys=True: Ordena las claves alfabéticamente
- ensure_ascii=False: Muestra caracteres unicode correctamente (acentos, ñ)

```python
json.dumps(data, indent=2, sort_keys=True, ensure_ascii=False)
```
