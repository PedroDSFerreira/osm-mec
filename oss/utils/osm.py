import os

from osmclient import client

osm_client = client.Client(host=os.getenv("OSM_HOSTNAME"), sol005=True)
