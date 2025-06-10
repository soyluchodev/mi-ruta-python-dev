# 📂 Abrir archivos en Python con open()

# 🔹 Crear un manejador de archivos (file handler)
archivo = open('mbox-short.txt', 'r')
print(archivo)
# Salida: <_io.TextIOWrapper name='mbox-short.txt' mode='r' encoding='cp1252'>
# Esto es un manejador de archivos, no el contenido del archivo.
# 🔹 Contar líneas de un archivo usando un bucle for
archivo = open('mbox-short.txt', 'r')
contador = 0
for linea in archivo:
    contador += 1
print("Contador de líneas:", contador)
# Salida: 11 (cantidad de líneas del archivo)

# 🔹 Leer todo el contenido del archivo con read()
archivo = open('mbox-short.txt', 'r')
contenido = archivo.read()
print(contenido)
# Esto imprime todo el contenido del archivo como un único string

# 🔹 Buscar líneas que empiezan con 'Las'
archivo = open('mbox-short.txt', 'r')
for linea in archivo:
    if linea.startswith('Las'):
        print(linea)


# 🔹 Leer todo el contenido con read() usando with / agregado para encoding= 'UTF-8' que se vea bien en consola
with open('mbox-short.txt', 'r', encoding= 'UTF-8') as archivo:
    contenido = archivo.read()
print(contenido)