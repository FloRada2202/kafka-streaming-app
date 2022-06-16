import os
import logging
import msgpack

from kafka import KafkaConsumer
from kafka_configuration import KafkaConfig

logging.basicConfig(level=logging.INFO)

class KafkaConsumerClient:
    def __init__(self):
        self.kafka_service_internal_host = KafkaConfig().kafka_service_host
        self.kafka_service_internal_port = KafkaConfig().kafka_service_port
        self.kafka_service_input_topic = KafkaConfig().kafka_service_input_topic

    def get_consumer(self):
        return KafkaConsumer(
                self.kafka_service_input_topic,
                bootstrap_servers=f"{self.kafka_service_internal_host}:{self.kafka_service_internal_port}",
                value_deserializer=msgpack.loads,
                enable_auto_commit=False
            )

