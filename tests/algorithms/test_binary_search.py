from pytest import mark, raises

from algorithms import binary_search
from ..conftest import ODD_ARRAY, EVEN_ARRAY


@mark.parametrize(
    "item, array, expected",
    [(item, EVEN_ARRAY.sorted, index) for index, item in enumerate(EVEN_ARRAY.sorted)]
    + [(item, ODD_ARRAY.sorted, index) for index, item in enumerate(ODD_ARRAY.sorted)],
)
def test_binary_search(item, array, expected):
    assert binary_search(item, array) == expected


def test_binary_search_errors():
    with raises(ValueError):
        binary_search(10, ODD_ARRAY.sorted)
