from data_structures import FenwickTree
from ...conftest import EVEN_ARRAY


def test_fenwick():
    fenwick = FenwickTree(*EVEN_ARRAY.sorted)
    assert len(fenwick) == 10
    assert fenwick[1:10] == 55
