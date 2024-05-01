from osmclient.common.exceptions import ClientException
from utils.appd_parser import AppdParser
from utils.appd_validation import *
from utils.capture_io import CaptureIO
from utils.db import DB
from utils.exceptions import handle_exceptions
from utils.file_management import *
from utils.osm import get_osm_client


@handle_exceptions
def callback(message):
    app_pkg_id = message.get("app_pkg_id")
    if app_pkg_id:
        app_pkg = DB._get(id=app_pkg_id, collection="app_pkgs").get("appd")
        appd_data = get_descriptor_data(app_pkg)
        appd = validate_descriptor(appd_data)

        appd_parser = AppdParser(appd)

        artifacts = appd_parser.get_artifacts()
        artifacts_data = get_artifacts_data(app_pkg, artifacts)

        vnfd_file = appd_parser.export_vnfd(get_dir("vnfd"), app_pkg_id, artifacts_data)
        nsd_file = appd_parser.export_nsd(get_dir("nsd"), app_pkg_id)

        with CaptureIO() as out:
            get_osm_client().vnfd.create(vnfd_file)
        vnf_pkg_id = out[0]

        try:
            with CaptureIO() as out:
                get_osm_client().nsd.create(nsd_file)
            ns_pkg_id = out[0]
        except ClientException as e:
            get_osm_client().vnfd.delete(vnf_pkg_id)
            raise e

        DB._update(
            id=app_pkg_id,
            collection="app_pkgs",
            data={
                "vnf_pkg_id": vnf_pkg_id,
                "ns_pkg_id": ns_pkg_id,
            },
        )

        delete_file(vnfd_file)
        delete_file(nsd_file)

        return {"msg_id": message["msg_id"], "status": 201}
