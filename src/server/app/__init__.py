import os
from dotenv import load_dotenv
from app.cloud_requester import get_translations

load_dotenv()

SUBSCRIPTION_KEY = os.getenv('SUBSCRIPTION_KEY')
CLOUD_MIDDLEWARE_HOST = os.getenv('CLOUD_MIDDLEWARE_HOST')
CLOUD_MIDDLEWARE_PORT = os.getenv('CLOUD_MIDDLEWARE_PORT')
DIGIT_RECOGNITION_HOST = os.getenv('DIGIT_RECOGNITION_HOST')
DIGIT_RECOGNITION_PORT = os.getenv('DIGIT_RECOGNITION_PORT')


def main():
    print(f"I will connect to cloud middleware using {CLOUD_MIDDLEWARE_HOST}:{CLOUD_MIDDLEWARE_PORT}")

main()