from typing import Optional, List

from ..decorators import process_timer
from ..quick_select import partition


@process_timer
def quick_sort(
    array: List[int],
    *,
    start: int = 0,
    end: Optional[int] = None,
) -> List[int]:
    """
    ## Quick Sort
    Like Merge Sort, QuickSort is a Divide and Conquer algorithm.
    it picks an element as a pivot and partitions given array around the picked pivot.
    There are many different versions of quickSort that pick pivot in different ways:

    1. Always pick the first element as a pivot.
    2. Always pick the last element as a pivot (implemented below)
    3. Pick a random element as a pivot.
    4. Pick median as the pivot.

    The key process in quicks ort is a `partition()` function.

    ### Time Complexity:
        - Worst case time complexity is `O(n^2)`
        - Average case time complexity is `O(n*log(n))`

    ### Auxiliary Space: `O(1)`

    :param array: list of integer numbers that we want sort
    :type array: list[int]
    :param start: start point of the array in left direction, defaults to 0
    :type start: int
    :param end: end point of the array in right direction, defaults to None
    :type end: int, optional
    :return: list of sorted integer number with quick sort algorithm
    :rtype: list[int]
    """
    length = len(array)
    end = length - 1 if end is None else end
    if length == 1 or end <= start:
        return array

    pivot = partition(array, start=start, end=end)
    quick_sort(array, start=start, end=pivot - 1)
    quick_sort(array, start=pivot + 1, end=end)
    return array
