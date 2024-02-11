#!/usr/bin/env python

"""
CherryPy-based webservice
"""

import cherrypy
import cherrypy_cors
from app_routes import set_routes
from osmclient import client
from utils import jsonify_error, load_env


def main():
    cherrypy_cors.install()

    cherrypy.tree.mount(root=None, config={})
    cherrypy.config.update(load_env(".env-template"))

    dispatcher = set_routes(
        client=client.Client(host=cherrypy.config.get("OSM_HOST"), sol005=True)
    )

    config = {
        "/": {
            "request.dispatch": dispatcher,
            "error_page.default": jsonify_error,
            "cors.expose.on": True,
            # "tools.auth_basic.on": True,
            "tools.auth_basic.realm": "localhost",
        },
        "server.socket_host": "0.0.0.0",
        "server.socket_port": 8080,
    }

    cherrypy.config.update(config)
    cherrypy.engine.start()
    cherrypy.engine.block()


if __name__ == "__main__":
    main()
