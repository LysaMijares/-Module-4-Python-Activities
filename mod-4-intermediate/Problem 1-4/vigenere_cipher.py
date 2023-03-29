alphabet = "abcdefghijklmnopqrstuvwxyz"

letter_to_index = dict(zip(alphabet, range(len(alphabet))))
index_to_letter = dict(zip(range(len(alphabet)), alphabet))


def vigenere_cipher(message, key):
    encrypted = ""
    split_message = [
        message[i: i + len(key)] for i in range(0, len(message), len(key))
    ]

    for each_split in split_message:
        i = 0
        for letter in each_split:
            number = (letter_to_index[letter] + letter_to_index[key[i]]) % len(alphabet)
            encrypted += index_to_letter[number]
            i += 1

    return encrypted


def result():
    message = input("Enter the message here: ".upper())
    key = "funcooding"
    encrypted_message = vigenere_cipher(message, key)
    # prints the original message and the encrypted message, the cipher depends on the value of key
    print("Original message: " + message.upper().strip())
    print("Encrypted message: " + encrypted_message.upper().strip())


result()
