import logging
import ujson

from confluent_kafka import KafkaException

from kafka_configuration import KafkaConfig
from kafka_consumer import KafkaConsumerClient
from kafka_producer import KafkaProducerClient
from kafka_stream_event import KafkaStreamEvent
from kafka_events_processor import KafkaEventsProcessor

logging.basicConfig(level=logging.INFO)

if __name__ == '__main__':
    kafka_consumer = KafkaConsumerClient().get_consumer()
    kafka_producer = KafkaProducerClient().get_producer()
    kafka_events_processor = KafkaEventsProcessor()

    try:
        while True:
            message = kafka_consumer.poll(1.0)
    
            if message is None: continue
            if message.error(): raise KafkaException(message.error())
            else:
                event = ujson.loads(ujson.loads(message.value()))
                event = KafkaStreamEvent(uid=event.get('uid'), timestamp=event.get('ts'))
                kafka_events_processor.add_event(event)

    except KeyboardInterrupt as e:
        logging.info('Process interupted by user.')
    
    finally:
        kafka_consumer.close()
