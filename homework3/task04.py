def is_armstrong(number: int) -> bool:
    """
    Define is the number is Armstrong one

    :param number: number to check
    :return: True if number is Armstrong else false
    """
    digit_list = [int(x) for x in str(number)]
    n = len(digit_list)
    armstrong_sum = sum([x ** n for x in digit_list])
    return armstrong_sum == number
