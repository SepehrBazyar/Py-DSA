from pytest import mark

from algorithms import bucket_sort
from ...conftest import Array


array = Array(["farzane", "jane", "lucy", "sepehr", "tom"])


@mark.parametrize(
    "array, expected",
    [
        (array, array),
        (array.shuffled, array),
        (array.reversed, array),
    ],
)
def test_bucket_sort(array, expected):
    assert bucket_sort(array) == expected
