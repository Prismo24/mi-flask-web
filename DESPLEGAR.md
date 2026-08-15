# Desplegar esta app Flask en PythonAnywhere

Guía paso a paso (sección 28 del curso). Lo que YA está listo en esta carpeta:
- `app.py` — la app, con `debug` apagado en producción y `SECRET_KEY` por variable de entorno.
- `requirements.txt` — dependencias con versión fija.
- `wsgi_pythonanywhere.py` — ejemplo del archivo WSGI (para copiar en PythonAnywhere).
- `.gitignore` — para no subir basura (cache, venv, .env).
- Repositorio git ya inicializado con el primer commit.

---

## Paso 1 · Subir el código a GitHub

En <https://github.com> crea un repositorio **vacío** (sin README), por ejemplo `mi-flask-deploy`.
Luego, desde esta carpeta:

```bash
cd /home/brandon/Escritorio/Proyectos/Python/28_desplegar
git remote add origin https://github.com/TU_USUARIO/mi-flask-deploy.git
git push -u origin main
```

> Si te pide usuario/contraseña, GitHub ya no acepta la contraseña normal: usa un
> **token** (github.com → Settings → Developer settings → Personal access tokens).

---

## Paso 2 · Crear cuenta en PythonAnywhere

Regístrate gratis en <https://www.pythonanywhere.com> (el plan **Beginner** es gratis
y suficiente). Tu web quedará en `https://TU_USUARIO.pythonanywhere.com`.

---

## Paso 3 · Clonar el proyecto en PythonAnywhere

En PythonAnywhere abre una **Bash console** (menú "Consoles" → "Bash") y clona tu repo:

```bash
git clone https://github.com/TU_USUARIO/mi-flask-deploy.git 28_desplegar
```

---

## Paso 4 · Crear el entorno virtual e instalar dependencias

En la misma consola Bash de PythonAnywhere:

```bash
cd 28_desplegar
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

## Paso 5 · Crear la Web App

1. Ve a la pestaña **"Web"** → **"Add a new web app"**.
2. Elige **"Manual configuration"** (NO "Flask", para controlar todo).
3. Elige la versión de Python (la misma con la que creaste el venv, ej. 3.10/3.12).

---

## Paso 6 · Configurar el Virtualenv

En la página de la Web app, sección **"Virtualenv"**, escribe la ruta de tu venv:

```
/home/TU_USUARIO/28_desplegar/venv
```

---

## Paso 7 · Configurar el archivo WSGI

En la sección **"Code"** hay un enlace al archivo WSGI
(algo como `/var/www/TU_USUARIO_pythonanywhere_com_wsgi.py`). Ábrelo, **borra todo**
y pon esto (mira `wsgi_pythonanywhere.py` de referencia), cambiando `TU_USUARIO`:

```python
import sys

project_home = '/home/TU_USUARIO/28_desplegar'
if project_home not in sys.path:
    sys.path.insert(0, project_home)

from app import app as application
```

Guarda.

---

## Paso 8 · (Opcional) Variable de entorno del SECRET_KEY

Para producción real, en el WSGI puedes añadir antes del import:

```python
import os
os.environ['SECRET_KEY'] = 'pon-aqui-una-clave-larga-y-secreta'
```

---

## Paso 9 · Recargar y probar

Vuelve a la pestaña **"Web"** y pulsa el botón verde **"Reload"**.
Abre `https://TU_USUARIO.pythonanywhere.com` — deberías ver la página
"¡Mi aplicación Flask está en línea!". 🚀

Si algo falla, revisa el **"Error log"** (enlace en la misma pestaña Web).

---

## Cuando hagas cambios más adelante

1. Editas en tu PC → `git add -A && git commit -m "cambios" && git push`
2. En la consola Bash de PythonAnywhere: `cd 28_desplegar && git pull`
3. Pestaña Web → botón **Reload**.
