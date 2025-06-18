# 📦 Inventario Básico

Proyecto simple en Python para gestionar un inventario de productos utilizando diccionarios y listas. Permite al usuario ingresar productos con su nombre, cantidad y precio, ver todos los productos ingresados.

---

## 🎯 Objetivos del proyecto

- Practicar el uso de **diccionarios** y **listas**.
- Capturar datos usando `input()` y validarlos.
- Estructurar datos en una lista de diccionarios.
- Implementar control de errores con `try-except`.

---

## 🧠 Conceptos aplicados

- Diccionarios (`dict`)
- Listas (`list`)
- Bucles (`while`, `for`)
- Entrada de datos con `input()`
- Conversión de tipos (`int`, `float`)
- Validación de errores (`try-except`)
- Funciones para organizar el código

---

## 💻 Cómo funciona

1. El programa muestra un menú con tres opciones:
   - Agregar producto
   - Mostrar productos
   - Salir
2. Si el usuario elige **"Agregar producto"**:
   - Pide nombre, cantidad y precio del producto.
   - Verifica que la cantidad sea un número entero y el precio un número flotante.
   - Guarda cada producto como un diccionario.
   - Agrega el diccionario a una lista (`inventario`).
3. Si elige **"Mostrar productos"**, muestra todos los productos registrados con formato.
4. Si elige **"Salir"**, termina el programa.

---

## 📌 Ejemplo de uso

```bash
1 - Agregar otro producto
2 - Mostrar productos
3 - Salir
Elige una opcion: 1
Ingresa el nombre del producto: Mouse
Ingresa la cantidad: 10
Ingresa el precio del producto: 25.99
Producto agregado al inventario con éxito

1 - Agregar otro producto
2 - Mostrar productos
3 - Salir
Elige una opcion: 2
Producto: Mouse | Cantidad: 10 | Precio:  2.22€

1 - Agregar otro producto
2 - Mostrar productos
3 - Salir
Elige una opcion: 3

Presiona Enter para terminar
