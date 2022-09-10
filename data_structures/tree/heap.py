import heapq
from abc import ABC, abstractmethod
from typing import List


class _AbstractHeap(ABC):
    """
    _summary_
    """
    def __init__(self):
        """Initialize the empty heap."""
        self.__count: int = 0
        self.__heap: List[int] = []

    def parent(self, index: int) -> int:
        """
        Returns the parent node index.

        :param index: index of current node
        :type index: int
        :return: index of parent node
        :rtype: int
        """
        return (index - 1) // 2

    @abstractmethod
    def bubble_up(self, index: int):
        pass

    @abstractmethod
    def bubble_down(self, index: int):
        pass

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
