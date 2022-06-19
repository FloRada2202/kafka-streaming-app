import os
import logging

from confluent_kafka import Consumer, KafkaException

from kafka_configuration import KafkaConfig

logging.basicConfig(level=logging.INFO)


class KafkaConsumerClient:
    def __init__(self):
        self.kafka_service_internal_host = KafkaConfig().kafka_service_host
        self.kafka_service_internal_port = KafkaConfig().kafka_service_port
        self.kafka_service_group_id = KafkaConfig().kafka_service_group_id
        self.kafka_service_input_topic = KafkaConfig().kafka_service_input_topic
        self.kafka_service_username = KafkaConfig().kafka_service_username
        self.kafka_service_password = KafkaConfig().kafka_service_password
        self.kafka_service_auto_offset_reset = KafkaConfig().kafka_auto_offset_reset

    def get_consumer(self):
        try:
            consumer_configuration = {
                'bootstrap.servers': self.kafka_service_internal_host,
                'group.id': self.kafka_service_group_id,
                'auto.offset.reset': self.kafka_service_auto_offset_reset,
                'enable.auto.commit': 'true',
                'max.poll.interval.ms': '86400000',
                'security.protocol': 'SASL_SSL',
                'sasl.mechanisms': 'PLAIN',
                'sasl.username': self.kafka_service_username,
                'sasl.password': self.kafka_service_password
            }

            consumer = Consumer(
                    consumer_configuration
                )
            consumer.subscribe([self.kafka_service_input_topic])

            return consumer
        except KafkaException as e:
            raise KafkaException(str(e))

