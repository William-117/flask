"""Ejercico 1:Crea una aplicación web básica en Flask que,
 al ser ejecutada, inicia un servidor local en el puerto 5000.
  Cuando visita la ruta principal (http://localhost:5000/),
  el srvidor esponderá con un mensaje HTML que dice "Hello, World Flask". 
"""

#Se importa el módulo Flask desde el paquete flask
from flask import Flask

#Crea una instacia de la clase Flask.
#El argumento __name__ le dice a Flask
#que utilice el nombre del archico actual main.py
app = Flask(__name__)


#Este es un decorador que define una ruta 
#corresponde a la página princial del app
@app.route("/")
#Cuando alguien visite app (por ejemplo, (http://localhost:5000/),
#la función hello() será ejecutada
def hello():
    return "<h1>Hello, World Flask !</h1>"

#Solo se ejecuta si el archivo es ejecutado directamente
#arranca la apicación Flask en modo de depuracón (debug=True)
if __name__ == '__main__':
    app.run(debug=True, port=5000)