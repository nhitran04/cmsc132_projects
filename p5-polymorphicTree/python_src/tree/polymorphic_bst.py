from typing import TypeVar, Generic, Set
from tree.tree import Tree
from tree.empty_tree import EmptyTree
from tree.tree_is_empty_exception import TreeIsEmptyException
from tree.traversal_task import TraversalTask

K = TypeVar('K')
V = TypeVar('V')

"""
This class represents the polymorphic tree.
The implementation uses classes implementing the Tree interface to represent the
actual search tree. Some methods of this class has been implemented for you.
"""

class PolymorphicBST(Generic[K, V]):
    
    def __init__(self):
        self.root: Tree[K, V] = EmptyTree.get_instance()
    
    def get(self, k: K) -> V:
        """
        Find the value the key is mapped to
        
        :param k: Search key
        :return: value k is mapped to, or None if there is no mapping for the key
        """
        return self.root.search(k)
    
    def put(self, k: K, v: V) -> None:
        """
        Update the mapping for the key
        
        :param k: key value
        :param v: value the key should be bound to
        """
        self.root = self.root.insert(k, v)
    
    def size(self) -> int:
        """
        Return number of keys bound by this map
        
        :return: number of keys bound by this map
        """
        return self.root.size()
    
    def remove(self, k: K) -> None:
        """
        Remove any existing binding for a key
        
        :param k: key to be removed from the map
        """
        self.root = self.root.delete(k)
    
    def key_set(self) -> Set[K]:
        """
        Return a Set of all the keys in the map
        
        :return: Set of all the keys in the map
        """
        result = set()
        self.root.add_keys_to_collection(result)
        return result
    
    def get_min(self) -> K:
        """
        Return the minimum key value in the map
        
        :return: the minimum key value in the map
        :raises KeyError: if the map is empty
        """
        try:
            return self.root.min()
        except TreeIsEmptyException:
            raise KeyError("No such element")
    
    def get_max(self) -> K:
        """
        Return the maximum key value in the map
        This has been implemented for you as an example of
        handling control flow through exceptions
        
        :return: the maximum key value in the map
        :raises KeyError: if the map is empty
        """
        try:
            return self.root.max()
        except TreeIsEmptyException:
            raise KeyError("No such element")
    
    def __str__(self) -> str:
        """
        Return a string representation of the tree. You don't need
        to implement this method.
        """
        return str(self.root)
    
    def sub_map(self, from_key: K, to_key: K) -> 'PolymorphicBST[K, V]':
        """
        Return subset of TreeMap between the values from_key-to_key. It will
        include from_key and to_key if they are found in the original map.
        The values for from_key and to_key do not actually need to be in the map.
        You can assume that from_key is less than or equal to to_key.
        
        :return: TreeMap consisting of subset of SearchTreeMap
        """
        s_tree = PolymorphicBST()
        s_tree.root = self.root.sub_tree(from_key, to_key)
        return s_tree
    
    def clear(self) -> None:
        """
        Clears the tree by setting the root to EmptyTree
        """
        self.root = EmptyTree.get_instance()
    
    def height(self) -> int:
        """
        Returns height of the tree.
        
        :return: height of the tree.
        """
        return self.root.height()
    
    def inorder_traversal(self, p: TraversalTask[K, V]) -> None:
        """
        Performs an inorder traversal applying the task to each tree key,value pair.
        
        :param p: traversal task
        """
        self.root.inorder_traversal(p)
    
    def right_root_left_traversal(self, p: TraversalTask[K, V]) -> None:
        """
        Performs the specified task on the tree using a right tree, root, left tree
        traversal.
        
        :param p: object defining task
        """
        self.root.right_root_left_traversal(p)
