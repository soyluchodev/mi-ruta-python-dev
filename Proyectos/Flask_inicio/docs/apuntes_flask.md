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