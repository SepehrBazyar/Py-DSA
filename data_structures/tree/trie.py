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

    def delete(self, string: str):
        """
        Delete a string from the Trie.

        :param string: string to delete from the Trie
        :type string: str
        """
        return self._delete(string=string, node=self.__root)

    def __contains__(self, string: str) -> bool:
        """
        Search a string into the Trie with `in` keyword.

        :param string: string to search into the Trie
        :type string: str
        :return: boolean result of search string in trie
        :rtype: _type_
        """
        return self._search(string=string, node=self.__root)

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
        next_node = self.__get(character=char, node=node)
        if next_node is None:
            next_node = _Node(parent=node)
            node.edges.append(_Edge(label=char, start=node, end=next_node))

        return self._insert(string=string, node=next_node, index=index + 1)

    def _search(self, *, string: str, node: "_Node", index: int = 0) -> bool:
        """
        Protected Recursive Search Utility Method in trie.

        :param string: string to search the trie
        :type string: str
        :param node: root node to search and mark
        :type node: _Node
        :param index: index number of string character, defaults to 0
        :type index: int, optional
        :return: boolean result of search string in trie
        :rtype: bool
        """
        if index == len(string):  # base case
            return node.is_end

        char = string[index]
        next_node = self.__get(character=char, node=node)
        if next_node is None:
            return False

        return self._search(string=string, node=next_node, index=index + 1)

    def _delete(self, *, string: str, node: "_Node", index: int = 0) -> None:
        """
        Protected Recursive Delete Utility Method in trie.

        :param string: string to search the trie
        :type string: str
        :param node: root node to search and mark
        :type node: _Node
        :param index: index number of string character, defaults to 0
        :type index: int, optional
        :raises ValueError: if not find this string item in trie.
        :return: boolean result of search string in trie
        :rtype: bool
        """
        if index == len(string):  # base case
            node.unset_mark()
            return

        char = string[index]
        next_node = self.__get(character=char, node=node)
        if next_node is None:
            raise ValueError("Could not find this string item in trie.")

        return self._delete(string=string, node=next_node, index=index + 1)

    def __get(self, character: str, node: "_Node") -> Optional["_Node"]:
        """
        Private method for getting the node has this character label.

        :return: returned node object if exist and find values otherwise None
        :rtype: Optional[_Node]
        """
        for edge in node.edges:
            if edge.label == character:
                return edge.end


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

    def unset_mark(self):
        """
        Unset mark flag for end of words.

        :raises Exception: if mark flag is false
        """
        if not self.is_end:
            raise Exception("Node already isn't end of words.") 

        self.is_end = False


@dataclass
class _Edge:
    """Edge Class Model Contains Label Data and Start and End Node Objects"""
    label: str
    start: _Node
    end: _Node
