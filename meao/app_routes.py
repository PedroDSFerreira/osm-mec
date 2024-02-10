import cherrypy
from controllers import load_controllers

controllers = load_controllers()

# {prefix: [(function_name, route, controller, method),...]}
endpoints = {
    "/api/v1": [
        ("index", "/dummy", "DummyController", "GET"),
        ("hello", "/dummy/hello/{name}", "DummyController", "GET"),
        (
            "get_vnf_packages_content",
            "/vnf_packages_content",
            "VnfPackageController",
            "GET",
        ),
        (
            "new_vnf_package_content",
            "/vnf_packages_content",
            "VnfPackageController",
            "POST",
        ),
        (
            "get_vnf_package_content",
            "/vnf_packages/{vnf_package_id}/package_content",
            "VnfPackageController",
            "GET",
        ),
        (
            "update_vnf_package_content",
            "/vnf_packages/{vnf_package_id}/package_content",
            "VnfPackageController",
            "PUT",
        ),
        (
            "get_vnfd",
            "/vnf_packages/{vnf_package_id}/vnfd",
            "VnfPackageController",
            "GET",
        ),
        (
            "delete_vnf_package_content",
            "/vnf_packages_content/{package_content_id}",
            "VnfPackageController",
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
