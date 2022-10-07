from pytest import mark, raises

from data_structures import Queue
from exceptions import UnderflowError


@mark.parametrize(
    "n",
    [i for i in range(1, 6)],
)
def test_queue(n):
    queue = Queue(length=n)
    assert queue.length == n

    assert queue.is_empty is True
    assert queue.is_full is False

    for i in range(n):
        assert queue.size == i
        queue.enqueue(value=i)
        assert queue.rear == i
        assert queue.front == 0
        assert queue.size == i + 1

    with raises(OverflowError):
        queue.enqueue(value=n)

    assert queue.is_empty is False
    assert queue.is_full is True

    for i in range(n):
        assert queue.size == n - i
        assert queue.rear == n - 1
        assert queue.front == queue.dequeue() == i
        assert queue.size == n - i - 1

    with raises(UnderflowError):
        queue.dequeue()

    with raises(UnderflowError):
        queue.front

    with raises(UnderflowError):
        queue.rear
