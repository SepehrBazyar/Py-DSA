from typing import Union, Sequence


class FenwickTree:
    """
    # Fenwick Tree (Binary Indexed Tree)
    We have an array `arr[0 . . . n-1]`. We would like to:

        1- Compute the sum of the first `i` elements.\n
        2- Modify the value of a specified element of the array `arr[i] = x`.

    A simple solution is to run a loop from `0` to `i-1` and
    calculate the sum of the elements. To update a value, simply do `arr[i] = x`.
    The first operation takes `O(n)` time and the second operation takes `O(1)` time.
    Another simple solution is to create an extra array and store the sum of the first
    `i-th` elements at the `i-th` index in this new array.
    The sum of a given range can now be calculated in `O(1)` time,
    but the update operation takes `O(n)` time now.
    This works well if there are a large number of query operations
    but a very few number of update operations.
    Could we perform both the query and update operations in `O(log(n))` time? 
    An alternative solution is Binary Indexed Tree, which also achieves `O(log(n))`
    time complexity for both operations.
    """
    def __init__(self, *args: int):
        """Initialize Fenwick Binary Indexed Tree with integer arguments"""
        self.__length = len(args)
        self.__fenwick = [0 for _ in range(self.__length + 1)]
        self.__make_tree(array=args)

    @staticmethod
    def __step(index: int) -> int:
        """
        Utility Method to Step for next index in Fenwick Tree.

        :param index: integer number of started index
        :type index: int
        :return: integer number of value to change index
        :rtype: int
        """
        return index & -index

    def __make_tree(self, array: Sequence[int]):
        """
        Private method to making fenwick tree with sequence of integers

        :param array: sequence of integer numbers to add in fenwick tree
        :type array: Sequence[int]
        """
        for index in range(self.__length):
            self.add(index=index + 1, value=array[index])

    def add(self, index: int, value: int):
        """
        Add & Update value of index item with value number.

        :param index: index number position of item in fenwick tree
        :type index: int
        :param value: value to change add on item in index
        :type value: int
        """
        while index <= self.__length:
            self.__fenwick[index] += value
            index += self.__step(index=index)

    def __getitem__(self, key: Union[int, slice]) -> int:
        """
        Get Sum of Items in key index or key ranges span.

        :param key: an positive integer or slice object range of numbers
        :type key: int | slice
        :return: sum of items in key
        :rtype: int
        """
        if isinstance(key, slice):
            return self[key.stop] - self[key.start - 1]

        result = 0
        while key > 0:
            result += self.__fenwick[key]
            key -= self.__step(index=key)

        return result

    def __len__(self) -> int:
        """
        Returned the Length of Fenwick Binary Indexed Tree.

        :return: integer number size of fenwick tree
        :rtype: int
        """
        return self.__length
