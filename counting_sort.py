from collections import Counter
from typing import List, Tuple
from functools import reduce


def minimum_maximum(accumulator: Tuple[int, int], element: int) -> Tuple[int, int]:
    """Used in reduce function to find minimum and maximum number in one loop.

    :param accumulator: tuple of minimum and maximum number
    :type accumulator: tuple[int, int]
    :param element: an integer number to compare with min and max
    :type element: int
    :return: returned the tuple of two integer number min and max
    :rtype: tuple[int, int]
    """
    minimum, maximum = accumulator
    return (
        element if element < minimum else minimum,
        element if element > maximum else maximum,
    )


def counting_sort(*args: int) -> List[int]:
    """_summary_

    :return: list of sorted integer number with counting sort algorithm
    :rtype: list[int]
    """
    minimum, maximum = reduce(minimum_maximum, args, (args[0], args[0]))
    counter = {i: 0 for i in range(minimum, maximum + 1)}  # dictionary comprehension
    counter.update(Counter(args))

    result = []
    for key, value in counter.items():
        result += [key] * value
    return result
