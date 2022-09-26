from enum import Enum
from dataclasses import dataclass, field
from typing import Optional, Dict, Tuple, Callable, Literal


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
        while node.parent is not None and node.parent.color is _Color.RED:
            parent, grand_parent = node.parent, node.parent.parent
            direction = "left" if grand_parent.right is parent else "right"

            node = self.__insert_fixup(
                node=node,
                parent=parent,
                grand_parent=grand_parent,
                case=direction,
            )

        self._root.color = _Color.BLACK

    def _rotate_left(self, node: "_RBNode"):
        """
        Left Rotate Red-Black Node Object.

        :param node: node object rotate to left in red-black binary tree
        :type node: _RBNode
        """
        right_child, node.right = node.right, node.right.left
        self.__rotate(node=node, child=right_child, direction="left")

    def _rotate_right(self, node: "_RBNode"):
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

    def __insert_fixup(
        self,
        *,
        node: "_RBNode",
        parent: "_RBNode",
        grand_parent: "_RBNode",
        case: Literal["left", "right"],
    ) -> "_RBNode":
        """
        Private method to dynamic fixing up on node after insert.

        :param node: node object fixup on it
        :type node: _RBNode
        :param parent: parent object of this node
        :type parent: _RBNode
        :param grand_parent: grand parent object of this node
        :type grand_parent: _RBNode
        :param case: direction case left or right child
        :type case: Literal['left', 'right']
        :return: node replacement to continues fixing up
        :rtype: _RBNode
        """
        other_child: Optional[_RBNode] = getattr(grand_parent, case)
        if other_child is None or other_child.color is _Color.BLACK:
            switcher: Dict[
                Literal["left", "right"],
                Tuple[Callable[["_RBNode"], None], Callable[["_RBNode"], None]],
            ] = {
                "left": (self._rotate_left, self._rotate_right),
                "right": (self._rotate_right, self._rotate_left),
            }

            rotates = switcher[case]
            if getattr(parent, case) is node:
                node = parent
                rotates[1](node)

            node.parent.color = _Color.BLACK
            node.parent.parent.color = _Color.RED
            rotates[0](node.parent.parent)
        else:
            parent.color = _Color.BLACK
            other_child.color = _Color.BLACK
            grand_parent.color = _Color.RED
            node = grand_parent

        return node


class _Color(Enum):
    """Enumeration Values of Color Data Variables"""

    RED = 1
    BLACK = 2


@dataclass
class _RBNode(_Node):
    """New Node Class Model Additional Color Field Red or Black"""

    color: _Color = field(default=_Color.RED, kw_only=True)
