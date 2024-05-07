import cherrypy
from utils.appd_validation import *
from utils.cherrypy_utils import is_valid_id
from utils.db import DB
from utils.file_management import *
from utils.kafka import KafkaUtils, producer
from views.app_pkg import AppPkgView


class AppPkgController:
    def __init__(self):
        self.collection = "app_pkgs"
        self.topics = [
            "new_app_pkg",
            "delete_app_pkg",
            "update_app_pkg",
            "instantiate_app_pkg",
        ]
        self.producer = producer
        self.consumer = KafkaUtils.create_consumer(self.topics)

    @cherrypy.tools.json_out()
    def list_app_pkgs(self):
        """
        /app_pkgs (GET)
        """
        app_pkgs = DB._list(self.collection)
        return [AppPkgView._list(app_pkg) for app_pkg in app_pkgs]

    @cherrypy.tools.json_out()
    def get_app_pkg(self, app_pkg_id):
        """
        /app_pkgs/{app_pkg_id} (GET)
        """
        if not is_valid_id(app_pkg_id) or not DB._exists(app_pkg_id, self.collection):
            raise cherrypy.HTTPError(404, "App package not found")

        app_pkg = DB._get(app_pkg_id, self.collection)
        return AppPkgView._get(app_pkg)

    @cherrypy.tools.json_out()
    def new_app_pkg(self, appd):
        """
        /app_pkgs (POST)
        """
        appd_gz = read_stream(appd.file)
        appd_data = get_descriptor_data(appd_gz)
        validate_descriptor(appd_data)

        app_pkg_id = DB._add(
            self.collection, AppPkgView._save(appd_data.get("mec-appd"), appd_gz)
        )

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

    def update_app_pkg(self, appd, app_pkg_id):
        """
        /app_pkgs/{app_pkg_id} (PATCH)
        """
        appd_gz = read_stream(appd.file)
        appd_data = get_descriptor_data(appd_gz)
        validate_descriptor(appd_data)

        if not is_valid_id(app_pkg_id) or not DB._exists(app_pkg_id, self.collection):
            raise cherrypy.HTTPError(404, "App package not found")

        msg_id = KafkaUtils.send_message(
            self.producer,
            "update_app_pkg",
            {"app_pkg_id": app_pkg_id, "appd_data": appd_data},
        )
        response = KafkaUtils.wait_for_response(msg_id)

        DB._update(
            app_pkg_id,
            self.collection,
            AppPkgView._save(appd_data.get("mec-appd"), appd_gz),
        )

        cherrypy.response.status = response["status"]

    def delete_app_pkg(self, app_pkg_id):
        """
        /app_pkgs/{app_pkg_id} (DELETE)
        """
        if not is_valid_id(app_pkg_id) or not DB._exists(app_pkg_id, self.collection):
            raise cherrypy.HTTPError(404, "App package not found")

        msg_id = KafkaUtils.send_message(
            self.producer,
            "delete_app_pkg",
            {"app_pkg_id": app_pkg_id},
        )
        response = KafkaUtils.wait_for_response(msg_id)

        DB._delete(app_pkg_id, self.collection)

        cherrypy.response.status = response["status"]

    @cherrypy.tools.json_out()
    def instantiate_app_pkg(self, app_pkg_id, vim_id, name, description, wait=False):
        """
        /app_pkgs/{app_pkg_id}/instantiate (POST)
        """
        if not is_valid_id(app_pkg_id) or not DB._exists(app_pkg_id, self.collection):
            raise cherrypy.HTTPError(404, "App package not found")

        wait = str(wait).lower() == "true"
        msg_id = KafkaUtils.send_message(
            self.producer,
            "instantiate_app_pkg",
            {
                "app_pkg_id": app_pkg_id,
                "vim_id": vim_id,
                "name": name,
                "description": description,
                "wait": wait,
            },
        )
        response = KafkaUtils.wait_for_response(msg_id)
        instance_id = response.get("instance_id")

        cherrypy.response.status = response["status"]
        return {"id": instance_id}
