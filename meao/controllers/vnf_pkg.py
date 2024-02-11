import cherrypy
from osmclient.common.exceptions import ClientException
from utils import CaptureIO, delete_file, save_file


class VnfPkgController:
    def __init__(self, client):
        self.descriptors_dir = "vnf_pkgs"
        self.client = client

    @cherrypy.tools.json_out()
    def get_vnf_pkgs(self):
        """
        /vnf_pkgs (GET)
        """
        return self.client.vnfd.list()

    @cherrypy.tools.json_out()
    def get_vnf_pkg(self, vnf_pkg_id):
        """
        /vnf_pkgs/{vnf_pkg_id} (GET)
        """
        return self.client.vnfd.get(name=vnf_pkg_id)

    @cherrypy.tools.json_out()
    def new_vnf_pkg(self, vnfd):
        """
        /vnf_pkgs (POST)
        """

        file_path = save_file(self.descriptors_dir, vnfd)

        try:
            with CaptureIO() as out:
                self.client.vnfd.create(filename=file_path)

            cherrypy.response.status = 201
            return {"id": out}

        except ClientException as e:
            return {"error": str(e)}
        finally:
            delete_file(file_path)

    @cherrypy.tools.json_out()
    def update_vnf_pkg(self, vnf_pkg_id, vnfd):
        """
        /vnf_pkgs/{vnf_pkg_id} (PUT)
        """

        file_path = save_file(self.descriptors_dir, vnfd)

        try:
            cherrypy.response.status = 200
            return self.client.vnfd.update(name=vnf_pkg_id, filename=file_path)
        except ClientException as e:
            return {"error": str(e)}
        finally:
            delete_file(file_path)

    @cherrypy.tools.json_out()
    def delete_vnf_pkg(self, vnf_pkg_id):
        """
        /vnf_pkgs/{vnf_pkg_id} (DELETE)
        """
        cherrypy.response.status = 204
        return self.client.vnfd.delete(name=vnf_pkg_id)
