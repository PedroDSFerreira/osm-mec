#!/usr/bin/env python

"""
CherryPy-based webservice
"""

import cherrypy
import cherrypy_cors
from app_routes import set_routes
from utils import jsonify_error, load_env


def main():
    cherrypy_cors.install()

    dispatcher = set_routes()

    config = {
        "/": {
            "request.dispatch": dispatcher,
            "error_page.default": jsonify_error,
            "cors.expose.on": True,
            # "tools.auth_basic.on": True,
            "tools.auth_basic.realm": "localhost",
        },
    }

    cherrypy.tree.mount(root=None, config=config)

    cherrypy.config.update(load_env(".env-template"))
    #In a container when using 127.0.0.1 it does not allow communication outside
    #that container since 127.0.0.1 is loopback
    #Remove the comments if needed
    cherrypy.config.update({
        'server.socket_host': '0.0.0.0',  # Bind to all available interfaces
        'server.socket_port': 8080,        # Use port 8080
    })

    cherrypy.engine.start()
    cherrypy.engine.block()


if __name__ == "__main__":
    main()
