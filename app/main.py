import time
import logging
import os

from kafka_consumer import KafkaConsumerClient

logging.basicConfig(level=logging.INFO)

if __name__ == '__main__':
    kafka_consumer = KafkaConsumerClient().get_consumer()
    logging.info(kafka_consumer.topics())
    while True:
        time.sleep(10)
        logging.info('Sleeping for 10 seconds')