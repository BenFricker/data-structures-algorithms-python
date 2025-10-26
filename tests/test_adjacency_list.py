
# TEST EXECUTION BLOCK
print()
print("=" * 50)
print("TESTING ADJACENCY LIST")
print("=" * 50)
print()

def run_graph_test():
    # 1. Setup Graph
    g = Graph()
    print("--- Graph Construction ---")

    # Add 5 Vertices
    for v in ['1', '2', '3', '4', '5']:
        g.add_vertex(v)
        print(f"Added Vertex: {v}")

    # Add Edges (Undirected Graph)
    # 1 is connected to 2 and 3
    g.add_edge('1', '2', 1)
    g.add_edge('1', '3', 1)

    # 2 is connected to 4
    g.add_edge('2', '4', 1)

    # 3 is connected to 5
    g.add_edge('3', '5', 1)

    # 4 is connected to 5
    g.add_edge('4', '5', 1)

    print("Edges added: (1,2), (1,3), (2,4), (3,5), (4,5)")
    print("-" * 35)

    # 2. Run Breadth-First Search (BFS)
    print("--- BFS Traversal (Start: 1) ---")
    # Expected order: 1, 2, 3, 4, 5 (Level by Level)
    g.Breadth_First_Search('1')
    print("-" * 35)

    # 3. Run Depth-First Search (DFS)
    print("--- DFS Traversal (Start: 1) ---")
    g.depth_first_search('1')
    print("-" * 35)

if __name__ == "__main__":
    run_graph_test()



