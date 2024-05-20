responses = {}

def callback(data):
    msg_id = data.pop("msg_id")
    responses[msg_id] = data
