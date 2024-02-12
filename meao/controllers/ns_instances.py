import cherrypy
from osmclient import client
from osmclient.common.exceptions import ClientException
import json
import requests
import os
import io, sys
from utils import CaptureIO

class NsInstancesController:
    def __init__(self):
        self.descriptors_dir = "ns_instances"
        #self.client = client
        self.client = client.Client(host="10.255.41.31", sol005=True)
        
    @cherrypy.tools.json_out()
    def get_ns_instances(self, filter=None):
        """
        /ns_instances_content (GET)
        """
        return self.client.ns.list(filter=filter)
        

    @cherrypy.tools.json_out()
    def new_ns_instance(
        self, 
        nsd_name, 
        nsr_name, 
        vim_account_id, 
        config=None, 
        ssh_keys=None,
        description="default description", 
        admin_status="ENABLED", 
        wait=False, 
        timeout=None,
    ):
        """
        /ns_instances_content (POST)
        """
          
        try:
            with CaptureIO() as out:
                self.client.ns.create(
                    nsd_name=str(nsd_name), 
                    nsr_name=str(nsr_name), 
                    account=str(vim_account_id), 
                    config=config, 
                    ssh_keys=ssh_keys, 
                    description=description, 
                    admin_status=admin_status, 
                    wait=wait, 
                    timeout=timeout,
                )

            cherrypy.response.status = 201
            return {"id": out}
        
        except ClientException as e:
            raise cherrypy.HTTPError(400, str(e))
        
        
        
    @cherrypy.tools.json_out()
    def get_ns_instance(self, ns_id):
        """
        /ns_instances_content/{ns_id} (GET)
        """
        return self.client.ns.get(name=str(ns_id))
        

    @cherrypy.tools.json_out()
    def delete_ns_instance(self, ns_id, force=False, config=None, wait=False):
        """
        /ns_instances_content/{ns_id} (DELETE)
        """
        cherrypy.response.status = 204
        return self.client.ns.delete(name=str(ns_id), force=force, config=config, wait=wait)
        
