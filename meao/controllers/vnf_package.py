import cherrypy
from osmclient.common.exceptions import ClientException
from utils import CaptureIO, delete_file, save_file


class VnfPackageController:
    def __init__(self, client):
        self.descriptors_dir = "vnf_package_descriptors"
        self.client = client

    @cherrypy.tools.json_out()
    def get_vnf_packages_content(self):
        """
        /vnf_packages_content (GET)
        """
        return self.client.vnfd.list()

    @cherrypy.tools.json_out()
    def new_vnf_package_content(self, file):
        """
        /vnf_packages_content (POST)
        """

        file_path = save_file(self.descriptors_dir, file)

        try:
            with CaptureIO() as out:
                self.client.vnfd.create(filename=file_path)

            return {"response": out}
        except ClientException as e:
            return {"error": str(e)}
        finally:
            delete_file(file_path)

    @cherrypy.tools.json_out()
    def get_vnf_package_content(self, vnf_package_id):
        """
        /vnf_packages/{vnfPkgId}/package_content (GET)
        """
        return self.client.vnfd.get(name=vnf_package_id)

    @cherrypy.tools.json_out()
    def update_vnf_package_content(self, vnf_package_id, file):
        """
        /vnf_packages/{vnfPkgId}/package_content (PUT)
        """

        file_path = save_file(self.descriptors_dir, file)

        try:
            return self.client.vnfd.update(name=vnf_package_id, filename=file_path)
        except ClientException as e:
            return {"error": str(e)}
        finally:
            delete_file(file_path)

    @cherrypy.tools.json_out()
    def get_vnfd(self, vnf_package_id):
        """
        /vnf_packages/{vnfPkgId}/vnfd (GET)
        """
        return self.client.vnfd.get(name=vnf_package_id)

    @cherrypy.tools.json_out()
    def delete_vnf_package_content(self, package_content_id):
        """
        /vnf_packages_content/{packageContentId} (DELETE)
        """
        return self.client.vnfd.delete(name=package_content_id)
