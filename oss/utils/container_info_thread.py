import threading
import time
import requests
from cherrypy.process import plugins

containers = {}

class ContainerInfoThread(plugins.SimplePlugin):
    """Background thread that mapps container id to ns id"""

    def __init__(self, bus):
        super().__init__(bus)
        self.t = None

    def start(self):
        """Plugin entrypoint"""

        self.t = threading.Thread(target=get_containers_info)
        self.t.daemon = True
        self.t.start()


def get_containers_info():
    while True:
        response = requests.get("http://container-data-api:8000/containerInfo")
        for container in response.json()["ContainerInfo"]:
            containers[container["id"]] = container["ns_id"]
        time.sleep(5)
