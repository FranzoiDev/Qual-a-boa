"""
Módulo que implementa as rotas de autenticação da API.
Inclui endpoints para registro, login e obtenção de informações do usuário atual.
"""

from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from app.extensions import db, csrf
from app.models import User
from app.utils.validators import validate_schema
from marshmallow import Schema, fields, ValidationError
from app.core.logger import logger

# Blueprint para agrupar as rotas de autenticação
auth_bp = Blueprint('auth', __name__)

class LoginSchema(Schema):
    """
    Schema para validação dos dados de login.

    Campos:
        email: Email do usuário
        password: Senha do usuário
    """
    email = fields.String(required=True)
    password = fields.String(required=True)

@auth_bp.route('/login', methods=['POST'])
@csrf.exempt  # Isenta a rota de login da proteção CSRF
@validate_schema(LoginSchema())
def login():
    """
    Endpoint para autenticação de usuários.

    Returns:
        tuple: (JSON response, status code)
            - 200: Login bem sucedido, retorna token de acesso
            - 401: Credenciais inválidas
    """
    data = request.get_json()
    email = data['email']
    logger.info(f"Tentativa de login para o email: {email}")

    user = User.query.filter_by(email=email).first()
    if not user or not user.check_password(data['password']):
        logger.warning(f"Credenciais inválidas para o email: {email}")
        return jsonify({'message': 'Invalid email or password'}), 401

    access_token = create_access_token(identity=str(user.id))
    logger.info(f"Login bem-sucedido para o usuário ID: {user.id} (Email: {email})")
    return jsonify({'access_token': access_token}), 200

@auth_bp.route('/me', methods=['GET'])
@jwt_required()
def get_current_user():
    """
    Endpoint para obter informações do usuário autenticado.
    Requer token JWT válido.

    Returns:
        tuple: (JSON response, status code)
            - 200: Informações do usuário
            - 401: Token inválido ou ausente
    """
    current_user_id = get_jwt_identity()
    logger.info(f"Buscando informações para o usuário ID: {current_user_id}")
    user = User.query.get(int(current_user_id))
    if not user:
        logger.error(f"Usuário com ID {current_user_id} não encontrado no banco, mas o JWT era válido.")
        return jsonify({'message': 'User not found'}), 404
    logger.debug(f"Informações obtidas com sucesso para o usuário ID: {current_user_id}")
    return jsonify(user.to_dict()), 200