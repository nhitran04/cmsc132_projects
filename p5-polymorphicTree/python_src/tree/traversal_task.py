# NO TOUCHY TOUCH

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

K = TypeVar('K')
V = TypeVar('V')

"""
When we perform a traversal of a tree, we call the
perform_task method to process each key,value pair in
the tree. Classes implementing this interface allow
us to collect keys, print values, etc.
"""

class TraversalTask(ABC, Generic[K, V]):
    @abstractmethod
    def perform_task(self, key: K, value: V) -> None:
        pass
