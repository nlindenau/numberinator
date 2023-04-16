import requests

def create_request(key_1, value_1, key_2, value_2):
    """Creates a request body for cloud middleware service.
    """
    request_body = {
        key_1: value_1,
        key_2: value_2,
    }

    return request_body

def get_data_from_response(response, searched_data):
    """Returns data under a given key from a raw request.
    """
    response_contents = response.json()
    value = response_contents[searched_data]

    return value

def make_get_request(api_url, request_body):
    """Returns result of a GET call.
    """
    response = requests.get(api_url, json=request_body)
    return response

