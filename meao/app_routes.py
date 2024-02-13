# copy paste from main branch, solve on merging
import cherrypy
from controllers import load_controllers

controllers = load_controllers()

# {prefix: [(function_name, route, controller, method),...]}
endpoints = {
    "/api/v1": [
        # ("index", "/dummy", "DummyController", "GET"),
        # ("hello", "/dummy/hello/{name}", "DummyController", "GET"),
        # VNF PACKAGES
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
            "PATCH",
        ),
        (
            "delete_vnf_pkg",
            "/vnf_pkgs/{vnf_pkg_id}",
            "VnfPkgController",
            "DELETE",
        ),
        # NS PACKAGES
        (
            "get_ns_pkgs",
            "/ns_pkgs",
            "NsPkgController",
            "GET",
        ),
        (
            "new_ns_pkg",
            "/ns_pkg",
            "NsPkgController",
            "POST",
        ),
        (
            "get_ns_pkg",
            "/ns_pkg/{ns_pkg_id}",
            "NsPkgController",
            "GET",
        ),
        (
            "update_ns_pkg",
            "/ns_pkgs/{ns_pkg_id}",
            "NsPkgController",
            "PUT",
        ),
        (
            "get_nsd",
            "/nsd/{ns_pkg_id}",
            "NsPkgController",
            "GET",
        ),
        (
            "delete_ns_pkg",
            "/ns_pkg/{ns_pkg_id}",
            "NsPkgController",
            "DELETE",
        ),
        # VNF INSTANCES
        (
            "get_vnf_instances",
            "/vnf_instances",
            "VnfInstancesController",
            "GET",
        ),
        (
            "get_vnf_instance",
            "/vnf_instances/{vnf_instance_id}",
            "VnfInstancesController",
            "GET",
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