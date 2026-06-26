import requests

URL = "http://127.0.0.1:5000/api/protegido"
TOKEN = "segredo-da-turma-123"

cabecalhos = {"Authorization": f"Bearer {TOKEN}"}

print(">> Com token valido:")
r1 = requests.get(URL, headers=cabecalhos)
print("  ", r1.status_code, r1.json())

print(">> Sem token nenhum:")
r2 = requests.get(URL)
print("  ", r2.status_code, r2.json())

print(">> Com token errado:")
r3 = requests.get(URL, headers={"Authorization": "Bearer chute-errado"})
print("  ", r3.status_code, r3.json())
