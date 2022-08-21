from typing import List, Tuple

from ..decorators import process_timer


@process_timer
def merge_sort(array: List[int]) -> List[int]:
    """
    ## Merge Sort
    Merge Sort is a Divide and Conquer algorithm. It divides input array in two halves,
    calls itself for the two halves and then merges the two sorted halves.

    Time Complexity: `O(n*log(n))`
        Is a recursive algorithm; always divides the array into two halves
        and takes linear time to merge two halves.
    Auxiliary Space: `O(n)`
        * In merge sort all elements are copied into an auxiliary array .
        * so N auxiliary space is required for merge sort.

    :param array: list of integer numbers that we want sort
    :type array: list[int]
    :return: list of sorted integer number with merge sort algorithm
    :rtype: list[int]
    """
    length = len(array)
    if length <= 1:  # base case
        return array

    middle = length // 2
    return merge_arrays(
        one=(merge_sort(array[:middle]), middle),
        two=(merge_sort(array[middle:]), length - middle),
    )


def merge_arrays(one: Tuple[List[int], int], two: Tuple[List[int], int]) -> List[int]:
    """Used for merging two halves; merges the two sorted sub-arrays into one.

    :param first: a tuple of sub-array and length of array
    :type first: tuple[list[int], int]
    :param second: a tuple of sub-array and length of array
    :type second: tuple[list[int], int]
    :return: returned the one array merged of two this array
    :rtype: list[int]
    """
    result, i, j = [], 0, 0
    while i < one[1] and j < two[1]:
        if one[0][i] < two[0][j]:
            result.append(one[0][i])
            i += 1
        else:
            result.append(two[0][j])
            j += 1

    return result + one[0][i:] + two[0][j:]
