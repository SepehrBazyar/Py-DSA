from typing import List

from ..decorators import process_timer


@process_timer
def bubble_sort(array: List[int]) -> List[int]:
    """
    ## Bubble Sort
    Bubble Sort is the simplest sorting algorithm that works by
    repeatedly swapping the adjacent elements if they are in the wrong order.

    Time Complexity: `O(N^2)`, The worst case occurs when an array is reverse sorted.
    Auxiliary Space: `O(1)`, bubble sort is an in-place sorting algorithm.

    :param array: list of integer numbers that we want sort
    :type array: list[int]
    :return: list of sorted integer number with bubble sort algorithm
    :rtype: list[int]
    """
    length = len(array)
    for counter in range(length - 1):
        bubble_flag: bool = False
        for index in range(length - counter - 1):
            if array[index] > array[index + 1]:
                array[index], array[index + 1] = array[index + 1], array[index]  # swap
                bubble_flag = True

        if not bubble_flag:
            return array

    return array
