import heapq

class Node:
    def __init__(self, x, y, g, h):
        self.x, self.y, self.g, self.h = x, y, g, h
        self.f = g + h
        self.parent = None
    def __lt__(self, other):  
        return self.f < other.f

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])  # Manhattan distance

def a_star(grid, start, goal):
    open_list, closed_set = [], set()
    heapq.heappush(open_list, Node(start[0], start[1], 0, heuristic(start, goal)))

    while open_list:
        current = heapq.heappop(open_list)  # Get lowest f-cost node

        if (current.x, current.y) == goal:  # Goal reached
            path = []
            while current:
                path.append((current.x, current.y))
                current = current.parent
            return path[::-1]  # Reverse path

        closed_set.add((current.x, current.y))  # Mark as visited

        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:  # Move directions
            x, y = current.x + dx, current.y + dy
            if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 0 and (x, y) not in closed_set:
                neighbor = Node(x, y, current.g + 1, heuristic((x, y), goal))
                neighbor.parent = current
                heapq.heappush(open_list, neighbor)

    return None  # No path found

grid = [
    [0, 0, 0, 0, 1],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

start, goal = (0, 0), (4, 4)
path = a_star(grid, start, goal)
print("Path:", path)
