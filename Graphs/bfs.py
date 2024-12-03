def bfs(graph, start):
    visited = set()
    queue = []
    traversal = []

    queue.append(start)
    visited.add(start)

    while queue:
        node = queue.pop(0)
        traversal.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)

    return traversal
