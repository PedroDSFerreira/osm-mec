import threading
from time import sleep


class MEAO:
    def __init__(self, nbi_k8s_connector, update_container_ids_freq) -> None:
        self.nbi_k8s_connector = nbi_k8s_connector
        self.update_container_ids_freq = update_container_ids_freq
        self.nodeSpecs = self.nbi_k8s_connector.getNodeSpecs()
        self.containerInfo = self.nbi_k8s_connector.getContainerInfo()

    def start(self):
        # Create threads
        update_thread = threading.Thread(target=self.update_container_ids)

        # Start threads
        update_thread.start()

    def get_node_specs(self, hostname=None):
        if hostname:
            if hostname in self.nodeSpecs.keys():
                return self.nodeSpecs[hostname]
            else:
                return None
        else:
            return self.nodeSpecs

    def get_container_ids(self):
        return self.containerInfo

    def update_node_specs(self):
        self.nodeSpecs = self.nbi_k8s_connector.getNodeSpecs()

    def update_container_ids(self):
        while True:
            sleep(self.update_container_ids_freq)
            self.containerInfo = self.nbi_k8s_connector.getContainerInfo()
