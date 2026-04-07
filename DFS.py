# Define the tree using adjacency list
tree = {
    1: [2, 3],
    2: [4, 5],
    3: [6, 7],
    4: [],
    5: [],
    6: [],
    7: []
}

# DFS function
def dfs(node, visited):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        
        # Visit all adjacent nodes
        for neighbor in tree[node]:
            dfs(neighbor, visited)

# Main execution
visited = set()
print("DFS Traversal:")
dfs(1, visited)