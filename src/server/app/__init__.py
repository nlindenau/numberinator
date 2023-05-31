import os
from dotenv import load_dotenv
from cloud_requester import get_translations

load_dotenv()

SUBSCRIPTION_KEY = os.getenv('SUBSCRIPTION_KEY')
CLOUD_MIDDLEWARE_HOST = os.getenv('CLOUD_MIDDLEWARE_HOST')
CLOUD_MIDDLEWARE_PORT = os.getenv('CLOUD_MIDDLEWARE_PORT')
DIGIT_RECOGNITION_HOST = os.getenv('DIGIT_RECOGNITION_HOST')
DIGIT_RECOGNITION_PORT = os.getenv('DIGIT_RECOGNITION_PORT')
TRANSLATION_ENDPOINT = os.getenv('TRANSLATION_ENDPOINT')

TRANSLATION_API_URL = CLOUD_MIDDLEWARE_HOST + ":" + CLOUD_MIDDLEWARE_PORT + TRANSLATION_ENDPOINT

def main():
    my_number = 3 

    print (f"Your number is {my_number}")

    swedish_translation = get_translations(my_number, SUBSCRIPTION_KEY, TRANSLATION_API_URL)

    print(f"In swedish, that's {swedish_translation}")


main()