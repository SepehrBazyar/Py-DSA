from dataclasses import dataclass
from typing import Optional, List


class Trie:
    """
    # Trie
    Is an efficient information retrieval data structure.
    Using Trie, search complexities can be brought to optimal limit(key length).
    If we store keys in a binary search tree,
    a well balanced `BST` will need time proportional to `k * log(n)`,
    where `k` is the maximum string length and `n` is the number of keys in the tree.
    Using Trie, we can search the key in `O(k)` time.
    However, the penalty is on Trie storage requirements.
    """
    def __init__(self):
        """Initialize the Trie with a node root without parent nodes."""
        self.__root = _Node()

    def insert(self, string: str) -> "_Node":
        """
        Insert a string into the Trie.

        :param string: string to insert into the Trie
        :type string: str
        :return: node object of the string inserted
        :rtype: _type_
        """
        return self._insert(string=string, node=self.__root)

    def _insert(self, *, string: str, node: "_Node", index: int = 0) -> "_Node":
        """
        Protected Recursive Insert Utility Method in trie.

        :param string: string to insert into the trie
        :type string: str
        :param node: root node to insert and mark
        :type node: _Node
        :param index: index number of string character, defaults to 0
        :type index: int, optional
        :return: node object of the string inserted
        :rtype: _Node
        """
        if index == len(string):  # base case
            node.is_end = True
            return node

        char = string[index]
        for edge in node.edges:
            if edge.label == char:
                next_node = edge.end
                break
        else:
            next_node = _Node(parent=node)
            node.edges.append(_Edge(label=char, start=node, end=next_node))

        return self._insert(string=string, node=next_node, index=index + 1)


class _Node:
    """Node Class Model Contains Boolean Mark End Word and List of Edge Objects"""
    def __init__(self, mark: bool = False, parent: Optional["_Node"] = None):
        """
        Initialize the Node object with mark flag and parent node.

        :param mark: boolean flag for end of words, defaults to False
        :type mark: bool, optional
        :param parent: parent node to back space, defaults to None
        :type parent: Optional[_Node], optional
        """
        self.is_end, self.parent = mark, parent
        self.edges: List[_Edge] = []


@dataclass
class _Edge:
    """Edge Class Model Contains Label Data and Start and End Node Objects"""
    label: str
    start: _Node
    end: _Node
