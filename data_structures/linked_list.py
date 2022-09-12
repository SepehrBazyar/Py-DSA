from dataclasses import dataclass, field
from typing import Optional, Callable


class LinkedList:
    """
    # Linked List
    Like arrays, Linked List is a linear data structure.
    Unlike arrays, linked list elements are not stored at a contiguous location;
    the elements are linked using pointers. They include a series of connected nodes.
    Here, each node stores the data and the address of the next node.
    ## Time Complexity:
        * Search: `O(n)`
        * Insert: `O(1)`
        * Deletion: `O(1)`

    ## Auxiliary Space: `O(n)`
    """
    def __init__(self, head: int):
        """
        Initialize the linked list with a list of nodes.

        :param head: head node data integer value of this linked list
        :type head: int
        """
        self.__head, self.__length = _Node(head), 1

    def insert(
        self,
        value: int,
        node: "_Node",
        *,
        after: bool = True,
    ) -> "_Node":
        """
        Insert a integer value into linked list.

        :param value: the data value to insert into the linked list
        :type value: int
        :param node: the node to be then insert this new value
        :type node: _Node
        :param after: flag to insert value after node or before, defaults to True
        :type after: bool, optional
        :return: node object of this new inserted value
        :rtype: _Node
        """
        self.__length += 1
        function: Callable[[int, "_Node"], "_Node"] = (
            self._insert_after if after else self._insert_before
        )
        return function(value=value, node=node)

    def delete(self, node: "_Node"):
        """
        Deletes a node from the linked list.

        :param node: node object to delete from linked list
        :type node: _Node
        """
        self.__length -= 1
        if node.previous is not None:
            node.previous.next = node.next

        if node.next is not None:
            node.next.previous = node.previous

    def search(self, value: int) -> Optional["_Node"]:
        """
        Search for a node integer value into linked list.

        :param value: value of node data to search into linked list
        :type value: int
        :return: node object of this value
        :rtype: _Node
        """
        node = self.__head
        while node is not None:
            if node.data == value:
                return node

            node = node.next

    @property
    def is_empty(self) -> bool:
        """
        Boolean indicating whether the linked list is empty.

        :return: flag to check if linked list is empty
        :rtype: bool
        """
        return self.__length == 0

    @property
    def head(self) -> "_Node":
        """
        Getter for the head of the linked list.

        :return: Node object of head of linked list
        :rtype: _Node
        """
        return self.__head

    @head.setter
    def head(self, node: "_Node"):
        """
        Setter for head of linked list.

        :param node: Node object to set head of linked list
        :type node: _Node
        :raises TypeError: if the node is not Node object
        """
        if not isinstance(node, _Node):
            raise TypeError("Node must be a node objects.")

        self.__head = node

    @staticmethod
    def _insert_after(value: int, node: "_Node") -> "_Node":
        """
        Utility protected method to insert a new node after a next node.

        :param value: the data value to insert into the linked list
        :type value: int
        :param node: the node to be then inserted after
        :type node: _Node
        :return: node object of this new inserted value
        :rtype: _Node
        """
        new = _Node(value, previous=node, next=node.next)
        node.next = new
        if new.next is not None:
            new.next.previous = new

        return new

    @staticmethod
    def _insert_before(value: int, node: "_Node") -> "_Node":
        """
        Utility protected method to insert a new node before a previous node.

        :param value: the data value to insert into the linked list
        :type value: int
        :param node: the node to be then inserted before
        :type node: _Node
        :return: node object of this new inserted value
        :rtype: _Node
        """
        new = _Node(value, next=node, previous=node.previous)
        node.previous = new
        if new.previous is not None:
            new.previous.next = new

        return new

    def __iter__(self) -> "_Node":
        """
        Iterator linked list object.

        :return: returned iterable object has `__next__` method
        :rtype: _Node
        """
        return _Node(data=None, next=self.__head)

    def __len__(self) -> int:
        """
        Return the length of the linked list.

        :return: number of nodes in the list.
        :rtype: int
        """
        return self.__length

    def __repr__(self) -> str:
        """
        Representation the linked list as a string.

        :return: representation string
        :rtype: str
        """
        node, items = self.__head, []
        while node is not None:
            items.append(str(node.data))
            node = node.next

        return f"{' <=> '.join(items)}"


@dataclass
class _Node:
    """Node Class Model Contains Data Value with Next & Previous Pointers"""
    data: int
    next: Optional["_Node"] = field(default=None, kw_only=True)
    previous: Optional["_Node"] = field(default=None, kw_only=True)

    def __next__(self) -> int:
        """
        Next Pointer to Node object while traversing the linked list.

        :raises StopIteration: Signal the end of next nodes.
        :return: returned integer value of next node data.
        :rtype: int
        """
        if (next_node := self.next) is not None:
            self.next = next_node.next
            return next_node.data

        raise StopIteration
 