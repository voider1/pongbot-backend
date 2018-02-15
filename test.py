from flask import Flask
from flask import request
import queue

app = Flask(__name__)

actions = queue.Queue()

@app.route('/add_command', methods=['POST']) #GET requests will be blocked
def add_command():
    req_data = request.get_json()

    type = req_data['type']
    actions.put(type)

    return '''added: {}'''.format(type)

@app.route('/get_command') #GET requests will be blocked
def get_command():
    if actions.empty():
        return 'none'

    return actions.get()
