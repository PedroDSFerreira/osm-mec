import cherrypy
from osmclient.common.exceptions import ClientException
from utils import CaptureIO, delete_file, save_file


class VnfInstancesController:
    def __init__(self, client):
        self.descriptors_dir = "vnf_instances"
        self.client = client

    @cherrypy.tools.json_out()
    def get_vnf_instances(self, ns=None, filter=None):
        """
        /vnf_instances (GET)
        """
        return self.client.vnf.list(ns=ns, filter=filter)

    @cherrypy.tools.json_out()
    def get_vnf_instance(self, vnf_instance_id):
        """
        /vnf_instances/{vnf_instance_id} (GET)
        """
        return self.client.vnf.get(name=vnf_instance_id)