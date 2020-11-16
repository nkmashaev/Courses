from typing import List


def fizzbuzz(n: int) -> List[str]:
    """
    fizzbuzz function takes a number N as an input and
    returns N FizzBuzz numbers

    :param n: size of fizz buzz sequence list
    :return: fizz buzz list

    >>> fizzbuzz(5)
    ['1', '2', 'Fizz', '4', 'Buzz']
    >>> fizzbuzz(15)
    ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz']
    >>> fizzbuzz(1.3)
    Traceback (most recent call last):
        ...
    ValueError: Error: Expected integer number!

    """

    if not isinstance(n, int):
        raise ValueError("Error: Expected integer number!")

    def numb_to_fizzbuzz(n: int):
        fizzbuzz_str = ""
        if n % 3 == 0:
            fizzbuzz_str += "Fizz"
        if n % 5 == 0:
            fizzbuzz_str += "Buzz"
        if len(fizzbuzz_str) == 0:
            return str(n)
        return fizzbuzz_str

    return [numb_to_fizzbuzz(i) for i in range(1, n + 1)]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
