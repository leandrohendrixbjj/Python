# Exemplo SIMPLES de impressão de logs em Tela
import logging

# Configuração básica do logging
logging.basicConfig(
    level=logging.INFO,  # Nível de log
    format='%(asctime)s - %(levelname)s - %(message)s',  # Formato do log
    datefmt='%Y-%m-%d %H:%M:%S'  # Formato da data
)

# Exemplos de logs
logging.info('Mensagem de info')
logging.warning('Mensagem de aviso')
logging.error('Mensagem de erro')