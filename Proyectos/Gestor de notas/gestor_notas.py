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

# 📋 Menú de opciones
def menu():
    print("\n📚 Este es tu gestor de notas 📒🥸")
    print("1 - Agregar nota")
    print("2 - Ver últimas 10 notas")
    print("3 - Buscar notas por fecha")
    print("4 - Salir")
    
    while True:
        opcion = input("Elige una opcion: ")
        if opcion == '1':
            entrada = input('Introduce tu nota: ')
            escribir(entrada)
        elif opcion == '2':
            ver_notas()
        elif opcion == '3':
            buscar_por_fechas()
        elif opcion == '4':
            print("Hasta luego!")
            input("\nPresiona Enter para cerrar el programa...")
            break
        else:
            print("Por favor selecciona una opcion valida.")

menu()