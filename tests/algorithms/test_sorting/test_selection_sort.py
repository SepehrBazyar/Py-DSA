from pytest import mark

from algorithms import selection_sort
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
def test_selection_sort(array, expected):
    assert selection_sort(array) == expected
