from typing import Collection, TypeVar, Generic, Optional
from tree.tree import Tree
from tree.tree_is_empty_exception import TreeIsEmptyException
from tree.traversal_task import TraversalTask

K = TypeVar('K')
V = TypeVar('V')

"""
This class is used to represent the empty search tree: a search tree that
contains no entries.

This class is a singleton class: since all empty search trees are the same,
there is no need for multiple instances of this class. Instead, a single
instance of the class is created and made available through the class method
get_instance().

The constructor is private, preventing other code from mistakenly creating
additional instances of the class.
"""

class EmptyTree(Tree[K, V]):
    """
    This class variable references the one and only instance of this class.
    We won't declare generic types for this one, so the same singleton
    can be used for any kind of EmptyTree.
    """
    _SINGLETON = None
    
    @classmethod
    def get_instance(cls):
        if cls._SINGLETON is None:
            cls._SINGLETON = EmptyTree()
        return cls._SINGLETON
    
    def __new__(cls):
        if cls._SINGLETON is None:
            cls._SINGLETON = super(EmptyTree, cls).__new__(cls)
        return cls._SINGLETON
    
    """
    Constructor is private to enforce it being a singleton
    """
    def __init__(self):
        # Nothing to do
        pass
    
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
        raise TreeIsEmptyException()
    
    def min(self) -> K:
        raise TreeIsEmptyException()
    
    def size(self) -> int:
        # TODO
        pass
    
    def add_keys_to_collection(self, collection: Collection[K]) -> None:
        return
    
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


# Forward reference for NonEmptyTree
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from tree.non_empty_tree import NonEmptyTree
