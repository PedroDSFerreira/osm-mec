from time import sleep
import threading

class MEAO:
    def __init__(self, nbi_k8s_connector,update_container_ids_freq) -> None:
        self.nbi_k8s_connector = nbi_k8s_connector
        self.update_container_ids_freq = update_container_ids_freq
        self.containerInfo = self.nbi_k8s_connector.getContainerInfo()


    def start(self):
        # Create threads
        update_thread = threading.Thread(target=self.update_container_ids)

        # Start threads
        update_thread.start()

    def update_container_ids(self):
        while True:
            sleep(self.update_container_ids_freq)
            self.containerInfo = self.nbi_k8s_connector.getContainerInfo()
