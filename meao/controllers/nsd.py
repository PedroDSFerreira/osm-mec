import cherrypy
from utils import CaptureIO, handle_osm_exceptions, save_file


class NsdController:
    def __init__(self, client):
        self.descriptors_dir = "nsd"
        self.client = client

    @cherrypy.tools.json_out()
    @handle_osm_exceptions
    def get_nsds(self, filter=None):
        """
        /nsd (GET)
        """
        return self.client.nsd.list(filter=filter)

    @cherrypy.tools.json_out()
    @handle_osm_exceptions
    def get_nsd(self, nsd_id):
        """
        /nsd/{nsd_id} (GET)
        """
        return self.client.nsd.get(name=nsd_id)

    @cherrypy.tools.json_out()
    @handle_osm_exceptions
    def new_nsd(self, nsd, overwrite=None, skip_charm_build=False):
        """
        /nsd (POST)
        """
        file_path = save_file(self.descriptors_dir, nsd)

        with CaptureIO() as out:
            self.client.nsd.create(
                filename=file_path,
                overwrite=overwrite,
                skip_charm_build=skip_charm_build,
            )

        cherrypy.response.status = 201
        return {"id": out}

    @handle_osm_exceptions
    def update_nsd(self, nsd_id, nsd):
        """
        /nsd/{nsd_id} (PATCH)
        """
        file_path = save_file(self.descriptors_dir, nsd)
        self.client.nsd.update(name=nsd_id, filename=file_path)

    @handle_osm_exceptions
    def delete_nsd(self, nsd_id, force=False):
        """
        /nsd/{nsd_id} (DELETE)
        """
        cherrypy.response.status = 204
        self.client.nsd.delete(name=nsd_id, force=force)
