from utils.appd_parser import AppdParser
from utils.appd_validation import *
from utils.db import DB
from utils.exceptions import handle_exceptions
from utils.file_management import *
from utils.osm import get_osm_client


@handle_exceptions
def callback(message):
    app_pkg_id = message.get("app_pkg_id")
    updated_appd = message.get("appd_data")

    if app_pkg_id and updated_appd:
        app_pkg = DB._get(id=app_pkg_id, collection="app_pkgs")

        appd_binary = app_pkg.get("appd")
        ns_pkg_id = app_pkg.get("ns_pkg_id")
        vnf_pkg_id = app_pkg.get("vnf_pkg_id")

        appd = validate_descriptor(updated_appd)

        appd_parser = AppdParser(appd)

        artifacts = appd_parser.get_artifacts()
        artifacts_data = get_artifacts_data(appd_binary, artifacts)

        vnfd_file = appd_parser.export_vnfd(get_dir("vnfd"), app_pkg_id, artifacts_data)
        nsd_file = appd_parser.export_nsd(get_dir("nsd"), app_pkg_id)

        get_osm_client().vnfd.update(vnf_pkg_id, vnfd_file)
        get_osm_client().nsd.update(ns_pkg_id, nsd_file)

        delete_file(vnfd_file)
        delete_file(nsd_file)

        return {"msg_id": message["msg_id"], "status": 201}
