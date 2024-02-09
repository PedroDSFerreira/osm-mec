import json

import cherrypy
import uuid
import os

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


def load_env(env_file):
    """Load environment variables from a file"""
    with open(env_file) as f:
        env = dict(
            tuple(line.strip().split("=")) for line in f if not line.startswith("#")
        )
    return env


def save_file(path, file):
    """Save File sent on server side"""
    save_file_path = os.path.join(os.getcwd(), "configurations", path)

    if not os.path.exists(save_file_path):
        os.makedirs(save_file_path)

    filename = generate_filename() + os.path.splitext(file.filename)[1]
    print(f"File Name: {filename}")

    file_path = os.path.join(save_file_path, filename)
    
    with open(file_path, 'wb') as f:
        while True:
            data = file.file.read(8192)
            if not data:
                break
            f.write(data) 
    f.close()

    return file_path
    
def generate_filename():
    filename = str(uuid.uuid4())
    return filename
