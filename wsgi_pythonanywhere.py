# ============================================================================
#  EJEMPLO de archivo WSGI para PythonAnywhere.
#  ----------------------------------------------------------------------------
#  NO se ejecuta en local. En PythonAnywhere, en la pestaña "Web", hay un
#  enlace a un archivo WSGI (algo como /var/www/TUUSUARIO_pythonanywhere_com_wsgi.py).
#  Abre ESE archivo, borra su contenido y pega algo como esto, cambiando
#  "TUUSUARIO" por tu usuario y la ruta por donde clonaste el proyecto.
# ============================================================================

import sys

# Ruta a la carpeta del proyecto (donde esta app.py)
project_home = '/home/TUUSUARIO/28_desplegar'
if project_home not in sys.path:
    sys.path.insert(0, project_home)

# Importa la variable 'app' de app.py y la expone como 'application'
from app import app as application  # noqa: E402
