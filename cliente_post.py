import requests

URL = "http://127.0.0.1:5000/api/soma"
corpo = {"a": 10, "b": 7}
cabecalhos = {"X-Cliente": "turma-ciberseguranca"}

resposta = requests.post(URL, json=corpo, headers=cabecalhos)

print("Status:", resposta.status_code)
print("Corpo (JSON):", resposta.json())
