import time
import logging
import os
import msgpack
import time

from kafka_configuration import KafkaConfig
from kafka_consumer import KafkaConsumerClient
from kafka_producer import KafkaProducerClient

logging.basicConfig(level=logging.INFO)

if __name__ == '__main__':
    try:
        kafka_consumer = KafkaConsumerClient().get_consumer()
        kafka_producer = KafkaProducerClient().get_producer()
        unique_customer_ids = set()
        while True:
            first_message_timestamp_arrival = time.time()
            for msg in kafka_consumer:
                unpacked_msg = msgpack.loads(msg.value)
                unique_customer_ids.add(unpacked_msg.get('uid'))
                if (unpacked_msg.get('ts') - first_message_timestamp_arrival) > 59:
                    first_message_timestamp_arrival = unpacked_msg.get('ts')
                    unique_users_ids_message = f"Unique users count per minute: {len(unique_customer_ids)}"
                    kafka_producer.send(KafkaConfig().kafka_service_output_topic, value=msgpack.packb(unpacked_msg))
                    kafka_consumer.commit()
                    unique_customer_ids.clear()
    except Exception as e:
        logging.info(str(e))
