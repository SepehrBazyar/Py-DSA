from pytest import mark

from algorithms import merge_sort
from algorithms.sorting.merge_sort import _merge_arrays
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
def test_merge_sort(array, expected):
    assert merge_sort(array) == expected


@mark.parametrize(
    "left, right",
    [
        ((ODD_ARRAY, 9), (EVEN_ARRAY, 10)),
        ((EVEN_ARRAY, 10), (ODD_ARRAY, 9)),
    ],
)
def test_merge_arrays(left, right):
    assert _merge_arrays(left, right) == [
        1,
        1,
        2,
        2,
        3,
        3,
        4,
        4,
        5,
        5,
        6,
        6,
        7,
        7,
        8,
        8,
        9,
        9,
        10,
    ]
