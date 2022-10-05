from copy import deepcopy
from random import shuffle


class Array(list):
    @property
    def sorted(self) -> list:
        return list(deepcopy(self))

    @property
    def reversed(self) -> list:
        copied = list(deepcopy(self))
        copied.reverse()
        return copied

    @property
    def shuffled(self) -> list:
        copied = list(deepcopy(self))
        shuffle(copied)
        return copied


ODD_ARRAY = Array([i for i in range(1, 10)])
EVEN_ARRAY = Array([i for i in range(1, 11)])
