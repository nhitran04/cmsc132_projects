from typing import Collection, TypeVar, Generic, Optional
from tree.tree import Tree
from tree.traversal_task import TraversalTask

K = TypeVar('K')
V = TypeVar('V')

"""
This class represents a non-empty search tree. An instance of this class
should contain:
- A key
- A value (that the key maps to)
- A reference to a left Tree that contains key:value pairs such that the
  keys in the left Tree are less than the key stored in this tree node.
- A reference to a right Tree that contains key:value pairs such that the
  keys in the right Tree are greater than the key stored in this tree node.
"""

class NonEmptyTree(Tree[K, V]):
    
    # Provide whatever instance variables you need
    def __init__(self, key: K, value: V, left: Tree[K, V], right: Tree[K, V]):
        """
        Only constructor we need.
        :param key: key
        :param value: value
        :param left: left subtree
        :param right: right subtree
        """
        # TODO
        self.left = left
        self.right = right
        self.key = key
        self.value = value
    
    def search(self, key: K) -> Optional[V]:
        # TODO
        pass
    
    def insert(self, key: K, value: V) -> 'NonEmptyTree[K, V]':
        # TODO
        pass
    
    def delete(self, key: K) -> Tree[K, V]:
        # TODO
        pass
    
    def max(self) -> K:
        # TODO
        pass
    
    def min(self) -> K:
        # TODO
        pass
    
    def size(self) -> int:
        # TODO
        pass
    
    def add_keys_to_collection(self, collection: Collection[K]) -> None:
        self.left.add_keys_to_collection(collection)
        collection.add(self.key)
        self.right.add_keys_to_collection(collection)
    
    def sub_tree(self, from_key: K, to_key: K) -> Tree[K, V]:
        # TODO
        pass
    
    def height(self) -> int:
        # TODO
        pass
    
    def inorder_traversal(self, task: TraversalTask[K, V]) -> None:
        # TODO
        pass
    
    def right_root_left_traversal(self, task: TraversalTask[K, V]) -> None:
        # TODO
        pass
