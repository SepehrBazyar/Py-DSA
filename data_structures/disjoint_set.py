class DisjointSet:
    """
    # Disjoint Set
    data structure that stores non-overlapping or disjoint subset of elements
    is called disjoint set data structure.
    The disjoint set data structure supports the following operations:

    * Adding new sets to the a disjoint set.
    * Merging disjoint sets to a single disjoint set using Union operation.
    * Finding representative of a disjoint set using Find operation.
    * Check if two sets are disjoint or not.

    Two sets are called disjoint sets if they dont have any element in common,
    the intersection of sets is a null set.
    """
    def __init__(self, number: int):
        """
        Initialize a Disjoint Set Data Structure with n number nodes in tuple

        :param number: integer value of nodes count in this disjoint set
        :type number: int
        """
        self.__nodes = tuple(_Node(i) for i in range(1, number + 1))

    def __getitem__(self, key: int) -> "_Node":
        """
        Dunder Magic Method to get an item with index in sequence of nodes.

        :param key: index of node item between 1 and length of disjoint set
        :type key: int
        :raises IndexError: if not valid index key node item
        :return: node object with key index in sequence list
        :rtype: _Node
        """
        length = len(self.__nodes)
        if not 1 <= key <= length:
            raise IndexError(f"Index of node items must be between 1 and {length}.")

        return self.__nodes[key - 1]


class _Node:
    """Node Objects Value Data to Collect in Disjoint Set"""
    def __init__(self, label: int):
        """
        Initialize a Node object for Disjoint Set Data Structure

        :param label: integer number to label this node
        :type label: int
        """
        self.label, self.rank, self.parent = label, 0, self

    @property
    def root(self) -> "_Node":
        """
        Find Node Root Object of this Disjoint Set.

        :return: node object of this disjoint set root
        :rtype: _Node
        """
        if self.parent is self:  # base case
            return self

        self.parent = self.parent.root  # here we user path compression trick
        return self.parent

    def __add__(self, other: "_Node") -> int:
        """
        Union two nodes in disjoint set

        :param other: second node to added to self node
        :type other: _Node
        :return: new root node label after union two nodes
        :rtype: int
        """
        u, v = self.root, other.root
        if u is not v:  # u and v are not in the same component
            if v.rank > u.rank:  # making u the vertex with better rank
                u, v = v, u  # swap
            
            v.parent = u  # merging two components
            if u.rank == v.rank:
                u.rank += 1  # updating maximum depth as rank

        return u.label
