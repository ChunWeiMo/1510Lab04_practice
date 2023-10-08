def shift_capital_letter_unicode(letter, shift):
    """
    >>> shift_capital_letter(78, 3)
    81
    >>> shift_capital_letter(89, 10)
    73
    """
    letter += shift
    if letter > 90:
        letter = letter - 26
    elif letter < 65:
        letter = letter + 26
    return letter


def shift_lower_letter_unicode(letter, shift):
    letter += shift
    if letter > 122:
        letter = letter - 26
    elif letter < 97:
        letter = letter + 26
    return letter


def caesarcipher(message, encode, shift):
    """
    Convert a base 10 number to destination bass.

    param message:
    param encode:
    param shift: 
    precondition: 
    postcondition: 
    return: a integer
    """
    message_after_cipher = ""

    # decode
    if encode == False:
        shift *= -1

    for character in message:
        character = ord(character)
        # unicode A ~ Z : 65 ~ 90
        # # unicode a ~ z : 97 ~ 122
        if character >= 65 and character <= 90:
            encoded_character = shift_capital_letter_unicode(character, shift)
        elif character >= 97 and character <= 122:
            encoded_character = shift_lower_letter_unicode(character, shift)
        else:
            encoded_character = character

        message_after_cipher += chr(encoded_character)

    return message_after_cipher


def main():
    print(caesarcipher("catCAT", True, 2))


if __name__ == "__main__":
    import doctest
    doctest.testmod()

    main()
