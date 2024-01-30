import cherrypy
from controllers import load_controllers

controllers = load_controllers()

# {prefix: [(name, route, action, controller, method),...]}
endpoints = {
    "/api/v1": [
        ("index", "/dummy", "DummyController", "GET"),
        ("hello", "/dummy/hello/{name}", "DummyController", "GET"),
        (
            "get_vim",
            "/vims/{vimID}",
            "VimsController",
            "GET",
        ),
        (
            "new_vim",
            "/vims",
            "VimsController",
            "POST",
        ),
        (
            "delete_vim",
            "/vims/{vimID}",
            "VimsController",
            "DELETE",
        ),
        (
            "update_vim",
            "/vims/{vimID}",
            "VimsController",
            "PATCH",
        ),
    ],
}



def set_routes():
    dispatcher = cherrypy.dispatch.RoutesDispatcher()

    for prefix, routes_info in endpoints.items():
        for route_info in routes_info:
            dispatcher.connect(
                name=route_info[0],
                route=prefix + route_info[1],
                action=route_info[0],
                controller=controllers[route_info[2]](),
                conditions={"method": [route_info[3]]},
            )

    return dispatcher