
"""
Binary Search Tree Implementation

KEY NOTES:
1. Binary Search Tree (BST) is a tree where each node has a maximum
   of two child nodes, the left and right

2. LEFT CHILDREN: Are always smaller/less than the parent node and
   their sibling (right)

3. RIGHT CHILDREN: Are always bigger/larger than the parent node and
   their sibling (left)
"""

# ----------- CREATE NODE OBJECT ----------- #
class Node:
  """Create Node Object:
  value:          Info we want to store
  self.content:  Where we permanently store value info
  self.left:      Stores node's left child
  self.right:     Stores node's right child
  """
  def __init__(self, value):
    self.value = value

    # Set content pointer
    self.content = value

    # Set left & right pointers
    self.left = None
    self.right = None

# ----------- CREATE BINARY SEARCH TREE ----------- #
class BinarySearchTree:
  def __init__(self):

    # Initialise Root
    self.root = None

  # ------ INSERT METHOD ------ #
  def insert(self, value):
    """Method to Insert Values into the BST"""

    # Step 1: HANDLE EMPTY TREE CASE
    if self.root is None: # If root is None, new node becomes the root
      self.root = Node(value)
      return


    # Step 2. INITIALISE TRAVERSAL VARIABLES
    current = self.root # "next" in week 4 pseudocode (node currently being examined)
    parent = None # "node" in week 4 pseudocode

    # Step 3. Begin: MAIN TRAVERSAL LOOP

    # Loop continues as long as we havent found a None spot
    while current is not None:
      # **A. TRACK THE PARENT**: Always save the current node before moving
      parent = current

      # **B. CHECK BST PROPERTY**: Decide to go Left, Right, or Stop (Duplicate)
      if value < current.content:
        # Go left
        current = current.left
      elif value > current.content:
        # Go right
        current = current.right

      # If duplicate is found, Stop insertion immediately
      else:
        return
      # End main loop

    # Step 4 FINAL LINKING
    # Create new node
    new_node = Node(value)

    # Update parent's pointer
    # If larger than parent, place to the right
    if value < parent.content:
      parent.left = new_node

    # If smaller than parent, place to the left
    else:
      parent.right = new_node


  # ------ IN ORDER TRAVERSAL METHOD ------ #
  def in_order_traversal(self):
    """
    Initializes the traversal from the root and calls the recursive helper.
    """

    # 1. Define Recursive Helper Function
    def visit(node):
      if node is None:
        return

      # STEP 1 (left): Recursively visit the left subtree
      visit(node.left)

      # STEP 2 (root): Process & print current node's value
      print(node.content, end=" ")

      # STEP 3 (right): Resursively visit the right subtree
      visit(node.right)

    # 2. Start the Traversal at the root of the tree
    visit(self.root)

    print()

  # ------ SEARCH METHOD METHOD ------ #
  def find(self, value):

    # Create helper recursive function
    def search_helper(node, value_to_find):

      # Handle empty tree
      if node is None:
        return None

      # If value to find is the node's value, return
      if value_to_find == node.content:
        return node

      # If value to find is less than node's content, search left
      elif value_to_find < node.content:
        return search_helper(node.left, value_to_find)

      # If value to find is more than node's content, go right
      else:
        return search_helper(node.right, value_to_find)

    # Begin recursion at the root
    return search_helper(self.root, value)

  def delete(self, value):

    # Helper function to delete value
    def delete_helper(node, value_to_delete):

      # Handle empty tree
      if node is None:
        return None

      # Check if node's value is less than value to delete
      if node.content < value_to_delete:
        # search right subtree
        node.right = delete_helper(node.right, value_to_delete)

      # Check if node's value is more than value to delete
      elif  node.content > value_to_delete:
        node.left = delete_helper(node.left, value_to_delete)

      # Check if node to delete it found
      elif node.content == value_to_delete:

        # CASE 1: LEAF NODE
        # Check if it is a leaf node (no children)
        if (node.left is None and node.right is None):
          return None #

        # CASE 2: Has Left Child & No Right Child (Only smaller child)
        elif node.right == None:
          return node.left # Replace with left child

        # CASE 3: Has Right Child & No Left Child (Only larger child)
        elif node.left == None:
          return node.right # Replace with right child

        # CASE 4: Has BOTH children:
        # Replace parent with the smallest right child
        else:
          # Create helper function to find smallest right node
          def get_smallest_right(node):

            # Begin at current the node
            current = node

            # Keep going down the left
            while current.left is not None:
              current = current.left
            return current # Return the Inorder Successor Node

          succesor_node = get_smallest_right(node.right)

          node.content = succesor_node.content

          node.right = delete_helper(node.right, succesor_node.content)

      return node

    # Call delete helper function
    self.root = delete_helper(self.root, value)

print(" ===== Delete Test ===== ")
delete_test = my_tree.delete(70)
delete_test = my_tree.delete(80)
delete_test = my_tree.delete(60)
my_tree.in_order_traversal()
