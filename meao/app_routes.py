# copy paste from main branch, solve on merging
import cherrypy
from controllers import load_controllers

controllers = load_controllers()

# {prefix: [(function_name, route, controller, method),...]}
endpoints = {
    "/api/v1": [
        ("index", "/dummy", "DummyController", "GET"),
        ("hello", "/dummy/hello/{name}", "DummyController", "GET"),
        (
            "get_ns_descriptors",
            "/ns_descriptors_content",
            "NsDescriptorsController",
            "GET",
        ),
        (
            "new_ns_descriptor",
            "/ns_descriptors_content",
            "NsDescriptorsController",
            "POST",
        ),
        (
            "get_ns_descriptor",
            "/ns_descriptors/nsd_content",
            "NsDescriptorsController",
            "GET",
        ),
        (
            "update_ns_descriptor",
            "/ns_descriptors/{nsd_info_id}/nsd_content",
            "NsDescriptorsController",
            "PUT",
        ),
        (
            "get_nsd",
            "/ns_descriptors/nsd",
            "NsDescriptorsController",
            "GET",
        ),
        (
            "delete_ns_descriptor",
            "/ns_descriptors_content/{nsd_info_id}",
            "NsDescriptorsController",
            "DELETE",
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