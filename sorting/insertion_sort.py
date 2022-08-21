from typing import List

from ..decorators import process_timer


@process_timer
def insertion_sort(array: List[int]) -> List[int]:
    """
    ## Insertion Sort
    Insertion sort is used when number of elements is small.

    It can also be useful when input array is almost sorted,
    only few elements are misplaced in complete big array.

    Time Complexity: `O(N^2)`, If items are reverse order, worst case complexity occurs.
    Auxiliary Space: `O(1)`, insertion sort is an in-place sorting algorithm.

    :param array: list of integer numbers that we want sort
    :type array: list[int]
    :return: list of sorted integer number with insertion sort algorithm
    :rtype: list[int]
    """
    for index, item in enumerate(array[1:], start=1):
        while 0 < index and item < array[index - 1]:
            array[index] = array[index - 1]
            index -= 1

        array[index] = item

    return array
