# Polymorphic Binary Search Tree - Python Version

This is a Python conversion of the Java polymorphic binary search tree project.

## Project Structure

```
python_src/
├── tree/                          # Main tree package
│   ├── __init__.py
│   ├── tree.py                    # Abstract base class for Tree interface
│   ├── empty_tree.py              # Singleton empty tree implementation
│   ├── non_empty_tree.py          # Non-empty tree node implementation
│   ├── polymorphic_bst.py         # Main BST wrapper class
│   ├── tree_is_empty_exception.py # Custom exception
│   ├── traversal_task.py          # Abstract traversal task interface
│   └── place_keys_values_in_lists.py  # Traversal task implementation
├── tests/                         # Test files
│   ├── __init__.py
│   ├── test_tree.py              # Main test cases
│   └── test_student.py           # Student test placeholder
├── expected_outputs/              # Expected output examples
│   ├── expected_output_basic.txt      # Basic operations examples
│   ├── expected_output_tests.txt      # Test execution examples
│   └── expected_output_traversals.txt # Traversal examples
├── requirements.txt              # Python dependencies
└── README.md                     # This file
```

## Installation

1. Make sure you have Python 3.7+ installed
2. Create and activate a virtual environment:
   ```bash
   cd python_src
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running Tests

Run all tests:
```bash
cd python_src
pytest tests/ -v
```

Run specific test file:
```bash
cd python_src
pytest tests/test_tree.py -v
```

## Project Specification

### Overview

This project implements recursive tree functions based on a polymorphic tree class. You will practice error handling, recursion, and polymorphism.

### Design

Notice that the `insert` and `delete` methods on `Tree` objects return references to `Tree` objects. In many cases, these functions may return a reference to the `self` object. However, in some cases they can't. For example, `EmptyTree.get_instance().insert("a", "1")` has to return an instance of a `NonEmptyTree` object.

### What to Modify

You only need to modify `EmptyTree`, `NonEmptyTree`, and `PlaceKeysValuesInLists`. **You may not add any classes**.

### Implementation Restrictions

- You may not use any form of looping construct (no `for`, `while`, etc.)
- You may not use arrays (use lists instead)
- You may not explicitly check a `Tree` to see whether it is an `EmptyTree` or `NonEmptyTree`
- Your `EmptyTree` and `NonEmptyTree` implementations may not have any comparisons against the `None` value
- You should not need to do any casting for this project. If you are casting, you are probably not using polymorphism correctly
- If you insert multiple values with the same key, only the value associated with the most recent insertion will be saved
- You may not add any public methods
- You may not check whether a tree is empty by using comparisons similar to:
  - `left == EmptyTree.get_instance()`
  - `tree.size() == 0`
  - Other comparisons similar to the above
- You are expected to use polymorphism (and exception handling, where appropriate) to handle the differences between empty and nonempty trees
- You may not use `isinstance()` or `type()` to check tree types
- The `delete` method must use the standard BST deletion approach (find min in right subtree or max in left subtree). You may not implement delete by creating a new tree and inserting all the keys from the source tree except the one you want to delete
- For the `sub_tree` method you may not create an empty tree and traverse the whole tree inserting only those entries within the specified range. If a simple check will tell you that an entire subtree can be excluded, your implementation should not traverse that subtree

**Note:** The above restrictions do not apply to your test cases; you may write them however you wish.

## Implementation Notes

### TODO Items

The following methods need to be implemented (marked with `# TODO`):

**EmptyTree:**
- `search()`
- `insert()`
- `delete()`
- `size()`
- `sub_tree()`
- `height()`
- `inorder_traversal()`
- `right_root_left_traversal()`

**NonEmptyTree:**
- Constructor initialization
- `search()`
- `insert()`
- `delete()`
- `max()`
- `min()`
- `size()`
- `sub_tree()`
- `height()`
- `inorder_traversal()`
- `right_root_left_traversal()`

**PlaceKeysValuesInLists:**
- `perform_task()`

## Usage Example

```python
from tree import PolymorphicBST

# Create a new tree
tree = PolymorphicBST()

# Insert key-value pairs
tree.put(5, "Five")
tree.put(3, "Three")
tree.put(7, "Seven")

# Search for values
print(tree.get(5))  # Output: "Five"

# Get tree properties
print(tree.size())     # Output: 3
print(tree.get_min())  # Output: 3
print(tree.get_max())  # Output: 7

# Remove a key
tree.remove(3)
```

## Testing

The test suite includes:
- Basic operations (insert, search, update)
- Empty tree operations
- Height calculation
- Inorder traversal
- Clear functionality

Add your own tests in `tests/test_student.py`.

## Expected Outputs

The `expected_outputs/` folder contains example outputs for reference:
- `expected_output_basic.txt` - Expected results for basic tree operations
- `expected_output_tests.txt` - Expected pytest output and test descriptions
- `expected_output_traversals.txt` - Expected results for tree traversals
