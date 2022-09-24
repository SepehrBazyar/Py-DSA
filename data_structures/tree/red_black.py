from enum import Enum
from dataclasses import dataclass, field
from typing import Optional, Literal


from .binary_tree import BinaryTree, _Node


class RBBinaryTree(BinaryTree):
    """
    # Red-Black Binary Tree
    A red-black tree is a kind of self-balancing binary search tree where each node
    has an extra bit, and that bit is often interpreted as the color (red or black).
    These colors are used to ensure that the tree remains balanced during insertions
    and deletions. Although the balance of the tree is not perfect,
    it's good enough to reduce the searching time and maintain around `O(log(n))` time,
    where n is the total number of elements in the tree.

    That as each node requires only 1 bit of space to store the color information,
    these types of trees show identical memory to the classic binary search tree. 

    Rules That Every Red-Black Tree Follows: 
        * Every node has a color either red or black.
        * The root of the tree is always black.
        * There are no two adjacent red nodes.
        * Every path from a node to any `NULL` nodes has the same number of black nodes.
        * All leaf nodes are black nodes.

    ## Why Red-Black Trees?
    Most of the BST operations take `O(h)` time where `h` is the height of the BST.
    The cost of these operations may become `O(n)` for a skewed Binary tree.
    If we make sure that the height of the tree remains `O(log(n))`
    after every insertion and deletion, then we can guarantee an upper bound of
    `O(log(n))` for all these operations. The height of a Red-Black tree is always
    `O(log(n))` where n is the number of nodes in the tree.
    """
    def __init__(self, value: int):
        self._root = _RBNode(value, color=_Color.BLACK)

    def _set_node(
        self,
        value: int,
        *,
        node: "_RBNode",
        direction: Literal["left", "right"],
    ) -> "_RBNode":
        new = _RBNode(data=value, parent=node)
        setattr(node, direction, new)
        self._insert_fixup(node=new)
        return new

    def _insert_fixup(self, *, node: "_RBNode"):
        """
        Restore Red-Black properties after insert new node.

        :param node: new node object set in red-black binary tree
        :type node: _RBNode
        """
        while node.parent.color is _Color.RED:
            parent, grand_parent = node.parent, node.parent.parent
            if grand_parent.left is parent:
                other_child: _RBNode = grand_parent.right
                if other_child.color is _Color.RED:
                    grand_parent.color = _Color.RED
                    other_child.color = _Color.BLACK
                    parent.color = _Color.BLACK
                    node = grand_parent
                else:
                    if parent.right is node:
                        node = parent
                        self._rotate_left(node=node)

                    node.parent.color = _Color.BLACK
                    node.parent.parent.color = _Color.RED
                    self._rotate_right(node=node.parent.parent)
            else:
                other_child: _RBNode = grand_parent.left
                if other_child.color is _Color.RED:
                    grand_parent.color = _Color.RED
                    other_child.color = _Color.BLACK
                    parent.color = _Color.BLACK
                    node = grand_parent
                else:
                    if parent.left is node:
                        node = parent
                        self._rotate_right(node=node)

                    node.parent.color = _Color.BLACK
                    node.parent.parent.color = _Color.RED
                    self._rotate_left(node=node.parent.parent)

        self._root.color = _Color.BLACK

    def _rotate_left(self, *, node: "_RBNode"):
        """
        Left Rotate Red-Black Node Object.

        :param node: node object rotate to left in red-black binary tree
        :type node: _RBNode
        """
        right_child, node.right = node.right, node.right.left
        self.__rotate(node=node, child=right_child, direction="left")

    def _rotate_right(self, *, node: "_RBNode"):
        """
        Right Rotate Red-Black Node Object.

        :param node: node object rotate to right in red-black binary tree
        :type node: _RBNode
        """
        left_child, node.left = node.left, node.left.right
        self.__rotate(node=node, child=left_child, direction="right")

    def __rotate(
        self,
        *,
        node: "_RBNode",
        child: "_RBNode",
        direction: Literal["left", "right"],
    ):
        """
        Private Rotate Method Red-Black Node Object.

        :param node: node object rotate to right in red-black binary tree
        :type node: _RBNode
        :param child: child node object to replacement rotate
        :type child: _RBNode
        :param direction: left or right child of direction rotate
        :type direction: Literal['left', 'right']
        """
        grand_child: Optional[_RBNode] = getattr(child, direction)
        if grand_child is not None:
            grand_child.parent = node

        child.parent = node.parent
        if node.parent is None:
            self._root = child
        elif node.parent.left is node:
            node.parent.left = child
        else:
            node.parent.right = child

        setattr(child, direction, node)
        node.parent = child


class _Color(Enum):
    """Enumeration Values of Color Data Variables"""
    RED = 1
    BLACK = 2


@dataclass
class _RBNode(_Node):
    """New Node Class Model Additional Color Field Red or Black"""
    color: _Color = field(default=_Color.RED, kw_only=True)