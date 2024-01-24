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
            "http://10.255.41.77:9999/vnfpkgm/v1/vnf_packages",
            headers={"Authorization": token},
        )
        return response.json()

    @cherrypy.tools.json_out()
    def get_package(self):
        """
        /vnf_packages/{packageId} (GET)
        """

        token = cherrypy.request.headers["Authorization"]
        response = requests.get(
            "http://10.255.41.77:9999/vnfpkgm/v1/vnf_packages",
            headers={"Authorization": token},
        )
        return response.json()
