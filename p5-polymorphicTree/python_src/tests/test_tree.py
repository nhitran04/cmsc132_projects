import pytest
from tree import PolymorphicBST, PlaceKeysValuesInLists


def test_basics():
    ptree = PolymorphicBST()
    
    assert ptree.size() == 0
    
    ptree.put(2, "Two")
    ptree.put(1, "One")
    ptree.put(3, "Three")
    ptree.put(1, "OneSecondTime")
    assert ptree.size() == 3
    assert ptree.get(1) == "OneSecondTime"
    assert ptree.get(2) == "Two"
    assert ptree.get(3) == "Three"
    assert ptree.get(8) is None


def test_empty_search_tree():
    ptree = PolymorphicBST()
    
    assert ptree.size() == 0
    
    with pytest.raises(KeyError):
        ptree.get_min()
    
    with pytest.raises(KeyError):
        ptree.get_max()
    
    assert ptree.get("a") is None


def test_height_inorder_clear():
    ptree = PolymorphicBST()
    
    ptree.put(2, "Two")
    ptree.put(1, "One")
    ptree.put(3, "Three")
    ptree.put(4, "Four")
    assert ptree.height() == 3
    
    task = PlaceKeysValuesInLists()
    ptree.inorder_traversal(task)
    assert str(task.get_keys()) == "[1, 2, 3, 4]"
    assert str(task.get_values()) == "['One', 'Two', 'Three', 'Four']"
    
    ptree.clear()
    assert ptree.size() == 0


def verify(tree_map, insert_order, i, i2, detailed):
    foo = f"{insert_order}:{i}:{i2}"
    
    assert tree_map.size() == i2 - i, foo
    if detailed:
        keys = set()
        min_val = float('inf')
        max_val = float('-inf')
        for j in range(i, i2):
            min_val = min(min_val, insert_order[j])
            max_val = max(max_val, insert_order[j])
            keys.add(insert_order[j])
        
        if min_val <= max_val:
            assert tree_map.get_min() == int(min_val)
            assert tree_map.get_max() == int(max_val)
        
        if max_val < float('inf'):
            assert tree_map.get(int(max_val) + 1) is None
        
        in_tree = tree_map.key_set()
        assert keys == in_tree
    
    for j in range(len(insert_order)):
        result = tree_map.get(insert_order[j])
        if j < i or j >= i2:
            assert result is None
        else:
            assert insert_order[j] == result


all_permutations = []


def initialize():
    global all_permutations
    all_permutations = []
    start = [1, 2, 3, 4, 5]
    recurse(start, 0)


def recurse(a, n):
    if n == len(a):
        all_permutations.append(a[:])
        return
    
    for i in range(n, len(a)):
        a[i], a[n] = a[n], a[i]
        recurse(a, n + 1)
        a[i], a[n] = a[n], a[i]


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
