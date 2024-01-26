import cherrypy
import requests


class NsDescriptorController:
    @cherrypy.tools.json_out()
    def get_ns_descriptors(self):
        """
        /ns_descriptors (GET)
        """

        token = cherrypy.request.headers["Authorization"]
        response = requests.get(
            f"{cherrypy.config.get('OSM_HOST')}/osm/nsd/v1/ns_descriptors",
            headers={"Authorization": token, "Accept": "application/json"},
        )

        cherrypy.response.status = response.status_code

        return response.json()

    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def new_ns_descriptor(self):
        """
        /ns_descriptors (POST)
        """

        token = cherrypy.request.headers["Authorization"]
        data = cherrypy.request.json
        response = requests.post(
            f"{cherrypy.config.get('OSM_HOST')}/osm/nsd/v1/ns_descriptors",
            headers={"Authorization": token, "Accept": "application/json"},
            json=data,
        )

        cherrypy.response.status = response.status_code

        return response.json()

@cherrypy.tools.json_out()
    def get_ns_descriptor(self, nsd_info_id=None):
        """
        /ns_descriptors/{nsd_info_id} (GET)
        """

        token = cherrypy.request.headers["Authorization"]
        response = requests.get(
            f"{cherrypy.config.get('OSM_HOST')}/osm/nsd/v1/ns_descriptors/{nsd_info_id}",
            headers={"Authorization": token, "Accept": "application/json"},
        )

        cherrypy.response.status = response.status_code

        return response.json()

    @cherrypy.tools.json_out()
    def delete_ns_descriptor(self, nsd_info_id=None):
        """
        /ns_descriptors/{nsd_info_id} (DELETE)
        """

        token = cherrypy.request.headers["Authorization"]
        response = requests.delete(
            f"{cherrypy.config.get('OSM_HOST')}/osm/nsd/v1/ns_descriptors/{nsd_info_id}",
            headers={"Authorization": token, "Accept": "application/json"},
        )

        cherrypy.response.status = response.status_code

        if response.status_code == 204:
            return
        else:
            return response.json()

    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def update_ns_descriptor(self, nsd_info_id=None):
        """
        /ns_descriptors/{nsd_info_id} (PATCH)
        """

        token = cherrypy.request.headers["Authorization"]
        data = cherrypy.request.json
        response = requests.patch(
            f"{cherrypy.config.get('OSM_HOST')}/osm/nsd/v1/ns_descriptors/{nsd_info_id}",
            headers={"Authorization": token, "Accept": "application/json"},
            json=data,
        )

        cherrypy.response.status = response.status_code

        if response.status_code == 204:
            return
        else:
            return response.json()
   