import os

import cherrypy
import cherrypy_cors
from app_routes import set_routes
from utils.cherrypy_utils import jsonify_error
from utils.kafka.callbacks.error_handler import callback as error_handler
from utils.kafka.callbacks.get_metrics import callback as get_metrics
from utils.threads import (ContainerInfoThread, KafkaConsumerThread,
                           WebSocketServiceThread)


def main():
    cherrypy_cors.install()

    KafkaConsumerThread(cherrypy.engine, "responses", error_handler).subscribe()
    KafkaConsumerThread(cherrypy.engine, "k8s-cluster", get_metrics).subscribe()
    ContainerInfoThread(cherrypy.engine).subscribe()
    WebSocketServiceThread(cherrypy.engine).subscribe()

    dispatcher = set_routes()

    config = {
        "/": {
            "request.dispatch": dispatcher,
            "error_page.default": jsonify_error,
            "cors.expose.on": True,
            # "tools.auth_basic.on": True,
            "tools.auth_basic.realm": "localhost",
        }
    }

    cherrypy.tree.mount(root=None, config=config)
    cherrypy.config.update(
        {
            "server.socket_host": "0.0.0.0",
            "server.socket_port": int(os.getenv("OSS_PORT")),
        }
    )
    cherrypy.engine.start()
    cherrypy.engine.block()


if __name__ == "__main__":
    main()
