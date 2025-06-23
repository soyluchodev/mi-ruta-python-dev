from archivo import cargar_tareas, guardar_tareas, mostrar_tareas, mostrar_menu, eliminar_tarea, marcar_completada

def main():
    # Cargamos la lista de tareas (vacía o con datos)
    tareas = cargar_tareas()
    while True:
        opcion = mostrar_menu() 
        if opcion == '1':
            # Mostramos las tareas actuales enumeradas
            print("Tareas actuales:")
            mostrar_tareas(tareas)
            
        elif opcion == '2':
            # Pedimos una tarea nueva (string)
            tarea = input("Introduce una tarea: ")
            # Agregamos esa tarea a la lista
            tareas.append({"titulo": tarea, 'completada': False})
            # Guardamos la lista actualizada en el archivo
            guardar_tareas(tareas)
            print("Tarea agregada y guardada correctamente.")
        elif opcion == '3':
            marcar_completada(tareas)
            guardar_tareas(tareas)
        elif opcion == '4':
            tareas = eliminar_tarea(tareas)
            guardar_tareas(tareas)
        elif opcion == '5':
            break

if __name__ == "__main__":
    main()
    