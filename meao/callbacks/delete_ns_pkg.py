from utils.db import DB
from utils.osm import osm_client
from utils.exceptions import handle_exceptions

@handle_exceptions
def callback(message):
    ns_pkg_id = message.get('ns_pkg_id')
    if ns_pkg_id:
        ns_pkg = DB._get(id=ns_pkg_id, collection='ns_pkgs')
        osm_client.nsd.delete(name=ns_pkg.get('osm_id'))
        DB._delete(id=ns_pkg_id, collection='ns_pkgs')

        return {"msg_id": message["msg_id"], "status": 204}