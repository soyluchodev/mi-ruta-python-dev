# 📂 Escribir archivos en Python

# 1. Modo "a" (append): Agrega contenido al final del archivo si existe. Si no existe, lo crea.
with open("archivoprueba.txt", "a", encoding="UTF-8") as f:
    f.write("Esta es una nueva línea en mi archivo")
    f.write("\nY podemos agregar tantas como queramos")

# 2. Modo "w" (write): Sobrescribe el contenido del archivo. Si no existe, lo crea.
with open("archivoprueba.txt", "w", encoding="UTF-8") as f:
    f.write("Eliminé el contenido, lo siento")

# 3. Leer el contenido del archivo para verificar lo escrito
with open("archivoprueba.txt", encoding="UTF-8") as f:
    print(f.read())

# 4. Modo "x" (exclusive creation): Crea un nuevo archivo. Si ya existe, lanza un error.
# Nota: El archivo debe tener una extensión y nombre válidos.
try:
    with open("nuevoarchivo.txt", "x", encoding="UTF-8") as f:
        f.write("Este archivo fue creado con modo 'x'")
except FileExistsError:
    print("El archivo ya existe y no se puede crear nuevamente con modo 'x'")
