import heapq
def heuristic(state, target):
    return abs(state[0] - target) + abs(state[1] - target)  # Updated heuristic
def astar_waterjug(cap1, cap2, target):
    open_list = []
    visited = set()
    start = (0, 0)
    heapq.heappush(open_list, (0, start, []))  # Add path tracking
    solutions = []
    
    while open_list:
        _, current, path = heapq.heappop(open_list)
        
        if current in visited:
            continue
        visited.add(current)
        
        jug1, jug2 = current
        new_path = path + [current]  # Track path
        
        if jug1 == target or jug2 == target:
            solutions.append(new_path)  # Store found solution
        
        # Generate all possible next states
        next_steps = {
            (cap1, jug2),  # Fill Jug 1
            (jug1, cap2),  # Fill Jug 2
            (0, jug2),  # Empty Jug 1
            (jug1, 0),  # Empty Jug 2
            (max(0, jug1 - (cap2 - jug2)), min(cap2, jug1 + jug2)),  # Pour Jug 1 -> Jug 2
            (min(cap1, jug1 + jug2), max(0, jug2 - (cap1 - jug1)))  # Pour Jug 2 -> Jug 1
        }
        
        for next_step in next_steps:
            if next_step not in visited:
                cost = 1 + heuristic(next_step, target)
                heapq.heappush(open_list, (cost, next_step, new_path))  # Push new path
    
    return solutions


cap1 = 5
cap2 = 3
target = 2


solutions = astar_waterjug(cap1, cap2, target)


if solutions:
    print("Multiple Solutions Found:")
    for i, sol in enumerate(solutions):
        print(f"Solution {i + 1}: {sol}")
else:
    print("No solution found.")
