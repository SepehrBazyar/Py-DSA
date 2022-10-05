from pytest import mark

from algorithms import quick_sort
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
def test_quick_sort(array, expected):
    assert quick_sort(array) == expected
