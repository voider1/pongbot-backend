#!venv/bin/python
from multiprocessing import Queue

from flask import Flask
from flask import request

app = Flask(__name__)
actions = Queue()


@app.route('/test', methods=['POST'])
def test():
    alexa_stuff = request.get_json()
    print(alexa_stuff)


@app.route('/add_command', methods=['POST'])
def add_command():
    req_data = request.get_json()

    type = req_data['type']
    actions.put(type)

    return 'added: {}'.format(type)


@app.route('/get_command')
def get_command():
    if actions.empty():
        return 'none'

    return actions.get()


if __name__ == '__main__':
      app.run(host='0.0.0.0', port=80)
