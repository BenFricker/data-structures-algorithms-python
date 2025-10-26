# Test 1: Basic operations
tree = BinarySearchTree()
tree.insert(50)
tree.insert(30)
tree.insert(70)
tree.in_order_traversal()  # Should print: 30 50 70

# Test 2: Duplicate handling
tree.insert(50)  # Should not add duplicate
tree.in_order_traversal()  # Should still be: 30 50 70

# Test 3: Delete leaf node
tree.delete(30)
tree.in_order_traversal()  # Should print: 50 70

# Test 4: Delete node with two children
tree.insert(30)
tree.insert(40)
tree.insert(60)
tree.insert(80)
tree.delete(70)  # Has two children
tree.in_order_traversal()  # Should properly reorganize

# Test 5: Search
result = tree.find(50)
print(result.content if result else "Not found")  # Should print: 50
