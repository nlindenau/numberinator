from flask import Flask, jsonify, request
from cloud_middleware.translator import get_number_translation_sv

def create_app():
    app = Flask(__name__, instance_relative_config=True)

    @app.route('/')
    def hello():
        return 'Hello from cloud middleware service!'
    
    @app.route('/tts')
    def produce_tts():
        return 'I will return a TTS file!'

    @app.route('/sv-translation')
    def produce_sv_translation():
        example_number = get_number_translation_sv(3)
        return 'I will return a Swedish translation of your number! Did you know {example_number} is 3 in Swedish?'
    
    @app.route('/v1/test', methods=['GET'])
    def test():
        request_data = request.get_json()

        user = request_data['username']

        response = {
            "you": user,
        }

        json_response = jsonify(response)

        return json_response, 200
        


    return app