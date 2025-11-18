from typing import TypeVar, Generic, List
from tree.traversal_task import TraversalTask

K = TypeVar('K')
V = TypeVar('V')

"""
This task places key/values in two arrays in the order
in which the key/values are seen during the traversal. If no keys/values
are found the List will be empty (constructor creates two
empty Lists).
"""

class PlaceKeysValuesInArrayLists(TraversalTask[K, V], Generic[K, V]):
    
    def __init__(self):
        """
        Creates two List objects: one for the keys and one for the values.
        """
        self.keys: List[K] = []
        self.values: List[V] = []
    
    def perform_task(self, key: K, value: V) -> None:
        """
        Adds key/value to the corresponding Lists.
        """
        # TODO
        pass
    
    def get_keys(self) -> List[K]:
        """
        Returns reference to List holding keys.
        
        :return: List
        """
        return self.keys
    
    def get_values(self) -> List[V]:
        """
        Returns reference to List holding values.
        
        :return: List
        """
        return self.values
