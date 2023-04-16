from request_processor import create_request, make_get_request, get_data_from_response

def get_translations(user_number, subscription_key, api_url):
    """Gets translations from the cloud middleware service."""
    request_body = create_request("number", user_number, "subscription-key", subscription_key)
    response = make_get_request(api_url, request_body)
    translation = get_data_from_response(response, "swedish_translation")

    return translation

def get_tts(written_number, subscription_key):
    """Gets a link to TTS file from the cloud middleware service."""
    request = create_request("written-number", written_number, "subscription-key", subscription_key)

    print(request)

