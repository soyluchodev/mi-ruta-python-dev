
# 📘 Diccionarios en Python – Introducción básica

# Un diccionario guarda pares clave:valor
persona = {
    "nombre": "Ana",
    "edad": 30,
    "profesion": "Desarrolladora"
}

# Acceder a un valor
print("Nombre:", persona["nombre"])

# Modificar un valor
persona["edad"] = 31

# Agregar un nuevo par clave:valor
persona["ciudad"] = "Madrid"

# Ver todo el diccionario
print("Diccionario completo:", persona)

# Recorrer claves y valores
for clave, valor in persona.items():
    print(f"{clave}: {valor}")

# Obtener valor sin error si no existe (devuelve None)
print("Altura:", persona.get("altura"))

# Eliminar un elemento
persona.pop("ciudad")

# Ver solo claves
print("Claves:", list(persona.keys()))

# Ver solo valores
print("Valores:", list(persona.values()))
