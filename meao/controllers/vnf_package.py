import cherrypy
from osmclient import client
from osmclient.common.exceptions import ClientException
import json
import requests
import os
import io, sys
from utils import save_file


#myclient = client.Client(host="10.255.41.31", sol005=True)

class VnfPackageController:
    def __init__(self, client):
        self.configuration_file_path="vnf_package_configurations"
        self.myclient = client


    @cherrypy.tools.json_out()
    def get_vnf_packages_content(self):
        """
        /vnf_packages_content (GET)
        """
        return self.myclient.vnfd.list()
    
        
    @cherrypy.tools.json_out()
    def new_vnf_package_content(self, file):
        """
        /vnf_packages_content (POST)
        """
    
        file_path = save_file(self.configuration_file_path, file)

        try:
            #create function returns null, so we need to capture the output from stdout stream
            backup = sys.stdout
            sys.stdout = io.StringIO()
            self.myclient.vnfd.create(filename=file_path) 
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


    @cherrypy.tools.json_out()
    def get_vnf_package_content(self, vnf_package_id):
        """
        /vnf_packages/{vnfPkgId}/package_content (GET)
        """
        return self.myclient.vnfd.get(name=vnf_package_id)
        

    @cherrypy.tools.json_out()
    def update_vnf_package_content(self, vnf_package_id, file):
        """
        /vnf_packages/{vnfPkgId}/package_content (PUT)
        """

        file_path = save_file(self.configuration_file_path, file)

        try:
            return self.myclient.vnfd.update(name=vnf_package_id, filename=file_path)
        except ClientException as e:
            return {"error": str(e)}
        finally:
            # Delete configuration file after use
            if os.path.exists(file_path):
                os.remove(file_path)  


    @cherrypy.tools.json_out()
    def get_vnfd(self, vnf_package_id):
        """
        /vnf_packages/{vnfPkgId}/vnfd (GET)
        """
        return self.myclient.vnfd.get(name=vnf_package_id)
        

    @cherrypy.tools.json_out()
    def delete_vnf_package_content(self, package_content_id):
        """
        /vnf_packages_content/{packageContentId} (DELETE)
        """
        return self.myclient.vnfd.delete(name=package_content_id)