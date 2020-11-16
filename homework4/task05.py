def fizzbuzz(n: int):
    """
    fizzbuzz function takes a number N as an input and returns a generator
    that yields N FizzBuzz numbers.

    :param int: size of fizzbuzz sequence
    :return: generator of fizzbuzz sequence
    :raise: ValueError
    """

    if not isinstance(n, int):
        raise ValueError("Error: Expected integer number!")
    fizzbuzz_dict = {}
    last_el = n + 1
    for i in range(3, last_el, 3):
        fizzbuzz_dict[i] = "Fizz"
    for i in range(5, last_el, 5):
        fizzbuzz_dict[i] = fizzbuzz_dict.get(i, "") + "Buzz"
    for i in range(1, last_el):
        yield fizzbuzz_dict.get(i, str(i))
