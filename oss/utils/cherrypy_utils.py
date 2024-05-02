import json

import cherrypy
from bson import ObjectId
import uuid

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


def is_valid_id(id):
    try:
        ObjectId(id)
    except Exception:
        return False
    return True


def is_valid_uuid(id):
    try:
        uuid.UUID(id)
    except Exception:
        return False
    return True