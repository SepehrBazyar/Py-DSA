from pytest import mark, raises

from algorithms import quick_select
from ..conftest import ODD_ARRAY, EVEN_ARRAY


@mark.parametrize(
    "k, array",
    [(i, ODD_ARRAY) for i in range(1, 10)]
    + [(i, ODD_ARRAY.reversed) for i in range(1, 10)]
    + [(i, ODD_ARRAY.shuffled) for i in range(1, 10)]
    + [(i, EVEN_ARRAY) for i in range(1, 11)]
    + [(i, EVEN_ARRAY.reversed) for i in range(1, 11)]
    + [(i, EVEN_ARRAY.shuffled) for i in range(1, 11)],
)
def test_quick_select(k, array):
    assert quick_select(k, array) == k


@mark.parametrize("k", [0, 10])
def test_quick_select_errors(k):
    with raises(ValueError):
        quick_select(k, ODD_ARRAY)
