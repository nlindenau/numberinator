from flask import Flask, jsonify, request
import os
from dotenv import load_dotenv
from cloud_requester import get_translations, get_tts
from recognition_requester import get_number_recognition
from request_processor import get_data_from_response

load_dotenv()

SUBSCRIPTION_KEY = os.getenv('SUBSCRIPTION_KEY')
CLOUD_MIDDLEWARE_HOST = os.getenv('CLOUD_MIDDLEWARE_HOST')
CLOUD_MIDDLEWARE_PORT = os.getenv('CLOUD_MIDDLEWARE_PORT')
DIGIT_RECOGNITION_HOST = os.getenv('DIGIT_RECOGNITION_HOST')
DIGIT_RECOGNITION_PORT = os.getenv('DIGIT_RECOGNITION_PORT')
TRANSLATION_ENDPOINT = os.getenv('TRANSLATION_ENDPOINT')
TTS_ENDPOINT = os.getenv('TTS_ENDPOINT')
DIGIT_RECOGNITION_ENDPOINT = os.getenv('RECOGNITION_ENDPOINT')

TRANSLATION_API_URL = CLOUD_MIDDLEWARE_HOST + ":" + CLOUD_MIDDLEWARE_PORT + TRANSLATION_ENDPOINT
TTS_API_URL = CLOUD_MIDDLEWARE_HOST + ":" + CLOUD_MIDDLEWARE_PORT + TTS_ENDPOINT

def create_app():
    app = Flask(__name__, instance_relative_config=True)

    @app.route('/')
    def hello():
        return 'Hello from the server!'
    
    @app.route('/v1/process-image', methods=['POST'])
    def produce_number_predition():
        response = {
            "prediction": "3",
            "written-number": "three",
            "probability": "95%",
            "swedish-translation": "tre",
            "tts-link": "link to file"
        }

        json_response = jsonify(response)

        return json_response, 201


    return app

main()