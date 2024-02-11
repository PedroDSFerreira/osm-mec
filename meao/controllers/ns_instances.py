import cherrypy
from osmclient import client
from osmclient.common.exceptions import ClientException
import json
import requests
import os
import io, sys


class NsInstancesController:
    def __init__(self, client):
        self.configuration_file_path = "ns_instances_configurations"
        self.myclient = client
        

    @cherrypy.tools.json_out()
    def get_ns_instances(self):
        """
        /ns_instances_content (GET)
        """
        return self.myclient.ns.list()
        

    @cherrypy.tools.json_out()
    def new_ns_instance(self, nsd_name, nsr_name, vim_account_id, config=None, ssh_keys=None,
                         description="default description", admin_status="ENABLED", wait=False, timeout=None):
        """
        /ns_instances_content(POST)
        """
          
        ns_id_dict = {"id": self.myclient.ns.create(nsd_name=str(nsd_name), nsr_name=str(nsr_name), account=str(vim_account_id), config=config, 
                    ssh_keys=ssh_keys, description=description, admin_status=admin_status, wait=wait, timeout=timeout)}     
        return ns_id_dict
        
        
    @cherrypy.tools.json_out()
    def get_ns_instance(self, ns_id):
        """
        /ns_instances_content?nsInstanceId (GET)
        """
        
        return self.myclient.ns.get(name=str(ns_id))
        

    @cherrypy.tools.json_out()
    def delete_ns_instance(self, ns_id, force=False, config=None, wait=False):
        """
        /ns_instances (DELETE)
        """

        return self.myclient.ns.delete(name=str(ns_id), force=force, config=config, wait=wait)
        
