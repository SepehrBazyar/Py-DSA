from pytest import raises

from data_structures import Trie


def test_trie():
    trie = Trie()

    assert ("bar" in trie) is False

    foo = trie.insert(string="foo")
    foobar = trie.insert(string="foobar")

    assert foo.is_end is True
    assert foobar.is_end is True

    assert ("foo" in trie) is True
    assert ("foobar" in trie) is True

    trie.delete(string="foo")

    assert ("foo" in trie) is False
    assert ("foobar" in trie) is True

    assert foo.is_end is False
    assert foobar.is_end is True

    with raises(Exception, match="Node already isn't end of words."):
        trie.delete(string="foo")

    with raises(ValueError, match="Could not find this string item in trie."):
        trie.delete(string="bar")
