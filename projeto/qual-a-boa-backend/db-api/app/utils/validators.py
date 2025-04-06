"""
Módulo que implementa funções de validação para a API.
Inclui validação de chave API, schemas, email e senha.
"""

from flask import request, current_app, jsonify
from functools import wraps
from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity
from marshmallow import ValidationError

def validate_api_key():
    """
    Valida a chave API presente nos headers da requisição.
    
    Returns:
        bool: True se a chave API for válida, False caso contrário
    """
    api_key = request.headers.get('X-API-Key')
    if not api_key or api_key != current_app.config['API_KEY']:
        return False
    return True

def api_key_required(f):
    """
    Decorator que exige uma chave API válida para acessar uma rota.
    
    Args:
        f: Função a ser decorada
        
    Returns:
        function: Função decorada que verifica a chave API
    """
    @wraps(f)
    def decorated(*args, **kwargs):
        if not validate_api_key():
            return {'message': 'Invalid or missing API key'}, 401
        return f(*args, **kwargs)
    return decorated

def handle_validation_error(error):
    """
    Converte erros de validação Pydantic em resposta da API.
    
    Args:
        error: Erro de validação
        
    Returns:
        tuple: (dict, int) - Resposta JSON e código de status
    """
    errors = []
    for err in error.errors():
        errors.append({
            'loc': err['loc'],
            'msg': err['msg'],
            'type': err['type']
        })
    return {'detail': errors}, 400

def validate_schema(schema):
    """
    Decorator que valida os dados da requisição contra um schema.
    
    Args:
        schema: Schema do Marshmallow para validação
        
    Returns:
        function: Decorator que valida os dados
    """
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            try:
                data = request.get_json()
                schema.load(data)
                return f(*args, **kwargs)
            except ValidationError as err:
                return jsonify({"message": "Validation error", "errors": err.messages}), 400
        return decorated_function
    return decorator

def validate_email(email):
    """
    Valida o formato de um endereço de email.
    
    Args:
        email (str): Endereço de email a ser validado
        
    Returns:
        bool: True se o email for válido, False caso contrário
    """
    import re
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

def validate_password(password):
    """
    Valida a força de uma senha.
    Requer:
    - Mínimo de 8 caracteres
    - Pelo menos uma letra maiúscula
    - Pelo menos uma letra minúscula
    - Pelo menos um número
    
    Args:
        password (str): Senha a ser validada
        
    Returns:
        bool: True se a senha for forte o suficiente, False caso contrário
    """
    if len(password) < 8:
        return False
    if not any(c.isupper() for c in password):
        return False
    if not any(c.islower() for c in password):
        return False
    if not any(c.isdigit() for c in password):
        return False
    return True 