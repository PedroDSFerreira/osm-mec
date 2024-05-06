import warnings
import requests
import json
import subprocess
import yaml

class NBIConnector:

    def __init__(self, nbi_url, kubectl_command, kubectl_config_path) -> None:
        self.nbi_url = nbi_url
        self.authToken = self.getAuthToken()
        self.kubectl_command = kubectl_command
        self.kubectl_config_path = kubectl_config_path
        kubectl_config = json.loads(self.callEndpoints("/admin/v1/k8sclusters", "GET"))[0]
        with open(self.kubectl_config_path, 'w') as file:
            yaml.dump(kubectl_config["credentials"], file)

    def getAuthToken(self):
        # Authentication
        endpoint = self.nbi_url + '/admin/v1/tokens'
        result = {'error': True, 'data': ''}
        headers = {"Content-Type": "application/yaml", "accept": "application/json"}
        data = {"username": 'admin', "password": 'admin'}
        try:
            with warnings.catch_warnings():
                warnings.filterwarnings("ignore", category=requests.packages.urllib3.exceptions.InsecureRequestWarning)
                r = requests.post(endpoint, headers=headers,  json=data, verify=False)
        except Exception as e:
            result["data"] = str(e)
            return result

        if r.status_code == requests.codes.ok:
            result['error'] = False

        result["data"] = r.text
        token = json.loads(r.text)
        return token["id"]

    def callEndpoints(self, endpoint, method, data=None):
        if not self.authToken:
            return None

        # Get NS Instances
        endpoint = self.nbi_url + endpoint
        result = {'error': True, 'data': ''}
        headers = {"Content-Type": "application/yaml", "accept": "application/json",
                'Authorization': 'Bearer {}'.format(self.authToken)}
        try:
            with warnings.catch_warnings():
                warnings.filterwarnings("ignore", category=requests.packages.urllib3.exceptions.InsecureRequestWarning)
                match method:
                    case "GET":
                        r = requests.get(endpoint, data=data, params=None, verify=False, stream=True, headers=headers)
                    case "POST":
                        r = requests.post(endpoint, data=data, params=None, verify=False, stream=True, headers=headers)
        except Exception as e:
            result['data'] = str(e)
            return result

        if r.status_code == requests.codes.ok:
            result['error'] = False

        result['data'] = r.text
        info = r.text

        return info

    def getContainerInfo(self):
        ns_instances = self.callEndpoints("/nslcm/v1/ns_instances", "GET")
        try:
            ns_instances = json.loads(ns_instances)
        except Exception as e:
            print(e)

        if len(ns_instances) < 1:
            print('ERROR: No deployed ns instances')
        elif 'code' in ns_instances[0].keys():
            print('ERROR: Error calling ns_instances endpoint')

        containerInfo = []

        for ns_instance in ns_instances:
            ns_id = ns_instance["_id"]
            vnf_ids = ns_instance["constituent-vnfr-ref"]
            vnf_instances = {}
            for vnf_id in vnf_ids:
                vnfContent = self.callEndpoints("/nslcm/v1/vnf_instances/{}".format(vnf_id), "GET")
                try:
                    vnfContent = json.loads(vnfContent)
                except Exception as e:
                    print(e)
                vnf_instances[vnfContent["member-vnf-index-ref"]] = vnfContent["_id"]
            if "deployed" not in ns_instance["_admin"].keys():
                break
            kdu_instances = ns_instance["_admin"]["deployed"]["K8s"]
            for kdu in kdu_instances:
                kdu_instance = kdu["kdu-instance"]
                member_vnf_index = kdu["member-vnf-index"]
                namespace = kdu["namespace"]
                vnf_id = vnf_instances[member_vnf_index]

                command = (
                    "{} --kubeconfig={} --namespace={} get pods -l ns_id={} -o=json".format(
                        self.kubectl_command,
                        self.kubectl_config_path,
                        namespace,
                        ns_id,
                    )
                )
                try:
                    # Execute the kubectl command and capture the output
                    k8s_info = json.loads(subprocess.check_output(command.split()))
                except subprocess.CalledProcessError as e:
                    # Handle any errors if the command fails
                    print("Error executing kubectl command:", e)
                    return None

                for pod in k8s_info["items"]:
                    nodeName = pod["spec"]["nodeName"]
                    containers = pod["status"]["containerStatuses"]
                    for container in containers:
                        if "containerID" in container:
                            id = container["containerID"]
                            containerInfo.append({
                                "id": id.strip('"').split('/')[-1],
                                "ns_id": ns_id,
                                "vnf_id": vnf_id,
                                "kdu_id": kdu_instance,
                                "node": nodeName,
                                }
                            )

        return containerInfo
