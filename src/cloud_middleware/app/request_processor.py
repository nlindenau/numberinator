from flask import request

def get_written_number(user_request):
    """Retruns written number from the incoming request.
    """
    user_number = user_request['written-number']

    return user_number

def get_user_number(user_request):
    """Returns the number to be processed from the incoming request.
    """
    user_number = user_request['number']
    user_number = int(user_number)

    return user_number

def get_azure_subscription_key(user_request):
    """Retruns Azure subscription key from the incoming request.
    """
    subscription_key = user_request['subscription-key']

    return subscription_key
