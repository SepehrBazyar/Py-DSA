from pytest import raises

from data_structures import BinaryTree
from data_structures.tree.binary_tree import _Node


def test_binary_tree():
    binary_tree = BinaryTree(value=4.5)
    nodes = {num: binary_tree.insert(value=num) for num in [2, 6, 1, 3, 5, 7]}

    with raises(TypeError):
        binary_tree.root = 4

    pre_root = binary_tree.root
    four = _Node(data=4, left=pre_root.left, right=pre_root.right)
    binary_tree.root = pre_root.left.parent = pre_root.right.parent = four
    assert binary_tree.root is four

    assert binary_tree.minimum == 1
    assert binary_tree.maximum == 7

    assert binary_tree._in_order(node=binary_tree.root) == [1, 2, 3, 4, 5, 6, 7]
    assert binary_tree._pre_order(node=binary_tree.root) == [4, 2, 1, 3, 6, 5, 7]
    assert binary_tree._post_order(node=binary_tree.root) == [1, 3, 2, 5, 7, 6, 4]

    assert binary_tree.lca(3, 6) == four
    assert binary_tree.lca(8, 9) is None

    nodes[4] = four
    for i in [1, 3, 2, 6, 7, 4]:
        assert binary_tree.search(value=i) is nodes[i]
        binary_tree.delete(node=nodes[i])
        assert binary_tree.search(value=i) is None

    four = binary_tree.insert(value=4)
    binary_tree.delete(node=binary_tree.search(value=5))

    two = binary_tree.insert(value=2)
    five = binary_tree.insert(value=5)

    binary_tree.insert(value=3)
    binary_tree.delete(node=four)

    one, six = _Node(data=1), _Node(data=6)
    binary_tree._replace(old=two, new=one)
    binary_tree._replace(old=five, new=six)

    three = binary_tree.search(value=3)
    assert three.left is one
    assert three.right is six
    assert one.parent is six.parent is three
