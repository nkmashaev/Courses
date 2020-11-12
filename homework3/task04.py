from functools import reduce


def is_armstrong(number: int) -> bool:
    digit_list = [int(x) for x in str(number)]
    n = len(digit_list)
    first_digit, digit_list[0] = digit_list[0], 0
    armstrong_sum = reduce(lambda x, y: x + y ** n, digit_list)
    armstrong_sum += first_digit ** n
    return armstrong_sum == number
