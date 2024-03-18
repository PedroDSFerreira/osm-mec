from osmclient import client
import os

osm_client = client.Client(host=os.getenv("OSM_HOSTNAME"), sol005=True)