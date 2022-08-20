from typing import List, Callable
from string import ascii_lowercase

from insertion_sort import insertion_sort


def bucket_sort(
    array: List[str],
    *,
    function: Callable[[list], list] = insertion_sort,
) -> List[str]:
    """
    ## Bucket Sort
    Bucket sort is mainly useful when input is uniformly distributed over a range.

    `Counting Sort` can not be applied here as we use keys as index in counting sort;
    Here keys are floating point numbers.  

    :param array: list of string characters that we want sort
    :type array: list[str]
    :param function: keyword argument sorting function, defaults to insertion_sort
    :type function: Callable[[list], list], optional
    :return: list of sorted string characters with bucket sort algorithm
    :rtype: list[str]
    """
    buckets = {char: [] for char in ascii_lowercase}  # dictionary comprehension
    for element in array:
        buckets[element[0]].append(element)

    result = []
    for bucket in buckets.values():
        result += function(bucket)

    return result
