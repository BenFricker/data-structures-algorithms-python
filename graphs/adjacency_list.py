"""
Implement Adjacency List

Description: Based on the idea of storing a list of neighbours for every vertex.
             It is an array (or hash table), of length |V|, of linked lists where:

             - The lisst stored in "li" consts of all the vertices directly
               reachable from vertex "i"
"""

# =========== STEP 1: Core Components =========== #

# -------- A: Vertex Class -------- #
class Vertex:
  def __init__(self, name):
    self.name = name
    # Container storing weighted connections leaving this vertex
    self.neighbour_links = {} # Keys = Neighbour Name, Value = Edge Weight


# -------- B: Queue & Stack Classes -------- #
# Step 1. Create Queue Class for Breadth First Search
class Queue:
  """Queue for BFS (FIFO)"""
  def __init__(self):

    # Initialise Queue
    self.bfs_queue = []

  # Method to check if queue is empty
  def is_empty(self):
    """Check if Queue is Empty"""
    if len(self.bfs_queue) <= 0:
      return True
    else:
      return False

  # Method to add item to Queue
  def enqueue(self, item):
    """Add item to Queue"""
    self.bfs_queue.append(item)

  # Method to remove item from Queue
  def dequeue(self):
    """Remove item from Queue"""

    # Check queue is not empty
    if self.is_empty():
      return None

    # If queue contains items: FIFO Removal
    else:
      return self.bfs_queue.pop(0)

# Step 2. Create Stack Class for Depth First Search
class Stack:
  """Stack for DFS (LIFO)"""
  def __init__(self):
    # Initialise Empty Stack
    self.stack = []

  # Create Push Method
  def push(self, item):
    """Add item to stack"""
    self.stack.append(item)

  # Method to check if Stack is Empty
  def is_empty(self):
    if len(self.stack) <= 0:
      return True
    else:
      return False

  # Method to Remove & Return Items
  def pop(self):
    # Check if Stack is Empty
    if self.is_empty():
      return None

    # If Stack contains items:
    else:
      # Find index of last item
      last_index = len(self.stack) - 1
      # Retrieve & store last item's value
      item_value = self.stack[last_index]

      # Use 'del' to remove the item at that index
      del self.stack[last_index]

      # Return the stored value
      return item_value


# -------- C: CREATE MAIN GRAPH CLASS -------- #
class Graph:
  def __init__(self):

    # Vertex Name (string/int) to actual vertex object
    self.vertex_map = {}

  # Method to add Vertices
  def add_vertex(self, v_name):
    """Add Vertex to Graph"""

    # Ensure if v_name already exists, return
    if v_name in self.vertex_map:
      return

    # Otherwise
    else:

      # Create Vertex Object
      vertex = Vertex(v_name)

      # Add Vertex Object's to vertex_map
      self.vertex_map[v_name] = vertex

  def add_edge(self, u_name, v_name, weight):
    """Add Edge to Graph"""

    if u_name not in self.vertex_map or v_name not in self.vertex_map:
      return

    else:
      u_obj = self.vertex_map[u_name]
      v_obj = self.vertex_map[v_name]

      u_obj.neighbour_links[v_name] = weight
      v_obj.neighbour_links[u_name] = weight


  # ================= SEARCH METHODS ================= #

  # 1. Breadth First Search
  def Breadth_First_Search(self, start_vertex_name):
    """
    Breadth First Search Method:
    Search are wide as possible on every level
    """

    # Check vertex exists in vertex map
    if start_vertex_name not in self.vertex_map:
      return

    # Initialisation
    else:
      # Initialise Queue with starting vertex
      q = Queue()
      q.enqueue(start_vertex_name)

      # Initialise visitied vertices
      visited_set = []
      visited_set.append(start_vertex_name)

      # STEP A: Begin Main Traversal Loop
      while not q.is_empty():

        # Get name of the vertex to process next
        u_name = q.dequeue()
        # Retrieve actual object for neighbour access
        u_obj = self.vertex_map[u_name]

        # Print the vertex to show the BFS order
        print(f"Visited: {u_name}")

        for v_name in u_obj.neighbour_links:

          # Step B: Check Visited Set: Check if v_name is the neighbour's name
          if v_name not in visited_set:
            # Step C: Mark as Visited and Enqueue
            # 1. Mark as Visited: Add v_name to the list
            visited_set.append(v_name)

            # 2. Enqueue: Add v_name to the Queue for later processing (FIFO)
            q.enqueue(v_name)

  def depth_first_search(self, start_vertex_name):

    print("Longest Path:")

    # Check if vertex exists in vertex map
    if start_vertex_name not in self.vertex_map:
      return

    # Initialisation
    else:

      # Create stack and push the start vertex
      stack = Stack()
      stack.push(start_vertex_name)

      # Initialise visited vertices
      visited_set = set()
      visited_set.add(start_vertex_name)

      # Step A: Begin Main Traversal Loop
      while not stack.is_empty():
        # Retrieve name of vertex to process next
        u_name = stack.pop()
        # Retrieve actual data from the vertex
        u_obj = self.vertex_map[u_name]

        # Print the vertex to show DFS order
        print(f"Visited: {u_name}")

        # Iterate through all neighbors of u_obj
        for v_name in u_obj.neighbour_links:

          # Check if the neighbour is ubvisited
          if v_name not in visited_set:

            # Action 1: Mark as visited
            visited_set.add(v_name) # Use add: O(1)

            # Action 2: Add to Stack
            stack.push(v_name)
