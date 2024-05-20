import os

from osmclient import client


def get_osm_client():
    return client.Client(host=os.getenv("OSM_HOSTNAME"), sol005=True)
