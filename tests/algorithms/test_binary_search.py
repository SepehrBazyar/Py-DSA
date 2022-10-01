from pytest import mark, raises

from algorithms import binary_search
from ..conftest import SORTED_ODD_ARRAY, SORTED_EVEN_ARRAY


@mark.parametrize(
    "item, array, expected",
    [(item, SORTED_EVEN_ARRAY, index) for index, item in enumerate(SORTED_EVEN_ARRAY)]
    + [(item, SORTED_ODD_ARRAY, index) for index, item in enumerate(SORTED_ODD_ARRAY)],
)
def test_binary_search(item, array, expected):
    assert binary_search(item, array) == expected


def test_binary_search_errors():
    with raises(ValueError):
        binary_search(10, SORTED_ODD_ARRAY)
