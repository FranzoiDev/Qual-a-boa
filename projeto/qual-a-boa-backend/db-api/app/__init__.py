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
from app.core.logger import logger

def create_app(config_name=None):
    """
    Função factory que cria e configura a aplicação Flask.

    Args:
        config_name (str): Nome da configuração a ser utilizada.
                          Se None, usa o valor de FLASK_ENV ou 'development'.

    Returns:
        Flask: Aplicação Flask configurada e pronta para uso.
    """
    logger.info("Criando a aplicação Flask...")
    # Carrega as variáveis de ambiente do arquivo .env
    load_dotenv()
    logger.debug("Variáveis de ambiente carregadas.")

    if config_name is None:
        config_name = os.getenv('FLASK_ENV', 'development')
        logger.debug(f"Nenhum config_name fornecido, usando FLASK_ENV ou o padrão: {config_name}")

    app = Flask(__name__)
    app.config.from_object(config[config_name])
    logger.info(f"Aplicação configurada com as definições de '{config_name}'.")

    # Inicializa todas as extensões necessárias
    logger.debug("Inicializando extensões...")
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    cors.init_app(app, resources={r"/api/*": {"origins": app.config['CORS_ORIGINS']}})
    csrf.init_app(app)
    logger.info("Extensões Flask inicializadas (DB, Migrate, JWT, CORS, CSRF).")

    # Adiciona cabeçalhos de segurança
    if app.config.get('ENABLE_SECURITY_HEADERS', False):
        logger.debug("Cabeçalhos de segurança habilitados.")
        @app.after_request
        def add_security_headers(response):
            response.headers['X-Content-Type-Options'] = 'nosniff'
            response.headers['X-Frame-Options'] = 'DENY'
            response.headers['X-XSS-Protection'] = '1; mode=block'
            response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'
            response.headers['Content-Security-Policy'] = "default-src 'self'"
            return response
    else:
        logger.debug("Cabeçalhos de segurança desabilitados.")

    # Configura o handler para tokens JWT inválidos ou ausentes
    @jwt.unauthorized_loader
    def unauthorized_response(callback):
        logger.warning("Tentativa de acesso não autorizado (JWT inválido/ausente).")
        return jsonify({
            'message': 'Missing or invalid token'
        }), 401

    # Registra handlers de erro para diferentes situações
    logger.debug("Registrando manipuladores de erro (error handlers)...")
    @app.errorhandler(ValidationError)
    def validation_error_handler(error):
        logger.error(f"Erro de validação: {error}", exc_info=True)
        return handle_validation_error(error)

    @app.errorhandler(404)
    def not_found_error(error):
        logger.warning(f"Recurso não encontrado (404): {request.path}")
        return jsonify({'message': 'Resource not found'}), 404

    @app.errorhandler(500)
    def internal_error(error):
        logger.critical("Erro interno do servidor (500).", exc_info=True)
        return jsonify({'message': 'Internal server error'}), 500
    logger.info("Manipuladores de erro registrados.")

    # Registra o blueprint da API com o prefixo /api
    logger.debug("Registrando blueprint da API em /api...")
    app.register_blueprint(api_bp, url_prefix='/api')
    logger.info("Blueprint da API registrado.")

    # Isentar todas as rotas /api/ da proteção CSRF após o registro
    logger.debug("Isentando blueprint da API da proteção CSRF.")
    csrf.exempt(api_bp)

    # Cria as tabelas do banco de dados se não existirem
    with app.app_context():
        logger.debug("Garantindo que as tabelas do banco de dados existam...")
        db.create_all()
        logger.info("Tabelas do banco de dados verificadas/criadas.")

    logger.info(f"Aplicação Flask criada com sucesso usando a configuração '{config_name}'.")
    return app