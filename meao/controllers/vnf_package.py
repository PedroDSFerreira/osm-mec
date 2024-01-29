import cherrypy
import requests


class VnfPackageController:
    @cherrypy.tools.json_out()
    def get_packages(self):
        """
        /vnf_packages (GET)
        """

        token = cherrypy.request.headers["Authorization"]
        response = requests.get(
            f"{cherrypy.config.get('OSM_HOST')}/osm/vnfpkgm/v1/vnf_packages",
            headers={"Authorization": token, "Accept": "application/json"},
        )

        cherrypy.response.status = response.status_code

        return response.json()

    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def new_package(self):
        """
        /vnf_packages (POST)
        """

        token = cherrypy.request.headers["Authorization"]
        data = cherrypy.request.json
        response = requests.post(
            f"{cherrypy.config.get('OSM_HOST')}/osm/vnfpkgm/v1/vnf_packages",
            headers={"Authorization": token, "Accept": "application/json"},
            json=data,
        )

        cherrypy.response.status = response.status_code

        return response.json()

    @cherrypy.tools.json_out()
    def get_package(self, package_id=None):
        """
        /vnf_packages/{packageId} (GET)
        """

        token = cherrypy.request.headers["Authorization"]
        response = requests.get(
            f"{cherrypy.config.get('OSM_HOST')}/osm/vnfpkgm/v1/vnf_packages/{package_id}",
            headers={"Authorization": token, "Accept": "application/json"},
        )

        cherrypy.response.status = response.status_code

        return response.json()

    @cherrypy.tools.json_out()
    def delete_package(self, package_id=None):
        """
        /vnf_packages/{packageId} (DELETE)
        """

        token = cherrypy.request.headers["Authorization"]
        response = requests.delete(
            f"{cherrypy.config.get('OSM_HOST')}/osm/vnfpkgm/v1/vnf_packages/{package_id}",
            headers={"Authorization": token, "Accept": "application/json"},
        )

        cherrypy.response.status = response.status_code

        if response.status_code == 204:
            return
        else:
            return response.json()

    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def update_package(self, package_id=None):
        """
        /vnf_packages/{packageId} (PATCH)
        """

        token = cherrypy.request.headers["Authorization"]
        data = cherrypy.request.json
        response = requests.patch(
            f"{cherrypy.config.get('OSM_HOST')}/osm/vnfpkgm/v1/vnf_packages/{package_id}",
            headers={"Authorization": token, "Accept": "application/json"},
            json=data,
        )

        cherrypy.response.status = response.status_code

        if response.status_code == 204:
            return
        else:
            return response.json()
