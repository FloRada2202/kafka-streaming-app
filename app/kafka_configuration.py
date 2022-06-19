import os
import logging

logging.basicConfig(level=logging.INFO)


class KafkaConfig(object):
    @property 
    def kafka_service_host(self):
        return os.getenv('KAFKA_SERVICE_INTERNAL_HOST') or logging.info('KAFKA_SERVICE_INTERNAL_HOST not defined')
    
    @property 
    def kafka_service_port(self):
        return os.getenv('KAFKA_SERVICE_INTERNAL_PORT') or logging.info('KAFKA_SERVICE_INTERNAL_PORT not defined')
    
    @property 
    def kafka_service_input_topic(self):
        return os.getenv('KAFKA_SERVICE_INPUT_TOPIC') or logging.info('KAFKA_SERVICE_INPUT_TOPIC not defined')
    
    @property 
    def kafka_service_output_topic(self):
        return os.getenv('KAFKA_SERVICE_OUTPUT_TOPIC') or logging.info('KAFKA_SERVICE_OUTPUT_TOPIC not defined')
    
    @property
    def kafka_service_group_id(self):
        return os.getenv('KAFKA_SERVICE_GROUP_ID') or logging.info('KAFKA_SERVICE_GROUP_ID not defined')

    @property
    def kafka_service_username(self):
        return os.getenv('KAFKA_SERVICE_USERNAME') or logging.info('KAFKA_SERVICE_USERNAME not defined')

    @property
    def kafka_service_password(self):
        return os.getenv('KAFKA_SERVICE_PASSWORD') or logging.info('KAFKA_SERVICE_PASSWORD not defined')
    
    @property
    def kafka_auto_offset_reset(self):
        return os.getenv('KAFKA_AUTO_OFFSET_RESET') or logging.info('KAFKA_AUTO_OFFSET_RESET not defined')
