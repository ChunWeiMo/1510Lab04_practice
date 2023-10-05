def shift_capital_letter(letter, shift):
    # print("letter= ", letter)
    # print("shift= ", shift)
    letter += shift
    if letter > 90:
        letter = letter - 26
    elif letter < 65:
        letter = letter + 26
    # print("letter after shift", letter)
    return letter


def shift_lower_letter(letter, shift):
    # print("letter= ", letter)
    # print("shift= ", shift)
    letter += shift
    if letter > 122:
        letter = letter - 26
    elif letter < 97:
        letter = letter + 26
    # print("letter after shift", letter)
    return letter


def caesarcipher(message, encode, shift):
    """
    Convert a base 10 number to destination bass.

    :param message:
    :param encode:
    :param shift: 
    :precondition: 
    :postcondition: 
    :return: a integer
    """
    message_after_cipher = ""

    # decode
    if encode == False:
        shift *= -1

    for character in message:
        print(character)
        character = ord(character)
        print(character)
        # ASCII code A ~ Z : 65 ~ 90
        # # ASCII code a ~ z : 97 ~ 122
        if character >= 65 and character <= 90:
            print("into capital case")
            encoded_character = shift_capital_letter(character, shift)
        elif character >= 97 and character <= 122:
            print("into lower case")
            encoded_character = shift_lower_letter(character, shift)
        else:
            encoded_character = character

        message_after_cipher += chr(encoded_character)

    return message_after_cipher


def main():
    print(caesarcipher("catCAT", True, 2))


if __name__ == "__main__":
    main()
