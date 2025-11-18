# NO TOUCHY TOUCH

from abc import ABC, abstractmethod
from typing import TypeVar, Generic, Collection, Optional
from tree.tree_is_empty_exception import TreeIsEmptyException
from tree.traversal_task import TraversalTask

K = TypeVar('K')
V = TypeVar('V')

"""
This interface describes the interface for both empty and non-empty search
trees.
"""

class Tree(ABC, Generic[K, V]):
    
    @abstractmethod
    def search(self, key: K) -> Optional[V]:
        """
        Find the value that this key is bound to in this tree.
        
        :param key: Key to search for
        :return: value associated with the key by this Tree, or None if the key
                 does not have an association in this tree.
        """
        pass
    
    @abstractmethod
    def insert(self, key: K, value: V) -> 'NonEmptyTree[K, V]':
        """
        Insert/update the Tree with a new key:value pair. If the key already
        exists in the tree, update the value associated with it. If the key
        doesn't exist, insert the new key value pair.
        
        This method returns a reference to a Tree that represents the updated
        value. In many, but not all cases, the method may just return a
        reference to this. You have to pay attention to the return value;
        if you simply invoke insert on a Tree and ignore the return value,
        your code is almost certainly wrong.
        
        :param key: Key
        :param value: Value that the key maps to
        :return: updated tree
        """
        pass
    
    @abstractmethod
    def delete(self, key: K) -> 'Tree[K, V]':
        """
        Delete any binding the key has in this tree. If the key isn't bound, this
        is a no-op
        
        This method returns a reference to a Tree that represents the updated
        value. In many, but not all cases, the method may just return a
        reference to this. You have to pay attention to the return value;
        if you simply invoke delete on a Tree and ignore the return value,
        your code is almost certainly wrong.
        
        :param key: Key
        :return: updated tree
        """
        pass
    
    @abstractmethod
    def max(self) -> K:
        """
        Return the maximum key in the subtree
        
        :return: maximum key
        :raises TreeIsEmptyException: if the tree is empty
        """
        pass
    
    @abstractmethod
    def min(self) -> K:
        """
        Return the minimum key in the subtree
        
        :return: minimum key
        :raises TreeIsEmptyException: if the tree is empty
        """
        pass
    
    @abstractmethod
    def size(self) -> int:
        """
        Return number of keys that are bound in this tree.
        
        :return: number of keys that are bound in this tree.
        """
        pass
    
    @abstractmethod
    def add_keys_to_collection(self, c: Collection[K]) -> None:
        """
        Add all keys bound in this tree to the collection c.
        The elements can be added in any order.
        """
        pass
    
    @abstractmethod
    def sub_tree(self, from_key: K, to_key: K) -> 'Tree[K, V]':
        """
        Returns a Tree containing all entries between from_key and to_key, inclusive.
        It may not modify the original tree (a common mistake while implementing this method).
        
        :param from_key: Lower bound value for keys in subtree
        :param to_key: Upper bound value for keys in subtree
        :return: Tree containing all entries between from_key and to_key, inclusive
        """
        pass
    
    @abstractmethod
    def height(self) -> int:
        """
        Returns the height (maximum level) in the tree. A tree with only one
        entry has a height of 1.
        
        :return: height of the tree.
        """
        pass
    
    @abstractmethod
    def inorder_traversal(self, p: TraversalTask[K, V]) -> None:
        """
        Performs the specified task on the tree using an inorder traversal.
        
        :param p: object defining task
        """
        pass
    
    @abstractmethod
    def right_root_left_traversal(self, p: TraversalTask[K, V]) -> None:
        """
        Performs the specified task on the tree using a right tree, root, left tree
        traversal.
        
        :param p: object defining task
        """
        pass


# Forward reference for NonEmptyTree
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from tree.non_empty_tree import NonEmptyTree
