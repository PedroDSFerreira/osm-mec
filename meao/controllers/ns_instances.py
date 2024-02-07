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
    def new_ns_instance(self, nsd_name, nsr_name, vim_account_id, config=None, ssh_keys=None,
                         description="default description", admin_status="ENABLED", wait=False, timeout=None):
        """
        /ns_instances_content(POST)
        """
        print("Making POST ns_instances_content")

        try:
            #create function returns null, so we need to capture the output from stdout stream
            
            ns_id_dict = {"id": myclient.ns.create(nsd_name=str(nsd_name), nsr_name=str(nsr_name), account=str(vim_account_id), config=config, 
                        ssh_keys=ssh_keys, description=description, admin_status=admin_status, wait=wait, timeout=timeout)}     
            return ns_id_dict
        except ClientException as e:
            return {"error": str(e)}   

    @cherrypy.tools.json_out()
    def get_ns_instance(self, ns_id=None):
        """
        /ns_instances_content?nsInstanceId (GET)
        """
        print("Making GET ns_instances_content?nsInstanceId")
        try:
            return myclient.ns.get(name=str(ns_id))
        except ClientException as e:
            return {"error": str(e)}

    @cherrypy.tools.json_out()
    def delete_ns_instance(self, ns_id=None, force=False, config=None, wait=False):
        """
        /ns_instances (DELETE)
        """

        print(f"Making DELETE ns_instances/nsInstanceId")
        try:
            return myclient.ns.delete(name=str(ns_id), force=force, config=config, wait=wait)
        except ClientException as e:
            return {"error": str(e)}