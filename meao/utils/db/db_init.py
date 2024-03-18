from .db_utils import db


class DatabaseInitializer:
    def create_collections(self):
        collections = ["ns_pkgs", "nsis", "app_pkgs", "appis"]
        for collection in collections:
            if collection not in db.list_collection_names():
                db.create_collection(collection)

    def insert_default_data(self):
        db['ns_pkgs'].insert_one({'osm_id': 'ff97b85b-251f-43f0-82f1-f52429847e23'})

    @classmethod
    def initialize_database(cls):
        initializer = cls()
        initializer.create_collections()
        initializer.insert_default_data()