import cherrypy
from controllers import load_controllers

controllers = load_controllers()

# {prefix: [(function_name, route, controller, method),...]}
endpoints = {
    "/api/v1": [
        # ("index", "/dummy", "DummyController", "GET"),
        # ("hello", "/dummy/hello/{name}", "DummyController", "GET"),
        (
            "get_vnf_pkgs",
            "/vnf_pkgs",
            "VnfPkgController",
            "GET",
        ),
        (
            "get_vnf_pkg",
            "/vnf_pkgs/{vnf_pkg_id}",
            "VnfPkgController",
            "GET",
        ),
        (
            "new_vnf_pkg",
            "/vnf_pkgs",
            "VnfPkgController",
            "POST",
        ),
        (
            "update_vnf_pkg",
            "/vnf_pkgs/{vnf_pkg_id}",
            "VnfPkgController",
            "PUT",
        ),
        (
            "delete_vnf_pkg",
            "/vnf_pkgs/{vnf_pkg_id}",
            "VnfPkgController",
            "DELETE",
        ),
    ],
}


def set_routes(client):
    dispatcher = cherrypy.dispatch.RoutesDispatcher()

    for prefix, routes_info in endpoints.items():
        for route_info in routes_info:
            dispatcher.connect(
                name=route_info[0],
                route=prefix + route_info[1],
                action=route_info[0],
                controller=controllers[route_info[2]](client),
                conditions={"method": [route_info[3]]},
            )

    return dispatcher
