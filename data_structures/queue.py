from collections import deque
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
        Initialize the queue list with front and rear pointers.

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

        :raises UnderflowError: If the queue is empty, then it's Underflow exception
        :return: the value to be popped
        :rtype: int
        """
        if self.__number == 0:
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
        if self.__number >= self.__length:
            raise OverflowError("Queue is full.")

        self.__queue[(self.__number + self.__first) % self.__length] = value
        self.__number += 1

    def __repr__(self) -> str:
        """
        Representation the queue list.

        :return: representation string
        :rtype: str
        """
        items = []
        for index in range(self.__number):
            items.append(str(self.__queue[(index + self.__first) % self.__length]))

        return f"-> _ {' | '.join(reversed(items))} ->"
