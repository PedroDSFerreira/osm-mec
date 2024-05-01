from utils.appd_validation import *
from utils.capture_io import CaptureIO
from utils.db import DB
from utils.exceptions import handle_exceptions
from utils.file_management import *
from utils.osm import get_osm_client


@handle_exceptions
def callback(message):
    app_pkg_id = message.get("app_pkg_id")
    vim_id = message.get("vim_id")
    name = message.get("name")
    description = message.get("description")
    wait = message.get("wait")

    if app_pkg_id and vim_id and name and description:
        app_pkg = DB._get(id=app_pkg_id, collection="app_pkgs")
        ns_pkg_id = app_pkg.get("ns_pkg_id")

        with CaptureIO() as out:
            get_osm_client().ns.create(
                nsd_name=ns_pkg_id,
                nsr_name=name,
                account=vim_id,
                description=description,
                wait=wait,
            )
        instance_id = out[0]

        return {"msg_id": message["msg_id"], "status": 200, "instance_id": instance_id}
