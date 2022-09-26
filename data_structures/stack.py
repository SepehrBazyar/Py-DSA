from collections import deque  # noqa: F401
from typing import Optional, List

from exceptions import UnderflowError


class Stack:
    """
    # Stack
    A stack is a linear data structure that stores items in a Last-In/First-Out `(LIFO)`
    or First-In/Last-Out `(FILO)` manner.
    A new element is added at one end and an element is removed from that end only.
    """

    def __init__(self, length: int):
        """
        Initialize the stack list with a number pointer.

        :param length: the maximum length size of this queue
        :type length: int
        """
        self.__length, self.__number = length, 0
        self.__stack: List[Optional[int]] = [None for _ in range(self.__length)]

    def pop(self) -> int:
        """
        Deletes the topmost element of the stack.
        Time Complexity: `O(1)`

        :raises UnderflowError: if the stack is empty, then it's Underflow exception
        :return: the value to be popped
        :rtype: int
        """
        if self.is_empty:
            raise UnderflowError("Stack is empty.")

        self.__number -= 1
        return self.__stack[self.__number]

    def push(self, value: int):
        """
        Inserts the element at the top of the stack.
        Time Complexity: `O(1)`

        :raises OverflowError: if the stack is full, then it's Overflow exception
        :param value: the value to be pushed
        :type value: int
        """
        if self.is_full:
            raise OverflowError("Stack Overflow.")

        self.__stack[self.__number] = value
        self.__number += 1

    @property
    def size(self) -> int:
        """
        The number size of stack elements.

        :return: the stack size number
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
    def top(self) -> int:
        """
        Topmost element of the stack

        :raises UnderflowError: If the stack is empty
        :return: top integer in stack
        :rtype: int
        """
        if self.is_empty:
            raise UnderflowError("Queue is empty.")

        return self.__stack[self.__number - 1]

    @property
    def is_empty(self) -> bool:
        """
        Boolean indicating whether the stack is empty.

        :return: flag to check if stack is empty
        :rtype: bool
        """
        return self.__number == 0

    @property
    def is_full(self) -> bool:
        """
        Boolean indicating whether the stack is full.

        :return: flag to check if stack is full
        :rtype: bool
        """
        return self.__number == self.__length

    def __repr__(self) -> str:
        """
        Representation the stack list.

        :return: representation string
        :rtype: str
        """
        items = (str(elem) for elem in self.__stack[: self.__number])
        return f"{' | '.join(items)} <=>"
