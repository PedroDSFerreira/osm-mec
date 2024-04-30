import cherrypy
from utils.appd_validation import *
from utils.db import DB
from utils.file_management import *
from utils.kafka_utils import KafkaUtils, producer
from utils.osm import get_osm_client


class AppPkgController:
    def __init__(self):
        self.collection = "app_pkgs"
        self.topics = ["new_app_pkg", "delete_app_pkg", "update_app_pkg"]
        self.producer = producer
        self.consumer = KafkaUtils.create_consumer(self.topics)

    @cherrypy.tools.json_out()
    def list_app_pkgs(self, filter=None):
        """
        /app_pkgs (GET)
        """
        return get_osm_client().vnfd.list(filter=filter)

    @cherrypy.tools.json_out()
    def get_app_pkg(self, app_pkg_id):
        """
        /app_pkgs/{app_pkg_id} (GET)
        """
        vnfd_id = DB._get(app_pkg_id, self.collection).get("vnfd_id")
        return get_osm_client().vnfd.get(name=vnfd_id)

    @cherrypy.tools.json_out()
    def new_app_pkg(self, appd):
        """
        /app_pkgs (POST)
        """
        data = read_stream(appd.file)
        appd_data = get_descriptor_data(data)
        validate_descriptor(appd_data)

        app_pkg_id = DB._add(collection=self.collection, data={"appd": data})

        try:
            msg_id = KafkaUtils.send_message(
                self.producer,
                "new_app_pkg",
                {"app_pkg_id": app_pkg_id},
            )
            response = KafkaUtils.wait_for_response(msg_id)

            cherrypy.response.status = response["status"]
            return {"id": app_pkg_id}
        except Exception as e:
            DB._delete(app_pkg_id, self.collection)
            raise e

    def update_app_pkg(self, app_pkg_id, appd):
        """
        /app_pkgs/{app_pkg_id} (PATCH)
        """

    def delete_app_pkg(self, app_pkg_id, force=False):
        """
        /app_pkgs/{app_pkg_id} (DELETE)
        """
