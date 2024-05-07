from ..container_info_thread import containers

def callback(data):
    for container_id in containers.keys():
        if container_id in data.get("container_Name"):
            print(data)
            print(f"mem_usage: {get_mem_usage(data)}")

def get_mem_usage(c_info):
    return c_info["container_stats"]["memory"]["usage"]

