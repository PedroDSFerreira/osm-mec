import cherrypy
from utils import handle_osm_exceptions


class AppiController:
    def __init__(self, client):
        self.client = client

    @cherrypy.tools.json_out()
    @handle_osm_exceptions
    def list_appis(self, ns=None, filter=None):
        """
        /appis (GET)
        """
        return self.client.vnf.list(ns=ns, filter=filter)

    @cherrypy.tools.json_out()
    @handle_osm_exceptions
    def get_appi(self, appi_id):
        """
        /appis/{appi_id} (GET)
        """
        return self.client.vnf.get(name=appi_id)
