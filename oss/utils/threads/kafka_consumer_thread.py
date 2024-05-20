import threading
import time

from cherrypy.process import plugins

from ..kafka import KafkaUtils


class KafkaConsumerThread(plugins.SimplePlugin):
    """Background thread that consumes messages from Kafka"""

    def __init__(self, bus, topic, callback):
        super().__init__(bus)
        self.topic = topic
        self.callback = callback
        self.t = None

    def start(self):
        """Plugin entrypoint"""

        self.t = threading.Thread(target=consume_messages, args=(self.topic, self.callback))
        self.t.daemon = True
        self.t.start()


def consume_messages(topic, callback):
    consumer = KafkaUtils.create_consumer(topics=[topic])

    while True:
        KafkaUtils.consume_messages(consumer, callback)
        time.sleep(0.2)
