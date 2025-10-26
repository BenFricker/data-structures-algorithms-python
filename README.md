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
- [Features](#-features)
- [Usage](#-usage)
- [Complexity Analysis](#-complexity-analysis)
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
- **Use Cases:** GPS navigation, network routing, game AI
- **Time Complexity:** O((V + E) log V) with priority queue
- **Guarantees:** Optimal shortest path (non-negative weights)

**2. A* (A-Star) Algorithm**
- **Purpose:** Efficient shortest path with heuristics
- **Method:** Uses Euclidean distance heuristic: `f(n) = g(n) + h(n)`
  - `g(n)`: Cost from start to current node
  - `h(n)`: Estimated cost from current to goal
- **Use Cases:** Game pathfinding, robotics navigation, route planning
- **Time Complexity:** O(E) in best case, O(V²) in worst case
- **Advantage:** More efficient than Dijkstra's with good heuristics

**3. Depth-First Search (DFS) - Longest Path**
- **Purpose:** Find longest path in weighted directed graphs
- **Method:** Exhaustive recursive exploration with backtracking
- **Time Complexity:** O(V!) in worst case (exponential)
- **Note:** NP-hard problem, suitable for small graphs

**Priority Queue Implementation:**
- Min-heap data structure for efficient pathfinding
- O(log n) insert and extract operations

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

## ✨ Features

- ✅ **Pure Python Implementations** - No external dependencies, only standard library
- ✅ **Educational Focus** - Clear code with extensive comments
- ✅ **Well-Documented** - Docstrings and inline explanations
- ✅ **Tested Implementations** - All data structures verified with test cases
- ✅ **Object-Oriented Design** - Clean class-based architecture
- ✅ **Algorithmic Efficiency** - Optimal time and space complexity

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

| Data Structure | Insert | Delete | Search | Space |
|---------------|--------|--------|--------|-------|
| **Stack** | O(1) | O(1) | O(n) | O(n) |
| **Queue** | O(1) | O(1) | O(n) | O(n) |
| **Binary Search Tree** | O(log n)* | O(log n)* | O(log n)* | O(n) |
| **Max Heap** | O(log n) | O(log n) | O(n) | O(n) |
| **Adjacency List** | O(1) | O(1) | O(V+E) | O(V+E) |

*Average case for balanced tree; worst case O(n) for unbalanced

| Algorithm | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| **BFS** | O(V + E) | O(V) |
| **DFS** | O(V + E) | O(V) |
| **Dijkstra's** | O((V + E) log V) | O(V) |
| **A*** | O(E) to O(V²) | O(V) |

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
Shortest path: 1 2 4 5
Shortest length: 8.500
Expanded nodes: 4
```

---

## 🎓 Learning Outcomes

This repository demonstrates proficiency in:

- **Data Structure Design** - Understanding when and why to use specific structures
- **Algorithm Analysis** - Evaluating time and space complexity
- **Problem Solving** - Implementing solutions to classic CS problems
- **Graph Theory** - Working with vertices, edges, and graph traversals
- **Search Algorithms** - Understanding uninformed vs. informed search
- **Recursion** - Implementing recursive algorithms effectively
- **Object-Oriented Programming** - Clean class design and encapsulation
- **Code Quality** - Writing maintainable, well-documented code

---

## 🎯 Use Cases by Domain

### **Game Development**
- A* for NPC pathfinding
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
- [ ] Bellman-Ford Algorithm
- [ ] Floyd-Warshall Algorithm
- [ ] Dynamic Programming examples

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

- Developed as part of Computer Science coursework at University of Wollongong
- Implementations based on classical algorithms from computer science literature
- Inspired by the study of fundamental data structures and algorithms

---

<div align="center">

**⭐ Star this repository if you find it helpful!**

Built with 💻 and ☕ by Ben Fricker

</div>
