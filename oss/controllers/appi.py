import cherrypy
from utils.osm import get_osm_client


class AppiController:
    @cherrypy.tools.json_out()
    def list_appis(self, ns=None, filter=None):
        """
        /appis (GET)
        """
        return get_osm_client().vnf.list(ns=ns, filter=filter)

    @cherrypy.tools.json_out()
    def get_appi(self, appi_id):
        """
        /appis/{appi_id} (GET)
        """
        return get_osm_client().vnf.get(name=appi_id)
