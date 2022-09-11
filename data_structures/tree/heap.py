import heapq
from abc import ABC, abstractmethod


class _AbstractHeap(ABC):
    """
    # Heap
    It's a complete tree (All levels are completely filled except possibly
    the last level and the last level has all keys as left as possible).
    This property of Binary Heap makes them suitable to be stored in an array.

    ## Time Complexity:
        * Get: `O(1)`
        * Insert: `O(log(n))`
        * Deletion: `O(log(n))`

    ## Auxiliary Space: `O(n)`
    """
    def __init__(self, *args: int, build_down: bool = True):
        """
        Initialize a new instance of a heap with the integer values.

        :param build_down: set bubble function builder, defaults to True
        :type build_down: bool, optional
        """
        self.__heap, self.__count = list(args), len(args)
        if build_down:
            bubble_func, indexes = self.bubble_down, range(self.__count - 1, -1, -1)
        else:
            bubble_func, indexes = self.bubble_up, range(self.__count)

        for index in indexes:
            bubble_func(index=index)

    def insert(self, item: int):
        """
        Insert new integer value inserted into the heap.

        :param item: new integer item value to inserted
        :type item: int
        """
        self.__heap.append(item)
        self.bubble_up(index=self.__count)
        self.__count += 1

    def delete(self) -> int:
        """
        Delete the top head node in the heap and returned value.

        :return: integer value of the top head node
        :rtype: int
        """
        if self.is_empty:
            raise Exception("Heap is empty.")

        result = self.__heap[0]
        self.__heap[0] = self.__heap[-1]
        self.__heap.pop()
        self.__count -= 1
        self.bubble_down(index=1)
        return result

    @staticmethod
    def parent(index: int) -> int:
        """
        Static method utility to returns the parent node index.

        :param index: index of current node
        :type index: int
        :return: index of parent node
        :rtype: int
        """
        return (index - 1) // 2

    @staticmethod
    def left_child(index: int) -> int:
        """
        Static method utility to returns the left child node index.

        :param index: index of current node
        :type index: int
        :return: index of left child node
        :rtype: int
        """
        return 2 * index + 1

    @staticmethod
    def right_child(index: int) -> int:
        """
        Static method utility to returns the right child node index.

        :param index: index of current node
        :type index: int
        :return: index of right child node
        :rtype: int
        """
        return 2 * index + 2

    @abstractmethod
    def bubble_up(self, index: int):
        pass

    @abstractmethod
    def bubble_down(self, index: int):
        pass

    @property
    def top(self) -> int:
        """
        Get Top Node in the heap Min or Max.

        :return: top of heap node minimum or maximum
        :rtype: int
        """
        if self.is_empty:
            raise Exception("Heap is empty.")

        return self.__heap[0]

    @property
    def is_empty(self) -> bool:
        """
        Boolean indicating whether the heap is empty.

        :return: flag to check if heap is empty
        :rtype: bool
        """
        return self.__count == 0

    def __len__(self) -> int:
        """
        Return the length of the heap.

        :return: number of element items in the heap.
        :rtype: int
        """
        return self.__count

    def __repr__(self) -> str:
        """
        Representation the heap as a string.

        :return: representation string
        :rtype: str
        """
        return ", ".join(str(item) for item in self.__heap)


class MinHeap(_AbstractHeap):
    """
    _summary_
    """
    pass


class MaxHeap(_AbstractHeap):
    """
    _summary_
    """
    pass
