# Exemplo SIMPLES de impressão de logs em um arquivo
import logging

# Configuração básica do logging
logging.basicConfig(
    level=logging.INFO,  # Nível de log
    format='%(asctime)s - %(levelname)s - %(message)s',  # Formato do log
    datefmt='%Y-%m-%d %H:%M:%S',  # Formato da data
    filename='app.log',  # Arquivo de log
    filemode='a'  # Modo de escrita (a = append)
)

# Exemplos de logs
logging.debug('Mensagem de debug')
logging.info('Mensagem de info')
logging.warning('Mensagem de aviso')
logging.error('Mensagem de erro')
logging.critical('Mensagem crítica')