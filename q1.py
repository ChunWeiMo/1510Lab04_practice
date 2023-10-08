def prime(number):
    """
    Check prime number.

    A simple function that check if a positive integer is prime.

    :param number: a positive integer
    :precondition: number must be a positive integer greater than 1
    :postcondition: check number
    :return: a boolean 
    """

    divisor = 2
    if number == 1:
        is_prime = False
    elif number == 2:
        is_prime = True
    else:
        while divisor < number:
            if number % divisor == 0:
                is_prime = False
                break
            else:
                is_prime = True
            divisor += 1

    return is_prime


def main():
    print(prime(53))


if __name__ == "__main__":
    main()
