from flask import Flask, jsonify, Response
import json

app = Flask(__name__)

def get_biblioteca():
    with open('biblioteca.json', 'r', encoding='utf-8') as f:
        biblioteca = json.load(f)
    return biblioteca

@app.route('/livros', methods=['GET'])
def get_livros():
    biblioteca = get_biblioteca()
    pretty_json = json.dumps(biblioteca['livros'], ensure_ascii=False, indent=4)
    return Response(pretty_json, mimetype='application/json')

@app.route('/autores', methods=['GET'])
def get_autores():
    biblioteca = get_biblioteca()
    pretty_json = json.dumps(biblioteca['autores'], ensure_ascii=False, indent=4)
    return Response(pretty_json, mimetype='application/json')

@app.route('/usuarios', methods=['GET'])
def get_usuarios():
    biblioteca = get_biblioteca()
    pretty_json = json.dumps(biblioteca['usuarios'], ensure_ascii=False, indent=4)
    return Response(pretty_json, mimetype='application/json')

@app.route('/')
def hello():
    return "hello"

if __name__ == '__main__':
    app.run(debug=True)