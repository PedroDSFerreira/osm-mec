import os

import cherrypy
import cherrypy_cors
from app_routes import set_routes
from utils.cherrypy_utils import jsonify_error
from utils.error_handler import BackgroundThread

def main():
    cherrypy_cors.install()

    BackgroundThread(cherrypy.engine).subscribe()

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
            "server.socket_host": os.getenv("OSS_HOSTNAME"),
            "server.socket_port": int(os.getenv("OSS_PORT")),
        }
    )
    cherrypy.engine.start()
    cherrypy.engine.block()


if __name__ == "__main__":
    main()
