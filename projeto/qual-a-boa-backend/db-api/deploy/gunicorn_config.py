"""
Configuração do Gunicorn para ambiente de produção
"""

import multiprocessing

# Número de workers com base no número de núcleos
workers = multiprocessing.cpu_count() * 2 + 1

# Tipo de worker (use o tipo de worker sync para Flask)
worker_class = 'sync'

# Tempo limite para requests em segundos
timeout = 60

# Número máximo de requests por worker antes de recarregar
max_requests = 1000
max_requests_jitter = 50

# Vínculo a todas as interfaces na porta 5000
bind = '0.0.0.0:5000'

# Nível de log
loglevel = 'info'

# Diretório para os arquivos de log
errorlog = '/var/log/gunicorn/error.log'
accesslog = '/var/log/gunicorn/access.log'

# Formatar logs de acesso
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'

# Preload da aplicação para melhor performance
preload_app = True

# Modo demônio (desabilite se estiver usando supervisord ou systemd)
daemon = False 