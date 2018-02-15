from flask import Flask, request, jsonify
from multiprocessing import Queue
import random

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


@app.route('/add_command', methods=['POST']) #GET requests will be blocked
def add_command():
    req_data = request.get_json()
    dir = req_data['request']['intent']['slots']['Direction']['value']
    response['response']['outputSpeech']['text'] = random.choice(move_responses).format(dir)

    actions.put(dir)
    return jsonify(response)


@app.route('/get_command')
def get_command():
    if actions.empty():
        return 'none'

    return actions.get()


@app.route('/test_alexa', methods=['POST'])
def test_alexa():
    print(request.get_json())

    return jsonify(response)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
