from views.dummy import DummyView
import cherrypy
import requests

class VIMController:

    osm_api_url = "https://osm.etsi.org/nbapi/v1.0.0/admin/v1/vims"
    @cherrypy.tools.json_out()
    def vims(self, osm_api_url):
        """
        api/v1/vims/ (POST)
        """

        response = requests.post(osm_api_url)

        if response.status_code == 200: # Success
            data = response.json()
            return data
        else: # Error
            print(f"Error: {response.status_code}")
            return -1 # Temporary --> An appropriate procedure/message should be done/presented based on the error



    @cherrypy.tools.json_out()
    @cherrypy.tools.json_in()
    def vims(self, osm_api_url, vimId=None):
        """
        api/v1/vims/{vimId} (GET)
        api/v1/vims/{vimId} (PATCH)
        api/v1/vims/{vimId} (DELETE)
        """

        if vimId is None: # Temporary --> An appropriate procedure/message should be done/presented based on the error
            return -1 
        
        if cherrypy.request.method == 'GET':
            response = requests.get(osm_api_url, params={'vimId': vimId})
        elif cherrypy.request.method == 'PATCH':
            response = requests.patch(osm_api_url, params={'vimId': vimId})
        elif cherrypy.request.method == 'DELETE':
            response = requests.delete(osm_api_url, params={'vimId': vimId})

        if response.status_code == 200: # Success
            data = response.json()
            return data
        else: # Error
            print(f"Error: {response.status_code}")
            return -1 # Temporary --> An appropriate procedure/message should be done/presented based on the error

