from typing import List


def selection_sort(array: List[int]) -> List[int]:
    """
    ## Selection Sort
    The selection sort algorithm sorts an array by repeatedly finding the minimum item
    from unsorted part and putting it at the beginning.

    Time Complexity: `O(N^2)`, The time complexity is O(N2) as there are 2 nested loops:
        * One loop to select an element of Array one by one: `O(N)`
        * Another loop to compare that element with every other Array element: `O(N)`

    Therefore overall complexity = `O(N)` *` O(N)` = `O(N*N)` = `O(N^2)`

    Auxiliary Space: `O(1)`, selection sort is an in-place sorting algorithm.

    :param array: list of integer numbers that we want sort
    :type array: list[int]
    :return: list of sorted integer number with selection sort algorithm
    :rtype: list[int]
    """
    length = len(array)
    for counter in range(length - 1):
        selected = counter
        for index, element in enumerate(array[counter + 1 :], start=counter + 1):
            if element < array[selected]:
                selected = index

        array[counter], array[selected] = array[selected], array[counter]

    return array
