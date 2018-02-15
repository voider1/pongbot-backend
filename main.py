#!venv/bin/python
from flask import Flask
from flask import request
from multiprocessing import Queue

app = Flask(__name__)

actions = Queue()

@app.route('/add_command', methods=['POST']) #GET requests will be blocked
def add_command():
    req_data = request.get_json()

    type = req_data['type']
    actions.put(type)

    return '''added: {}'''.format(type)

@app.route('/get_command')
def get_command():
    if actions.empty():
        return 'none'

    return actions.get()

if __name__ == '__main__':
      app.run(host='0.0.0.0', port=80)
