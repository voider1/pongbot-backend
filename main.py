import random
from multiprocessing import Queue
from enum import Enum

from flask import Flask, request, jsonify, make_response
from flask_restful import Resource, Api


response = {
    "version": "1.0",
    "response": {
        "outputSpeech": {
            "type": "PlainText",
            "text": "Hello World"
        }
    }
}

MOVE_RESPONSES = [
    "I'd rather not, but alright then... Going {}.",
    "Alright, I'll go {}... But not because I like you or anything.",
    "Okay, but I'm only going {} because I'm programmed to do so."
]

app = Flask(__name__)
api = Api(app)
actions = Queue()


class Format(Enum):
    plain = "plain"
    json = "json"


class Command(Resource):
    def get(self):
        _format = request.args.get('format', None)
        if _format == Format.plain.value or _format is None:
            if actions.empty():
                return make_response("", 204)
            action = actions.get()
            return "{},{}".format(action['direction'], action['degrees'])
        elif _format == Format.json.value:
            if actions.empty():
                return make_response(jsonify(""), 204)
            return jsonify(actions.get())

    def post(self):
        req_data = request.get_json()
        direction = req_data['request']['intent']['slots']['Direction']['value']
        degrees = req_data['request']['intent']['slots']['Degrees']['value']
        response['response']['outputSpeech']['text'] = random.choice(MOVE_RESPONSES).\
            format(direction)
        action = {'direction': direction, 'degrees': degrees}
        actions.put(action)
        return jsonify(response)

api.add_resource(Command, "/commands")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
