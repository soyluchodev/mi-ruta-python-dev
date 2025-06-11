# 📄 Usar readlines(): devuelve una lista con todas las líneas del archivo
with open('archivoprueba.txt', 'r', encoding='UTF-8') as f:
    lineas = f.readlines()
    print(lineas)  # ['línea 1\n', 'línea 2\n', ...]

# 📄 Usar readline(): devuelve solo la primera línea del archivo
with open('archivoprueba.txt', 'r', encoding='UTF-8') as f:
    primera_linea = f.readline()
    print(primera_linea)  # 'Primera línea del archivo\n'