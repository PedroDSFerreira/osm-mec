import os

from bson import ObjectId
from pymongo import MongoClient

client = MongoClient(
    "mongodb://mongo:27017/",
    username=os.getenv("MONGO_USER"),
    password=os.getenv("MONGO_PASSWORD"),
)

db = client["db"]


class DB:
    @staticmethod
    def _get(id, collection):
        return db[collection].find_one({"_id": ObjectId(id)})

    @staticmethod
    def _find(collection, filter=None):
        return db[collection].find_one(filter)

    @staticmethod
    def _list(collection, filter=None):
        return list(db[collection].find(filter))

    @staticmethod
    def _add(collection, data):
        id = db[collection].insert_one(data).inserted_id
        return str(id)

    @staticmethod
    def _update(id, collection, data):
        db[collection].update_one({"_id": ObjectId(id)}, {"$set": data})

    @staticmethod
    def _delete(id, collection):
        db[collection].delete_one({"_id": ObjectId(id)})

    @staticmethod
    def _exists(id, collection):
        return db[collection].find_one({"_id": ObjectId(id)}) is not None
