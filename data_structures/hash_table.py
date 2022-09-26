class HashTable(set):
    """
    Hash maps are indexed data structures.
    A hash map makes use of a hash function to compute an index with a key into an array
    of buckets or slots. Its value is mapped to the bucket with the corresponding index.
    The key is unique and immutable.
    """

    def __contains__(self, __o: "String") -> bool:
        return super().__contains__(hash(__o))

    def add(self, __element: "String") -> None:
        return super().add(hash(__element))

    def remove(self, __element: "String") -> None:
        return super().remove(hash(__element))


class String(str):
    """Customized String Object Class to Override Hashing."""

    __P, __MOD = 447, 10**9 + 7

    def __hash__(self) -> int:
        """
        Override hash value to calls `hash()` function.

        Hash function is the core of implementing a hash map.
        It takes in the key and translates it to the index of bucket in the bucket list.
        Ideal hashing should produce a different index for each key.
        However, collisions can occur. When hashing gives an existing index,
        we can simply use bucket for multiple values by appending list or by rehashing.

        :return: integer number hash value of this string
        :rtype: int
        """
        result = 0
        for char in self:
            result = result * self.__P + ord(char)

        return result % self.__MOD
