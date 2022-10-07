from collections import deque  # noqa: F401
from typing import Optional, List

from exceptions import UnderflowError


class Queue:
    """
    # Queue
    Is a linear data structure that stores items in First In First Out `(FIFO)` manner;
    With a queue the least recently added item is removed first.
    """

    def __init__(self, length: int):
        """
        Initialize the queue list with fir and number pointers.

        :param length: the maximum length size of this queue
        :type length: int
        """
        self.__length, self.__first, self.__number = length, 0, 0
        self.__queue: List[Optional[int]] = [None for _ in range(self.__length)]

    def dequeue(self) -> int:
        """
        Removes an item from the queue;
        The items are popped in the same order in which they are pushed.
        Time Complexity: `O(1)`

        :raises UnderflowError: if the queue is empty, then it's Underflow exception
        :return: the value to be popped
        :rtype: int
        """
        if self.is_empty:
            raise UnderflowError("Queue is empty.")

        item, self.__queue[self.__first] = self.__queue[self.__first], None
        self.__first = (self.__first + 1) % self.__length
        self.__number -= 1
        return item

    def enqueue(self, value: int):
        """
        Adds an item to the queue.
        Time Complexity: `O(1)`

        :raises OverflowError: if the queue is full, then it's Overflow exception
        :param value: the value to be pushed
        :type value: int
        """
        if self.is_full:
            raise OverflowError("Queue is full.")

        self.__queue[(self.__first + self.__number) % self.__length] = value
        self.__number += 1

    @property
    def size(self) -> int:
        """
        The number size of queue elements.

        :return: the queue size number
        :rtype: int
        """
        return self.__number

    @property
    def length(self) -> int:
        """
        The maximum length of the queue.

        :return: the maximum size number
        :rtype: int
        """
        return self.__length

    @property
    def front(self) -> int:
        """
        First In item added to the queue.

        :raises UnderflowError: If the queue is empty
        :return: first integer into queue
        :rtype: int
        """
        if self.__number == 0:
            raise UnderflowError("Queue is empty.")

        return self.__queue[self.__first]

    @property
    def rear(self) -> int:
        """
        Last In item added to the queue.

        :raises UnderflowError: If the queue is empty
        :return: last integer into queue
        :rtype: int
        """
        if self.__number == 0:
            raise UnderflowError("Queue is empty.")

        return self.__queue[(self.__first + self.__number - 1) % self.__length]

    @property
    def is_empty(self) -> bool:
        """
        Boolean indicating whether the queue is empty.

        :return: flag to check if queue is empty
        :rtype: bool
        """
        return self.__number == 0

    @property
    def is_full(self) -> bool:
        """
        Boolean indicating whether the queue is full.

        :return: flag to check if queue is full
        :rtype: bool
        """
        return self.__number == self.__length

    def __repr__(self) -> str:  # pragma: no cover
        """
        Representation the queue list.

        :return: representation string
        :rtype: str
        """
        items = []
        for index in range(self.__number):
            items.append(str(self.__queue[(self.__first + index) % self.__length]))

        return f"-> _ {' | '.join(reversed(items))} ->"
