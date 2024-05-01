import cherrypy
from utils.db import DB
from utils.file_management import *
from utils.kafka_utils import KafkaUtils, producer
from utils.osm import osm_client


class NsPkgController:
    def __init__(self):
        self.collection = "ns_pkgs"
        self.topics = ["new_ns_pkg", "delete_ns_pkg", "update_ns_pkg"]
        self.producer = producer
        self.consumer = KafkaUtils.create_consumer(self.topics)

    @cherrypy.tools.json_out()
    def list_ns_pkgs(self, filter=None):
        """
        /ns_pkgs (GET)
        """
        return osm_client.nsd.list(filter=filter)

    @cherrypy.tools.json_out()
    def get_ns_pkg(self, ns_pkg_id):
        """
        /ns_pkgs/{ns_pkg_id} (GET)
        """
        ns_pkg = DB._get(ns_pkg_id, self.collection)
        return osm_client.nsd.get(name=ns_pkg.get("osm_id"))

    @cherrypy.tools.json_out()
    def new_ns_pkg(self, nsd):
        """
        /ns_pkgs (POST)
        """
        file = stream_to_binary(nsd.file)
        ns_pkg_id = DB._add(collection=self.collection, data={"nsd": file})

        try:
            file_name = get_file_name(ns_pkg_id, nsd.filename)

            msg_id = KafkaUtils.send_message(
                self.producer,
                "new_ns_pkg",
                {"ns_pkg_id": ns_pkg_id, "file_name": file_name},
            )
            response = KafkaUtils.wait_for_response(msg_id)

            cherrypy.response.status = response["status"]
            return {"id": ns_pkg_id}
        finally:
            delete_file(file_name)
            DB._delete(ns_pkg_id, self.collection)

    def update_ns_pkg(self, ns_pkg_id, nsd):
        """
        /ns_pkgs/{ns_pkg_id} (PATCH)
        """
        pass

    def delete_ns_pkg(self, ns_pkg_id, force=False):
        """
        /ns_pkgs/{ns_pkg_id} (DELETE)
        """
        if not DB._exists(ns_pkg_id, self.collection):
            cherrypy.HTTPError(404, "ns_pkg_id not found")

        msg_id = KafkaUtils.send_message(
            self.producer, "delete_ns_pkg", {"ns_pkg_id": ns_pkg_id, "force": force}
        )
        response = KafkaUtils.wait_for_response(msg_id)
        cherrypy.response.status = response["status"]
