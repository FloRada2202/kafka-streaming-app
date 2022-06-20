# Kafka Streaming Application

## Initial setup
### Start service container using following command
'''docker-compose -f docker-compose-kafka-connect.yml up --build'''

Main application logic can be found in `app/main.py` file. 
All service requirements are defined in `service-requirements.txt`.

### About
Kafka streaming application is a python application that consumes messages from a Kafka topic which contain information about users visiting a website at specific times. The main application logic calculates the number of unique users that visited the website in 1 minute intervals and outputs the result to another kafka topic specified as a value of KAFKA_SERVICE_OUTPUT_TOPIC topic.

The Kafka consumer is implemented in the `app/kafka_consumer.py` file. Every consumed message is converted to an `Event` object that contains the timestamp and user id extracted from the message.

The event is then added to the `KafkaEventsProcessor` that is responsible for the management of the state of received events.
This is accomplished with a map where timestamps are mapped to sets of unique user ids.
In order to allow event aggragation per minute, timestamps are always rounded to a full minute, so that events with timestamps within the same minute are added to the same time slot by the aggreagator.
After count of unique users visits is produced to Kafka topic, the set data structure will be cleared, since there are no more events with this timestamp are expected to arrive. In case this happens, the new event would be treated as a new entry and it will be stored inside a set.
### Environment variables used by this application:
```
KAFKA_SERVICE_INTERNAL_HOST=''  kafka host
KAFKA_SERVICE_INTERNAL_PORT=''  kafka port
KAFKA_SERVICE_INPUT_TOPIC='' kafka topic to subscribe
KAFKA_SERVICE_OUTPUT_TOPIC='' kafka topic to produce results
KAFKA_SERVICE_GROUP_ID='' group of consumer
KAFKA_SERVICE_PASSWORD='' confluent kafka access key
KAFKA_SERVICE_USERNAME='' confluent kafka secret access key
KAFKA_AUTO_OFFSET_RESET='' starting offset position
```


