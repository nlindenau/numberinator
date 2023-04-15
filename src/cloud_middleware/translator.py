from cloud_middleware.dummy_values import numbers_sv

def get_number_translation_sv(raw_number):
    user_number = int(raw_number)
    number_translation = numbers_sv[user_number]
    return number_translation