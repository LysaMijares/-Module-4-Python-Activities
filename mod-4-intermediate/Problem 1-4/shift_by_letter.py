def shift_by_letter(letter, letter_shift):
    letter = str(input("Please Enter a Letter: "))
    letter_shift = str(input("Please Enter a new Letter to shift on: "))

    # Capitalizes the letter
    letter = letter.upper()
    letter_shift = letter_shift.upper()

    letter_value = ord(letter) - ord('A')
    number_shift = ord(letter_shift) - ord('A')

    shifted_value = (letter_value + number_shift) % 26

    shifted_letter = chr(shifted_value + ord('A'))
    return shifted_letter, shifted_value


shifted_letter, shifted_value = shift_by_letter('', '')
print(shifted_letter, shifted_value)  # Output: 'F', 5

