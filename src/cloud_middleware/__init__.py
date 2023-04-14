from flask import Flask

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
        return 'I will return a Swedish translation of your number!'

    return app