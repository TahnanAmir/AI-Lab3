class Graph:
    def __init__(self, adjacency_list, heuristics):
        """Initializes the graph with an adjacency list and heuristics."""
        self.adjacency_list = adjacency_list
        self.heuristics = heuristics

    def get_neighbors(self, v):
        """Returns the neighbors of a given node."""
        return self.adjacency_list[v]

    def h(self, n):
        """Heuristic function: estimates the cost from node n to the goal."""
        return self.heuristics[n]

    def a_star_algorithm(self, start_node, stop_node):
        """Implements the A* search algorithm to find the optimal path."""
        open_list = set([start_node])
        closed_list = set([])

        g = {}  # Cost from start node to all other nodes
        g[start_node] = 0

        parents = {}  # Keeps track of paths
        parents[start_node] = start_node

        while len(open_list) > 0:
            n = None  # Current node

            # Find the node with the lowest f(n) = g(n) + h(n)
            for v in open_list:
                if n is None or g[v] + self.h(v) < g[n] + self.h(n):
                    n = v

            if n is None:
                print("Path does not exist!")
                return None

            # If goal node is found, reconstruct and return the path
            if n == stop_node:
                reconst_path = []

                while parents[n] != n:
                    reconst_path.append(n)
                    n = parents[n]

                reconst_path.append(start_node)
                reconst_path.reverse()

                print("Path found:", reconst_path)
                return reconst_path, g[stop_node]

            # Explore all neighbors of the current node
            for (m, weight) in self.get_neighbors(n):
                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight
                else:
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        parents[m] = n

                        if m in closed_list:
                            closed_list.remove(m)
                            open_list.add(m)

            open_list.remove(n)
            closed_list.add(n)

        print("Path does not exist!")
        return None

# Define the graph given in adjacency list
adjacency_list = {
    'The': [('cat', 2), ('dog', 3)],
    'cat': [('runs', 1)],
    'dog': [('runs', 2)],
    'runs': [('fast', 2)],
    'fast': []
}

heuristics = {
    'The': 4,
    'cat': 3,
    'dog': 3,
    'runs': 2,
    'fast': 1
}

graph1 = Graph(adjacency_list, heuristics)
start_node = 'The'
end_node = 'fast'
result = graph1.a_star_algorithm(start_node, end_node)

if result:
    path, total_cost = result
    print("Sentence:", ' '.join(path))
    print("Total cost:", total_cost)