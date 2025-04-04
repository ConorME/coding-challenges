# 4.1 Route Between Nodes: Given a directed graph and two nodes, design an algorithm to find out whether there is a route from S to E.

import unittest
from graph import Graph
from collections import deque

def route_between_nodes(graph, start, end):
    if (start == end):
        return True

    visited = set([start])
    queue = deque([start])

    while queue:
        current = queue.popleft()
        if current == end:
            return True
        for neighbor in graph.get_neighbors(current):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return False

class TestRouteBetweenNodes(unittest.TestCase):
    def setUp(self):
        self.graph_str = Graph(True)
        self.graph_str.add_edge('A', 'B')
        self.graph_str.add_edge('B', 'C')
        self.graph_str.add_edge('C', 'D')
        
        self.graph_int = Graph(True)
        self.graph_int.add_edge(1, 2)
        self.graph_int.add_edge(2, 3)
        self.graph_int.add_edge(3, 4)
        
    def test_route_string(self):
        self.assertTrue(route_between_nodes(self.graph_str, 'A', 'D'))
        self.assertFalse(route_between_nodes(self.graph_str, 'D', 'A'))
        self.assertTrue(route_between_nodes(self.graph_str, 'A', 'A'))
    
    def test_route_int(self):
        self.assertTrue(route_between_nodes(self.graph_int, 1, 4))
        self.assertFalse(route_between_nodes(self.graph_int, 4, 1))
        self.assertTrue(route_between_nodes(self.graph_int, 1, 1))

if __name__ == '__main__':
    unittest.main()
