import io
import tarfile

import yaml
from models.mec_app import mec_app_descriptor
from pyangbind.lib.serialise import pybindJSONDecoder


def get_descriptor_data(tgz_data):
    buffer = io.BytesIO(tgz_data)
    yaml_files = []
    with tarfile.open(fileobj=buffer, mode="r:gz") as tar:
        for member in tar.getmembers():
            if member.name.endswith(".yaml"):
                yaml_files.append(member.name)

        if len(yaml_files) == 0:
            raise Exception("No .yaml file found in the archive.")
        elif len(yaml_files) > 1:
            raise Exception("More than one .yaml file found in the archive.")

        yaml_file = yaml_files.pop()
        return yaml.safe_load(tar.extractfile(yaml_file).read())


def get_artifacts_data(tgz_data, artifacts_name):
    buffer = io.BytesIO(tgz_data)
    artifacts = {}
    with tarfile.open(fileobj=buffer, mode="r:gz") as tar:
        for member in tar.getmembers():
            if member.name in artifacts_name:
                artifacts[member.name] = tar.extractfile(member).read()
    return artifacts


def validate_descriptor(data):
    appd = mec_app_descriptor()
    pybindJSONDecoder.load_ietf_json(data, None, None, obj=appd, path_helper=True)
    return appd
