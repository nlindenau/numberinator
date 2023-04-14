from dummy_values import numbers_sv, TTS_file

user_number = int(input("What number would you like to be translated? "))

number_translation = numbers_sv[user_number]

print(f"Your TTS file for {user_number} in English: {TTS_file}")
print(f"{user_number} is {number_translation} in Swedish.")