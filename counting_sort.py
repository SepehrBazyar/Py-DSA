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


def counting_sort(array: List[int]) -> List[int]:
    """
    ## Counting Sort
    Counting sort is efficient if the range of input data
    is not significantly greater than the number of objects to be sorted.

    for example the input sequence is between range 1 to 10 and the data is 1, 2, 5, 10.

    Time complexity: `O(n)`, where n is total number of elements
    Auxiliary Space: `O(n)`, It uses a temp array making it a non In Place algorithm.

    :param array: list of integer numbers that we want sort
    :type array: list[int]
    :return: list of sorted integer number with counting sort algorithm
    :rtype: list[int]
    """
    minimum, maximum = reduce(minimum_maximum, array, (array[0], array[0]))
    counter = {i: 0 for i in range(minimum, maximum + 1)}  # dictionary comprehension
    counter.update(Counter(array))

    result = []
    for key, value in counter.items():
        result += [key] * value
    return result
