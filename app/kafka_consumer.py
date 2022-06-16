import os
import logging
from kafka import KafkaConsumer

logging.basicConfig(level=logging.INFO)

class KafkaConsumerClient:
    def __init__(self):
        self.kafka_service_internal_host = os.getenv('KAFKA_SERVICE_INTERNAL_HOST')
        self.kafka_service_internal_port = os.getenv('KAFKA_SERVICE_INTERNAL_PORT')
        self.kafka_topic_subscribe = os.getenv('KAFKA_TOPIC_SUBSCRIBE')

    def get_consumer(self):
        return KafkaConsumer(
                self.kafka_topic_subscribe,
                bootstrap_servers=f"{self.kafka_service_internal_host}:{self.kafka_service_internal_port}"
            )

