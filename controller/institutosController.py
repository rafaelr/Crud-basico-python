import json
from flask import Flask
from model.institutosModel import *


app = Flask(__name__)

@app.route('/listar')
def json_list():
    return json.dumps(read())

@app.route('/inserir/<nome>/<acronimo>')
def inserir(nome, acronimo):
    insert_data(nome, acronimo)
    return json.dumps("Inserido com sucesso")

@app.route('/deletar/<id>')
def deletar(id):
    delete(id)
    return json.dumps("Deletado com sucesso")


