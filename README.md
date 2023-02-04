# ERP Wallet

## Requerimentos

- Docker
- Docker Compose
- Python 3.10
- Poetry 1.3.2

## Setup
Para inicializar você irá precisar clonar esse repositório e ter os requerimentos (acima), após ter instalado todos os requerimentos e ter clonado o repositório basta rodar (na raiz do projet):

```
./scripts/setup.py
```
Após a aplicação ter iniciado, você pode acessar a documentação da API atráves: <http://localhost:8000/docs> será listado os endpoints disponíveis.

## Como testar a  API
Foi criado uma autenticação de uma forma bem simples usando JWT. <br>
Para testar a API você irá precisar gerar um token JWT: <https://jwt.io/> <br>
No "VERIFY SIGNATURE" você precisar colocar o jwt secret. default: erp-wallet <br>
No payload do JWT precisa ter o campo "permission" com o valor "full-access" (foi uma forma de representar o permissionamento, poderia ser "access-limited" ou algo do tipo) <br>
Você pode testar diretamente pela doc da API: <http://localhost:8000/docs> clicando em "Authorize" e colocando o token JWT e fazendo a requisição para a API ou você pode usar algum testador de API de sua preferência, insomnia, postman, etc. <br>

Exemplo de CURL:
```
curl --request POST \
  --url http://localhost:8000/api/cashback/ \
  --header 'Authorization: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwicGVybWlzc2lvbiI6ImZ1bGwtYWNjZXNzIn0.p-YGNbWkLzIBjY2OFSpBceckQV51WsFF1KmQ-1vmTBk' \
  --header 'Content-Type: application/json' \
  --data '{
    "sold_at": "2026-01-02 00:00:00",
    "customer": {
       "document": "00000000000",
       "name": "JOSE DA SILVA"
    },
    "total": "100.00",
    "products": [
       {
          "type": "A",
          "value": "40.00",
          "qty": 1
       },
       {
          "type": "B",
          "value": "60.00",
          "qty": 5
       }
    ]
}'
```

## Tecnologias
Foi utilizado o framework FastAPI para fazer a API. <br>
Foi utilizado o Pydantic para fazer as validações dos Schemas. <br>
Foi utilizado a ORM do SQLAlchemy para ajudar a fazer as query para o banco de dados. <br>
Foi utilizado o postgres como banco de dados. <br>
Foi utilizado Docker e Docker Compose para auxiliar no build da aplicação. <br>
Foi utilizado Python Jose para a autenticação com JWT. <br>
Foi utilizado Poetry para o gerenciamento dos pacotes e dependências da aplicação. <br>


## Estrutura do Projeto
- `app/`
  - Local aonde ficará toda a aplicação.
  - `entrypoint/`
    - `api/`
      - `routers/`
        - Local aonde ficará todos os nossos endpoints.
        - `cashback.py`
          - Criação do Endpoint de cashback
      - `dependencies.py`
        - Criação de algumas dependencias para serem utilizadas nos Endpoints e ficar mais facil para criar testes.
      - `main.py`
        - Startup da aplicação FastAPI
      - `schemas.py`
        - Schemas utilizado pelos Routers.
    - `api_client.py`
      - Client da API externa
    - `database.py`
      - Criação da engine do banco de dados usando SQLAlchemy.
    - `factories.py`
      - Criação de uma instância do client da API externa.
    - `models.py`
      - Criação das tabelas do banco de dados utilizando SQLAlchemy.
    - `repositories.py`
      - Criação do PostgresRepository, para facilitar a usar as query, utilizando a ORM do SQLAlchemy.
    - `utils.py`
      - Funções para auxiliar o desenvolvimento.
- `scripts/`
  - Local aonde ficará os scripts da aplicação, no momento só temos o script de setup da aplicação.


