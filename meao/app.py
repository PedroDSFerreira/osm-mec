#!/usr/bin/env python

"""
CherryPy-based webservice
"""

import os

import cherrypy
import cherrypy_cors
from app_routes import set_routes
from osmclient import client
from utils import jsonify_error, load_env


def main():
    cherrypy_cors.install()

    dispatcher = set_routes(
        client=client.Client(host=os.getenv("OSM_HOSTNAME"), sol005=True)
    )

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
            "server.socket_host": os.getenv("MEAO_HOSTNAME"),
            "server.socket_port": os.getenv("MEAO_PORT"),
        }
    )
    cherrypy.engine.start()
    cherrypy.engine.block()


if __name__ == "__main__":
    main()
