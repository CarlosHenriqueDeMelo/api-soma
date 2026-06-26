from functools import wraps
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/api/soma", methods=["GET"])
def soma():
    a = request.args.get("a", type=float)
    b = request.args.get("b", type=float)
    if a is None or b is None:
        return jsonify({"erro": "informe a e b, ex: ?a=2&b=3"}), 400
    return jsonify({"resultado": a + b})

@app.route("/api/soma", methods=["POST"])
def soma_post():
    dados = request.get_json(silent=True) or {}
    a = dados.get("a")
    b = dados.get("b")
    cliente = request.headers.get("X-Cliente", "anonimo")
    if a is None or b is None:
        return jsonify({"erro": "envie a e b no corpo JSON"}), 400
    return jsonify({"resultado": a + b, "chamado_por": cliente})

TOKEN_VALIDO = "segredo-da-turma-123"

def requer_token(funcao):
    @wraps(funcao)
    def envoltorio(*args, **kwargs):
        cabecalho = request.headers.get("Authorization", "")
        if not cabecalho.startswith("Bearer "):
            return jsonify({"erro": "token ausente"}), 401
        token = cabecalho.split(" ", 1)[1]
        if token != TOKEN_VALIDO:
            return jsonify({"erro": "token invalido"}), 401
        return funcao(*args, **kwargs)
    return envoltorio

@app.route("/api/protegido", methods=["GET"])
@requer_token
def protegido():
    return jsonify({"mensagem": "Acesso autorizado! Dados secretos aqui."})

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
