from datetime import datetime

archivo = 'notas.txt'

# ✍️ Función para escribir una nota nueva en el archivo
def escribir(entrada):
    with open('notas.txt', 'a', encoding='UTF-8') as f:
        f.write(f'{datetime.now().strftime("%d/%m/%y")}: -- {entrada}\n')
        print("Nota agregada a 'notas.txt' 📒")
        
        

# 📄 Función para mostrar las últimas 10 notas guardadas
def ver_notas():
    with open('notas.txt', encoding='UTF-8') as f:
        lineas = f.readlines()
        print("\n📄 Últimas 10 notas:\n")
        for linea in lineas[-10:]:
            print(linea, end="")



# 🔍 Función para buscar notas por una fecha específica
def buscar_por_fechas():
    busca_fecha = input("Introduce una fecha (formato dd/mm/aa): ")
    with open('notas.txt', encoding='UTF-8') as f:
        encontradas = False
        for linea in f:
            if linea.startswith(busca_fecha):
                print(linea, end="")
                encontradas = True
        if not encontradas:
            print("No se encontraron notas con esa fecha.")


# 📝 Flujo inicial simple: agregar una nota, mostrar últimas, y buscar por fecha
entrada = input('Introduce tu nota: ')
escribir(entrada)
ver_notas()
buscar_por_fechas()


# 📋 Menú de opciones (en construcción)
def menu():
    print("\n📚 Este es tu gestor de notas 📒🥸")
    print("01 - Agregar nota")
    print("02 - Ver últimas 10 notas")
    print("03 - Buscar notas por fecha")
    print("04 - Salir")
