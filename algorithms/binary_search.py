from typing import Optional, List


def binary_search(
    item: int,
    array: List[int],
    *,
    start: Optional[int] = None,
    end: Optional[int] = None,
) -> int:
    """
    Given a sorted array of n integers, return the index of item in the array.
    `Linear Search`: simple approach is a linear search; The time complexity is `O(n)`\n
    `Binary Search`: is a searching algorithm used in a sorted array
    by repeatedly dividing the search interval in half.
    The idea of binary search is to use the information that the array is sorted and
    reduce the time complexity to `O(log(n))`.
    :raises ValueError: if item isn't present in the array
    :param item: an integer value to search for binary search
    :type item: int
    :param array: array of sorted integers to search for binary searching
    :type array: list[int]
    :param start: start point of array index, defaults to None
    :type start: Optional[int], optional
    :param end: end point of array index, defaults to None
    :type end: Optional[int], optional
    :return: index of item in array
    :rtype: int
    """
    start = start if start is not None else 0
    end = end if end is not None else len(array)
    if start > end:
        raise ValueError("Item isn't present in the array.")

    middle = (start + end) // 2
    if array[middle] < item:
        return binary_search(item=item, array=array, start=middle + 1, end=end)
    elif array[middle] > item:
        return binary_search(item=item, array=array, start=start, end=middle - 1)

    return middle  # base case
