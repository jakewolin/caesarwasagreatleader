def shift(letter, shift_amount):
    unicode_value=ord(letter)+shift_amount\
                   
    new_letter=chr(unicode_value)
    return new_letter

def encrypt(message, shift_amount):
    result=""

    for letter in message:
        result+=shift(letter, shift_amount)
    return result


def decrypt(message, shift_amount):
    result=""

    for letter in message:
        result+=shift(letter, -shift_amount)
    return result

secret_message = "encryption is fun"
encrypted_message = encrypt(secret_message, 3)
decrypted_message = decrypt(encrypted_message, 3)
print(secret_message)
print(encrypted_message)
print(decrypted_message)


