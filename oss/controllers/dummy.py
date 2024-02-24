import cherrypy
from models.dummy import DummyModel
from views.dummy import DummyView


class DummyController:
    def __init__(self, client):
        self.view = DummyView()
        self.client = client

    @cherrypy.tools.json_out()
    def index(self):
        """
        /dummy (GET)
        """

        dummy = DummyModel()
        dummy.name = "Dummy"

        return self.view.name_view(dummy)

    @cherrypy.tools.json_out()
    @cherrypy.tools.json_in()
    def hello(self, name=None):
        """
        /dummy/hello/{name} (GET)
        """

        dummy = DummyModel()
        dummy.name = name

        return self.view.name_view(dummy)
