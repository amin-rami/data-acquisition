from kafka import KafkaProducer
import json
from enum import Enum

from datagateway.settings import KAFKA_BOOTSTRAP_SERVERS


class MessageBrokerType(Enum):
    KAFKA = 1
    RABBITMQ = 2


class KafkaBroker:
    def __new__(cls, *arg, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(KafkaBroker, cls).__new__(cls, *arg, *kwargs)
            cls.instance.producer = KafkaProducer(
                bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
                value_serializer=lambda value: json.dumps(value).encode('utf-8')
            )
        return cls.instance

    def send(self, message, topic):
        self.producer.send(topic=topic, value=message)


def get_message_broker(message_broker_type: MessageBrokerType):
    if message_broker_type == MessageBrokerType.KAFKA:
        return KafkaBroker()
