import cherrypy
from osmclient import client
from osmclient.common.exceptions import ClientException
import json
import requests
import os
import io, sys

#arg is the _id of the ns package

myclient = client.Client(host="10.255.41.31", sol005=True)

class NsDescriptorsController:
    @cherrypy.tools.json_out()
    def get_ns_descriptors(self):
        """
        /ns_descriptors_content (GET)
        """
        print("Making GET ns_descriptors_content")
        try:
            return myclient.nsd.list()
        except ClientException as e:
            return {"error": str(e)}

    @cherrypy.tools.json_out()
    def new_ns_descriptor(self, config_file_path):
        """
        /ns_descriptors_content (POST)
        """
        print("Making POST ns_descriptors_content")

        try:
            #create function returns null, so we need to capture the output from stdout stream
            backup = sys.stdout
            sys.stdout = io.StringIO()
            myclient.nsd.create(filename=config_file_path) 
            out = sys.stdout.getvalue()
            sys.stdout.close()
            sys.stdout = backup
            return {"response": out}
        except ClientException as e:
            return {"error": str(e)}   

    def get_ns_descriptor(self, nsd_info_id=None):
        """
        /ns_descriptors/{nsd_info_id}/nsd_content (GET)
        """
        print("Making GET ns_descriptors/nsd_info_id/nsd_content")
        try:
            return myclient.nsd.get(nsd_info_id)
        except ClientException as e:
            return {"error": str(e)}

    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def update_ns_descriptor(self, nsd_info_id=None, config_file_path=None):
        """
        /ns_descriptors/{nsd_info_id}/nsd_content (PUT)
        """

        print("Making PUT ns_descriptors/nsd_info_id/nsd_content")
        try:
            return myclient.nsd.update(nsd_info_id, config_file_path)
        except ClientException as e:
            return {"error": str(e)}

    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def get_nsd(self, nsd_info_id=None):
        """
        /ns_descriptors/{nsd_info_id}/nsd (GET)
        """

        print(f"Making GET ns_descriptors/nsd_info_id/nsd")
        try:
            return myclient.nsd.get_descriptor(nsd_info_id, None)
        except ClientException as e:
            return {"error": str(e)}

    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def delete_ns_descriptor(self, nsd_info_id=None):
        """
        /ns_descriptors_content/nsd_info_id (DELETE)
        """

        print(f"Making DELETE ns_descriptors_content/nsd_info_id")
        try:
            return myclient.nsd.delete(nsd_info_id)
        except ClientException as e:
            return {"error": str(e)}

   