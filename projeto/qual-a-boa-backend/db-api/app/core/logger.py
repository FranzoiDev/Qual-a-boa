import logging
import sys
import os
from logging.handlers import TimedRotatingFileHandler

class LoggerSingleton:
    _instance = None
    _logger = None

    LOG_FORMAT = "%(asctime)s - %(levelname)s - %(name)s - %(message)s"
    LOG_DATE_FORMAT = "%Y-%m-%d %H:%M:%S"
    LOG_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'logs')
    LOG_FILE = os.path.join(LOG_DIR, 'app.log')

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(LoggerSingleton, cls).__new__(cls)
            # Garante que a configuração do logger seja feita apenas uma vez
            cls._instance._configure_logger()
        return cls._instance

    def _configure_logger(self):
        # Cria o diretório de logs se ele não existir
        if not os.path.exists(self.LOG_DIR):
            os.makedirs(self.LOG_DIR)

        self._logger = logging.getLogger("QualABoaAppLogger")
        self._logger.setLevel(logging.DEBUG) # Define o nível base para capturar tudo

        formatter = logging.Formatter(self.LOG_FORMAT, datefmt=self.LOG_DATE_FORMAT)

        # Handler para o Console
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(logging.INFO) # Loga mensagens INFO ou superiores no console
        console_handler.setFormatter(formatter)
        self._logger.addHandler(console_handler)

        # Handler para Arquivo
        # Rotaciona os logs diariamente e mantém 7 arquivos de backup
        file_handler = TimedRotatingFileHandler(
            self.LOG_FILE, when="midnight", interval=1, backupCount=7, encoding='utf-8'
        )
        file_handler.setLevel(logging.DEBUG) # Loga mensagens DEBUG ou superiores no arquivo
        file_handler.setFormatter(formatter)
        self._logger.addHandler(file_handler)

        self._logger.info("Logger inicializado com sucesso.")

    def get_logger(self):
        """Retorna a instância configurada do logger."""
        if self._logger is None:
            self._configure_logger()
        return self._logger

# Disponibiliza a instância do logger para fácil importação
logger = LoggerSingleton().get_logger()

if __name__ == '__main__':
    # Exemplo de como usar o logger
    logger.debug("Exemplo de mensagem de debug.")
    logger.info("Exemplo de mensagem informativa.")
    logger.warning("Exemplo de mensagem de aviso.")
    logger.error("Exemplo de mensagem de erro.")
    logger.critical("Exemplo de mensagem crítica.")