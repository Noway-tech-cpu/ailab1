def dls(graph, node, goal, depth, visited):
    # Depth-Limited Search
    if depth == 0 and node == goal:
        return True

    if depth > 0:
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                if dls(graph, neighbor, goal, depth - 1, visited):
                    return True
                visited.remove(neighbor)
    return False


def iddfs(graph, start, goal, max_depth):
    for depth in range(max_depth + 1):
        visited = set()
        visited.add(start)
        print(f"Searching at depth level: {depth}")

        if dls(graph, start, goal, depth, visited):
            print(f"Goal node '{goal}' found at depth {depth}")
            return True

    print("Goal node not found within depth limit")
    return False


# Example graph (Adjacency List)
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

start_node = 'A'
goal_node = 'F'
max_depth = 3

iddfs(graph, start_node, goal_node, max_depth)