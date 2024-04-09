import cherrypy
from utils.file_management import save_file
from utils.osm import osm_client


class AppPkgController:
    def __init__(self):
        self.descriptors_dir = "app_pkgs"

    @cherrypy.tools.json_out()
    def list_app_pkgs(self, filter=None):
        """
        /app_pkgs (GET)
        """
        return osm_client.vnfd.list(filter=filter)

    @cherrypy.tools.json_out()
    def get_app_pkg(self, app_pkg_id):
        """
        /app_pkgs/{app_pkg_id} (GET)
        """
        return osm_client.vnfd.get(name=app_pkg_id)

    @cherrypy.tools.json_out()
    def new_app_pkg(self, appd, overwrite=None):
        """
        /app_pkgs (POST)
        """
        file_path = save_file(self.descriptors_dir, appd)
        pass

    def update_app_pkg(self, app_pkg_id, appd):
        """
        /app_pkgs/{app_pkg_id} (PATCH)
        """
        file_path = save_file(self.descriptors_dir, appd)
        pass

    def delete_app_pkg(self, app_pkg_id, force=False):
        """
        /app_pkgs/{app_pkg_id} (DELETE)
        """
        pass
