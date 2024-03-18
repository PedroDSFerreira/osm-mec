import json
import logging
import os

from callbacks import load_callback_functions
from kafka import KafkaConsumer, KafkaProducer
from utils.db import DatabaseInitializer

logging.basicConfig(level=logging.INFO)


def main():
    producer = KafkaProducer(
        bootstrap_servers=os.getenv("KAFKA_BOOTSTRAP_SERVERS"),
        value_serializer=lambda v: json.dumps(v).encode("utf-8"),
    )
    consumer = KafkaConsumer(
        bootstrap_servers=os.getenv("KAFKA_BOOTSTRAP_SERVERS"),
        group_id="group",
        auto_offset_reset="earliest",  # Consume from the beginning of the topic
        # enable_auto_commit=False,  # Disable auto-committing offsets
        value_deserializer=lambda x: json.loads(x.decode("utf-8")),
    )

    callbacks = load_callback_functions()

    topics = list(callbacks.keys())
    consumer.subscribe(topics=topics)

    logging.info(f"Listening for messages on topics: {topics}")
    try:
        for message in consumer:
            logging.info(f"Received message: {message.value}")
            topic = message.topic
            if topic in callbacks:
                callback_function = callbacks[topic]
                response = callback_function(message.value)
                producer.send("responses", value=response)
                logging.info(f"Sent response: {response}")

    except Exception as e:
        logging.error(f"An error occurred: {e}")

    finally:
        consumer.close()


if __name__ == "__main__":
    DatabaseInitializer.initialize_database()
    main()
