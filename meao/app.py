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

    cherrypy.config.update(load_env(".env"))

    cherrypy.engine.start()
    cherrypy.engine.block()


if __name__ == "__main__":
    main()
