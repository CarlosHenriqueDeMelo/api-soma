import requests

URL = "http://127.0.0.1:5000/api/soma"
parametros = {"a": 2, "b": 3}

resposta = requests.get(URL, params=parametros)

print("Status:", resposta.status_code)
print("Cabecalhos:", dict(resposta.headers))
print("Corpo (JSON):", resposta.json())
