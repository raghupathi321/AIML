def alpha_beta_pruning(node, depth, alpha, beta, maximizing):
    print(f"Depth: {depth}, Node: {node}, Alpha: {alpha}, Beta: {beta}, Maximizing: {maximizing}")
    
    if depth == 0 or isinstance(node, int):
        print(f"Returning leaf node value: {node}")
        return node

    if maximizing:
        value = float('-inf')
        for child in node:
            value = max(value, alpha_beta_pruning(child, depth - 1, alpha, beta, False))  # Toggle maximizing
            alpha = max(alpha, value)
            print(f"Updated Alpha: {alpha}, Value: {value}")
            if alpha >= beta:
                print("Pruning remaining branches (Maximizing)")
                break
    else:
        value = float('inf')
        for child in node:
            value = min(value, alpha_beta_pruning(child, depth - 1, alpha, beta, True))  # Toggle maximizing
            beta = min(beta, value)
            print(f"Updated Beta: {beta}, Value: {value}")
            if beta <= alpha:
                print("Pruning remaining branches (Minimizing)")
                break
    
    return value

def build_tree(leaf_values, b):
    while len(leaf_values) > 1:
        leaf_values = [leaf_values[i:i + b] for i in range(0, len(leaf_values), b)]
    return leaf_values[0]

# **User Input and Execution**
levels = int(input("Enter number of levels: "))
b = int(input("Enter branching factor: "))
leaf_values = list(map(int, input("Enter leaf values: ").split()))

tree = build_tree(leaf_values, b)
print("\nBest Outcome:", alpha_beta_pruning(tree, levels - 1, float('-inf'), float('inf'), True))
