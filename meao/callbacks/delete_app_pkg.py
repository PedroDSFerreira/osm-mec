from utils.db import DB
from utils.exceptions import handle_exceptions
from utils.osm import get_osm_client


@handle_exceptions
def callback(message):
    app_pkg_id = message.get("app_pkg_id")
    if app_pkg_id:
        app_pkg = DB._get(id=app_pkg_id, collection="app_pkgs")
        ns_pkg_id = app_pkg.get("ns_pkg_id")
        vnf_pkg_id = app_pkg.get("vnf_pkg_id")

        if ns_pkg_id:
            get_osm_client().nsd.delete(name=ns_pkg_id)
            DB._update(id=app_pkg_id, collection="app_pkgs", data={"ns_pkg_id": None})
        if vnf_pkg_id:
            get_osm_client().vnfd.delete(name=vnf_pkg_id)
            DB._update(id=app_pkg_id, collection="app_pkgs", data={"vnf_pkg_id": None})

        return {"msg_id": message["msg_id"], "status": 204}
