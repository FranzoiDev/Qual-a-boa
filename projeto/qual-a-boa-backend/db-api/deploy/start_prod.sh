#!/bin/bash

# Script para iniciar a aplicação em ambiente de produção

# Criar diretórios de log caso não existam
mkdir -p /var/log/gunicorn

# Ativar ambiente virtual se existir
if [ -d "venv" ]; then
    source venv/bin/activate
fi

# Verificar atualizações de dependências
pip install -r requirements.txt

# Aplicar migrações do banco de dados
flask db upgrade

# Iniciar aplicação com Gunicorn
exec gunicorn -c deploy/gunicorn_config.py run:app 