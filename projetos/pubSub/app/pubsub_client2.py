"""
    Esta versão usa o Google Secret Manager para carregar as credenciais do Pub/Sub
    Se executar essa rotina comentar a linha GOOGLE_APPLICATION_CREDENTIALS no arquivo .env
"""
import os
import logging
import html
from google.cloud import pubsub_v1
from dotenv import load_dotenv
from google.cloud import secretmanager

# Carrega variáveis de ambiente
load_dotenv()

# Configuração de log
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class PubSubPublisher:
    def __init__(self, topic_id: str):
        self._project_id = os.getenv("PUBSUB_PROJECT_ID")
        self.topic_id = topic_id

        # Primeiro carrega o segredo e define a variável de ambiente
        self._credentials_path = self.load_service_account_from_secret(
            secret_id="estudo-pubsub-python",
            project_id=self._project_id,
            file_path="service-account.json"
        )

        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = self._credentials_path

        # Validação
        self._validate_init_params()

        # Cria o client do PubSub
        self._publisher = pubsub_v1.PublisherClient()
        self.topic_path = self.publisher.topic_path(self.project_id, self.topic_id)

    @property
    def project_id(self):
        return self._project_id

    @property
    def publisher(self):
        return self._publisher    

    def _validate_init_params(self):
        if not self._credentials_path or not os.path.exists(self._credentials_path):
            raise ValueError("Credencial não encontrada.")
        if not self._project_id:
            raise ValueError("Variável de ambiente PUBSUB_PROJECT_ID não definida.")
        if not self.topic_id:
            raise ValueError("O nome do tópico não pode ser vazio.")

    def sanitize_message(self, message: str) -> str:
        return html.escape(message.strip())        

    def publish(self, message: str, attributes: dict = None):
        if not message:
            raise ValueError("A mensagem não pode ser vazia.")        
        try:
            message_to_publish = self.sanitize_message(message)
            data = message_to_publish.encode("utf-8")
            future = self.publisher.publish(self.topic_path, data, **(attributes or {}))
            message_id = future.result()
            logger.info(f"Mensagem publicada com ID: {message_id}")
            return message_id
        except Exception as e:
            logger.error(f"Erro ao publicar mensagem: {e}")
            raise

    def load_service_account_from_secret(self, secret_id, project_id=None, file_path="service-account.json"):
        if not project_id:
            project_id = os.getenv("PUBSUB_PROJECT_ID")

        if not project_id:
            raise ValueError("PUBSUB_PROJECT_ID não definido.")

        client = secretmanager.SecretManagerServiceClient()
        name = f"projects/{project_id}/secrets/{secret_id}/versions/latest"

        logger.info(f"Buscando segredo '{secret_id}' no projeto '{project_id}'...")
        response = client.access_secret_version(name=name)
        secret_content = response.payload.data.decode("UTF-8")

        with open(file_path, "w") as f:
            f.write(secret_content)

        logger.info(f"Credenciais salvas em {file_path}")
        return file_path
