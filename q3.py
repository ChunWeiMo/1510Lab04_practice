def shift_uppercase_letter(uppercase_letter, shift):
    """
    Return a uppercase letter after a unicode shift.

    :param uppercase_letter: a string 
    :param shift: an integer
    :precondition: uppercase_letter must be a single character and a uppercase letter
    :precondition: shift can be a positive or negative integer
    :postcondition: find the uppercase letter after the Unicode shift
    :return: a shifted uppercase letter

    >>> shift_uppercase_letter("Z", 3)
    "C"
    >>> shift_uppercase_letter("D", -2)
    "B"
    """
    uppercase_letter = ord(uppercase_letter)
    uppercase_letter += shift
    if uppercase_letter > 90:
        uppercase_letter -= - 26
    elif uppercase_letter < 65:
        uppercase_letter += 26
    return chr(uppercase_letter)


def shift_lowercase_letter(lowercase_letter, shift):
    """
    Return a lowercase letter after a unicode shift.

    :param lowercase_letter: a string
    :param shift: an integer
    :precondition: lowercase_letter must be a single character and a lowercase letter
    :precondition: shift can be a positive or negative integer
    :postcondition: find the lowercase letter after the Unicode shift
    :return: a shifted lowercase letter

    >>> shift_lowercase_letter("c", 3)
    "f"
    >>> shift_lowercase_letter("a", -2)
    "y"
    """
    lowercase_letter = ord(lowercase_letter)
    lowercase_letter += shift
    if lowercase_letter > 122:
        lowercase_letter -= 26
    elif lowercase_letter < 97:
        lowercase_letter += 26
    return chr(lowercase_letter)


def caesarcipher(message, encode, shift):
    """
    Encode or discover a message.

    A function encodes or discovers a message through a Unicode shift.

    :param message: a string
    :param encode: a boolean
    :param shift: an integer
    :precondition: message may be empty
    :precondition: encode must be True or False
    :precondition: shift can be a positive or negative integer
    :postcondition: encode or discover message through the Unicode shift
    :return: encoded or discovered message

    >>>caesarcipher("Chris", True, 2)
    "Ejtku"
    >>>caesarcipher("cat", True, 7)
    "jha"
    >>>caesarcipher("cat", True, -2)
    "ayr"
    """

    message_after_cipher = ""

    # decode
    if encode == False:
        shift *= -1

    for character in message:
        # Unicode A ~ Z : 65 ~ 90
        # Unicode a ~ z : 97 ~ 122
        if ord(character) >= 65 and ord(character) <= 90:
            encoded_character = shift_uppercase_letter(character, shift)
        elif ord(character) >= 97 and ord(character) <= 122:
            encoded_character = shift_lowercase_letter(character, shift)
        else:
            encoded_character = character

        message_after_cipher += encoded_character

    return message_after_cipher


def main():
    print(caesarcipher("cat", True, 7))
    print(caesarcipher("CAT", True, -2))
    print(caesarcipher("F-Z, Pr", False, 3))


if __name__ == "__main__":
    main()
