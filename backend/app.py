#!/usr/bin/env python

### DICA BOAS PRÁTICAS - imports
# primeiro sao importadas libs nativas do Python - ordem alfabética
# exemplo import os

# depois, após pular uma linha, importar libs que precisaram ser instaladas
from flask import Flask, request

# por ultimo importar de arquivos
from utils.task import Task

app = Flask(__name__)

@app.route('/task', methods = ['GET'])
def get_task():
    assert request.path == '/task'

    try:
        app.logger.info("Mensagem de exemplo")
        
        # aqui esse task está so como exemplo de como o diretorio pode ser organizado com as classes e como pode funcionar 
        # no exemplo do projeto
        task = Task(title="Ligar p/ Thamirys", category="friends", color="purple", status="to do").set_task()
        return {
            "status_code": "200",
            "message": f"Task encontrada: {task}",
            }
    except:
        # aqui é interessante ver como seria o error handling do flask
        # https://flask.palletsprojects.com/en/3.0.x/errorhandling/
        app.logger.error("Erro x")
        return {
            "status_code": "500",
            "message": "Deu ruim",
        }


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
