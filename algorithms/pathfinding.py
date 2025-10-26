"""
1. Dijkstra's Algorithm
2. A* Algorithm
3. Depth First Search
"""

class Vertex:
  """
  Vertex Class:
  name:             Name of the Vertex
  neighbour_links:  Maps neighbours name to weight
  x:                x coordinate
  y:                y coordinate
  """
  def __init__(self, name, x=0, y=0):
    self.name = name
    self.neighbour_links = {}
    self.x = x
    self.y = y

class PriorityQueue:
  """
  Priority Queue: Min Heap

  Dijkstra's Algorithm:
  Utilised in Dijkstra's Algorithm by identifying which path has
  the lowest cost, expanding that node, before returning to the
  other neighbours and visiting them in order be

  A* Algorithm:
  """
  def __init__(self):
    # Initialise heap
    self.heap = []
    self.size = 0

  def is_empty(self):
    """Check if heap is empty"""
    return self.size == 0

  def enqueue(self, node):
    """Add node to heap"""
    self.heap.append(node)
    self.size += 1
    self.siftUp(self.size - 1)

  def dequeue(self):
    """Remove & return node from heap"""
    # Check for empty heap
    if self.is_empty():
      return None

    # Swap root & last node, remove & return old root then decrement size
    self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
    next_node = self.heap.pop()
    self.size -= 1

    # Sift new root down
    if self.size > 0:
      self.siftDown(0)

    return next_node

  def siftUp(self, index):
    """Sift nodes up the heap"""
    if index == 0:
      return

    # Initialise parent node
    parent = (index - 1) // 2

    # If current node is more than parent then return, otherwise swap
    if self.heap[index] > self.heap[parent]:
      return
    else:
      self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]

      # Recursively sift up
      self.siftUp(parent)

  def siftDown(self, index):
    """Sift nodes down the heap"""

    # Initialise smallest, left & right children
    left_child = (index * 2) + 1
    right_child = (index * 2) + 2
    smallest_node = index

    # If left child exists and smaller than current node
    if left_child < self.size and self.heap[left_child] < self.heap[smallest_node]:
      # Assign smallest node to left child
      smallest_node = left_child

    # If right child exists and smaller than current node & left child
    if right_child < self.size and self.heap[right_child] < self.heap[smallest_node]:
      # Assign smallest node to right child
      smallest_node = right_child

    # If index remains smallest node
    if smallest_node!= index:
      self.heap[index], self.heap[smallest_node] = self.heap[smallest_node], self.heap[index]
      self.siftDown(smallest_node)


