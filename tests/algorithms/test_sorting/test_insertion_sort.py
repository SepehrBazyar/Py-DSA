from pytest import mark

from algorithms import insertion_sort
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
def test_counting_sort(array, expected):
    assert insertion_sort(array) == expected
