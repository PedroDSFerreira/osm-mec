import cherrypy
from utils import CaptureIO, handle_osm_exceptions, save_file


class AppPkgController:
    def __init__(self, client):
        self.descriptors_dir = "app_pkgs"
        self.client = client

    @cherrypy.tools.json_out()
    @handle_osm_exceptions
    def list_app_pkgs(self, filter=None):
        """
        /app_pkgs (GET)
        """
        return self.client.vnfd.list(filter=filter)

    @cherrypy.tools.json_out()
    @handle_osm_exceptions
    def get_app_pkg(self, app_pkg_id):
        """
        /app_pkgs/{app_pkg_id} (GET)
        """
        return self.client.vnfd.get(name=app_pkg_id)

    @cherrypy.tools.json_out()
    @handle_osm_exceptions
    def new_app_pkg(
        self,
        appd,
        overwrite=None,
        skip_charm_build=False,
        override_epa=False,
        override_nonepa=False,
        override_paravirt=False,
    ):
        """
        /app_pkgs (POST)
        """
        file_path = save_file(self.descriptors_dir, appd)

        with CaptureIO() as out:
            self.client.vnfd.create(
                filename=file_path,
                overwrite=overwrite,
                skip_charm_build=skip_charm_build,
                override_epa=override_epa,
                override_nonepa=override_nonepa,
                override_paravirt=override_paravirt,
            )

        cherrypy.response.status = 201
        return {"id": out}

    @handle_osm_exceptions
    def update_app_pkg(self, app_pkg_id, appd):
        """
        /app_pkgs/{app_pkg_id} (PATCH)
        """

        file_path = save_file(self.descriptors_dir, appd)
        self.client.vnfd.update(name=app_pkg_id, filename=file_path)

    @handle_osm_exceptions
    def delete_app_pkg(self, app_pkg_id, force=False):
        """
        /app_pkgs/{app_pkg_id} (DELETE)
        """
        cherrypy.response.status = 204
        self.client.vnfd.delete(name=app_pkg_id, force=force)
