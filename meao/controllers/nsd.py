import cherrypy
from utils import CaptureIO, handle_osm_exceptions, save_file


class NsdController:
    def __init__(self, client):
        self.descriptors_dir = "nsd"
        self.client = client

    @cherrypy.tools.json_out()
    @handle_osm_exceptions
    def get_nsds(self):
        """
        /nsd (GET)
        """

        return self.client.nsd.list()

    @cherrypy.tools.json_out()
    @handle_osm_exceptions
    def new_nsd(self, nsd):
        """
        /nsd (POST)
        """

        file_path = save_file(self.descriptors_dir, nsd)

        with CaptureIO() as out:
            self.client.nsd.create(filename=file_path)
        return {"id": out}

    @cherrypy.tools.json_out()
    @handle_osm_exceptions
    def get_nsd(self, nsd_id):
        """
        /nsd/{nsd_id} (GET)
        """

        return self.client.nsd.get(name=nsd_id)

    @cherrypy.tools.json_out()
    @handle_osm_exceptions
    def update_nsd(self, nsd_id, nsd):
        """
        /nsd/{nsd_id} (PATCH)
        """

        file_path = save_file(self.descriptors_dir, nsd)

        self.client.nsd.update(nsd_id, file_path)
        return {"response": "NSD updated"}

    @cherrypy.tools.json_out()
    @handle_osm_exceptions
    def delete_nsd(self, nsd_id):
        """
        /nsd/{nsd_id} (DELETE)
        """

        return self.client.nsd.delete(name=nsd_id)
