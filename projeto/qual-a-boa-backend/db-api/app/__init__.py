"""
Módulo principal da aplicação Flask que configura e inicializa a aplicação.
Este arquivo contém a função create_app que configura todas as extensões,
registra blueprints e configura os handlers de erro.
"""

import os
from flask import Flask, jsonify, request
from pydantic import ValidationError
from flask_cors import CORS
from dotenv import load_dotenv

from app.config import config
from app.extensions import db, migrate, jwt, cors, csrf
from app.utils import handle_validation_error
from app.models import User, Restaurant
from app.api import api_bp

def create_app(config_name=None):
    """
    Função factory que cria e configura a aplicação Flask.
    
    Args:
        config_name (str): Nome da configuração a ser utilizada. 
                          Se None, usa o valor de FLASK_ENV ou 'development'.
    
    Returns:
        Flask: Aplicação Flask configurada e pronta para uso.
    """
    # Carrega as variáveis de ambiente do arquivo .env
    load_dotenv()
    
    if config_name is None:
        config_name = os.getenv('FLASK_ENV', 'development')
    
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    
    # Inicializa todas as extensões necessárias
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    cors.init_app(app, resources={r"/api/*": {"origins": app.config['CORS_ORIGINS']}})
    csrf.init_app(app)  # Inicializa o CSRFProtect
    
    # Configurar exceções CSRF para endpoints da API que usam JWT
    @csrf.exempt
    def csrf_exempt_jwt_routes():
        # Isenta endpoints da API que usam JWT da proteção CSRF
        return request.path.startswith('/api/') and request.headers.get('Authorization')
        
    # Adiciona cabeçalhos de segurança
    if app.config.get('ENABLE_SECURITY_HEADERS', False):
        @app.after_request
        def add_security_headers(response):
            response.headers['X-Content-Type-Options'] = 'nosniff'
            response.headers['X-Frame-Options'] = 'DENY'
            response.headers['X-XSS-Protection'] = '1; mode=block'
            response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'
            response.headers['Content-Security-Policy'] = "default-src 'self'"
            return response
    
    # Configura o handler para tokens JWT inválidos ou ausentes
    @jwt.unauthorized_loader
    def unauthorized_response(callback):
        return jsonify({
            'message': 'Missing or invalid token'
        }), 401
    
    # Registra handlers de erro para diferentes situações
    @app.errorhandler(ValidationError)
    def validation_error_handler(error):
        return handle_validation_error(error)
    
    @app.errorhandler(404)
    def not_found_error(error):
        return jsonify({'message': 'Resource not found'}), 404
    
    @app.errorhandler(500)
    def internal_error(error):
        return jsonify({'message': 'Internal server error'}), 500
    
    # Registra o blueprint da API com o prefixo /api
    app.register_blueprint(api_bp, url_prefix='/api')
    
    # Cria as tabelas do banco de dados se não existirem
    with app.app_context():
        db.create_all()
    
    return app 