from data_structures import RBBinaryTree
from data_structures.tree.red_black import _Color


def test_red_black():
    red_black = RBBinaryTree(5)

    five = red_black.root
    assert five.color is _Color.BLACK

    four = red_black.insert(value=4)
    assert four.color is _Color.RED

    three = red_black.insert(value=3)
    assert red_black.root is four
    assert five.color is _Color.RED
    assert three.color is _Color.RED

    two = red_black.insert(value=2)
    assert two.color is _Color.RED
    assert three.color is _Color.BLACK

    one = red_black.insert(value=1)
    assert one.color is _Color.RED
    assert three.color is _Color.RED
    assert two.color is _Color.BLACK

    six = red_black.insert(value=6)
    assert six.color is _Color.RED
    assert five.color is _Color.BLACK

    twelve = red_black.insert(value=12)
    assert twelve.color is _Color.RED
    assert five.color is _Color.RED
    assert six.color is _Color.BLACK

    thirteen = red_black.insert(value=13)
    assert thirteen.color is _Color.RED
    assert twelve.color is _Color.BLACK

    ten = red_black.insert(value=10)
    assert ten.color is _Color.RED
    assert twelve.color is _Color.BLACK

    eleven = red_black.insert(value=11)
    assert eleven.color is _Color.RED
    assert ten.color is _Color.BLACK
    assert thirteen.color is _Color.BLACK
    assert twelve.color is _Color.RED

    nine = red_black.insert(value=9)
    assert nine.color is _Color.RED
    assert ten.color is _Color.BLACK

    seven = red_black.insert(value=7)
    assert seven.color is _Color.RED
    assert nine.color is _Color.BLACK
    assert ten.color is _Color.RED

    eight = red_black.insert(value=8)
    assert eight.color is _Color.BLACK
    assert seven.color is _Color.RED
    assert nine.color is _Color.RED

    assert red_black.root.color is _Color.BLACK
