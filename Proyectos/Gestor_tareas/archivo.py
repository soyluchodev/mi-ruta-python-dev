import json


def cargar_tareas(nombre_archivo="tareas.json"):
    try:
        # Intentamos abrir el archivo con el nombre dado en modo lectura
        with open(nombre_archivo, 'r') as archivo:
            # Si el archivo existe y se puede leer, cargamos su contenido JSON y lo devolvemos
            return json.load(archivo)
    except FileNotFoundError:
        # Si el archivo no existe, capturamos el error y devolvemos una lista vacía para evitar fallos
        return []
    except json.JSONDecodeError:
        # Si el archivo está corrupto o vacío (no es un JSON válido), también devolvemos lista vacía
        return []

def guardar_tareas(data, nombre_archivo="tareas.json"):
    # Abrimos (o creamos) el archivo con el nombre indicado en modo escritura ('w')
    # Esto significa que si el archivo existe, se sobreescribe su contenido
    with open(nombre_archivo, 'w') as archivo:
        # Convertimos la lista 'data' a formato JSON y la escribimos en el archivo
        # El parámetro 'indent=4' es para que el JSON quede con sangría y sea legible
        json.dump(data, archivo, indent=4)


def mostrar_tareas(tareas):
    if not tareas:
        print("No hay tareas.")
    else:
        for i, tarea in enumerate(tareas, 1):
            estado = "✔" if tarea["completada"] else "✘"
            print(f"{i}. [{estado}] {tarea['titulo']}")

def eliminar_tarea(tareas):
    if not tareas:
        print("No hay tareas para eliminar")
        return tareas
    mostrar_tareas(tareas)
    try:
        num = int(input('Introduce el numero de tarea a eliminar: '))
        if 1 <= num <= len(tareas):
            tarea_eliminada = tareas.pop(num - 1)
            print(f"tarea '{tarea_eliminada}' eliminada correctamente.")
        else:
            print('Número inválido.')
    except ValueError:
        print('Por favor ingresa un número válido.')
    return tareas

def marcar_completada(tareas):
    if not tareas:
        print("No hay tareas para marcar")
        return tareas
    mostrar_tareas(tareas)
    try:
        num = int(input("Introduce el numero de tarea a marcar como completada: "))
        if 1 <= num <= len(tareas):
            tareas[num - 1]['completada'] = True
            print('Tarea marcada como completada')
        else:
            print("Número inválido.")
    except ValueError:
        print("Por favor ingresa un número válido.")
    
    return tareas

def mostrar_menu():
    print("\n--- Gestor de Tareas ---")
    print("1. Ver tareas")
    print("2. Agregar tarea")
    print("3. Marcar tarea como completada")
    print("4. Eliminar tarea")
    print("5. Salir")
    opcion = input("Elige una opción: ")
    return opcion