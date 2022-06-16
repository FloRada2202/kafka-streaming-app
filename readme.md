# Kafka Streaming Application

## Initial setup
### 1. Create docker network using following command
'''docker network create kafka-streaming-app-network '''
### 2. Start single node apache kafka and zookeper using following command
'''docker-compose -f docker-compose-apache-kafka.yml up --build'''
### 3. Start main service container using follogin command
'''docker-compose -f docker-compose-kafka-connect.yml up --build'''


### Since this is demo application, environment variables will be included here:
'''
KAFKA_SERVICE_INTERNAL_HOST='kafka-service' # kafka host
KAFKA_SERVICE_INTERNAL_PORT='9092' # kafka port
KAFKA_SERVICE_INPUT_TOPIC='kafka-produce-users-topic' # topic to subscribe
KAFKA_SERVICE_INPUT_TOPIC='kafka-produce-users-output-topic' # topic to produce results
'''