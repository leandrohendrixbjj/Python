from app.pubsub_client import PubSubPublisher
from app.pubsub_client2 import PubSubPublisher as PubSubPublisher2

if __name__ == "__main__":
    # pubsub = PubSubPublisher('nps-topic-padrao')
    pubsub = PubSubPublisher2('nps-topic-padrao')
    
    msg = "Olá, Pub/Sub com melhorias!"
    atributos = {
        "origem": "app-python",
        "tipo": "mensagem-de-teste"
    }

    pubsub.publish(msg, attributes=atributos)
