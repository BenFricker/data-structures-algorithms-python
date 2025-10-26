
def main():
  while True:
      try:
        # Prompt User for the filename to extract customer data
        filename = input("Enter filename: ")
        if not filename.strip():
          filename = "a2-sample.txt"

        # Create graph
        graph, start_vertex, goal_vertex, number_vertices, number_edges  = \
          DirectedWeightedGraph.read_graph(filename)

        # Store start & goal verticies
        start_object = graph.vertex_map[start_vertex]
        goal_object = graph.vertex_map[goal_vertex]

        euclidean_distance = ((goal_object.x - start_object.x) ** 2 + (goal_object.y - start_object.y) ** 2) ** 0.5

        # --------------- General Info --------------- #
        print(f"Vertices: {number_vertices}, Edges: {number_edges}")
        print(f"Start: {start_vertex}, Goal: {goal_vertex}")
        print(f"Euclidean distance (start-goal): {euclidean_distance:.3f}")

        # --------------- Dijkstra's Algorithm --------------- #
        print("###### Shortest path by Dijkstra's Algorithm: ######")

        dijkstras_path, dijkstras_length, dijkstras_expanded = \
            graph.dijkstras_algorithm(start_vertex, goal_vertex)

        if dijkstras_path is None:
            print("Shortest path: No path")
            print("Shortest length: INF")
        else:
            print(f"Shortest path: {' '.join(map(str, dijkstras_path))}")
            print(f"Shortest length: {dijkstras_length:.3f}")
        print(f"Number of expanded nodes: {dijkstras_expanded}")

        # --------------- A* Algorithm --------------- #
        print("###### Shortest path by A* Algorithm ######")

        astar_path, astar_length, astar_expanded = \
          graph.astar_algorithm(start_vertex, goal_vertex)

        if astar_path is None:
          print("Shortest path: No path")
          print("Shortest length: INF")
        else:
          print(f"Shortest path: {' '.join(map(str, astar_path))}")
          print(f"Shortest length: {astar_length:.3f}")
        print(f"Number of expanded nodes: {astar_expanded}")

        # --------------- Depth First Search Algorithm --------------- #
        print("###### Longest Path by DFS ######")

        dfs_path, dfs_length = graph.depth_first_search(start_vertex, goal_vertex)

        if dfs_path is None:
          print("Longest path: No path")
          print("Longest length: INF")
        else:
          print(f"Longest path: {' '.join(map(str, dfs_path))}")
          print(f"Longest length: {dfs_length:.3f}")


      except FileNotFoundError as e:
        print(f"\nFile: \"{filename}\" cannot be found in directory.\nPlease enter a valid filename.\n") # type: ignore

        # Ask user if they would like to retry
        try_again = input("Would you like to try again (yes/no)? ")

        # If yes, allow user to retry
        if try_again.lower().strip() == "yes":
          print("\nTrying again...\n")

        # Anything else - end program
        else:
          break
      finally:
        break


if __name__ == "__main__":
