# 📦 Inventario Básico

Proyecto simple en Python para gestionar un inventario de productos utilizando diccionarios y listas. Permite al usuario ingresar productos con su nombre, cantidad y precio, además de ver, buscar o eliminar productos registrados.

---

## 🎯 Objetivos del proyecto

- Practicar el uso de **diccionarios** y **listas**.
- Capturar datos usando `input()` y validarlos.
- Estructurar datos en una lista de diccionarios.
- Implementar control de errores con `try-except`.
- Utilizar archivos JSON para guardar datos.

---

## 📁 Estructura del proyecto
```
inventario basico/
├── inventario_basico.py
└── READNE.md 
```


## 🧠 Conceptos aplicados

- Diccionarios (`dict`)
- Listas (`list`)
- Bucles (`while`, `for`)
- Entrada de datos con `input()`
- Conversión de tipos (`int`, `float`)
- Validación de errores (`try-except`)
- Funciones para organizar el código
- Manejo de archivos con el módulo `json`

---

## 💻 Cómo funciona

El programa muestra un menú con las siguientes opciones:

1. Agregar producto  
2. Mostrar productos  
3. Buscar producto por nombre  
4. Eliminar producto  
5. Salir

### Detalles por opción:

1. **Agregar producto**:
   - Solicita nombre, cantidad y precio.
   - Valida que la cantidad y el precio sean numéricos.
   - Guarda el producto como un diccionario.
   - Agrega el producto a la lista `inventario`.
   - Guarda o crea un archivo JSON si no existe.

2. **Mostrar productos**:
   - Lista todos los productos registrados con nombre, cantidad y precio.

3. **Buscar producto por nombre**:
   - Solicita el nombre del producto y muestra su información si existe.

4. **Eliminar producto**:
   - Permite eliminar un producto del inventario por nombre si se encuentra.

5. **Salir**:
   - Termina la ejecución del programa.

---

## 📌 Ejemplo de uso

```bash
1 - Agregar otro producto
2 - Mostrar productos
3 - Buscar producto por nombre
4 - Eliminar producto
5 - Salir
Elige una opcion: 1
Ingresa el nombre del producto: Manzana
Ingresa la cantidad: 10
Ingresa el precio del producto: 1.99
Producto agregado al inventario con éxito

1 - Agregar otro producto
2 - Mostrar productos
3 - Buscar producto por nombre
4 - Eliminar producto
5 - Salir
Elige una opcion: 2
Producto: Manzana | Cantidad: 10 | Precio: 1.99€

1 - Agregar otro producto
2 - Mostrar productos
3 - Buscar producto por nombre
4 - Eliminar producto
5 - Salir
Elige una opcion: 3
Ingresa nombre del producto: mouse
Producto: Mouse | Cantidad: 10 | Precio: 25.99€

1 - Agregar otro producto
2 - Mostrar productos
3 - Buscar producto por nombre
4 - Eliminar producto
5 - Salir
Elige una opcion: 4
Ingresa nombre del producto a eliminar: mouse
Producto eliminado con éxito.

1 - Agregar otro producto
2 - Mostrar productos
3 - Buscar producto por nombre
4 - Eliminar producto
5 - Salir
Elige una opcion: 5

Presiona Enter para terminar