def base_convert(base_10_number, destination_base):
    """
    Convert a base 10 number to destination bass.

    :param base_10_number: an integer >= 0
    :param destination_base: a positive integer [2,10]
    :precondition: 
    :postcondition: 
    :return: a integer
    """
    converted_number = ""
    while (base_10_number != 0):
        digit_to_concatenate = base_10_number % destination_base
        converted_number = str(digit_to_concatenate) + converted_number
        base_10_number //= destination_base
    
    return int(converted_number)

if __name__ == "__main__":
    print(base_convert(9487,7))
 