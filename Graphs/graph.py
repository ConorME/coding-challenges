class Graph:
    def __init__(self, directed=False):
        self.graph = {}
        self.directed = directed

    def add_node(self, node):
        if node is not in self.graph:
            self.graph[node] = []

    def add_edge(self, head, tail):
        if head not in self.graph:
            self.add_node(head)
        if tail not in self.graph:
            self.add_node(tail)

        self.graph[head].append(tail)

        if not self.directed:
            self.graph[tail].append(head)

    def remove_node(self, node):
        if node in self.graph:
            self.graph.pop(node)
        for neighbors in self.graph.values():
            if node in neighbors:
                neighbors.remove(node)

    def remove_edge(self, head, tail):
        if head in self.graph and tail in self.graph[head]:
            self.graph[head].remove(tail)
        if not self.directed and tail in self.graph and head in self.graph[tail]:
            self.graph[tail].remove(head)

    def get_neighbors(self, node):
        return self.graph.get(node, []) 

    def __str__(self):
        return "\n".join(f"{node}: {neighbors}" for node, neighbors in self.graph.items())

