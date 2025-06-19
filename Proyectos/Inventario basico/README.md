# 📦 Inventario Básico

Proyecto simple en Python para gestionar un inventario de productos utilizando diccionarios y listas. Permite al usuario ingresar productos con su nombre, cantidad y precio, ver todos los productos ingresados.

---

## 🎯 Objetivos del proyecto

- Practicar el uso de **diccionarios** y **listas**.
- Capturar datos usando `input()` y validarlos.
- Estructurar datos en una lista de diccionarios.
- Implementar control de errores con `try-except`.

---


📁 Estructura del proyecto

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

---

## 💻 Cómo funciona

. El programa muestra un menú con las siguientes opciones:
   - Agregar producto
   - Mostrar productos
   - Buscar producto por nombre
   - Salir

2. Si el usuario elige **"Agregar producto"**:
   - Se solicita nombre, cantidad y precio del producto.
   - Se valida que la cantidad sea un número entero y el precio un número decimal.
   - Se guarda el producto en un diccionario.
   - El producto se agrega a la lista `inventario`.

3. Si elige **"Mostrar productos"**, se listan todos los productos registrados.

4. Si elige **"Buscar producto por nombre"**: se lista el producto nombrado

5. Si elige **"Salir"**, el programa termina.
---

## 📌 Ejemplo de uso

```bash
1 - Agregar otro producto
2 - Mostrar productos
3 - Buscar producto por nombre
4 - Salir
Elige una opcion: 1
Ingresa el nombre del producto: Manzana
Ingresa la cantidad: 10
Ingresa el precio del producto: 1.99
Producto agregado al inventario con éxito

1 - Agregar otro producto
2 - Mostrar productos
3 - Buscar producto por nombre
4 - Salir
Elige una opcion: 2
Producto: Manzana | Cantidad: 10 | Precio: 1.99€

1 - Agregar otro producto
2 - Mostrar productos
3 - Buscar producto por nombre
4 - Salir
Elige una opcion: 3
Ingresa nombre del producto: mouse
Producto: Mouse | Cantidad: 10 | Precio: 25.99€

1 - Agregar otro producto
2 - Mostrar productos
3 - Buscar producto por nombre
4 - Salir
Elige una opcion: 4

Presiona Enter para terminar