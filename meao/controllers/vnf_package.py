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
            "http://10.255.41.77/osm/vnfpkgm/v1/vnf_packages",
            headers={"Authorization": token, "Accept": "application/json"},
        )
        return response.json()

    @cherrypy.tools.json_out()
    @cherrypy.tools.json_in()
    def get_package(self, package_id)
        """
        /vnf_packages/{packageId} (GET)
        """

        token = cherrypy.request.headers["Authorization"]

        response = requests.get(
            f"http://10.255.41.77/osm/vnfpkgm/v1/vnf_packages/{package_id}",
            headers={"Authorization": token, "Accept": "application/json"},
        )
        return response.json()
