import tarfile
from io import BytesIO

import yaml


class AppdParser:
    def __init__(self, data):
        self.appd = data
        self.vnfd = self.__make_vnfd()
        self.nsd = self.__make_nsd()

    def get_artifacts(self):
        return [
            artifact["file"]
            for _, artifact in self.appd.mec_appd.artifacts.get().items()
        ]

    def export_nsd(self, path, filename):
        file_path = path + "/" + filename + ".tar.gz"
        with tarfile.open(file_path, "w:gz") as tar:
            nsd_yaml = yaml.dump(self.nsd, sort_keys=False)
            nsd_yaml_bytes = BytesIO(nsd_yaml.encode())
            nsd_yaml_file = tarfile.TarInfo("nsd/nsd.yaml")
            nsd_yaml_file.size = len(nsd_yaml_bytes.getvalue())
            tar.addfile(nsd_yaml_file, nsd_yaml_bytes)

        return file_path

    def export_vnfd(self, path, filename, artifacts):
        file_path = path + "/" + filename + ".tar.gz"
        with tarfile.open(file_path, "w:gz") as tar:
            vnfd_yaml = yaml.dump(self.vnfd, sort_keys=False)
            vnfd_yaml_bytes = BytesIO(vnfd_yaml.encode())
            vnfd_yaml_file = tarfile.TarInfo("vnfd/vnfd.yaml")
            vnfd_yaml_file.size = len(vnfd_yaml_bytes.getvalue())
            tar.addfile(vnfd_yaml_file, vnfd_yaml_bytes)

            for name, artifact in artifacts.items():
                artifact_bytes = BytesIO(artifact)
                with tarfile.open(fileobj=artifact_bytes, mode="r:gz") as artifact_tar:
                    for member in artifact_tar.getmembers():
                        member.name = "vnfd/helm-chart-v3s/" + member.name
                        tar.addfile(member, artifact_tar.extractfile(member))

        return file_path

    def __make_vnfd(self):
        vnfd_id = str(self.appd.mec_appd.id + "-vnfd")
        name = str(self.appd.mec_appd.name)
        description = "VNF descriptor for " + self.appd.mec_appd.description.lower()
        provider = str(self.appd.mec_appd.provider)
        version = str(self.appd.mec_appd.version)
        ext_cpd = self.__get_ext_cpd_list()
        mgmt_net_id = str(ext_cpd[0]["id"])
        k8s_cluster = self.__get_k8s_cluster_list(ext_cpd)
        kdu = self.__get_kdu_list(self.appd.mec_appd.artifacts.get())

        return {
            "vnfd": {
                "id": vnfd_id,
                "product-name": name,
                "description": description,
                "provider": provider,
                "version": version,
                "mgmt-cp": mgmt_net_id,
                "df": [{"id": "default-df"}],
                "k8s-cluster": k8s_cluster,
                "kdu": kdu,
                "ext-cpd": ext_cpd,
            }
        }

    def __make_nsd(self):
        vnfd_id = str(self.appd.mec_appd.id + "-vnfd")
        vnf_id = str(self.appd.mec_appd.id + "-vnf")
        nsd_id = str(self.appd.mec_appd.id + "-nsd")
        name = str(self.appd.mec_appd.name)
        description = "NS descriptor for " + self.appd.mec_appd.description.lower()
        provider = str(self.appd.mec_appd.provider)
        version = str(self.appd.mec_appd.version)
        ext_cpd = self.__get_ext_cpd_list()
        mgmt_net_id = str(ext_cpd[0]["id"])
        virtual_link_connectivity = self.__get_virtual_link_connectivity_list(
            ext_cpd, mgmt_net_id, vnf_id
        )
        virtual_link_desc = self.__get_virtual_link_desc_list(ext_cpd)

        return {
            "nsd": {
                "nsd": [
                    {
                        "id": nsd_id,
                        "name": name,
                        "description": description,
                        "designer": provider,
                        "version": version,
                        "vnfd-id": [vnfd_id],
                        "df": [
                            {
                                "id": "default-df",
                                "vnf-profile": [
                                    {
                                        "id": vnf_id,
                                        "vnfd-id": vnfd_id,
                                        "virtual-link-connectivity": virtual_link_connectivity,
                                    }
                                ],
                            }
                        ],
                        "virtual-link-desc": virtual_link_desc,
                    }
                ]
            }
        }

    def __get_kdu_list(self, artifacts):
        kdu_list = []
        for key, kdu in artifacts.items():
            if kdu["type"] == "helm2":
                helm_version = "v2"
            elif kdu["type"] == "helm3":
                helm_version = "v3"
            else:
                raise ValueError(f"Unsupported artifact type: {kdu['type']}")

            kdu_list.append(
                {
                    "name": str(key) + "-kdu",
                    "helm-chart": str(key),
                    "helm-version": str(helm_version),
                }
            )
        return kdu_list

    def __get_ext_cpd_list(self):
        ext_cpd = self.appd.mec_appd.ext_cpd.get()
        ext_cpd_list = []
        for key, cpd in ext_cpd.items():
            ext_cpd_list.append(
                {"id": str(key), "k8s-cluster-net": str(cpd["k8s-cluster-net"])}
            )
        return ext_cpd_list

    def __get_k8s_cluster_list(self, ext_cpd):
        return {"nets": [{"id": i["k8s-cluster-net"]} for i in ext_cpd]}

    def __get_virtual_link_connectivity_list(self, ext_cpd, mgmt_net_id, vnf_id):
        virtual_link_connectivity_list = []
        for cpd in ext_cpd:
            virtual_link_connectivity_list.append(
                {
                    "virtual-link-profile-id": cpd["k8s-cluster-net"],
                    "constituent-cpd-id": [
                        {
                            "constituent-base-element-id": vnf_id,
                            "constituent-cpd-id": mgmt_net_id,
                        }
                    ],
                }
            )
        return virtual_link_connectivity_list

    def __get_virtual_link_desc_list(self, ext_cpd):
        return [{"id": i["k8s-cluster-net"], "mgmt-network": True} for i in ext_cpd]
