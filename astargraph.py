import heapq
class Node:
    def __init__(self, name, g, h):
        self.name = name
        self.g = g
        self.h = h
        self.f = g + h
        self.parent = None

    def __lt__(self, other):
        return self.f < other.f

def astar_graph(start, goal):
    open_list = []
    visited = set()

    start_node = Node(start, 0, heuristics[start])
    heapq.heappush(open_list, start_node)

    while open_list:
        current = heapq.heappop(open_list)

        if current.name in visited:
            continue
        
        visited.add(current.name)

        if current.name == goal:
            path = []
            while current:
                path.append(current.name)
                current = current.parent
            return path[::-1]

        for neigh, cost in graph[current.name].items():
            if neigh not in visited:
                new_node = Node(neigh, current.g + cost, heuristics[neigh])
                new_node.parent = current
                heapq.heappush(open_list, new_node)

    return None  # Move this outside the loop

graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'D': 2},
    'C': {'A': 4, 'E': 5},
    'D': {'B': 2, 'E': 1},
    'E': {'C': 5, 'D': 1, 'F': 3, 'G': 2},
    'F': {'E': 3},
    'G': {'E': 2}
}

# Define heuristic function (estimated cost to goal)
heuristics = {
    'A': 6, 'B': 5, 'C': 4, 'D': 3,
    'E': 2, 'F': 3, 'G': 0
}

start_node = 'A'
goal_node = 'G'
path = astar_graph(start_node, goal_node)

print("Shortest path:", path)
