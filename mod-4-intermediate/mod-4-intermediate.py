'''Module 3: Individual Programming Assignment 1
Thinking Like a Programmer
This assignment covers your intermediate proficiency with Python.
'''


def shift_letter(letter, shift):
    '''Shift Letter. 
    4 points.

    Shift a letter right by the given number.
    Wrap the letter around if it reaches the end of the alphabet.
    Examples:
    shift_letter("A", 0) -> "A"
    shift_letter("A", 2) -> "C"
    shift_letter("Z", 1) -> "A"
    shift_letter("X", 5) -> "C"
    shift_letter(" ", _) -> " "
    *Note: the single underscore `_` is used to acknowledge the presence
        of a value without caring about its contents.
    Parameters
    ----------
    letter: str
        a single uppercase English letter, or a space.
    shift: int
        the number by which to shift the letter. 
    Returns
    -------
    str
        the letter, shifted appropriately, if a letter.
        a single space if the original letter was a space.
    '''

    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    def shift_letter(letter, shift):
        letter = str(input("Please Enter a Letter: "))
        shift = int(input("Please Enter the # of shift made: "))

        # Capitalizes the letter
        letter = letter.upper()

        # converts the letter to ascii code
        ascii_code = ord(letter)

        # shifts the letters to the right
        shift_code = ascii_code + shift

        # wraps around the alphabet
        if shift_code > ord("Z"):
            shift_code = shift_code - ord("z") + ord("A") - 1

        shifted_letter = chr(shift_code)
        return shifted_letter

    # converts shift letter to shift_letter's values
    shifted_letter = shift_letter('A', 1)
    print(shifted_letter)  # prints the output


def caesar_cipher(message, shift):
    '''Caesar Cipher. 
    6 points.

    Apply a shift number to a string of uppercase English letters and spaces.
    Parameters
    ----------
    message: str
        a string of uppercase English letters and spaces.
    shift: int
        the number by which to shift the letters. 
    Returns
    -------
    str
        the message, shifted appropriately.
    '''

    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    def caesar_cipher(message, shift):
        # Converts the message to uppercase
        message = message.upper()
        # carries string to encrypted_message
        encrypted_message = []
        # this loops the z back to a
        new_shift = shift % 26
        for letter in message:
            encrypted_message.append(getNewMessage(letter, new_shift))

        return ''.join(encrypted_message)

    def getNewMessage(message, shift):
        new_message = ord(message) + shift
        return chr(new_message) if new_message <= 122 else chr(96 + new_message % 122)

    # prints the caesar cipher coded word
    print(caesar_cipher('Word', 0))


def shift_by_letter(letter, letter_shift):
    '''Shift By Letter. 
    4 points.

    Shift a letter to the right using the number equivalent of another letter.
    The shift letter is any letter from A to Z, where A represents 0, B represents 1, 
        ..., Z represents 25.
    Examples:
    shift_by_letter("A", "A") -> "A"
    shift_by_letter("A", "C") -> "C"
    shift_by_letter("B", "K") -> "L"
    shift_by_letter(" ", _) -> " "
    Parameters
    ----------
    letter: str
        a single uppercase English letter, or a space.
    letter_shift: str
        a single uppercase English letter.
    Returns
    -------
    str
        the letter, shifted appropriately.
    '''

    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.

    def shift_by_letter(letter, letter_shift):
        letter = str(input("Please Enter a Letter: "))
        letter_shift = str(input("Please Enter a new Letter to shift on: "))

        # Capitalizes the letter
        letter = letter.upper()
        letter_shift = letter_shift.upper()

        letter_value = ord(letter) - ord('A')
        number_shift = ord(letter_shift) - ord('A')
        # the shifted_value is linked to process of addition by adding letter_value and number shift while using
        # modulus which loops the letters z back to a
        shifted_value = (letter_value + number_shift) % 26

        shifted_letter = chr(shifted_value + ord('A'))
        return shifted_letter, shifted_value

    shifted_letter, shifted_value = shift_by_letter('', '')
    # prints the shifted_letter
    print(shifted_letter, shifted_value)  # Output: 'F', 5


def vigenere_cipher(message, key):
    '''Vigenere Cipher. 
    6 points.

    Encrypts a message using a keyphrase instead of a static number.
    Every letter in the message is shifted by the number represented by the 
        respective letter in the key.
    Spaces should be ignored.
    Example:
    vigenere_cipher("A C", "KEY") -> "K A"
    If needed, the keyphrase is extended to match the length of the key.
        If the key is "KEY" and the message is "LONGTEXT",
        the key will be extended to be "KEYKEYKE".
    Parameters
    ----------
    message: str
        a string of uppercase English letters and spaces.
    key: str
        a string of uppercase English letters. Will never be longer than the message.
        Will never contain spaces.
    Returns
    -------
    str
        the message, shifted appropriately.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    # creates a string alphabet for the message
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    # utilizes dictionary and zips the value of the alphabet and its range while shifting the letter to index
    letter_to_index = dict(zip(alphabet, range(len(alphabet))))
    index_to_letter = dict(zip(range(len(alphabet)), alphabet))

    def vigenere_cipher(message, key):
        # carries string to encrypted
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

    # runs the program
    def result():
        # capitalizes the message
        message = input("Enter the message here: ".upper())
        # the number of shift made while utilizing key letters
        key = "funcooding"
        encrypted_message = vigenere_cipher(message, key)
        # prints the original message and the encrypted message, the cipher depends on the value of key
        print("Original message: " + message.upper().strip())
        print("Encrypted message: " + encrypted_message.upper().strip())

    result()
