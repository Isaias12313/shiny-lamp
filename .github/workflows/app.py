from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>¡Hola Mundo desde Azure!</h1><p>Mi primera página con Python y Flask.</p>'