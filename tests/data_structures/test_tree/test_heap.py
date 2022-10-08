from pytest import mark, raises

from data_structures import MinHeap, MaxHeap
from ...conftest import ODD_ARRAY


@mark.parametrize(
    "Heap, build_down",
    [
        (MinHeap, True),
        (MaxHeap, True),
        (MinHeap, False),
        (MaxHeap, False),
    ],
)
def test_heap(Heap, build_down):
    heap = Heap(*ODD_ARRAY.shuffled, build_down=build_down)
    assert len(heap) == 9

    heap.insert(10)
    assert len(heap) == 10

    for counter in range(10, 0, -1):
        assert len(heap) == counter
        assert heap.is_empty is False
        assert heap.top == heap.delete()

    assert len(heap) == 0
    assert heap.is_empty is True

    with raises(Exception, match="Heap is empty."):
        heap.top

    with raises(Exception, match="Heap is empty."):
        heap.delete()
