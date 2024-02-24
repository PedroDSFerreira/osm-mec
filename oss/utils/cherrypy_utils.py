import json

import cherrypy
from osmclient.common.exceptions import ClientException


def jsonify_error(status, message, traceback, version):
    """JSONify all CherryPy error responses (created by raising the
    cherrypy.HTTPError exception)
    """

    cherrypy.response.headers["Content-Type"] = "application/json"
    response_body = json.dumps(
        {
            "error": {
                "http_status": status,
                "message": message,
            }
        }
    )

    cherrypy.response.status = status

    return response_body


def handle_osm_exceptions(f):
    def wrapper(*args, **kw):
        try:
            return f(*args, **kw)
        except ClientException as e:
            raise cherrypy.HTTPError(500, "OSM: " + str(e))

    return wrapper
