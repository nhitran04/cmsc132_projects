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
│   └── place_keys_values_in_arraylists.py  # Traversal task implementation
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

**PlaceKeysValuesInArrayLists:**
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
