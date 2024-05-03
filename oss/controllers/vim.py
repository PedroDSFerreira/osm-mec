import cherrypy
from utils.osm import get_osm_client
from views.vim import VimView


class VimController:
    @cherrypy.tools.json_out()
    def list_vims(self):
        """
        /vims (GET)
        """
        return [VimView._list(vim) for vim in get_osm_client().vim.list()]
