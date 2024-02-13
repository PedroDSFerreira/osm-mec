import cherrypy
from utils import CaptureIO, handle_osm_exceptions, save_file


class VnfPkgController:
    def __init__(self, client):
        self.descriptors_dir = "vnf_pkgs"
        self.client = client

    @cherrypy.tools.json_out()
    @handle_osm_exceptions
    def get_vnf_pkgs(self, filter=None):
        """
        /vnf_pkgs (GET)
        """
        return self.client.vnfd.list(filter=filter)

    @cherrypy.tools.json_out()
    @handle_osm_exceptions
    def get_vnf_pkg(self, vnf_pkg_id):
        """
        /vnf_pkgs/{vnf_pkg_id} (GET)
        """
        return self.client.vnfd.get(name=vnf_pkg_id)

    @cherrypy.tools.json_out()
    @handle_osm_exceptions
    def new_vnf_pkg(
        self,
        vnfd,
        overwrite=None,
        skip_charm_build=False,
        override_epa=False,
        override_nonepa=False,
        override_paravirt=False,
    ):
        """
        /vnf_pkgs (POST)
        """

        file_path = save_file(self.descriptors_dir, vnfd)

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
    def update_vnf_pkg(self, vnf_pkg_id, vnfd):
        """
        /vnf_pkgs/{vnf_pkg_id} (PATCH)
        """

        file_path = save_file(self.descriptors_dir, vnfd)

        self.client.vnfd.update(name=vnf_pkg_id, filename=file_path)

    @handle_osm_exceptions
    def delete_vnf_pkg(self, vnf_pkg_id, force=False):
        """
        /vnf_pkgs/{vnf_pkg_id} (DELETE)
        """
        cherrypy.response.status = 204
        return self.client.vnfd.delete(name=vnf_pkg_id, force=force)