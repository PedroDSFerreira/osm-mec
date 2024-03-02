import cherrypy
from utils import CaptureIO, handle_osm_exceptions, save_file


class NsPkgController:
    def __init__(self, client):
        self.descriptors_dir = "ns_pkgs"
        self.client = client

    @cherrypy.tools.json_out()
    @handle_osm_exceptions
    def list_ns_pkgs(self, filter=None):
        """
        /ns_pkgs (GET)
        """
        return self.client.nsd.list(filter=filter)

    @cherrypy.tools.json_out()
    @handle_osm_exceptions
    def get_ns_pkg(self, ns_pkg_id):
        """
        /ns_pkgs/{ns_pkg_id} (GET)
        """
        return self.client.nsd.get(name=ns_pkg_id)

    @cherrypy.tools.json_out()
    @handle_osm_exceptions
    def new_ns_pkg(self, nsd, overwrite=None, skip_charm_build=False):
        """
        /ns_pkgs (POST)
        """
        file_path = save_file(self.descriptors_dir, nsd)

        with CaptureIO() as out:
            self.client.nsd.create(
                filename=file_path,
                overwrite=overwrite,
                skip_charm_build=skip_charm_build,
            )

        cherrypy.response.status = 201
        return {"id": out}

    @handle_osm_exceptions
    def update_ns_pkg(self, ns_pkg_id, nsd):
        """
        /ns_pkgs/{ns_pkg_id} (PATCH)
        """
        file_path = save_file(self.descriptors_dir, nsd)
        self.client.nsd.update(name=ns_pkg_id, filename=file_path)

    @handle_osm_exceptions
    def delete_ns_pkg(self, ns_pkg_id, force=False):
        """
        /ns_pkgs/{ns_pkg_id} (DELETE)
        """
        cherrypy.response.status = 204
        self.client.nsd.delete(name=ns_pkg_id, force=force)
