"""
Script para inicialização do banco de dados.
Este script cria todas as tabelas necessárias no banco de dados,
apagando quaisquer dados existentes.
"""

from app import create_app
from app.extensions import db

def init_db():
    """
    Inicializa o banco de dados criando todas as tabelas necessárias.
    ATENÇÃO: Esta função apaga todos os dados existentes no banco de dados.
    
    O processo inclui:
    1. Criar uma instância da aplicação em modo desenvolvimento
    2. Apagar todas as tabelas existentes
    3. Criar todas as tabelas novamente
    """
    app = create_app('development')
    with app.app_context():
        db.drop_all()  # Cuidado: isso apaga todos os dados existentes
        db.create_all()
        print("Banco de dados inicializado com sucesso!")

if __name__ == '__main__':
    init_db() 