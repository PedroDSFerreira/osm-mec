from flask import Flask, jsonify

from nbi_k8s_connector import NBIConnector
from meao import MEAO
from os import getenv

app = Flask(__name__)

@app.route('/containerInfo', methods=['GET'])
def get_container_info():
    return jsonify(ContainerInfo=meao.containerInfo)

if __name__ == '__main__':
    nbi_k8s_connector = NBIConnector(
        getenv('NBI_URL'),
        getenv('KUBECTL_COMMAND'),
        getenv('KUBECTL_CONFIG_PATH')
    )

    meao = MEAO(
        nbi_k8s_connector,
        getenv('UPDATE_CONTAINER_IDS_FREQ')
    )

    meao.start()

    app.run(host='0.0.0.0', port=8000)
