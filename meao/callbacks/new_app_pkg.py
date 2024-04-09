from utils.db import DB
from utils.exceptions import handle_exceptions
from utils.file_management import delete_file, save_file
from utils.osm import osm_client


@handle_exceptions
def callback(message):
    app_pkg_id = message.get("app_pkg_id")
    if app_pkg_id:
        app_pkg = DB._get(id=app_pkg_id, collection="app_pkgs")
        # save file
        appd_path = save_file("app_pkgs", app_pkg.get("appd"))
        # create vnf pkg in osm
        osm_app_pkg_id = osm_client.vnfd.create(filename=appd_path)
        # delete file
        delete_file(appd_path)

        DB._update(
            id=app_pkg_id, collection="app_pkgs", data={"osm_id": osm_app_pkg_id}
        )

        return {"msg_id": message["msg_id"], "status": 201}
