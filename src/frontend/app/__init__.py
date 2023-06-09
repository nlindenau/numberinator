from flask import Flask, jsonify, request
import os
def create_app():
    app = Flask(__name__, instance_relative_config=True)

    @app.route('/')
    def hello():
        return 'Hello from the app!'

    return app

main()