import os

class KafkaConfig:
    @property 
    def kafka_service_host():
        return os.getenv('KAFKA_SERVICE_INTERNAL_HOST')
    
    @property 
    def kafka_service_port():
        return os.getenv('KAFKA_SERVICE_INTERNAL_PORT')
    
    @property 
    def kafka_service_input_topic():
        return os.getenv('KAFKA_SERVICE_INPUT_TOPIC')
    
    @property 
    def kafka_service_output_topic():
        return os.getenv('KAFKA_SERVICE_OUTPUT_TOPIC')