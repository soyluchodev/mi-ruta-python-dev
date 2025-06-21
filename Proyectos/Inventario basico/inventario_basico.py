#importamos el modulo json
import json


# Lista para almacenar todos los productos del inventario
inventario = []


# cargamos el archivo si existe, cargamos su contenido y lo guardamos en la variable inventario
try:
    with open('inventario.json', 'r') as f:  
        inventario = json.load(f)
except FileNotFoundError:
    print('No hay ningun archivo')

# Función para agregar un nuevo producto al inventario
def agregar_producto():
    nuevo_producto = {}  # Diccionario vacío para guardar los datos del producto

    # Solicita el nombre del producto al usuario
    nombre_producto = input('Ingresa el nombre del producto: ')
    # Bucle para asegurarse de que la cantidad ingresada sea un número decimal
    while True:
        try:
            cantidad_producto = float(input('Ingresa la cantidad: '))
            break
        except ValueError:
            print("Error: Debes ingresar un número entero válido para la cantidad.")

    # Bucle para asegurarse de que el precio ingresado sea un número decimal
    while True:
        try:
            precio_producto = float(input('Ingresa el precio del producto: '))
            break
        except ValueError:
            print('Error: Debes ingresar un número entero válido para el precio.')

    # Actualiza el diccionario con los datos del producto
    nuevo_producto.update(
        {'producto' : nombre_producto,
        'cantidad' : cantidad_producto,
        'precio' : precio_producto
        })
    # Agrega el diccionario del producto a la lista del inventario
    inventario.append(nuevo_producto)
    print('Producto agregado al inventario con éxito')
    
    with open('inventario.json', 'w') as f:
        json.dump(inventario, f, indent= 3)

# Función para mostrar todos los productos almacenados en el inventario
def mostrar_producto():
    for producto in inventario:
        nombre = producto['producto'].capitalize()  # Capitaliza el nombre del producto
        cantidad = producto['cantidad']
        precio = producto['precio']
        print(f'Producto: {nombre} | Cantidad: {cantidad} | Precio: {precio}€')

# Función vacía para buscar productos por nombre (en desarrollo)
def buscar_por_nombre():
    buscar_producto = input('\nIngresa nombre del producto: ').strip()
    encontrado = False
    for producto in inventario:
        nombre = producto['producto'].capitalize()  # Capitaliza el nombre del producto
        cantidad = producto['cantidad']
        precio = producto['precio']
        if producto['producto'].lower() ==  buscar_producto.lower():
            print(f'Producto: {nombre} | Cantidad: {cantidad} | Precio: {precio}€')
            encontrado = True
            break
    if not encontrado:
        print('Producto no encontrado.')

# Bucle principal del programa
while True:
    print("1 - Agregar otro producto")
    print("2 - Mostrar productos")  
    print("3 - Buscar producto por nombre")
    print("4 - Salir") 
    opcion = input('Elige una opcion: ')
    
    if opcion == '1':
        agregar_producto()
    elif opcion == '2':
        mostrar_producto()
    elif opcion == '3':
        buscar_por_nombre()
    elif opcion == '4':
        break 

input('Presiona Enter para terminar')
