from kafka import KafkaProducer, KafkaConsumer
import json
import os
import uuid
import cherrypy

responses = {}

producer = KafkaProducer(
        bootstrap_servers=os.getenv("KAFKA_BOOTSTRAP_SERVERS"),
        value_serializer=lambda v: json.dumps(v).encode("utf-8"),
        )

class KafkaUtils:
    @staticmethod
    def create_consumer(topics):
        consumer = KafkaConsumer(
            bootstrap_servers=os.getenv("KAFKA_BOOTSTRAP_SERVERS"),
            group_id="group",
            auto_offset_reset="earliest",
            value_deserializer=lambda x: json.loads(x.decode("utf-8")),
        )
        consumer.subscribe(topics=topics)
        return consumer

    @staticmethod
    def send_message(producer, topic, message):
        #  inject a unique message id
        msg_id = str(uuid.uuid4())
        message['msg_id'] = msg_id
        producer.send(topic, message)
        return msg_id

    @staticmethod
    def consume_messages(consumer):
        for message in consumer:
            response = message.value

            msg_id = response.pop('msg_id')
            responses[msg_id] = response

    @staticmethod
    def wait_for_response(msg_id=None):
        if msg_id and msg_id not in responses:
            responses[msg_id] = None

            while responses[msg_id] is None:
                pass

            response = responses.pop(msg_id)
            if response.get('error'):
                raise cherrypy.HTTPError(response['status'], response['error'])
            return response
        else:
            raise cherrypy.HTTPError(400, 'msg_id not found')
