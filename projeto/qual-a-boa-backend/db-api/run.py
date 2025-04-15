"""
Script principal para execução da aplicação Flask.
Carrega as variáveis de ambiente e inicia o servidor.
"""

from dotenv import load_dotenv
load_dotenv()

from app import create_app
from app.core.logger import logger # Importa a instância do logger

# Cria a aplicação Flask
app = create_app()

if __name__ == '__main__':
    # Inicia o servidor em todas as interfaces (0.0.0.0) na porta 5000
    logger.info("Iniciando a aplicação Flask Qual A Boa...")
    app.run(host='0.0.0.0', port=5000)