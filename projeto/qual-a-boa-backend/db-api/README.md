# API de Restaurantes

Uma API RESTful para gerenciamento de restaurantes construída com Flask.

## 🚀 Funcionalidades

- Autenticação de usuários com JWT
- Gerenciamento de restaurantes (operações CRUD)
- Busca de restaurantes com filtros
- Controle de taxa de requisições (rate limiting)
- Documentação completa da API com Swagger UI

## 🛠️ Tecnologias

- Python 3.11
- Flask 2.3.x
- PostgreSQL 15.x
- SQLAlchemy ORM
- Autenticação JWT
- Validação com Pydantic
- Flask-RestX para documentação da API
- Pytest para testes

## 📁 Estrutura do Projeto

```
api-db/
├── app/                    # Diretório principal da aplicação
│   ├── api/               # Endpoints da API
│   │   ├── auth.py        # Rotas de autenticação
│   │   ├── restaurants.py # Rotas de restaurantes
│   │   └── __init__.py    # Inicialização do blueprint da API
│   ├── models/            # Modelos do banco de dados
│   │   ├── user.py        # Modelo de usuário
│   │   ├── restaurant.py  # Modelo de restaurante
│   │   └── __init__.py    # Inicialização dos modelos
│   ├── utils/             # Utilitários
│   │   └── validators.py  # Funções de validação
│   ├── extensions.py      # Extensões do Flask
│   ├── config.py          # Configurações da aplicação
│   └── __init__.py        # Inicialização da aplicação
├── migrations/            # Migrações do banco de dados
├── tests/                # Testes da aplicação
├── venv/                 # Ambiente virtual Python
├── .env.example          # Exemplo de variáveis de ambiente
├── init_db.py           # Script de inicialização do banco
├── init_db.sql          # Script SQL de inicialização
├── requirements.txt     # Dependências do projeto
├── run.py              # Script de execução da aplicação
├── manage_users.py     # Script para gerenciar usários
└── README.md           # Documentação do projeto
```

### Descrição dos Diretórios e Arquivos Principais

- **app/**: Contém todo o código fonte da aplicação
  - **api/**: Implementação dos endpoints da API REST
  - **models/**: Definição dos modelos do banco de dados
  - **utils/**: Funções utilitárias e helpers
  - **extensions.py**: Configuração das extensões do Flask
  - **config.py**: Configurações da aplicação para diferentes ambientes
  - **__init__.py**: Inicialização e configuração da aplicação Flask

- **migrations/**: Contém os scripts de migração do banco de dados

- **tests/**: Diretório para os testes da aplicação

- **venv/**: Ambiente virtual Python (não versionado)

- **.env.example**: Template para configuração das variáveis de ambiente

- **init_db.py**: Script para inicialização do banco de dados

- **init_db.sql**: Script SQL para criação inicial do banco

- **requirements.txt**: Lista de dependências do projeto

- **run.py**: Script principal para execução da aplicação

## 📋 Pré-requisitos

- Python 3.11 ou superior
- PostgreSQL 15.x ou superior
- pip (gerenciador de pacotes Python)

## 🔧 Instalação

1. Clone o repositório:

```bash
git clone <url-do-repositorio>
cd restaurant-api
```

2. Crie um ambiente virtual e ative-o:

```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Configure as variáveis de ambiente:

```bash
cp .env.example .env
```

Edite o arquivo `.env` com seus valores de configuração.

5. Configure o banco de dados:

```bash
# Crie um banco de dados PostgreSQL
createdb restaurant_db

# Execute as migrações
flask db init
flask db migrate -m "Migração inicial"
flask db upgrade
```

## 🚀 Executando a API

```bash
python run.py
```

A API estará disponível em `http://localhost:5000`

A documentação da API estará disponível em `http://localhost:5000/api/docs`

## 📚 Endpoints da API

### Autenticação
  
- `POST /api/login` - Fazer login e obter token JWT

-  Para registrar um novo usuário, só será possível quando feita pelo ADM do servidor. O cadastro será manual através do manage_users.py
- Criar novo User:
```bash
    python manage_users.py create <username> <email> <password>
```
- Listar todos users:
```bash
python manage_users.py list
```
-Deletar um usuário:
```bash
    python manage_users.py delete <user_id>
```



### Gerenciamento de Restaurantes (requer autenticação JWT)

- `GET /api/restaurants` - Listar todos os restaurantes
- `POST /api/restaurants` - Criar um novo restaurante
- `GET /api/restaurants/{id}` - Obter detalhes de um restaurante
- `PUT /api/restaurants/{id}` - Atualizar um restaurante
- `DELETE /api/restaurants/{id}` - Deletar um restaurante

### Busca de Restaurantes

- `GET /api/search` - Buscar restaurantes com filtros
  - Parâmetros de consulta: `name`, `state`, `city`, `type`


### Buscar restaurantes

```bash
curl -X GET "http://localhost:5000/api/search?state=SP&city=São%20Paulo&type=Italiana"
```

## 🔒 Segurança

- Todas as senhas são hasheadas usando bcrypt
- Tokens JWT são utilizados para autenticação
- Validação de dados é feita em todas as requisições

