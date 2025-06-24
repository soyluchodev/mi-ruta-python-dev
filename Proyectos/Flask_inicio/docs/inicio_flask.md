## 📒Primeros pasos en Flask

**1️⃣Primero: Crear un entorno**

 Para instalar dependencias primero y recomendable segun el Quickstart. Creamos un entorno virtual. En mi caso en (VS Code + Windows). Entonces, creamos una carpeta de proyecto. Entonces en VS Code: ver -- > Terminal y escribimos:

```bash
mkdir myproject
cd myproject #Accedemos a esa carpeta desde la terminal
py -3 -m venv .venv
```

Esto nos crea todas las subcarpetas correspondientes para el proyecto.

**2️⃣Segundo: Activacion del entorno**

(La primera vez lo hice mal y me olvide de activar entonces me daba error por todos lados 😅). Ok para activar el entorno, otra vez consola y ejecutamos:

```Bash
.venv\Scripts\activate
```
y si todo va bien, se activa el entorno virtual. El prompt de consola cambia y se ve algo asi.

```Bash
(.venv) C:\ruta\del\proyecto>
```

**3️⃣Tercero: Instalacion de Flask en el entorno virtual**

instalamos Flask con el comando

```Bash
pip install Flask
```

esto instala todas las dependecians, y demas, por defecto. (como Jinja2, Werkzeug, etc.)

## PD:
**Para desactivar el entorno virtual** ponemos en consola ```deactivate```

## Creando primera app

Una vez la carpeta esta configurada y el entorno virtual con flask instalado listo. Creamos un archivo ejemplo (hello.py). Escribimos:

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

```
Y al abrir la web en "http://127.0.0.1:5000/". Deberiamos ver el "Hola, Mundo!/Hola, Flask!.
Ahora. ¿Que es esto? quiero desglosarlo para no olvidarme.

| Línea                     | ¿Qué hace?                                                          |
| ------------------------- | ------------------------------------------------------------------- |
| `from flask import Flask` | Importás Flask para poder usarlo                                    |
| `app = Flask(__name__)`   | Creás la app web|
| `@app.route('/')`         | Esta línea dice: *cuando el usuario va a `/`, hacé lo siguiente...* |
| `def hello_world():`            | Esta es la función que se ejecuta cuando alguien entra a `/`        |
| `return Hello, World!`     | Esto es lo que ve el navegador. Podría ser texto o HTML             |


## 🚀Damos el paso hacia una app web real.
**Mostrar una pagina html usando templates**

**1️⃣Primero, Flask busca los archivos HTML en una carpeta llamada templates. Creamos esa carpeta:**

```
myproject/
│
├── app.py
└── templates/
```
**2️⃣Segundo: Activacion del entorno**

Dentro de templates/ creamos un archivo ```index.html``` básica

```html
<!doctype html>
<html lang="es">
    <head>
    <meta charset="utf-8">
    <title>Mi primera página Flask</title>
    </head>
    <body>
    <h1>Hola desde una plantilla HTML</h1>
    <p>Este HTML lo carga Flask usando Jinja2</p>
    </body>
</html>
```
**3️⃣Crear la app.py**

Importante importar "render_template"
```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')
```

Ejecutamos el entorno virtual, entramos a "http://127.0.0.1:5000" y ahi esta mi primera web en flask!

✅ ¿Qué aprendi hasta aca?
- Cómo usar plantillas HTML reales
- Qué hace render_template()
- Cómo organizar la app de forma básica


## 🚀 Este paso te muestra cómo enviar datos desde Flask hacia HTML, usando Jinja2 (el motor de plantillas que usa Flask por defecto)

**1️⃣Paso 1: modificar app.py para enviar una variable:**

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    nombre = "Lucho"
    return render_template('index.html', nombre=nombre)
```
**2️⃣Paso 2: usar esa variable en index.html**

Dentro de templates/ creamos un archivo ```index.html``` básica

```html
<!doctype html>
<html lang="es">
    <head>
    <meta charset="utf-8">
    <title>Hola con Flask y Jinja</title>
    </head>
    <body>
    <h1>Hola {{ nombre }} 👋</h1>
    <p>Bienvenido a tu primera pagina con Flask y Jinja2.</p>
    </body>
</html>
```

```{{ nombre }}``` es cómo Jinja2 inserta el valor dentro del HTML.

✅ ¿Qué aprendi acá?

- Flask puede enviar datos a páginas HTML.
- Jinja2 puede mostrar variables dentro del HTML con {{ nombre }}.
- Esto permite hacer páginas dinámicas, no solo estáticas.

