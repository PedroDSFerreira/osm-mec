import cherrypy
from controllers import load_controllers

controllers = load_controllers()

# {prefix: [(function_name, route, controller, method),...]}
endpoints = {
    "/api/v1": [
        ("index", "/dummy", "DummyController", "GET"),
        ("hello", "/dummy/hello/{name}", "DummyController", "GET"),
        (
            "get_ns_instances",
            "/ns_instances",
            "NsInstancesController",
            "GET",
        ),
        (
            "get_ns_instance",
            "/ns_instances_content/{ns_id}",
            "NsInstancesController",
            "GET",
        ),
        (
            "new_ns_instance",
            "/ns_instances_content",
            "NsInstancesController",
            "POST",
        ),
        (
            "delete_ns_instance",
            "/ns_instances_content/{ns_id}",
            "NsInstancesController",
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
