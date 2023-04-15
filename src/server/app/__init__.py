import os
from dotenv import load_dotenv

load_dotenv()

SUBSCRIPTION_KEY = os.getenv('SUBSCRIPTION_KEY')
CLOUD_MIDDLEWARE_HOST = os.getenv('CLOUD_MIDDLEWARE_HOST')
CLOUD_MIDDLEWARE_PORT = os.getenv('CLOUD_MIDDLEWARE_PORT')
DIGIT_RECOGNITION_HOST = os.getenv('DIGIT_RECOGNITION_HOST')
DIGIT_RECOGNITION_PORT = os.getenv('DIGIT_RECOGNITION_PORT')


def main():
    print(f"I will connect to cloud middleware using {CLOUD_MIDDLEWARE_HOST}:{CLOUD_MIDDLEWARE_PORT}")

def get_number_recognition():
    print("I will get a number recognition from digit recognition service")


main()