class DirectedWeightedGraph:
  """Directed Weighted Graph"""
  def __init__(self):
    # Initialise vertex map
    self.vertex_map = {}

  def add_vertex(self, v_name, x, y):
    """Add Vertices to Graph"""

    # If vertex name exists, return
    if v_name in self.vertex_map:
      return

    # Create vertex object
    else:
      vertex = Vertex(v_name, x, y)

      # Add vertex object to vertex map
      self.vertex_map[v_name] = vertex

  def add_edge(self, u_name, v_name, weight):
    """Add Edges to Graph"""

    # Check if u/v vertices exist already
    if u_name not in self.vertex_map \
    or v_name not in self.vertex_map:
      return

    else:
      # Create u objects in vertex map
      u_object = self.vertex_map[u_name]

      # Create directed edge (from u to v)
      u_object.neighbour_links[v_name] = weight # Directed Graph

  # ============ Depth First Search Algorithm (DFS) ============ #
  def depth_first_search(self, start_vertex, goal_vertex=None):
    # Check start & goal vertices exist
    if start_vertex not in self.vertex_map or goal_vertex not in self.vertex_map:
      return None, float("-inf")

    # Initialise longest path
    longest_path = []
    longest_distance = float("-inf")

    # Initialise visited set & current path
    current_path = []
    visited_set = set()

    def depth_helper(u_name, path_distance):
      """DFS Recursive Helper Function"""
      # Initialise variables as enclosed within helper
      nonlocal longest_path, longest_distance

      # Add current vertex to visited set & add to current path
      visited_set.add(u_name)
      current_path.append(u_name)

      # Check if current vertex is the goal
      if u_name == goal_vertex:
        # If longer, update longest path
        if path_distance > longest_distance:
          longest_distance = path_distance
          longest_path = current_path.copy()

      # Recursively loop through & search neighbours: Even if goal is found
      else:
        u_object = self.vertex_map[u_name]

        for v_name, weight in u_object.neighbour_links.items():
          if v_name not in visited_set:
            depth_helper(v_name, path_distance + weight)

      visited_set.remove(u_name)
      current_path.pop()

    depth_helper(start_vertex, 0)

    if longest_distance == float("-inf"):
      return None, float("-inf")

    return longest_path, longest_distance


  # ================== Dijkstra's Algorithm ================== #
  def dijkstras_algorithm(self, start_vertex, goal_vertex):
    # Check start & goal vertices exist
    if start_vertex not in self.vertex_map or goal_vertex not in self.vertex_map:
      return None, float("inf"), 0

    # Initialise parent tracking & distances
    distance = {}
    parent = {}
    candidate_set = set()
    expanded_nodes = 0

    # Initialise distances to infinity
    for vertex in self.vertex_map:
      distance[vertex] = float("inf")
      parent[vertex] = None
      candidate_set.add(vertex)

    # Set start vertex distance = 0
    distance[start_vertex] = 0

    # Begin Main Loop
    while candidate_set:
      # Find vertex in candidate set with minimum distance
      shortest_vertex = None
      shortest_distance = float("inf")

      for candidate in candidate_set:
        if distance[candidate] < shortest_distance:
          shortest_distance = distance[candidate]
          shortest_vertex = candidate

      # If shortest vertex found, break
      if shortest_vertex is None or shortest_vertex == float("inf"):
        break

      # Remove from candidate set
      candidate_set.remove(shortest_vertex)
      expanded_nodes += 1

      # Store vertex object
      u_object = self.vertex_map[shortest_vertex]

      # Iterate through & process all neighbours
      for v_name, weight in u_object.neighbour_links.items():
        if v_name in candidate_set:
          new_distance = distance[shortest_vertex] + weight

          # If distance is shorter, update
          if new_distance < distance[v_name]:
            distance[v_name] = new_distance
            parent[v_name] = shortest_vertex

    # If goal not found, return
    if distance[goal_vertex] == float("inf"):
      return None, float("inf"), expanded_nodes

    path = []
    current = goal_vertex

    # Rebuild path to start
    while current is not None:
      path.append(current)
      current = parent[current]
    path.reverse()

    return path, distance[goal_vertex], expanded_nodes

  # ==================== A* Algorithm ==================== #
  def astar_algorithm(self, start_vertex, goal_vertex):
    # Check if start vertex exists
    if start_vertex not in self.vertex_map:
      return None, float("inf"), 0

    # Initialise parent tracking
    distance = {}
    parent = {}
    distance[start_vertex] = 0
    parent[start_vertex] = None

    # Initialise start & goal objects
    start_object = self.vertex_map[start_vertex]
    goal_object = self.vertex_map[goal_vertex]

    # Initialise priority queue
    priority_queue = PriorityQueue()
    priority_queue.enqueue((0, start_vertex)) # Start f(n) = 0

    # Initialise visited set & expanded nodes counter
    visited_set = set()
    expanded_nodes = 0

    # Initialise u_name
    u_name = start_vertex

    # Begin Main Loop: Run if queue is not empty
    while not priority_queue.is_empty():

      # Retreive current f(n) and vertex name
      result = priority_queue.dequeue()
      if result is None:
        continue

      # Get f(n) & vertex name
      fn, u_name = result

      # Ensure vertex name not already in visited set
      if u_name in visited_set:
        continue

      # Add to visited set & increment expanded nodes
      visited_set.add(u_name)
      expanded_nodes += 1

      # Create u_object
      u_object = self.vertex_map[u_name]

      if u_name == goal_vertex:
        break

      # Loop through neibours
      for v_name, weight in u_object.neighbour_links.items():

        # If vertex already visited, skip it
        if v_name in visited_set:
          continue

        # Initialise vertex object
        v_object = self.vertex_map[v_name]

        # 1) Calculate g(n)
        gn = distance[u_name] + weight

        if v_name not in distance or gn < distance[v_name]:
          distance[v_name] = gn
          parent[v_name] = u_name

        # 2) Calculate h(n)
        hn = ((goal_object.x - v_object.x) ** 2 + (goal_object.y - v_object.y) ** 2) ** 0.5

        # 3) Calculate f(n)
        fn = gn + hn

        # Enqueue f(n) score and vertex name
        priority_queue.enqueue((fn, v_name))

    if goal_vertex not in distance:
      return None, float("inf"), 0

    path = []
    current = goal_vertex

    # Rebuild path
    while current is not None:
      path.append(current)
      current = parent[current]
    path.reverse()

    return path, distance[goal_vertex], expanded_nodes

  @staticmethod
  def read_graph(filename):
    """Load and read graph from file"""
    graph = DirectedWeightedGraph()

    # Open file & read all lines
    with open(filename) as file:
      lines = file.readlines()

    # Clean all lines
    lines = [line.strip() for line in lines]

    # Split first line
    start_line = lines[0].split()
    # Store number of vertices & edges
    number_vertices = int(start_line[0])
    number_edges = int(start_line[1])

    # Split last line
    last_line = lines[-1].split()
    # Store start & goal vertices
    start_vertex = int(last_line[0])
    goal_vertex = int(last_line[1])

    # Initialise vertex coordinates
    vertex_coordinates = {}

    # Parse all vertex names & lines
    for i in range(1, number_vertices + 1):
      sections = lines[i].split()
      k = int(sections[0]) # Vertex name
      x = float(sections[1]) # X coordinate
      y = float(sections[2]) # Y coordinate

      # Add vertex to graph
      graph.add_vertex(k, x, y)

      # Set vertex coordinates
      vertex_coordinates[k] = (x, y)

    # Parse all edge lines
    for i in range(number_vertices + 1, number_vertices + number_edges + 1):
      sections = lines[i].split()
      u_edge = int(sections[0]) # From edge
      v_edge = int(sections[1]) # To edge
      weight = float(sections[2]) # Edge weight

      # Add edges to graph
      graph.add_edge(u_edge, v_edge, weight)

    return graph, start_vertex, goal_vertex, number_vertices, number_edges
  main()
