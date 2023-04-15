def create_request(key_1, value_1, key_2, value_2):
    """Creates a request body for cloud middleware service."""
    request_body = {
        key_1 : value_1,
        key_2 : value_2,
    }

    return request_body

def get_translations(user_number, subscription_key):
    """Gets translations from the cloud middleware service."""

    request = create_request("number", user_number, "subscription-key", subscription_key)

    print(request)

def get_tts(written_number, subscription_key):
    """Gets a link to TTS file from the cloud middleware service."""

    request = create_request("written-number", written_number, "subscription-key", subscription_key)

    print(request)

