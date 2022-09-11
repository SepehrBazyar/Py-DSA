from typing import List

from data_structures import MinHeap, MaxHeap
from ..decorators import process_timer


@process_timer
def heap_sort(array: List[int], reverse: bool = False) -> List[int]:
    """
    ## Heap Sort
    Is a comparison-based sorting technique based on a Binary Heap data structure.
    It is similar to selection sort where we first find the maximum element
    and place the maximum element at the end.
    We repeat the same process for the remaining element.

    ### Time Complexity: `O(n*log(n))`
        - The time complexity of heapify is `O(log(n))`.
        - Time complexity of Build Heap is `O(n)`.
        - And, hence the overall time complexity of Heap Sort is `O(n*log(n))`.

    ### Auxiliary Space: `O(n)`

    :param array: list of integer numbers that we want sort
    :type array: list[int]
    :param reverse: set reverse or normal sorting, defaults to False
    :type reverse: bool, optional
    :return: list of sorted integer number with heap sort algorithm
    :rtype: list[int]
    """
    Heap = MaxHeap if reverse else MinHeap
    heap, length = Heap(*array), len(array)

    result: List[int] = [None] * length
    for i in range(length):
        result[i] = heap.delete()

    return result
