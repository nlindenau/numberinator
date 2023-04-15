from cloud_middleware.translator import get_number_translation_sv
from cloud_middleware.tts import get_tts_file

def get_user_number(request):
    """Returns the number to be processed from the incoming request.
    """
    user_number = request
    user_number = int(user_number)
    
    return user_number

def run_cloud_middleware(request):
    """Returns the swedish translation of the number and a TTS file link.
    """
    user_number = get_user_number(request)
    user_number_sv = get_number_translation_sv(user_number)
    tts_number_file = get_tts_file(user_number)
    print(f"Your TTS file for {user_number} in English: {tts_number_file}")
    print(f"{user_number} is {user_number_sv} in Swedish.")
    
    return user_number_sv, tts_number_file

run_cloud_middleware()