from views.dummy import DummyView
import cherrypy

class DummyController:
    @cherrypy.tools.json_out()
    def index(self):
        """
        /dummy (GET)
        """

        return DummyView.render('test')

    @cherrypy.tools.json_out()
    @cherrypy.tools.json_in()
    def hello(self, name = None):
        """
        /dummy/hello/{name} (GET)
        """

        return DummyView.render(f"Hello {name}!")