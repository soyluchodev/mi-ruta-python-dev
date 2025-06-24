## 📋 Mostrar una lista en HTML con Flask y Jinja2

**1️⃣ En app.py – enviamos la lista**

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    tareas = ["Estudiar Flask", "Subir proyecto a GitHub", "Escribir nota en el blog"]
    return render_template('index.html', tareas=tareas)
```

**2️⃣ En templates/index.html - mostramos la lista**

```html
<!doctype html>
<html lang="es">
<head>
    <meta charset="utf-8">
    <title>Lista de Tareas</title>
</head>
<body>
    <h1>Mis Tareas</h1>
    <ul>
        {% for tarea in tareas %}
            <li>{{ tarea }}</li>
        {% endfor %}
    </ul>
</body>
</html>
```


✅ ¿Qué aprendi?
- Flask puede pasar listas al HTML.
- Jinja2 permite recorrerlas con for y mostrar cada ítem.
