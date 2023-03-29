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


shifted_letter = shift_letter('A', 1)
print(shifted_letter)  # prints the output
