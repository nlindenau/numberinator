from flask import Flask, jsonify, request
from cloud_middleware.request_processor import get_written_number, get_user_number, get_azure_subscription_key
from cloud_middleware.translator import get_number_translation_sv
from cloud_middleware.tts import get_tts_file

def create_app():
    app = Flask(__name__, instance_relative_config=True)

    @app.route('/')
    def hello():
        return 'Hello from cloud middleware service!'
    
    @app.route('/v1/text-to-speech', methods=['GET'])
    def produce_tts():
        request_data = request.get_json()

        user_number = get_written_number(request_data)
        subscription_key = request_data['subscirption-key']

        tts_link = get_tts_file(user_number, subscription_key)

        response = {
            "tts-link": tts_link
        }

        json_response = jsonify(response)

        return json_response, 200

    @app.route('/v1/sv-translation', methods=['GET'])
    def produce_sv_translation():
        request_data = request.get_json()

        user_number = get_user_number(request_data)
        subscription_key = request_data['subscirption-key']

        swedish_number = get_number_translation_sv(user_number, subscription_key)

        response = {
            "swedish_translation": swedish_number
        }

        json_response = jsonify(response)

        return json_response, 200

    return app