# Logger Singleton

Este módulo fornece uma implementação de Singleton para o gerenciador de logs da aplicação Qual A Boa.

## Visão Geral

O `LoggerSingleton` garante que exista apenas uma instância do logger configurado em toda a aplicação. Isso ajuda a manter a consistência na formatação e no destino dos logs.

O logger está configurado para:

1.  **Saída no Console:** Logs com nível `INFO` ou superior são exibidos no console (`stdout`).
2.  **Saída em Arquivo:** Logs com nível `DEBUG` ou superior são escritos em um arquivo rotativo.
    *   **Arquivo:** `logs/app.log` (localizado na raiz do projeto).
    *   **Rotação:** O arquivo de log é rotacionado diariamente à meia-noite.
    *   **Backup:** São mantidos backups dos últimos 7 dias.

## Configuração

*   **Formato do Log:** `%(asctime)s - %(levelname)s - %(name)s - %(message)s`
*   **Formato da Data:** `%Y-%m-%d %H:%M:%S`
*   **Nome do Logger:** `QualABoaAppLogger`
*   **Nível Padrão:** `DEBUG` (nível mais baixo, captura tudo)
*   **Nível Console:** `INFO`
*   **Nível Arquivo:** `DEBUG`

## Como Usar

Para usar o logger em qualquer parte da aplicação, importe a instância `logger` do módulo:

```python
from app.core.logger import logger

# Exemplo de uso
def minha_funcao():
    logger.debug("Esta é uma mensagem de debug detalhada.")
    try:
        # Código que pode falhar
        resultado = 10 / 0
    except ZeroDivisionError as e:
        logger.error(f"Ocorreu um erro: {e}", exc_info=True) # exc_info=True anexa o traceback
    logger.info("Função concluída.")
    logger.warning("Este é um aviso.")
```

## Níveis de Log

Use os níveis de log apropriados para diferentes tipos de mensagens:

*   `logger.debug(message)`: Informações detalhadas, tipicamente de interesse apenas ao depurar problemas.
*   `logger.info(message)`: Confirmação de que as coisas estão funcionando como esperado.
*   `logger.warning(message)`: Uma indicação de que algo inesperado aconteceu, ou indicativo de algum problema no futuro próximo (ex: 'espaço em disco baixo'). O software ainda está funcionando como esperado.
*   `logger.error(message, exc_info=True)`: Devido a um problema mais sério, o software não foi capaz de executar alguma função. Geralmente anexe o traceback com `exc_info=True`.
*   `logger.critical(message, exc_info=True)`: Um erro grave, indicando que o próprio programa pode ser incapaz de continuar rodando. Geralmente anexe o traceback com `exc_info=True`.

Lembre-se de escolher o nível de log correto para a mensagem que você deseja registrar. 