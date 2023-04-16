from request_processor import create_image_request, make_get_request, get_data_from_response

def get_number_recognition(image, api_url):
    """Returns prediction and confidence level of what number is written in the image via call to the digit recognition service.
    """
    request_body = create_image_request("image-base64", image)
    response = make_get_request(api_url, request_body)

    return response