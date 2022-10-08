from data_structures import HashTable, String


def test_hash_table():
    names = list(map(String, ["farzane", "jane", "lucy", "sepehr", "tom"]))

    hash_table = HashTable()
    for name in names:
        hash_table.add(name)

    for name in names:
        assert (name in hash_table) is True
        hash_table.remove(name)
        assert (name in hash_table) is False
