from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Pasamos el título a la plantilla
    titulo = "Pablo L en Python con Flask"
    return render_template('index.html', titulo=titulo)

if __name__ == '__main__':
    # Ejecutar en el puerto 5000
    app.run(debug=True, port=5000)