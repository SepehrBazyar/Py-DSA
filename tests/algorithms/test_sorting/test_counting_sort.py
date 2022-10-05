from pytest import mark

from algorithms import counting_sort
from algorithms.sorting.counting_sort import _minimum_maximum
from ...conftest import Array, ODD_ARRAY, EVEN_ARRAY


array = Array([1, 1, 2, 2, 2, 2, 5, 10, 10, 10])


@mark.parametrize(
    "array, expected",
    [
        (array.shuffled, array),
        (ODD_ARRAY.shuffled, ODD_ARRAY),
        (EVEN_ARRAY.shuffled, EVEN_ARRAY),
    ],
)
def test_counting_sort(array, expected):
    assert counting_sort(array) == expected


@mark.parametrize(
    "accumulator, element, expected",
    [
        ((2, 3), 1, (1, 3)),
        ((1, 3), 2, (1, 3)),
        ((1, 2), 3, (1, 3)),
        ((1, 3), 1, (1, 3)),
        ((1, 3), 3, (1, 3)),
    ],
)
def test_minimum_maximum(accumulator, element, expected):
    assert _minimum_maximum(accumulator, element) == expected
