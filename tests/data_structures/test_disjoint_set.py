from pytest import raises

from data_structures import DisjointSet


def test_disjoint_set():
    disjoint_set = DisjointSet(number=5)

    with raises(IndexError):
        disjoint_set[6]

    assert disjoint_set[5] + disjoint_set[3] == 5
    assert disjoint_set[1] + disjoint_set[2] == 1
    assert disjoint_set[4] + disjoint_set[2] == 1
    assert disjoint_set[4] + disjoint_set[3] == 1

    for i in range(1, 6):
        assert disjoint_set[i].root.label == 1
