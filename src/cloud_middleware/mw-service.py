from cloud_middleware.translator import get_number_translation_sv
from cloud_middleware.tts import get_tts_file

def get_user_number():
    user_number = int(input("What number would you like to be translated? "))
    return user_number

def run_cloud_middleware():
    user_number = get_user_number()
    user_number_sv = get_number_translation_sv(user_number)
    tts_number_file = get_tts_file()
    print(f"Your TTS file for {user_number} in English: {tts_number_file}")
    print(f"{user_number} is {user_number_sv} in Swedish.")

run_cloud_middleware()