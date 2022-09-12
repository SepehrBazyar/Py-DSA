from random import randint
from typing import Optional, List

from ..decorators import process_timer


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


def partition(array: List[int], *, start: int, end: int) -> int:
    """
    The target of partitions is, given an array and an element x of an array as pivot,
    put x at its correct position in a sorted array:

        1- and put all smaller elements (smaller than x) before x,\n
        2- and put all greater elements (greater than x) after x.

    All this should be done in linear time.

    :param array: list of integer numbers that we want applied pivot partition
    :type array: list[int]
    :param start: start point of the array in left direction
    :type start: int
    :param end: end point of the array in right direction
    :type end: int
    :return: index of the array pivot point into the array
    :rtype: int
    """
    random = randint(start, end)
    array[random], array[end] = array[end], array[random]  # swap random pivot

    pivot, left, right = array[end], start, end - 1
    while left <= right:
        while left < end and array[left] <= pivot:
            left += 1
        while right >= start and array[right] > pivot:
            right -= 1

        if left < right:
            array[left], array[right] = array[right], array[left]  # swap bubble

    array[left], array[end] = array[end], array[left]  # swap pivot
    return left
