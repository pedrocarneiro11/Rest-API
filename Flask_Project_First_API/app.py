import json

from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/<int:id>')
def pessoas(id):
    return jsonify({'id': id, 'nome': 'Pedro', 'nacionalidade': 'Brasil'})


@app.route('/soma/<int:valor1>/<int:valor2>', methods=['POST', 'GET'])
def soma(valor1, valor2):
    global total
    if request.method == 'POST':
        data = json.loads(request.data)
        total = sum[data('valores')]
    elif request.method == 'GET':
        total = valor1 + valor2
    return jsonify({'soma': total})


if __name__ == '__main__':
    app.run(debug=True)
