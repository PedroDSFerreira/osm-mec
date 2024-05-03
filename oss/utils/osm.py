import os

from osmclient import client
from osmclient.common.exceptions import ClientException


def get_osm_client():
    return client.Client(host=os.getenv("OSM_HOSTNAME"), sol005=True)
