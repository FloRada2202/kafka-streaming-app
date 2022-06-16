import logging
import msgpack

from kafka import KafkaProducer


from kafka_configuration import KafkaConfig

class KafkaProducerClient:
    def __init__(self):
        self.kafka_service_internal_host = KafkaConfig().kafka_service_host
        self.kafka_service_internal_port = KafkaConfig().kafka_service_port
        self.kafka_output_topic = KafkaConfig().kafka_service_output_topic

    def get_producer(self):
        return KafkaProducer(
                bootstrap_servers=f"{self.kafka_service_internal_host}:{self.kafka_service_internal_port}",
                value_serializer=msgpack.packb
            )