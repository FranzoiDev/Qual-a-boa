"""
Script principal para execução da aplicação Flask.
Carrega as variáveis de ambiente e inicia o servidor.
"""

from dotenv import load_dotenv
load_dotenv()

from app import create_app

# Cria a aplicação Flask
app = create_app()

if __name__ == '__main__':
    # Inicia o servidor em todas as interfaces (0.0.0.0) na porta 5000
    app.run(host='0.0.0.0', port=5000) 