# Data Structures & Algorithms in Python

A comprehensive collection of fundamental computer science data structures and algorithms implemented from scratch in Python, demonstrating core CS concepts and algorithmic problem-solving.

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)

</div>

---

## 📚 Table of Contents

- [Overview](#-overview)
- [Implementations](#-implementations)
- [Performance Analysis](#-performance-analysis)
- [Features](#-features)
- [Usage](#-usage)
- [Complexity Analysis](#-complexity-analysis)
- [Data Structures & Design Decisions](#-data-structures--design-decisions)
- [Testing](#-testing)
- [Learning Outcomes](#-learning-outcomes)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🎯 Overview

This repository contains educational implementations of essential data structures and algorithms, built to demonstrate deep understanding of computer science fundamentals. All implementations prioritize clarity, correctness, and educational value while maintaining efficient algorithmic complexity.

**Key Focus Areas:**
- Core data structures (trees, graphs, heaps, queues, stacks)
- Graph algorithms (BFS, DFS, pathfinding)
- Advanced search algorithms (Dijkstra's, A*)
- Custom implementations without external dependencies

---

## 🗂️ Implementations

### Linear Data Structures

#### **[Stack](linear/stack.py)**
LIFO (Last In, First Out) data structure
- **Operations:** Push, Pop, Peek
- **Use Cases:** Function call stack, undo mechanisms, expression evaluation
- **Time Complexity:** O(1) for all operations

#### **[Queue](linear/queue.py)**
FIFO (First In, First Out) data structure
- **Operations:** Enqueue, Dequeue
- **Use Cases:** BFS, task scheduling, buffer management
- **Time Complexity:** O(1) for all operations

---

### Trees

#### **[Binary Search Tree](trees/binary_search_tree.py)**
Ordered binary tree maintaining BST property
- **Operations:** Insert, Delete, Search, In-order Traversal
- **Features:**
  - Handles all deletion cases (leaf, one child, two children)
  - Duplicate prevention
  - Recursive traversal methods
- **Time Complexity:**
  - Average: O(log n) for insert, delete, search
  - Worst: O(n) for unbalanced tree

**Key Implementation Details:**
```python
# Deletion handles 4 cases:
# 1. Leaf node - Simple removal
# 2. One left child - Replace with left child
# 3. One right child - Replace with right child  
# 4. Two children - Replace with in-order successor
```

---

### Graphs

#### **[Adjacency List](graphs/adjacency_list.py)**
Efficient sparse graph representation
- **Features:**
  - Vertex and edge management
  - Weighted edge support
  - Custom Queue and Stack implementations
- **Algorithms Included:**
  - **Breadth-First Search (BFS)** - Level-by-level traversal
  - **Depth-First Search (DFS)** - Deep exploration traversal
- **Space Complexity:** O(V + E) where V = vertices, E = edges

**Graph Structure:**
```python
# Adjacency List stores neighbors for each vertex
# Vertex 1: [2, 3]  (connected to vertices 2 and 3)
# Vertex 2: [4]     (connected to vertex 4)
```

---

### Algorithms

#### **[Pathfinding Algorithms](algorithms/pathfinding.py)**
Classic graph search and shortest path algorithms on directed weighted graphs

**1. Dijkstra's Algorithm**
- **Purpose:** Find shortest path in weighted graphs
- **Method:** Uniform cost search, expands lowest cost nodes first
- **Implementation:** Uses linear scan for minimum distance vertex (O(V²))
- **Use Cases:** GPS navigation, network routing, game AI
- **Time Complexity:** O(V²) with linear scan; O((V + E) log V) possible with binary heap
- **Guarantees:** Optimal shortest path (non-negative weights)

**Why O(V²):** This implementation uses a simple linear scan to find the minimum distance vertex in each iteration. While a binary min-heap could optimize this to O((V + E) log V), the O(V²) approach has less overhead and is more suitable for small to medium-sized graphs with simpler implementation.

**2. A* (A-Star) Algorithm**
- **Purpose:** Efficient shortest path with heuristics
- **Method:** Uses Euclidean distance heuristic: `f(n) = g(n) + h(n)`
  - `g(n)`: Cost from start to current node
  - `h(n)`: Estimated cost from current to goal (Euclidean distance)
- **Use Cases:** Game pathfinding, robotics navigation, route planning
- **Time Complexity:** O((V + E) log V) with priority queue
- **Advantage:** Dramatically more efficient than Dijkstra's with good heuristics

**Heuristic Properties:**
- **Admissible:** The Euclidean distance heuristic never overestimates the actual cost (straight-line distance is always the shortest possible)
- **Consistent:** Satisfies the triangle inequality h(u) ≤ cost(u,v) + h(v), guaranteeing that estimated costs never decrease along any path
- **Optimal:** These properties ensure A* finds the optimal path while expanding far fewer nodes than Dijkstra's

**3. Depth-First Search (DFS) - Longest Path**
- **Purpose:** Find longest path in weighted directed graphs
- **Method:** Exhaustive recursive exploration with backtracking
- **Strategy:** Explores all simple paths from start to goal, maintaining a visited set to prevent cycles while allowing vertices in different paths
- **Time Complexity:** O(V!) in worst case (exponential)
- **Space Complexity:** O(V) for recursion stack and visited set
- **Note:** NP-hard problem - fundamentally different from shortest path problems which have optimal substructure

**Why Longest Path is Hard:** Unlike shortest path problems that can use dynamic programming or greedy approaches, finding the longest simple path requires exploring all possible paths. In a dense graph, there can be up to V! distinct simple paths between two vertices, making this an exponential-time problem.

**Priority Queue Implementation:**
- Custom min-heap data structure for efficient pathfinding
- O(log n) insert and extract operations
- Essential for A*'s guided search strategy

---

### Heaps

#### **[Max Heap](heaps/max_heap.py)**
Complete binary tree maintaining max-heap property
- **Operations:** Insert, Extract-Max, Heapify
- **Use Cases:** Priority queues, heap sort, task scheduling
- **Time Complexity:**
  - Insert: O(log n)
  - Extract-Max: O(log n)
  - Heapify: O(n)

---

## 📊 Performance Analysis

### Dijkstra's vs A* Algorithm Comparison

**Test Case:** 20 vertices, 100 edges, Start: vertex 2, Goal: vertex 13

| Algorithm | Path Found | Path Length | Nodes Expanded | Efficiency |
|-----------|-----------|-------------|----------------|------------|
| **Dijkstra's** | 2 → 13 | 85.000 | 20 | Baseline |
| **A*** | 2 → 13 | 85.000 | 2 | **90% reduction!** |

### Key Insights

**Why A* Outperforms Dijkstra's:**

A* uses the Euclidean distance heuristic h(n) to intelligently prioritize vertices that are closer to the goal, dramatically reducing the search space while still guaranteeing an optimal path. Dijkstra's algorithm explores uniformly in all directions without considering the goal location, making it less efficient when a good heuristic is available.

**Real-World Impact:** In this test case, A* achieved the same optimal path while expanding only 2 nodes compared to Dijkstra's 20 nodes - a 90% reduction in computational work. This efficiency gain becomes even more pronounced in larger graphs.

**Both algorithms guarantee optimality:** The key difference is efficiency. A* provides the best of both worlds - optimal pathfinding with significantly fewer node expansions when a good heuristic is available.

### DFS Longest Path Results

**Test Case:** Same graph (20 vertices, 100 edges)

**Result:**
- Longest Path: 2 → 17 → 9 → 16 → 4 → 18 → 14 → 8 → 6 → 19 → 3 → 12 → 5 → 20 → 1 → 15 → 11 → 7 → 10 → 13
- Path Length: 1595.000
- Demonstrates exponential exploration of all simple paths between vertices

**Performance Note:** Successfully found the longest simple path through exhaustive exploration, showcasing the exponential nature of this NP-Hard problem.

---

## ✨ Features

- ✅ **Pure Python Implementations** - No external dependencies, only standard library
- ✅ **Educational Focus** - Clear code with extensive comments
- ✅ **Well-Documented** - Docstrings and inline explanations
- ✅ **Tested Implementations** - All data structures verified with test cases
- ✅ **Object-Oriented Design** - Clean class-based architecture
- ✅ **Algorithmic Efficiency** - Optimal time and space complexity
- ✅ **Performance Validated** - Includes empirical testing and comparison

---

## 🚀 Usage

### Basic Example - Binary Search Tree

```python
from trees.binary_search_tree import BinarySearchTree

# Create tree
tree = BinarySearchTree()

# Insert values
tree.insert(50)
tree.insert(30)
tree.insert(70)
tree.insert(20)
tree.insert(40)

# Search for value
result = tree.find(30)
print(result.content)  # Output: 30

# In-order traversal (sorted order)
tree.in_order_traversal()  # Output: 20 30 40 50 70

# Delete node
tree.delete(30)
tree.in_order_traversal()  # Output: 20 40 50 70
```

### Graph Pathfinding Example

```python
from algorithms.pathfinding import DirectedWeightedGraph

# Create graph
graph = DirectedWeightedGraph()

# Add vertices with coordinates
graph.add_vertex(1, 0, 0)
graph.add_vertex(2, 1, 1)
graph.add_vertex(3, 2, 0)

# Add weighted edges
graph.add_edge(1, 2, 5.0)
graph.add_edge(2, 3, 3.0)
graph.add_edge(1, 3, 10.0)

# Find shortest path using Dijkstra's
path, distance, nodes = graph.dijkstras_algorithm(1, 3)
print(f"Shortest path: {path}")      # [1, 2, 3]
print(f"Distance: {distance}")       # 8.0
print(f"Nodes explored: {nodes}")    # 3

# Find shortest path using A*
path, distance, nodes = graph.astar_algorithm(1, 3)
print(f"A* path: {path}")            # [1, 2, 3]
print(f"A* distance: {distance}")    # 8.0
print(f"A* nodes: {nodes}")          # 2 (more efficient!)

# Find longest path using DFS
path, distance = graph.depth_first_search(1, 3)
print(f"Longest path: {path}")       # All vertices in longest path
print(f"Distance: {distance}")       # Maximum weighted path length
```

### Adjacency List Graph Example

```python
from graphs.adjacency_list import Graph

# Create graph
g = Graph()

# Add vertices
for v in ['A', 'B', 'C', 'D']:
    g.add_vertex(v)

# Add edges
g.add_edge('A', 'B', 1)
g.add_edge('A', 'C', 1)
g.add_edge('B', 'D', 1)

# Breadth-First Search
g.Breadth_First_Search('A')
# Output: Visited: A, Visited: B, Visited: C, Visited: D

# Depth-First Search
g.depth_first_search('A')
# Output: Visited: A, Visited: C, Visited: B, Visited: D
```

---

## 📊 Complexity Analysis

### Data Structure Complexities

| Data Structure | Insert | Delete | Search | Space |
|---------------|--------|--------|--------|-------|
| **Stack** | O(1) | O(1) | O(n) | O(n) |
| **Queue** | O(1) | O(1) | O(n) | O(n) |
| **Binary Search Tree** | O(log n)* | O(log n)* | O(log n)* | O(n) |
| **Max Heap** | O(log n) | O(log n) | O(n) | O(n) |
| **Adjacency List** | O(1) | O(1) | O(V+E) | O(V+E) |

*Average case for balanced tree; worst case O(n) for unbalanced

### Algorithm Complexities

| Algorithm | Time Complexity | Space Complexity | Notes |
|-----------|----------------|------------------|-------|
| **BFS** | O(V + E) | O(V) | Level-by-level traversal |
| **DFS** | O(V + E) | O(V) | Deep exploration |
| **Dijkstra's** | O(V²) or O((V + E) log V) | O(V) | O(V²) with linear scan; O((V+E) log V) with heap |
| **A*** | O((V + E) log V) | O(V) | Dramatically fewer expansions with good heuristic |
| **DFS Longest Path** | O(V!) | O(V) | NP-Hard; exponential worst case |

### Complexity Insights

**Dijkstra's O(V²) vs O((V + E) log V):**
Our implementation uses a linear scan to find the minimum distance vertex, resulting in O(V²) complexity. While this could be optimized to O((V + E) log V) using a binary min-heap for the candidate set (reducing minimum-finding from O(V) to O(log V)), the simpler O(V²) approach:
- Has less implementation overhead
- Performs comparably for small-to-medium graphs
- Is more straightforward to understand and debug

For the sample graph (20 vertices, 100 edges), both approaches have similar practical performance.

**A* Optimality and Efficiency:**
A* achieves O((V + E) log V) time complexity through its priority queue implementation, which retrieves the lowest f(n) vertex in O(log V) time. Every vertex is processed once (O(V log V)) and all edges are inspected when enqueuing neighbors (O(E log V)), resulting in O((V + E) log V) total complexity. The key advantage: A* expands far fewer nodes in practice while maintaining optimality.

**Why Longest Path is Exponential:**
Finding the longest simple path is fundamentally different from shortest path problems:
- **Shortest path:** Has optimal substructure, enabling dynamic programming/greedy approaches
- **Longest path:** Lacks optimal substructure - the longest path to an intermediate vertex doesn't guarantee the overall longest path
- **Result:** Must exhaustively explore all simple paths (up to V! in dense graphs), making it NP-Hard

---

## 🗃️ Data Structures & Design Decisions

### Strategic Design Choices

Each data structure was carefully selected to optimize the algorithm's critical operations:

#### **1. Dictionary (Hash Map)**
**Used in:** Dijkstra's and A* for distance/parent tracking

**Why:**
- O(1) average-case insertion, update, and lookup operations
- Critical for efficient path reconstruction via parent pointers
- Essential during path exploration for quick distance lookups

**Impact:** Enables fast tracking of shortest distances and path reconstruction without introducing algorithmic bottlenecks.

#### **2. Set**
**Used in:** Dijkstra's (candidate_set), A* and DFS (visited_set)

**Why:**
- O(1) average-case membership testing
- O(1) insertion and deletion operations
- Perfect for tracking which vertices have been processed

**Impact:** Prevents redundant work, avoids infinite loops, and enables efficient "have we seen this vertex?" checks that are crucial for correctness.

#### **3. Priority Queue (Min-Heap)**
**Used in:** A* algorithm for vertex ordering

**Why:**
- O(log V) extraction of minimum f(n) vertex
- Automatically maintains vertices in priority order
- Enables A*'s guided search strategy

**Impact:** This is what makes A* dramatically more efficient than Dijkstra's. By always exploring the most promising vertex first (lowest f(n) = g(n) + h(n)), A* reduces the search space by up to 90% while maintaining optimality.

#### **4. List**
**Used in:** Path reconstruction (A*, Dijkstra's), current path tracking (DFS)

**Why:**
- O(1) append/pop operations at the end
- Maintains ordered sequence of vertices
- Simple and efficient for incremental path building

**Impact:** Perfect for reconstructing the final path by following parent pointers backward, then reversing. In DFS, enables efficient backtracking during recursive exploration.

### Design Philosophy

**Efficiency where it matters:** Data structures are chosen to optimize the most frequent operations in each algorithm. For example, A*'s priority queue optimizes "find minimum f(n)" which happens V times, while simple lists handle the final path reconstruction that happens only once.

**Simplicity with purpose:** Where multiple options exist (e.g., Dijkstra's linear scan vs heap), the simpler approach is chosen when performance differences are negligible for the target graph sizes. This makes the code more maintainable and easier to understand without sacrificing practical performance.

---

## 🧪 Testing

All implementations include test files demonstrating functionality:

```bash
# Test Binary Search Tree
python tests/test_bst.py

# Test Adjacency List Graph
python tests/test_adjacency_list.py

# Test Pathfinding Algorithms
python tests/test_pathfinding.py
```

**Example Test Output:**
```
===== Binary Search Tree Test =====
In-order traversal: 20 30 40 50 60 70 80
Search for 80: Found
After deletions: 20 30 40 50

===== Graph BFS Test =====
Visited: 1
Visited: 2
Visited: 3
Visited: 4
Visited: 5

===== Dijkstra's Algorithm =====
Shortest path: 2 13
Shortest length: 85.000
Nodes expanded: 20

===== A* Algorithm =====
Shortest path: 2 13
Shortest length: 85.000
Nodes expanded: 2

===== DFS Longest Path =====
Longest path: 2 17 9 16 4 18 14 8 6 19 3 12 5 20 1 15 11 7 10 13
Longest length: 1595.000
```

---

## 🎓 Learning Outcomes

This repository demonstrates proficiency in:

- **Algorithm Analysis** - Deep understanding of time/space complexity and Big O notation
- **Performance Comparison** - Empirical testing showing A*'s 90% efficiency gain over Dijkstra's
- **Data Structure Design** - Strategic selection of structures to optimize critical operations
- **Graph Theory** - Working with vertices, edges, and various graph representations
- **Search Strategy Trade-offs** - Understanding uninformed vs. informed search approaches
- **NP-Hard Problems** - Recognizing why longest path is exponential vs shortest path being polynomial
- **Heuristic Design** - Creating admissible and consistent heuristics (Euclidean distance)
- **Recursion & Backtracking** - Implementing DFS with proper cycle prevention
- **Object-Oriented Programming** - Clean class design and encapsulation
- **Code Quality** - Writing maintainable, well-documented, production-ready code

### Key Technical Insights Gained

**Why A* is Superior with Good Heuristics:**
Through implementation and testing, demonstrated that A* with Euclidean distance heuristic expands 90% fewer nodes than Dijkstra's while guaranteeing the same optimal path. This showcases the power of informed search.

**Understanding NP-Hard vs P Problems:**
Implemented both shortest path (polynomial) and longest path (exponential) algorithms, experiencing firsthand why some problems are fundamentally harder - longest path lacks the optimal substructure property that makes shortest path tractable.

**Data Structure Impact on Performance:**
Learned that algorithm complexity is theory, but practical performance depends heavily on data structure choices. Priority queues enable A*'s efficiency; hash maps make O(1) lookups possible; sets prevent redundant work.

---

## 🎯 Use Cases by Domain

### **Game Development**
- A* for NPC pathfinding (90% more efficient than Dijkstra's!)
- Priority queues for event scheduling
- Trees for spatial partitioning

### **Web Development**
- BFS/DFS for web crawling
- Graphs for social networks
- Queues for request handling

### **Systems Programming**
- Stacks for function calls
- Heaps for memory management
- Queues for process scheduling

### **AI/Machine Learning**
- Search algorithms for decision trees
- Graphs for neural networks
- Priority queues for beam search

### **Navigation & Robotics**
- A* for optimal path planning with obstacles
- Dijkstra's for guaranteed shortest paths
- Graph representations for map data

---

## 💡 Future Enhancements

Potential additions to this repository:

- [ ] AVL Tree (self-balancing BST)
- [ ] Red-Black Tree
- [ ] B-Tree implementation
- [ ] Trie (prefix tree)
- [ ] Disjoint Set (Union-Find)
- [ ] Minimum Spanning Tree (Kruskal's, Prim's)
- [ ] Topological Sort
- [ ] Bellman-Ford Algorithm (handles negative weights)
- [ ] Floyd-Warshall Algorithm (all-pairs shortest path)
- [ ] Dynamic Programming examples
- [ ] Bidirectional search optimization for A*

---

## 🤝 Contributing

This is an educational project, but suggestions and improvements are welcome!

**If you find a bug or have a suggestion:**
1. Open an issue describing the problem
2. Feel free to fork and submit a pull request

**Guidelines:**
- Maintain code clarity and documentation
- Include test cases for new implementations
- Follow existing code style and structure

---

## ⚠️ Academic Integrity Notice

This repository is shared for educational and portfolio purposes. 

**For students:**
- Use this as a learning reference only
- Do not copy code for assignments
- Understand your institution's academic integrity policies
- Learn the concepts, don't just copy implementations

---

## 📄 License

MIT License

Copyright (c) 2025 Ben Fricker

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

---

## 📞 Contact

**Ben Fricker**
- GitHub: [@BenFricker](https://github.com/BenFricker)
- LinkedIn: [Ben Fricker](https://www.linkedin.com/in/benfricker/)

---

## 🙏 Acknowledgments

- Developed as part of Computer Science coursework (CSCI203) at University of Wollongong
- Implementations based on classical algorithms from computer science literature
- Pathfinding algorithms tested and analyzed with empirical performance validation
- Inspired by the study of fundamental data structures and algorithms

---

<div align="center">

**⭐ Star this repository if you find it helpful!**

Built with 💻 by Ben Fricker

</div>
