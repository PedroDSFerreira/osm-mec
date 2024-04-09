from utils.db import DB
from utils.exceptions import handle_exceptions
from utils.osm import osm_client


@handle_exceptions
def callback(message):
    app_pkg_id = message.get("app_pkg_id")
    if app_pkg_id:
        app_pkg = DB._get(id=app_pkg_id, collection="app_pkgs")
        osm_client.vnfd.delete(name=app_pkg.get("osm_id"))
        DB._delete(id=app_pkg_id, collection="app_pkgs")

        return {"msg_id": message["msg_id"], "status": 204}
