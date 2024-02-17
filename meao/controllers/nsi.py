import cherrypy
from utils import CaptureIO, handle_osm_exceptions


class NsiController:
    def __init__(self, client):
        self.client = client

    @cherrypy.tools.json_out()
    @handle_osm_exceptions
    def list_nsis(self, filter=None):
        """
        /nsis (GET)
        """
        return self.client.ns.list(filter=filter)

    @cherrypy.tools.json_out()
    @handle_osm_exceptions
    def new_nsi(
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
        /nsis (POST)
        """

        with CaptureIO() as out:
            self.client.ns.create(
                nsd_name=nsd_name,
                nsr_name=nsr_name,
                account=vim_account_id,
                config=config,
                ssh_keys=ssh_keys,
                description=description,
                admin_status=admin_status,
                wait=wait,
                timeout=timeout,
            )

        cherrypy.response.status = 201
        return {"id": out}

    @cherrypy.tools.json_out()
    @handle_osm_exceptions
    def get_nsi(self, nsi_id):
        """
        /nsis/{nsi_id} (GET)
        """
        return self.client.ns.get(name=nsi_id)

    @cherrypy.tools.json_out()
    @handle_osm_exceptions
    def delete_nsi(self, nsi_id, force=False, config=None, wait=False):
        """
        /nsis/{nsi_id} (DELETE)
        """
        cherrypy.response.status = 204
        return self.client.ns.delete(name=nsi_id, force=force, config=config, wait=wait)

    @cherrypy.tools.json_out()
    @handle_osm_exceptions
    def update_nsi(self, nsi_id, data=None, wait=False):
        """
        /ns_instances/{ns_id} (UPDATE)
        """
        self.client.ns.update(ns_name=str(nsi_id), data=data, wait=wait)
        return "NS instance updated"
