import os

import requests
import json
import flask
from flask import request

app = flask.Flask(__name__)

# These ports are injected automatically into the container.
dapr_port = os.getenv("DAPR_HTTP_PORT", 8000)
dapr_grpc_port = os.getenv("DAPR_GRPC_PORT", 5000)
dapr_url = "http://localhost:{}/v1.0/invoke/nodeapp/method/neworder".format(dapr_port)  # noqa

state_store_name = "statestore"
state_url = "http://localhost:{}/v1.0/state/{}".format(dapr_port, state_store_name)  # noqa

# Port to communicate with this HTTP server
port = 8080

@app.route('/order', methods=['GET'])
def get_orders():
    r = requests.get(state_url + "/order")
    try:
        return r.text
    except:
        return {}


@app.route('/order', methods=['POST'])
def new_order():
    content = request.json

    state = [{
        "key": "order",
        "value": content
    }]

    r = requests.post(state_url, data=json.dumps(state))

    return r.text

@app.route("/")
def ports():
    return {
        "DAPR_HTTP_PORT": dapr_port,
        "DAPR_GRPC_PORT": dapr_grpc_port
    }

app.run(host="0.0.0.0", port=8080)