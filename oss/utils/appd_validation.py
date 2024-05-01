import io
import tarfile

import yaml
from cherrypy import HTTPError
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
            raise HTTPError(422, "No .yaml file found in the archive.")
        elif len(yaml_files) > 1:
            raise HTTPError(422, "More than one .yaml file found in the archive.")
        yaml_file = yaml_files.pop()

        return yaml.safe_load(tar.extractfile(yaml_file).read())


def validate_descriptor(data):
    appd = mec_app_descriptor()
    try:
        pybindJSONDecoder.load_ietf_json(data, None, None, obj=appd, path_helper=True)
    except Exception as e:
        raise HTTPError(422, str(e))
    return appd
