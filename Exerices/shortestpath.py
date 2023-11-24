class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.edges = {vertex: [] for vertex in vertices}

    def add_edge(self, vertex1, vertex2, distance):
        self.edges[vertex1].append((vertex2, distance))
        self.edges[vertex2].append((vertex1, distance))

class Node:
    def __init__(self, name):
        self.name = name
        self.edges = []
        self.distance = float('inf')
        self.heuristic = float('inf')
        self.cost = float('inf')
        self.parent = None

def a_star(graph, start, end):
    open_set = set([start])
    closed_set = set([])
    current = start

    start.distance = 0
    start.heuristic = 0
    start.cost = 0

    while open_set:
        current = min(open_set, key=lambda o:o.cost)
        if current == end:
            path = []
            while current.parent:
                path.append(current)
                current = current.parent
            path.append(current)
            return path[::-1], end.cost

        open_set.remove(current)
        closed_set.add(current)

        for neighbor, distance in graph.edges[current.name]:
            if neighbor in closed_set:
                continue
            if neighbor not in open_set:
                neighbor_node = Node(neighbor)
                neighbor_node.parent = current
                neighbor_node.distance = current.distance + distance
                neighbor_node.heuristic = 0
                neighbor_node.cost = neighbor_node.distance + neighbor_node.heuristic
                open_set.add(neighbor_node)
            else:
                neighbor_node = next(node for node in open_set if node.name == neighbor)
                if current.distance + distance < neighbor_node.distance:
                    neighbor_node.distance = current.distance + distance
                    neighbor_node.cost = neighbor_node.distance + neighbor_node.heuristic
                    neighbor_node.parent = current

    return None, None

# Create graph with vertices A,B,C,D,E
graph = Graph(['A', 'B', 'C', 'D', 'E'])

# Connect edges with distances AB=3, BC=5, CD=7, DA=3, DE=10
graph.add_edge('A', 'B', 3)
graph.add_edge('B', 'C', 5)
graph.add_edge('C', 'D', 7)
graph.add_edge('D', 'A', 3)
graph.add_edge('D', 'E', 10)

# Set A as source, E as destination
start = Node('A')
end = Node('E')

# Run A* algorithm
path, cost = a_star(graph, start, end)

# Print results
if path:
    print('Path:', '->'.join(node.name for node in path))
    print('Cost:', cost)
else:
    print('No path found')