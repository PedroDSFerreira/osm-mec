from pathlib import Path

import yaml
from pyangbind.lib.serialise import pybindJSONDecoder
from pyangbind.lib import pybindJSON

from mec_app_descriptor import mec_app_descriptor

appd = mec_app_descriptor()
data = yaml.safe_load(Path("test.yaml").read_text())


# instance = pybindJSON.load(conf, mec_app_descriptor, 'mec_app_descriptor')
try:
    print(f"-----------------\ndata:\n{data}\n\n")
    pybindJSONDecoder.load_ietf_json(data, None, None, obj=appd, path_helper=True)
    out = pybindJSON.dumps(appd, mode="ietf")
    print(out)
    desc_out = yaml.safe_load(out)
#     # pybinconfdJSONDecoder.load_ietf_json(conf, None, None, obj=appd, overwrite=True)
except Exception as e:
    print(f"ERROR: {e}")
