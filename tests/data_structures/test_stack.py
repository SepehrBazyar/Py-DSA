from pytest import mark, raises

from data_structures import Stack
from exceptions import UnderflowError


@mark.parametrize(
    "n",
    [i for i in range(1, 6)],
)
def test_stack(n):
    stack = Stack(length=n)
    assert stack.length == n

    assert stack.is_empty is True
    assert stack.is_full is False

    with raises(UnderflowError):
        stack.top

    for i in range(n):
        assert stack.size == i
        stack.push(value=i)
        assert stack.top == i
        assert stack.size == i + 1

    with raises(OverflowError):
        stack.push(value=n)

    assert stack.is_empty is False
    assert stack.is_full is True

    for i in range(n):
        assert stack.size == n - i
        assert stack.top == stack.pop() == n - i - 1
        assert stack.size == n - i - 1

    with raises(UnderflowError):
        stack.pop()
