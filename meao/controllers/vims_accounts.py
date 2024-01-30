import cherrypy
import requests


class VimsAccountsController:
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def new_vim_account(self):
        """
        /vim_accounts (POST)
        """

        token = cherrypy.request.headers["Authorization"]
        data = cherrypy.request.json
        response = requests.post(
            f"{cherrypy.config.get('OSM_HOST')}/osm/admin/v1/vim_accounts",
            headers={"Authorization": token, "Accept": "application/json"},
            json=data
        )

        cherrypy.response.status = response.status_code

        return response.json()


    @cherrypy.tools.json_out()
    def get_vim_account(self, vim_id=None):
        """
        /vim_accounts/{vimID} (GET)
        """

        token = cherrypy.request.headers["Authorization"]
        response = requests.get(
            f"{cherrypy.config.get('OSM_HOST')}/osm/admin/v1/vim_accounts/{vim_id}",
            headers={"Authorization": token, "Accept": "application/json"},
        )

        cherrypy.response.status = response.status_code

        return response.json()


    @cherrypy.tools.json_out()
    def delete_vim_account(self, vim_id=None):
        """
        /vim_accounts/{vimID} (DELETE)
        """

        token = cherrypy.request.headers["Authorization"]
        response = requests.delete(
            f"{cherrypy.config.get('OSM_HOST')}/osm/admin/v1/vim_accounts/{vim_id}",
            headers={"Authorization": token, "Accept": "application/json"},
        )

        cherrypy.response.status = response.status_code

        return response.json()

    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def update_vim_account(self, vim_id=None):
        """
        /vim_accounts/{vimID} (PATCH)
        """

        token = cherrypy.request.headers["Authorization"]
        data = cherrypy.request.json
        response = requests.patch(
            f"{cherrypy.config.get('OSM_HOST')}/osm/admin/v1/vim_accounts/{vim_id}",
            headers={"Authorization": token, "Accept": "application/json"},
            json=data,
        )

        cherrypy.response.status = response.status_code

        return response.json()