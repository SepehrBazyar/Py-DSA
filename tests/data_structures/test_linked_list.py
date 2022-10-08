from pytest import raises

from data_structures import LinkedList
from data_structures.linked_list import _Node


def test_linked_list():
    linked_list = LinkedList(head=1)
    assert linked_list.is_empty is False

    one = linked_list.head
    two = linked_list.insert(value=2, node=one)
    four = linked_list.insert(value=4, node=two)
    three = linked_list.insert(value=3, node=two)
    linked_list.delete(node=three)

    three = linked_list.insert(value=3, node=four, after=False)
    assert len(linked_list) == 4

    assert linked_list.search(value=3) is three
    assert linked_list.search(value=5) is None

    with raises(TypeError):
        linked_list.head = 0

    node = _Node(data=0, next=one)
    linked_list.head = node
    assert [node_data for node_data in linked_list] == [0, 1, 2, 3, 4]

    linked_list.head = one
    linked_list.delete(node=three)
    linked_list.delete(node=four)
    linked_list.delete(node=two)
    linked_list.delete(node=one)
    assert linked_list.is_empty is True
