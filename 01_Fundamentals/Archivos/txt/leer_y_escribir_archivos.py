# 📄 Usar readlines(): devuelve una lista con todas las líneas del archivo
with open('archivoprueba.txt', 'r', encoding='UTF-8') as f:
    lineas = f.readlines()
    print(lineas)  # ['línea 1\n', 'línea 2\n', ...]

# 📄 Usar readline(): devuelve solo la primera línea del archivo
with open('archivoprueba.txt', 'r', encoding='UTF-8') as f:
    primera_linea = f.readline()
    print(primera_linea)  # 'Primera línea del archivo\n'

#.strip(): elimina espacios en blanco y saltos de línea

linea = "  Hola mundo \n"
print(linea.strip())  # → "Hola mundo"


#.split(): divide una cadena en partes (por defecto, en espacios)

frase = "Python es genial"
print(frase.split())  # → ['Python', 'es', 'genial']