import cherrypy
from osmclient import client
from osmclient.common.exceptions import ClientException
from utils import CaptureIO, save_file, delete_file

class NsPkgController:
    def __init__(self, client):
        self.descriptors_dir = "ns_pkgs"
        self.client = client
    @cherrypy.tools.json_out()
    def get_ns_pkgs(self):
        """
        /ns_descriptors_content (GET)
        """
        print("Making GET ns_descriptors_content")
        try:
            return self.client.nsd.list()
        except ClientException as e:
            return {"error": str(e)}

    @cherrypy.tools.json_out()
    def new_ns_pkg(self, file):
        """
        /ns_descriptors_content (POST)
        """
        print("Making POST ns_descriptors_content")

        file_path = save_file(self.descriptors_dir, file)
        try:
            with CaptureIO() as out:
                self.client.nsd.create(filename=file_path)
            return {"id": out}
        except ClientException as e:
            raise cherrypy.HTTPError(400, str(e))
        finally:
            delete_file(file_path)  

    @cherrypy.tools.json_out()
    def get_ns_pkg(self, ns_pkg_id):
        """
        /ns_descriptors/{nsd_info_id}/nsd_content (GET)
        """
        print("Making GET ns_descriptors/nsd_info_id/nsd_content")
        try:
            return self.client.nsd.get(name=ns_pkg_id)
        except ClientException as e:
            return {"error": str(e)}

    @cherrypy.tools.json_out()
    def update_ns_pkg(self, nsd_info_id, file):
        """
        /ns_descriptors/{nsd_info_id}/nsd_content (PUT)
        """

        print("Making PUT ns_descriptors/nsd_info_id/nsd_content")
        file_path = save_file(self.descriptors_dir, file)
        try:
            self.client.nsd.update(nsd_info_id, file_path)
            return {"response": "NSD updated"}
        except ClientException as e:
            raise cherrypy.HTTPError(400, str(e))
        finally:
            delete_file(file_path)

    @cherrypy.tools.json_out()
    def get_nsd(self, ns_pkg_id):
        """
        /ns_descriptors/{nsd_info_id}/nsd (GET)
        Don't know if it's necessary, also it's problematic
        """

        print(f"Making GET ns_descriptors/nsd_info_id/nsd")
        try:
            return self.client.nsd.get_descriptor(name=ns_pkg_id, filename=None)
        except ClientException as e:
            return {"error": str(e)}

    @cherrypy.tools.json_out()
    def delete_ns_pkg(self, ns_pkg_id):
        """
        /ns_descriptors_content/nsd_info_id (DELETE)
        """

        print(f"Making DELETE ns_descriptors_content/nsd_info_id")
        try:
            return self.client.nsd.delete(name=ns_pkg_id)
        except ClientException as e:
            return {"error": str(e)}

   