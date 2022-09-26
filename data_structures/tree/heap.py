import heapq  # noqa: F401
from abc import ABC, abstractmethod


class _AbstractHeap(ABC):
    """
    # Heap
    It's a complete tree (All levels are completely filled except possibly
    the last level and the last level has all keys as left as possible).
    This property of Binary Heap makes them suitable to be stored in an array.

    ## Time Complexity:
        * Get: `O(1)`
        * Insert: `O(log(n))`
        * Deletion: `O(log(n))`

    ## Auxiliary Space: `O(n)`
    """

    def __init__(self, *args: int, build_down: bool = True):
        """
        Initialize a new instance of a heap with the integer values.

        :param build_down: set bubble function builder, defaults to True
        :type build_down: bool, optional
        """
        self._heap, self._count = list(args), len(args)
        if build_down:
            bubble_func, indexes = self.bubble_down, range(self._count - 1, -1, -1)
        else:
            bubble_func, indexes = self.bubble_up, range(self._count)

        for index in indexes:
            bubble_func(index=index)

    def insert(self, item: int):
        """
        Insert new integer value inserted into the heap.

        :param item: new integer item value to inserted
        :type item: int
        """
        self._heap.append(item)
        self.bubble_up(index=self._count)
        self._count += 1

    def delete(self) -> int:
        """
        Delete the top head node in the heap and returned value.

        :return: integer value of the top head node
        :rtype: int
        """
        if self.is_empty:
            raise Exception("Heap is empty.")

        result = self._heap[0]
        self._heap[0] = self._heap[-1]
        self._heap.pop()
        self._count -= 1
        self.bubble_down(index=0)
        return result

    @staticmethod
    def parent(index: int) -> int:
        """
        Static method utility to returns the parent node index.

        :param index: index of current node
        :type index: int
        :return: index of parent node
        :rtype: int
        """
        return (index - 1) // 2

    @staticmethod
    def left_child(index: int) -> int:
        """
        Static method utility to returns the left child node index.

        :param index: index of current node
        :type index: int
        :return: index of left child node
        :rtype: int
        """
        return 2 * index + 1

    @staticmethod
    def right_child(index: int) -> int:
        """
        Static method utility to returns the right child node index.

        :param index: index of current node
        :type index: int
        :return: index of right child node
        :rtype: int
        """
        return 2 * index + 2

    @abstractmethod
    def bubble_up(self, index: int):
        pass

    @abstractmethod
    def bubble_down(self, index: int):
        pass

    @property
    def top(self) -> int:
        """
        Get Top Node in the heap Min or Max.

        :return: top of heap node minimum or maximum
        :rtype: int
        """
        if self.is_empty:
            raise Exception("Heap is empty.")

        return self._heap[0]

    @property
    def is_empty(self) -> bool:
        """
        Boolean indicating whether the heap is empty.

        :return: flag to check if heap is empty
        :rtype: bool
        """
        return self._count == 0

    def _swap(self, i: int, j: int, /):
        """
        Swap two nodes in the heap with indexes.

        :param i: index of first node to swap
        :type i: int
        :param j: index of second node to swap
        :type j: int
        """
        self._heap[i], self._heap[j] = self._heap[j], self._heap[i]

    def __len__(self) -> int:
        """
        Return the length of the heap.

        :return: number of element items in the heap.
        :rtype: int
        """
        return self._count

    def __repr__(self) -> str:
        """
        Representation the heap as a string.

        :return: representation string
        :rtype: str
        """
        return ", ".join(str(item) for item in self._heap)


class MinHeap(_AbstractHeap):
    """
    # Minimum Binary Heap
    The key at root must be minimum among all keys present in Binary Heap.
    the same property must be recursively true for all nodes in Binary Tree.
    """

    def bubble_up(self, index: int):
        """
        Bubble Up the heap node with the given index while less than the parent.

        :param index: index of element to bubble up
        :type index: int
        """
        while 0 < index and self._heap[index] < self._heap[self.parent(index)]:
            parent = self.parent(index=index)
            self._swap(index, parent)
            index = parent

    def bubble_down(self, index: int):
        """
        Bubble Down the heap node with the given index while less than the child's.

        :param index: index of element to bubble down
        :type index: int
        """
        while self.left_child(index=index) < self._count:
            child, left, right = index, self.left_child(index), self.right_child(index)
            if self._heap[left] < self._heap[child]:
                child = left
            if right < self._count and self._heap[right] < self._heap[child]:
                child = right

            if child == index:
                break

            self._swap(index, child)
            index = child


class MaxHeap(_AbstractHeap):
    """
    # Maximum Binary Heap
    The key at root must be maximum among all keys present in Binary Heap.
    the same property must be recursively true for all nodes in Binary Tree.
    """

    def bubble_up(self, index: int):
        """
        Bubble Up the heap node with the given index while greater than the parent.

        :param index: index of element to bubble up
        :type index: int
        """
        while 0 < index and self._heap[index] > self._heap[self.parent(index)]:
            parent = self.parent(index=index)
            self._swap(index, parent)
            index = parent

    def bubble_down(self, index: int):
        """
        Bubble Down the heap node with the given index while greater than the parent.

        :param index: index of element to bubble down
        :type index: int
        """
        while self.left_child(index=index) < self._count:
            child, left, right = index, self.left_child(index), self.right_child(index)
            if self._heap[left] > self._heap[child]:
                child = left
            if right < self._count and self._heap[right] > self._heap[child]:
                child = right

            if child == index:
                break

            self._swap(index, child)
            index = child
