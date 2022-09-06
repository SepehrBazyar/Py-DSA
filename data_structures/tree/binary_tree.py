from dataclasses import dataclass, field
from typing import Optional, List


class BinaryTree:
    """
    # Binary Tree
    A tree is a popular data structure that is non-linear in nature.
    Unlike other data structures like array, stack, queue, and linked list which are
    linear in nature, a tree represents a hierarchical structure.
    The ordering information of a tree is not important.

    A tree contains nodes and 3 pointers; These three pointers are:
        - The left child
        - The right child
        - The parent node

    ## Time Complexity:
        * Search: `O(log(n))`
        * Insert: `O(log(n))`
        * Deletion: `O(log(n))`

    ## Auxiliary Space: `O(n)`
    """
    def __init__(self, value: int):
        """
        Initialize the binary tree with a sequence of nodes.

        :param value: root node data integer value of this binary tree
        :type value: int
        """
        self.__root = _Node(value)

    def insert(self, value: int) -> "_Node":
        """
        Insert the new integer value in binary tree.

        :param value: integer value to inserted in binary tree
        :type value: int
        :return: returned new node object created after inserted
        :rtype: _Node
        """
        return self._insert(value=value, node=self.__root)

    def search(self, value: int) -> Optional["_Node"]:
        """
        Search the binary tree with an integer value.

        :param value: integer value to search and find node
        :type value: int
        :return: returned node object if exist and find value
        :rtype: Optional[_Node]
        """
        return self._search(value=value, node=self.__root)

    @property
    def root(self) -> "_Node":
        """
        Getter for the root of the binary tree.

        :return: Node object of root of binary tree
        :rtype: _Node
        """
        return self.__root

    @root.setter
    def root(self, node: "_Node"):
        """
        Setter for root of binary tree.

        :param node: Node object to set root of binary tree
        :type node: _Node
        :raises TypeError: if the node is not Node object or has parent
        """
        if not isinstance(node, _Node) or node.parent is not None:
            raise TypeError("Node must be a node objects without parent.")

        self.__root = node

    def _insert(self, value: int, *, node: "_Node") -> "_Node":
        """
        Protected Recursive Insert Utility Method in binary tree.

        :param value: integer value to inserted in binary tree
        :type value: int
        :param node: node object of subtree root
        :type node: _Node
        :return: returned new node object created after inserted
        :rtype: _Node
        """
        direction = "left" if value < node.data else "right"
        child: Optional[_Node] = getattr(node, direction)
        if child is None:  # base case
            new = _Node(data=value, parent=node)
            setattr(node, direction, new)
            return new

        return self._insert(value=value, node=child)

    def _search(
        self,
        value: int,
        *,
        node: Optional["_Node"] = None,
    ) -> Optional["_Node"]:
        """
        Protected Recursive Search Utility Method in binary tree.

        :param value: integer value to search and find node
        :type value: int
        :param node: node object of subtree root, defaults to None
        :type node: Optional[_Node], optional
        :return: returned node object if exist and find value
        :rtype: Optional[_Node]
        """
        if node is None:  # base case
            return
        if value < node.data:
            return self._search(value=value, node=node.left)
        if value > node.data:
            return self._search(value=value, node=node.right)

        return node  # base case

    def _in_order(self, node: Optional["_Node"] = None) -> List[int]:
        """
        In Order represents of this binary tree from root node

        :param node: node object of subtree root, defaults to None
        :type node: Optional[_Node], optional
        :return: list of left child subtree then root then right child subtree
        :rtype: list[int]
        """
        if node is None:  # base case
            return []

        return [*self._in_order(node.left), node.data, *self._in_order(node.right)]
 
    def _pre_order(self, node: Optional["_Node"] = None) -> List[int]:
        """
        Pre Order represents of this binary tree from root node

        :param node: node object of subtree root, defaults to None
        :type node: Optional[_Node], optional
        :return: list of root then left child subtree then right child subtree
        :rtype: list[int]
        """
        if node is None:  # base case
            return []

        return [node.data, *self._in_order(node.left), *self._in_order(node.right)]

    def _post_order(self, node: Optional["_Node"] = None) -> List[int]:
        """
        Post Order represents of this binary tree from root node

        :param node: node object of subtree root, defaults to None
        :type node: Optional[_Node], optional
        :return: list of left child subtree then right child subtree then root
        :rtype: list[int]
        """
        if node is None:  # base case
            return []

        return [*self._in_order(node.left), *self._in_order(node.right), node.data]

    def __repr__(self) -> str:
        """
        Three representation the binary tree as a string.

        :return: representation string
        :rtype: str
        """
        in_order = self._in_order(node=self.__root)
        pre_order = self._pre_order(node=self.__root)
        post_order = self._post_order(node=self.__root)
        return f"{in_order=}\n{pre_order=}\n{post_order=}"


@dataclass
class _Node:
    """Node Class Model Contains Data Value with Parent and Left & Right Child's"""
    data: int
    parent: Optional["_Node"] = field(default=None, kw_only=True)
    right: Optional["_Node"] = field(default=None, kw_only=True)
    left: Optional["_Node"] = field(default=None, kw_only=True)
