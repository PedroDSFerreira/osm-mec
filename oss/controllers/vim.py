from utils.osm import get_osm_client
import cherrypy

class VimController:
    @cherrypy.tools.json_out()
    def list_vims(self):
        """
        /vims (GET)
        """
        return get_osm_client().vim.list()