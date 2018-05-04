import random
from multiprocessing import Queue

from flask import Flask, request, jsonify

response = {
    "version": "1.0",
    "response": {
        "outputSpeech": {
            "type": "PlainText",
            "text": "Hello World"
        }
    }
}

move_responses = [
    "I'd rather not, but alright then... Going {}.",
    "Alright, I'll go {}... But not because I like you or anything.",
    "Okay, but I'm only going {} because I'm programmed to do so."
]

app = Flask(__name__)
actions = Queue()


@app.route('/add_command', methods=['POST'])
def add_command():
    req_data = request.get_json()
    direction = req_data['request']['intent']['slots']['Direction']['value']
    response['response']['outputSpeech']['text'] = random.choice(move_responses).\
        format(direction)

    actions.put(direction)
    return jsonify(response)


@app.route('/get_command')
def get_command():
    if actions.empty():
        return 'none'

    return actions.get()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

