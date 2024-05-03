import logging
import os

from osmclient import client

# osm_client = client.Client(host=os.getenv("OSM_HOSTNAME"), sol005=True)


def get_osm_client():
    # try:
    #     osm_client.vim.list()
    # except Exception as _:
    #     logging.error("OSM client is not connected, trying to reconnect")
    #     osm_client = client.Client(host=os.getenv("OSM_HOSTNAME"), sol005=True)
    # finally:
    #     return osm_client
    return client.Client(host=os.getenv("OSM_HOSTNAME"), sol005=True)
