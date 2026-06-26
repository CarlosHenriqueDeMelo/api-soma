# api-soma

TDE do Módulo 2 — Aplicação para ambiente WEB (API REST com Flask)
Bacharelado em Cibersegurança (noturno) — FEELT / UFU

Projeto dividido em 4 horários, cada um evoluindo o anterior:

1. **Horário 1** — servidor Flask com rota `GET /api/soma` (soma dois números via query string).
2. **Horário 2** — cliente Python (`requests`) consumindo a rota GET.
3. **Horário 3** — rota `POST /api/soma`, com dados no corpo (JSON) e parâmetro extra no cabeçalho (`X-Cliente`).
4. **Horário 4** — rota `GET /api/protegido`, protegida por autenticação Bearer token no cabeçalho `Authorization`.

## Arquivos

- `servidor.py` — servidor Flask com as rotas dos Horários 1, 3 e 4.
- `cliente.py` — cliente do Horário 2 (GET).
- `cliente_post.py` — cliente do Horário 3 (POST com corpo + cabeçalho).
- `cliente_token.py` — cliente do Horário 4 (testa token válido, ausente e inválido).

## Como rodar

```bash
python -m venv venv
source venv/bin/activate
pip install flask requests

# Terminal 1
python servidor.py

# Terminal 2 (com o servidor já rodando)
python cliente.py
python cliente_post.py
python cliente_token.py
```

## Resultados esperados

- `cliente.py` → `Status: 200` e `{'resultado': 5.0}`
- `cliente_post.py` → `Status: 200` e `{'resultado': 17, 'chamado_por': 'turma-ciberseguranca'}`
- `cliente_token.py`:
  - Com token válido → `200 {'mensagem': 'Acesso autorizado! Dados secretos aqui.'}`
  - Sem token → `401 {'erro': 'token ausente'}`
  - Com token errado → `401 {'erro': 'token invalido'}`

## Observação de segurança

O token usado (`segredo-da-turma-123`) está fixo no código apenas para fins didáticos.
Em uma aplicação real, ele deveria vir de uma variável de ambiente e nunca ser
versionado no repositório.
