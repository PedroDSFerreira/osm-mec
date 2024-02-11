import cherrypy
from osmclient.common.exceptions import ClientException
from utils import CaptureIO, delete_file, save_file


class VnfPkgController:
    def __init__(self, client):
        self.descriptors_dir = "vnf_pkgs"
        self.client = client

    @cherrypy.tools.json_out()
    def get_vnf_pkgs(self, filter=None):
        """
        /vnf_pkgs (GET)
        """
        return self.client.vnfd.list(filter=filter)

    @cherrypy.tools.json_out()
    def get_vnf_pkg(self, vnf_pkg_id):
        """
        /vnf_pkgs/{vnf_pkg_id} (GET)
        """
        return self.client.vnfd.get(name=vnf_pkg_id)

    @cherrypy.tools.json_out()
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

        try:
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

        except ClientException as e:
            raise cherrypy.HTTPError(400, str(e))
        finally:
            delete_file(file_path)

    @cherrypy.tools.json_out()
    def update_vnf_pkg(self, vnf_pkg_id, vnfd):
        """
        /vnf_pkgs/{vnf_pkg_id} (PUT)
        """

        file_path = save_file(self.descriptors_dir, vnfd)

        try:
            return self.client.vnfd.update(name=vnf_pkg_id, filename=file_path)
        except ClientException as e:
            raise cherrypy.HTTPError(400, str(e))
        finally:
            delete_file(file_path)

    def delete_vnf_pkg(self, vnf_pkg_id, force=False):
        """
        /vnf_pkgs/{vnf_pkg_id} (DELETE)
        """
        cherrypy.response.status = 204
        return self.client.vnfd.delete(name=vnf_pkg_id, force=force)
