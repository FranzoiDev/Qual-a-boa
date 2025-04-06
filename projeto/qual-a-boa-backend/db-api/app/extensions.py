"""
Módulo que inicializa e configura as extensões do Flask utilizadas na aplicação.
Cada extensão é inicializada aqui e pode ser importada em outros módulos.
"""

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from flask_wtf.csrf import CSRFProtect

# Instância do SQLAlchemy para gerenciamento do banco de dados
db = SQLAlchemy()

# Instância do Flask-Migrate para gerenciamento de migrações do banco de dados
migrate = Migrate()

# Instância do JWTManager para autenticação via tokens JWT
jwt = JWTManager()

# Instância do CORS para permitir requisições cross-origin
cors = CORS()

# Instância do CSRFProtect para proteção contra ataques CSRF
csrf = CSRFProtect() 