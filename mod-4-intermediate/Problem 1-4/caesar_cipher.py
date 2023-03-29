def caesar_cipher(message, shift):
    # Converts the message to uppercase
    message = message.upper()

    encrypted_message = []
    new_shift = shift % 26
    for letter in message:
        encrypted_message.append(getNewMessage(letter, new_shift))

    return ''.join(encrypted_message)


def getNewMessage(message, shift):
    new_message = ord(message) + shift
    return chr(new_message) if new_message <= 122 else chr(96 + new_message % 122)


print(caesar_cipher('Word', 0))
