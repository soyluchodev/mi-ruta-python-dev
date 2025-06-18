# Lista para almacenar todos los productos del inventario
inventario = []

# Función para agregar un nuevo producto al inventario
def agregar_producto():
    nuevo_producto = {}  # Diccionario vacío para guardar los datos del producto

    # Solicita el nombre del producto al usuario
    nombre_producto = input('Ingresa el nombre del producto: ')
    # Bucle para asegurarse de que la cantidad ingresada sea un número entero
    while True:
        try:
            cantidad_producto = int(input('Ingresa la cantidad: '))
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

# Función para mostrar todos los productos almacenados en el inventario
def mostrar_producto():
    for producto in inventario:
        nombre = producto['producto'].capitalize()  # Capitaliza el nombre del producto
        cantidad = producto['cantidad']
        precio = producto['precio']
        print(f'Producto: {nombre} | Cantidad: {cantidad} | Precio: {precio}€')

# Función vacía para buscar productos por nombre (en desarrollo)
def buscar_por_nombre():
    pass

# Bucle principal del programa
while True:
    print("1 - Agregar otro producto")
    print("2 - Mostrar productos")  
    print("3 - Salir") 
    opcion = input('Elige una opcion: ')
    
    if opcion == '1':
        agregar_producto()
    elif opcion == '2':
        mostrar_producto()
    elif opcion == '3':
        break 

input('Presiona Enter para terminar')
