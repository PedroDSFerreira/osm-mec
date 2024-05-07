from ..container_info_thread import containers

def callback(data):
    for container_id in containers.keys():
        if container_id in data.get("container_Name"):
            node_specs = containers[container_id]["node_specs"]
            print(f"Container: {container_id}:")
            print(f"\tMemory Load: {get_mem_load(data, node_specs)}%")
            print(f"\tCPU Load: {get_cpu_load(data, node_specs, container_id)}%")

def get_mem_load(c_info, node_specs):
    mem_load = (c_info["container_stats"]["memory"]["usage"]/(node_specs["memory_size"]*pow(1024,3))) * 100
    return round(mem_load, 2)

def get_cpu_load(c_info, node_specs, container_id):
    timestampParts = timestampParts = c_info["timestamp"].split(':')
    timestamp = (float(timestampParts[-3][-2:])*pow(60,2) + float(timestampParts[-2])*60 + float(timestampParts[-1][:-1])) * pow(10, 9)
    current_cpu = c_info["container_stats"]["cpu"]["usage"]["total"]
    prev_cpu = node_specs.get("prev_cpu")
    prev_timestamp = node_specs.get("prev_timestamp")

    cpu_load = 0
    if prev_cpu != 0 and prev_timestamp != 0:
        cpu_delta = current_cpu - prev_cpu
        system_delta = timestamp - prev_timestamp

        if system_delta > 0.0 and cpu_delta >= 0.0:
            cpu_load = ((cpu_delta / system_delta) / node_specs["num_cpu_cores"]) * 100

    containers[container_id]["node_specs"]["prev_cpu"] = current_cpu
    containers[container_id]["node_specs"]["prev_timestamp"] = timestamp
    return round(cpu_load, 2)
