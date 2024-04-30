import os

from osmclient import client
from osmclient.common.exceptions import ClientException

osm_client = client.Client(host=os.getenv("OSM_HOSTNAME"), sol005=True)


def get_osm_client():
    try:
        osm_client.get_token()
        return osm_client
    except ClientException as _:
        return client.Client(host=os.getenv("OSM_HOSTNAME"), sol005=True)
