# 📝 Gestor de Tareas en Python

Este es un sencillo gestor de tareas por consola, creado en Python puro. Permite agregar, ver, marcar como completadas y eliminar tareas, con almacenamiento persistente en un archivo `.json`.

---

## 🚀 Funcionalidades

- 📋 **Ver tareas:** muestra todas las tareas guardadas con su estado (completada o no).
- ➕ **Agregar tarea:** permite introducir una nueva tarea que se guarda automáticamente.
- ✅ **Marcar como completada:** cambia el estado de una tarea a "hecha".
- ❌ **Eliminar tarea:** elimina una tarea seleccionada de la lista.
- 💾 **Guardado persistente:** todas las tareas se almacenan en `tareas.json`.

---

## 📁 Estructura del proyecto

```
Gestor_tareas/
│
├── archivo.py           # Contiene las funciones principales del programa
├── main.py              # Archivo principal que ejecuta el menú e interactúa con el usuario
├── tareas.json          # Archivo donde se guardan las tareas en formato JSON
└── README.md            # Este archivo
```

---

## 🧠 Cómo funciona

Cada tarea se guarda como un diccionario con esta estructura:

```python
{
  "titulo": "Hacer ejercicio",
  "completada": False
}
```

La lista de tareas se guarda como un JSON para mantener los datos aunque se cierre el programa.

---

## ▶️ Cómo ejecutarlo

1. Clona o descarga este repositorio.
2. Asegúrate de tener Python 3 instalado.
3. Ejecutá el programa desde consola:

```bash
python main.py
```

---

## 📌 Ejemplo de uso

```
--- Gestor de Tareas ---
1. Ver tareas
2. Agregar tarea
3. Marcar tarea como completada
4. Eliminar tarea
5. Salir
Elige una opción:
```

---

## 📚 Aprendizajes

En este proyecto aplico:

- Lectura y escritura de archivos `.json`
- Listas y diccionarios en Python
- Uso de funciones
- Bucles y control de flujo
- Menú interactivo por consola

---

## 🛠️ Posibles mejoras

- Crear interfaz gráfica con Tkinter o Flask
- Buscar tareas por nombre
- Dividir tareas en categorías

---
