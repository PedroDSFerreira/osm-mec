from .db_utils import db


class DatabaseInitializer:
    def create_collections(self):
        collections = ["app_pkgs", "appis"]
        for collection in collections:
            if collection not in db.list_collection_names():
                db.create_collection(collection)

    @classmethod
    def initialize_database(cls):
        initializer = cls()
        initializer.create_collections()
