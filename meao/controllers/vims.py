import cherrypy
import requests


class VimsController:
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def new_vim(self):
        """
        /vims (POST)
        """

        token = cherrypy.request.headers["Authorization"]
        data = cherrypy.request.json
        response = requests.post(
            f"{cherrypy.config.get('OSM_HOST')}/osm/admin/v1/vims",
            headers={"Authorization": token, "Accept": "application/json"},
            json=data
        )

        cherrypy.response.status = response.status_code

        return response.json()


    @cherrypy.tools.json_out()
    def get_vim(self, vim_id=None):
        """
        /vims/{vimID} (GET)
        """

        token = cherrypy.request.headers["Authorization"]
        response = requests.get(
            f"{cherrypy.config.get('OSM_HOST')}/osm/admin/v1/vims/{vim_id}",
            headers={"Authorization": token, "Accept": "application/json"},
        )

        cherrypy.response.status = response.status_code

        return response.json()


    @cherrypy.tools.json_out()
    def delete_vim(self, vim_id=None):
        """
        /vims/{vimID} (DELETE)
        """

        token = cherrypy.request.headers["Authorization"]
        response = requests.delete(
            f"{cherrypy.config.get('OSM_HOST')}/osm/admin/v1/vims/{vim_id}",
            headers={"Authorization": token, "Accept": "application/json"},
        )

        cherrypy.response.status = response.status_code

        return response.json()

    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def update_vim(self, vim_id=None):
        """
        /vims/{vimID} (PATCH)
        """

        token = cherrypy.request.headers["Authorization"]
        data = cherrypy.request.json
        response = requests.patch(
            f"{cherrypy.config.get('OSM_HOST')}/osm/admin/v1/vims/{vim_id}",
            headers={"Authorization": token, "Accept": "application/json"},
            json=data,
        )

        cherrypy.response.status = response.status_code

        return response.json()