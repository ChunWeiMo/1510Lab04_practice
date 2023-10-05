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
        encoded_character = ord(character)
        # ASCII code A ~ Z : 65 ~ 90
        if encoded_character >= 65 and encoded_character <= 90:
            print("into capital case")
            encoded_character += shift
            if encoded_character > 90:
                encoded_character = encoded_character - 26
            elif encoded_character <65:
                encoded_character = encoded_character + 26
        
        #            a ~ z : 97 ~ 122
        elif encoded_character >= 97 and encoded_character <= 122:
            print("into lower case")
            encoded_character += shift
            if encoded_character > 122:
                encoded_character = encoded_character - 26
            elif encoded_character < 97:
                encoded_character = encoded_character + 26

        message_after_cipher += chr(encoded_character)
            
    return message_after_cipher


def main():
    print(caesarcipher("cAt", False, 2))

if __name__ == "__main__":
    main()
    # print(ord("a"))
