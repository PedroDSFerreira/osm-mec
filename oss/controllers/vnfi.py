import cherrypy
from utils import handle_osm_exceptions


class VnfiController:
    def __init__(self, client):
        self.client = client

    @cherrypy.tools.json_out()
    @handle_osm_exceptions
    def list_vnfis(self, ns=None, filter=None):
        """
        /vnfis (GET)
        """
        return self.client.vnf.list(ns=ns, filter=filter)

    @cherrypy.tools.json_out()
    @handle_osm_exceptions
    def get_vnfi(self, vnfi_id):
        """
        /vnfis/{vnfi_id} (GET)
        """
        return self.client.vnf.get(name=vnfi_id)
