"""
Módulo de configuração da aplicação Flask.
Define diferentes configurações para desenvolvimento, teste e produção.
"""

import os
from datetime import timedelta

class Config:
    """
    Configuração base que contém as configurações comuns a todos os ambientes.
    
    Atributos:
        SECRET_KEY: Chave secreta para assinatura de sessões
        JWT_SECRET_KEY: Chave secreta para tokens JWT
        JWT_ACCESS_TOKEN_EXPIRES: Tempo de expiração do token JWT
        SQLALCHEMY_DATABASE_URI: URI de conexão com o banco de dados
        API_KEY: Chave de API para serviços externos
        RATELIMIT_*: Configurações de rate limiting
        CORS_ORIGINS: Lista de origens permitidas para CORS
    """
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev')
    DEBUG = os.getenv('FLASK_DEBUG', '0') == '1'
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    API_KEY = os.getenv('API_KEY', 'dev_api_key')
    RATELIMIT_STORAGE_URL = os.getenv('RATELIMIT_STORAGE_URL', 'memory://')
    RATELIMIT_DEFAULT = "100/minute"
    RATELIMIT_HEADERS_ENABLED = True
    CORS_ORIGINS = os.getenv('CORS_ORIGINS', 'http://localhost:3000,http://127.0.0.1:3000').split(',')

class DevelopmentConfig(Config):
    """
    Configuração para ambiente de desenvolvimento.
    Habilita modo debug e desabilita modo de teste.
    """
    DEBUG = True
    TESTING = False

class TestingConfig(Config):
    """
    Configuração para ambiente de testes.
    Usa banco de dados em memória para testes rápidos.
    """
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'

class ProductionConfig(Config):
    """
    Configuração para ambiente de produção.
    Desabilita modo debug e teste para melhor performance.
    """
    DEBUG = False
    TESTING = False

# Dicionário que mapeia os nomes dos ambientes para suas respectivas classes de configuração
config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
} 