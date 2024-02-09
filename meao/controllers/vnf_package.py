import cherrypy
from osmclient import client
from osmclient.common.exceptions import ClientException
import json
import requests
import os
import io, sys
from utils import save_file


myclient = client.Client(host="10.255.41.31", sol005=True)

class VnfPackageController:
    configuration_file_paths="vnf_package_configurations"

    @cherrypy.tools.json_out()
    def get_vnf_packages_content(self):
        """
        /vnf_packages_content (GET)
        """
        print("Making GET vnf_packages_content")
        try:
            return myclient.vnfd.list()
        except ClientException as e:
            return {"error": str(e)}

    @cherrypy.tools.json_out()
    def new_vnf_package_content(self, file):
        """
        /vnf_packages_content (POST)
        """
        print("Making POST vnf_packages_content")

        file_path = save_file(self.configuration_file_paths, file)

        try:
            #create function returns null, so we need to capture the output from stdout stream
            backup = sys.stdout
            sys.stdout = io.StringIO()
            myclient.vnfd.create(filename=file_path) 
            out = sys.stdout.getvalue()
            sys.stdout.close()
            sys.stdout = backup
            return {"response": out}
        except ClientException as e:
            return {"error": str(e)}
        finally:
            # Delete configuration file after use
            if os.path.exists(file_path):
                os.remove(file_path)     

    def get_vnf_package_content(self, vnf_package_id=None):
        """
        /vnf_packages/{vnfPkgId}/package_content (GET)
        """
        print("Making GET vnf_packages/{{vnfPkgId}}/package_content")
        try:
            return myclient.vnfd.get(vnf_package_id)
        except ClientException as e:
            return {"error": str(e)}

    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def update_vnf_package_content(self, vnf_package_id=None, config_file_path=None):
        """
        /vnf_packages/{vnfPkgId}/package_content (PUT)
        """

        print("Making PUT /vnf_packages/{{vnfPkgId}}/package_content")
        try:
            return myclient.vnfd.update(vnf_package_id, config_file_path)
        except ClientException as e:
            return {"error": str(e)}

    @cherrypy.tools.json_out()
    def get_vnfd(self, vnf_package_id=None):
        """
        /vnf_packages/{vnfPkgId}/vnfd (GET)
        """

        print(f"Making GET /vnf_packages/{{vnfPkgId}}/vnfd")
        try:
            return myclient.vnfd.get_descriptor(vnf_package_id, None)
        except ClientException as e:
            return {"error": str(e)}

    @cherrypy.tools.json_out()
    def delete_vnf_package_content(self, package_content_id=None):
        """
        /vnf_packages_content/{packageContentId} (DELETE)
        """

        print(f"Making DELETE /vnf_packages_content/{{packageContentId}}")
        try:
            return myclient.vnfd.delete(package_content_id)
        except ClientException as e:
            return {"error": str(e)}
