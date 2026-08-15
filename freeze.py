"""
Convierte la app Flask en archivos estáticos dentro de docs/ (para GitHub Pages).
Uso:  python freeze.py
"""
import os
import re
import shutil

from app import app

BUILD = "docs"

# Rutas de la app -> nombre del archivo estático
PAGINAS = {
    "/": "index.html",
    "/acerca": "acerca.html",
}


def a_relativo(html):
    """Convierte los enlaces absolutos de Flask en relativos (GitHub Pages)."""
    html = html.replace('href="/static/', 'href="static/')
    html = html.replace('src="/static/', 'src="static/')
    html = html.replace('href="/acerca"', 'href="acerca.html"')
    html = re.sub(r'href="/"', 'href="index.html"', html)
    return html


def main():
    if os.path.exists(BUILD):
        shutil.rmtree(BUILD)
    os.makedirs(f"{BUILD}/static/css", exist_ok=True)

    client = app.test_client()
    for ruta, archivo in PAGINAS.items():
        html = a_relativo(client.get(ruta).get_data(as_text=True))
        with open(f"{BUILD}/{archivo}", "w", encoding="utf-8") as f:
            f.write(html)
        print(f"  {ruta:10} -> {BUILD}/{archivo}")

    shutil.copy("static/css/styles.css", f"{BUILD}/static/css/styles.css")
    open(f"{BUILD}/.nojekyll", "w").close()
    print(f"  Listo. Sube la carpeta '{BUILD}/' con git push.")


if __name__ == "__main__":
    main()
