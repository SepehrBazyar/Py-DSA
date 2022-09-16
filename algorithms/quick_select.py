from random import randint
from typing import List


def quick_select(k: int, /, array: List[int]) -> int:
    """
    Quick Select is a selection algorithm to find the `k-th` smallest element
    in an unordered list. It is related to the quick sort sorting algorithm.

    The algorithm is similar to QuickSort.
    The difference is, instead of recurring for both sides (after finding pivot),
    it recurs only for the part that contains the `k-th` smallest element.
    The logic is simple, if index of the partitioned element is more than `k`,
    then we recur for the left part. If index is the same as `k`,
    we have found the `k-th` smallest element and we return.
    If index is less than `k`, then we recur for the right part.
    This reduces the expected complexity from `O(n*(log n))` to `O(n)`,
    with a worst-case of `O(n^2)`.

    :raises ValueError: if the `k-th` number not valid between 1 and length array
    :param k: integer number to find the `k-th` smallest element
    :type k: int
    :param array: list of integer numbers that to selected `k-th` smallest element
    :type array: list[int]
    :return: integer value of `k-th` smallest element
    :rtype: int
    """
    length = len(array)
    if not 0 < k <= length:
        raise ValueError("K-th Must be between one and length of array.")

    pivot = partition(array, start=0, end=length - 1)
    if k - 1 < pivot:
        return quick_select(k, array=array[:pivot])
    elif k - 1 > pivot:
        return quick_select(k - (pivot + 1), array=array[pivot + 1:])

    return array[pivot]  # base case


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
