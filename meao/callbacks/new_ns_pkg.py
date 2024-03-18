from utils.capture_io import CaptureIO
from utils.db import DB
from utils.exceptions import handle_exceptions
from utils.file_management import delete_file, save_file
from utils.osm import osm_client


@handle_exceptions
def callback(message):
    ns_pkg_id = message.get("ns_pkg_id")
    if ns_pkg_id:
        ns_pkg = DB._get(id=ns_pkg_id, collection="ns_pkgs")
        # save file
        nsd_path = save_file("ns_pkgs", message.get("file_name"), ns_pkg.get("nsd"))
        # create ns pkg in osm
        with CaptureIO() as out:
            osm_client.nsd.create(filename=nsd_path)
        osm_ns_pkg_id = out[0]

        # delete file
        delete_file(nsd_path)
        # update ns pkg with osm id
        DB._update(id=ns_pkg_id, collection="ns_pkgs", data={"osm_id": osm_ns_pkg_id})
        print(f"NS on db: {DB._get(id=ns_pkg_id, collection='ns_pkgs')}")

        return {"msg_id": message["msg_id"], "status": 201}
