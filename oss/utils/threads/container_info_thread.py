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
        try:
            response = requests.get("http://container-data-api:8000/containerInfo")
            for container in response.json()["ContainerInfo"]:
                node_specs = requests.get("http://container-data-api:8000/nodeSpecs/" + container["node"]).json()
                if container["id"] not in containers:
                    containers[container["id"]] = {
                            "ns":container["ns_id"],
                            "node_specs": node_specs["NodeSpecs"],
                    }
                    containers[container["id"]]["node_specs"]["prev_cpu"] = 0
                    containers[container["id"]]["node_specs"]["prev_timestamp"] = 0
        except Exception as e:
            pass

        time.sleep(15)
