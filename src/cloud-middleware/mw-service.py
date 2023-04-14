from dummy_values import numbers_sv, TTS_file

def get_user_number():
    user_number = int(input("What number would you like to be translated? "))
    return user_number

def get_number_translation_sv(user_number):
    number_translation = numbers_sv[user_number]
    return number_translation

def get_tts_file():
    tts_file = TTS_file
    return tts_file

def main():
    user_number = get_user_number()
    user_number_sv = get_number_translation_sv(user_number)
    tts_number_file = get_tts_file()
    print(f"Your TTS file for {user_number} in English: {tts_number_file}")
    print(f"{user_number} is {user_number_sv} in Swedish.")