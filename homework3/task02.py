import hashlib
import random
import struct
import time
from functools import reduce
from multiprocessing import Pool
from typing import Tuple


def slow_calculate(value: int) -> int:
    """Some weird voodoo magic calculations"""
    time.sleep(random.randint(1, 3))
    data = hashlib.md5(str(value).encode()).digest()
    return sum(struct.unpack("<" + "B" * len(data), data))


def perform_calculate(
    start: int = 0, end: int = 500, step: int = 1
) -> Tuple[float, int]:
    """
    Designed to fast compute a sum of large number of
    function "slow_calculate" calls result

    :param start: first value of argument
    :param end: last value of argument(not included in range)
    :param step: increment
    :return: elapsed time and total sum
    """
    init_list = [i for i in range(start, end, step)]
    time_start = time.time()
    with Pool(end - start) as p:
        init_list = p.map(slow_calculate, init_list)
    time_end = time.time()
    total_sum = reduce(lambda x, y: x + y, init_list)

    elapsed = time_end - time_start
    return elapsed, total_sum
