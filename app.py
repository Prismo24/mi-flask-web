import os
from flask import Flask, render_template

app = Flask(__name__)

# En produccion, el SECRET_KEY se lee de una variable de entorno.
# Si no existe (desarrollo local), usa una de prueba.
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-cambiar-en-produccion')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/acerca')
def acerca():
    return render_template('acerca.html')


# Para ejecutar en LOCAL: python app.py
# En PythonAnywhere NO se usa esto (usa el archivo WSGI), por eso debug=False.
if __name__ == '__main__':
    app.run(debug=True)
