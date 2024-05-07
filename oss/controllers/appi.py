import cherrypy
from utils.cherrypy_utils import is_valid_uuid
from utils.kafka import KafkaUtils, producer
from utils.osm import get_osm_client
from views.appi import AppiView


class AppiController:
    def __init__(self):
        self.topics = ["terminate_app_pkg"]
        self.producer = producer
        self.consumer = KafkaUtils.create_consumer(self.topics)

    @cherrypy.tools.json_out()
    def list_appis(self):
        """
        /appis (GET)
        """
        return [AppiView._list(appi) for appi in get_osm_client().ns.list()]

    @cherrypy.tools.json_out()
    def get_appi(self, appi_id):
        """
        /appis/{appi_id} (GET)
        """
        if not is_valid_uuid(appi_id):
            raise cherrypy.HTTPError(404, "App instance not found")
        return AppiView._get(get_osm_client().ns.get(appi_id))

    def terminate_appi(self, appi_id, wait=False):
        """
        /appis/{appi_id} (DELETE)
        """
        if not is_valid_uuid(appi_id):
            raise cherrypy.HTTPError(404, "App instance not found")
        wait = str(wait).lower() == "true"
        msg_id = KafkaUtils.send_message(
            self.producer,
            "terminate_app_pkg",
            {
                "appi_id": appi_id,
                "wait": wait,
            },
        )
        response = KafkaUtils.wait_for_response(msg_id)

        cherrypy.response.status = response["status"]
