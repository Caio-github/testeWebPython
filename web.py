import os
from flask import Flask, jsonify, request
from math import sqrt

app = Flask(__name__)

@app.route('/')
def teste_python():

    numero = "Salve queixo"
    t = " testando, fica rilex baby beef"

    return numero + "," + t

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
