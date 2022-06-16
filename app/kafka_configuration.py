import os
import logging

logging.basicConfig(level=logging.INFO)
class KafkaConfig(object):
    @property 
    def kafka_service_host(self):
        return os.getenv('KAFKA_SERVICE_INTERNAL_HOST')
    
    @property 
    def kafka_service_port(self):
        return os.getenv('KAFKA_SERVICE_INTERNAL_PORT')
    
    @property 
    def kafka_service_input_topic(self):
        return os.getenv('KAFKA_SERVICE_INPUT_TOPIC')
    
    @property 
    def kafka_service_output_topic(self):
        return os.getenv('KAFKA_SERVICE_OUTPUT_TOPIC')