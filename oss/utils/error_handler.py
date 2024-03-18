import threading
from cherrypy.process import plugins
from .kafka_utils import KafkaUtils
import time

class BackgroundThread(plugins.SimplePlugin):
    """CherryPy plugin to create a background worker thread"""

    def __init__(self, bus):
        super().__init__(bus)

        self.t = None

    def start(self):
        """Plugin entrypoint"""

        self.t = threading.Thread(target=consume_messages)
        self.t.daemon = True
        self.t.start()

def consume_messages():
    """Background worker thread"""

    consumer = KafkaUtils.create_consumer(topics=["responses"])

    while True:
        KafkaUtils.consume_messages(consumer)
        time.sleep(0.2)