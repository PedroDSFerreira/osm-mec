import cherrypy
from controllers import load_controllers

controllers = load_controllers()

routes = [
    # (name, route, action, controller, method)
    ("index_test", "/dummy", "index", "DummyController", "GET"),
    ("hello", "/dummt/hello/{name}", "hello", "DummyController", "GET"),
]


def set_routes():
    dispatcher = cherrypy.dispatch.RoutesDispatcher()

    for route in routes:
        dispatcher.connect(
            name=route[0],
            route=route[1],
            action=route[2],
            controller=controllers[route[3]](),
            conditions={"method": [route[4]]},
        )

    return dispatcher
