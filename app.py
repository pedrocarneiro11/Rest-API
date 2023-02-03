from flask import Flask, jsonify, request
import json

app = Flask(__name__)

desenvolvedores = [
    {
        'id': '0',
        'nome': 'Pedro',
        'habilidades': ['Python', 'Flask']
    },
    {
        'id': '1',
        'nome': 'Pedro2',
        'habilidades': ['Python', 'Flask', 'Java']
    },

]


@app.route('/dev/<int:id>/', methods=['GET', 'PUT', 'DELETE'])
def dev(id):
    if request.method == 'GET':
        try:
            response = desenvolvedores[id]
            print(response)
        except IndexError:
            mensagem = 'Desenvolvedor de ID {} não existe'.format(id)
            response = {'status': 'erro', 'mensagem': mensagem}
        except Exception:
            mensagem = 'Erro desconhecido, entre em contato com o administrador do servidor'
            response = {'status': 'erro', 'mensagem': mensagem}

        return jsonify(response)

    elif request.method == 'PUT':
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify(dados)

    elif request.method == 'DELETE':
        desenvolvedores.pop(id)
        return jsonify({'status': 'sucesso', 'mensagem': 'registro excluido'})


@app.route('/dev/', methods=['POST', 'GET'])
def lista_desenvolvedores():
    if request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return jsonify(desenvolvedores[posicao])
    elif request.method == 'GET':
        # Retorna uma lista com todos os desenvolvedores
        return jsonify(desenvolvedores)


if __name__ == '__main__':
    app.run()
