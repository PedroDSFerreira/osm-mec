import cherrypy
from osmclient import client
from osmclient.common.exceptions import ClientException
import json
import requests
import os
import io, sys

#arg is the _id of the ns package

myclient = client.Client(host="10.255.41.31", sol005=True)

class NsInstancesController:
    @cherrypy.tools.json_out()
    def get_ns_instances(self):
        """
        /ns_instances_content (GET)
        """
        print("Making GET ns_instances_content")
        try:
            return myclient.ns.list()
        except ClientException as e:
            return {"error": str(e)}

    @cherrypy.tools.json_out()
    def new_ns_instance(self, nsd_name, nsr_name, vim_account_id):
        """
        /ns_instances_content(POST)
        """
        print("Making POST ns_instances_content")

        try:
            #create function returns null, so we need to capture the output from stdout stream
            backup = sys.stdout
            sys.stdout = io.StringIO()
            myclient.ns.create(nsd_name=str(nsd_name), nsr_name=str(nsr_name), account=str(vim_account_id)) 
            out = sys.stdout.getvalue()
            sys.stdout.close()
            sys.stdout = backup
            return {"response": out}
        except ClientException as e:
            return {"error": str(e)}   

    def get_ns_instance(self, ns_id=None):
        """
        /ns_descriptors/{nsd_info_id}/nsd_content (GET)
        """
        print("Making GET ns_descriptors/nsd_info_id/nsd_content")
        try:
            return myclient.ns.get(ns_id)
        except ClientException as e:
            return {"error": str(e)}

    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def update_ns_instance(self, ns_id=None, config_file_path=None):
        """
        /ns_descriptors/{nsd_info_id}/nsd_content (PUT)
        """

        print("Making PUT ns_descriptors/nsd_info_id/nsd_content")
        try:
            return myclient.ns.update(ns_id, config_file_path)
        except ClientException as e:
            return {"error": str(e)}

    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def delete_ns_instance(self, ns_id=None):
        """
        /ns_descriptors_content (DELETE)
        """

        print(f"Making DELETE ns_descriptors_content")
        try:
            return myclient.ns.delete(name=str(ns_id))
        except ClientException as e:
            return {"error": str(e)}