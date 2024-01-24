import cherrypy
import requests


class VnfPackageController:
    @cherrypy.tools.json_out()
    def get_packages(self):
        """
        /vnf_packages (GET)
        """

        print(f"{cherrypy.config.get('OSM_HOST')}/osm/vnfpkgm/v1/vnf_packages")
        token = cherrypy.request.headers["Authorization"]

        response = requests.get(
            f"{cherrypy.config.get('OSM_HOST')}/osm/vnfpkgm/v1/vnf_packages",
            headers={"Authorization": token, "Accept": "application/json"},
        )
        return response.json()

    # @cherrypy.tools.json_out()
    # def new_package(self):
    #     """
    #     /vnf_packages (POST)
    #     """

    @cherrypy.tools.json_out()
    def get_package(self, package_id):
        """
        /vnf_packages/{packageId} (GET)
        """

        token = cherrypy.request.headers["Authorization"]

        response = requests.get(
            f"{cherrypy.config.get('OSM_HOST')}/osm/vnfpkgm/v1/vnf_packages/{package_id}",
            headers={"Authorization": token, "Accept": "application/json"},
        )
        return response.json()
