import cherrypy
from utils.osm import get_osm_client


class VimController:
    @cherrypy.tools.json_out()
    def list_vims(self):
        """
        /vims (GET)
        """
        return get_osm_client().vim.list()
