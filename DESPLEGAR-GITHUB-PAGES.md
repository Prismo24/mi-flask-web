# Desplegar en GitHub Pages

## Importante: GitHub Pages solo sirve archivos ESTÁTICOS

GitHub Pages **no ejecuta Flask** (ni Python). Por eso convertimos la app a HTML
estático en la carpeta **`docs/`**. Eso es lo que se publica.

- `docs/index.html`, `docs/acerca.html` — las páginas ya renderizadas.
- `docs/static/css/styles.css` — los estilos.
- `docs/.nojekyll` — evita que GitHub ignore archivos.

Si más adelante cambias las plantillas de Flask, vuelve a generar la versión
estática con:
```bash
../env/bin/python freeze.py     # (script incluido; regenera docs/)
```

---

## Paso 1 · Crear el repositorio en GitHub

En <https://github.com> → **New repository**. Ponle un nombre, por ejemplo
`mi-flask-web`. Déjalo **vacío** (sin README). Crear.

## Paso 2 · Subir el código

Desde esta carpeta:
```bash
cd /home/brandon/Escritorio/Proyectos/Python/28_desplegar
git remote add origin https://github.com/TU_USUARIO/mi-flask-web.git
git push -u origin main
```
> Si pide contraseña: usa un **token** (GitHub → Settings → Developer settings →
> Personal access tokens → Generate new token, con permiso `repo`).

## Paso 3 · Activar GitHub Pages

1. En el repo, ve a **Settings** (⚙️) → **Pages** (menú izquierdo).
2. En **"Build and deployment" → Source**, elige **"Deploy from a branch"**.
3. En **Branch**, elige **`main`** y la carpeta **`/docs`**. Guarda (**Save**).
4. Espera 1–2 minutos. Arriba aparecerá el enlace:
   **`https://TU_USUARIO.github.io/mi-flask-web/`** 🚀

Ábrelo y verás tu página "¡Mi aplicación Flask está en línea!".

---

## Cuando hagas cambios

1. Editas las plantillas → `../env/bin/python freeze.py` (regenera `docs/`)
2. `git add -A && git commit -m "cambios" && git push`
3. Espera 1–2 min y recarga la página (GitHub Pages se actualiza solo).

---

## ¿Y si necesito el Flask REAL (con formularios, base de datos, login)?

GitHub Pages no sirve para eso. Para apps Flask con backend necesitas un hosting
que corra Python: **Render.com**, **Railway.app** o **PythonAnywhere** (todos con
plan gratis). GitHub Pages solo sirve para sitios estáticos como este.
