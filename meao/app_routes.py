import cherrypy
from controllers import load_controllers

controllers = load_controllers()

# {prefix: [(function_name, route, controller, method),...]}
endpoints = {
    "/api/v1": [
        # VNF PACKAGES
        (
            "list_vnf_pkgs",
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
            "list_nsds",
            "/nsds",
            "NsdController",
            "GET",
        ),
        (
            "get_nsd",
            "/nsds/{nsd_id}",
            "NsdController",
            "GET",
        ),
        (
            "new_nsd",
            "/nsds",
            "NsdController",
            "POST",
        ),
        (
            "update_nsd",
            "/nsds/{nsd_id}",
            "NsdController",
            "PATCH",
        ),
        (
            "delete_nsd",
            "/nsds/{nsd_id}",
            "NsdController",
            "DELETE",
        ),
        # VNF INSTANCES
        (
            "list_vnfis",
            "/vnfis",
            "VnfiController",
            "GET",
        ),
        (
            "get_vnfi",
            "/vnfis/{vnfi_id}",
            "VnfiController",
            "GET",
        ),
        # NS INSTANCES
        (
            "list_nsis",
            "/nsis",
            "NsiController",
            "GET",
        ),
        (
            "get_nsi",
            "/nsis/{nsi_id}",
            "NsiController",
            "GET",
        ),
        (
            "new_nsi",
            "/nsis",
            "NsiController",
            "POST",
        ),
        (
            "update_nsi",
            "/nsis/{nsi_id}",
            "NsiController",
            "PATCH",
        ),
        (
            "delete_nsi",
            "/nsis/{nsi_id}",
            "NsiController",
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
