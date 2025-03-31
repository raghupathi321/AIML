import heapq

# Goal state
goal_state = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]  # 0 represents the empty space
]

# Directions for moving blank space (row, col)
moves = {
    "UP": (-1, 0),
    "DOWN": (1, 0),
    "LEFT": (0, -1),
    "RIGHT": (0, 1)
}

# Function to find position of 0 (empty tile)
def find_empty_tile(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j  # Return row and col of empty space

# Function to calculate Manhattan Distance (Heuristic)
def heuristic(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0:  # Ignore empty tile
                goal_x, goal_y = divmod(state[i][j] - 1, 3)  # Goal position
                distance += abs(i - goal_x) + abs(j - goal_y)
    return distance

# Function to generate new states by moving the empty tile
def get_neighbors(state):
    neighbors = []
    x, y = find_empty_tile(state)

    for move, (dx, dy) in moves.items():
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < 3 and 0 <= new_y < 3:  # Check bounds
            new_state = [row[:] for row in state]  # Copy state
            new_state[x][y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[x][y]  # Swap
            neighbors.append((new_state, move))  # Store new state and move
    return neighbors

# Function to print the puzzle state
def print_state(state):
    for row in state:
        print(" ".join(str(num) if num != 0 else " " for num in row))
    print("\n" + "-" * 10)

# A* Algorithm
def a_star(initial_state):
    pq = []  # Priority queue
    heapq.heappush(pq, (heuristic(initial_state), 0, initial_state, []))  # (f(n), g(n), state, path)
    visited = set()

    while pq:
        f, g, state, path = heapq.heappop(pq)

        # Print the current state
        print(f"Move {g}: {'Start' if g == 0 else path[-1]}")
        print_state(state)

        if state == goal_state:
            return path  # Return the sequence of moves

        visited.add(tuple(map(tuple, state)))  # Convert list to tuple for hashing

        for new_state, move in get_neighbors(state):
            if tuple(map(tuple, new_state)) not in visited:
                new_g = g + 1  # g(n) = cost from start
                new_f = new_g + heuristic(new_state)  # f(n) = g(n) + h(n)
                heapq.heappush(pq, (new_f, new_g, new_state, path + [move]))

    return None  # No solution

# Example: Initial puzzle state
initial_state = [
    [1, 2, 3],
    [4, 0, 6],  
    [7, 5, 8]
]
solution = a_star(initial_state)
print("Moves to solve:", solution)
