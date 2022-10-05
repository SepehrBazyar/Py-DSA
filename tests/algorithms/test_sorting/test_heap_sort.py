from pytest import mark

from algorithms import heap_sort
from ...conftest import ODD_ARRAY, EVEN_ARRAY


@mark.parametrize(
    "array, expected",
    [
        (ODD_ARRAY, ODD_ARRAY),
        (EVEN_ARRAY, EVEN_ARRAY),
        (ODD_ARRAY.shuffled, ODD_ARRAY),
        (EVEN_ARRAY.shuffled, EVEN_ARRAY),
        (ODD_ARRAY.reversed, ODD_ARRAY),
        (EVEN_ARRAY.reversed, EVEN_ARRAY),
    ],
)
def test_heap_sort(array, expected):
    assert heap_sort(array) == expected


@mark.parametrize(
    "array, expected",
    [
        (ODD_ARRAY, ODD_ARRAY.reversed),
        (EVEN_ARRAY, EVEN_ARRAY.reversed),
        (ODD_ARRAY.shuffled, ODD_ARRAY.reversed),
        (EVEN_ARRAY.shuffled, EVEN_ARRAY.reversed),
        (ODD_ARRAY.reversed, ODD_ARRAY.reversed),
        (EVEN_ARRAY.reversed, EVEN_ARRAY.reversed),
    ],
)
def test_heap_sort_reversed(array, expected):
    assert heap_sort(array, reverse=True) == expected
