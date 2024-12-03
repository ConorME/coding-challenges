import unittest
from graph import Graph

class TestGraph(unittest.TestCase):
    def setUp(self):
        """Set up a fresh graph instance for each test."""
        self.graph = Graph(directed=False) 
        self.directed_graph = Graph(directed=True)

    def test_add_node(self):
        self.graph.add_node('A')
        self.assertIn('A', self.graph.graph)
        self.assertEqual(self.graph.get_neighbors('A'), [])

    def test_add_edge_undirected(self):
        self.graph.add_edge('A', 'B')
        self.assertIn('B', self.graph.get_neighbors('A'))
        self.assertIn('A', self.graph.get_neighbors('B'))

    def test_add_edge_directed(self):
        self.directed_graph.add_edge('A', 'B')
        self.assertIn('B', self.directed_graph.get_neighbors('A'))
        self.assertNotIn('A', self.directed_graph.get_neighbors('B'))

    def test_remove_edge_undirected(self):
        self.graph.add_edge('A', 'B')
        self.graph.remove_edge('A', 'B')
        self.assertNotIn('B', self.graph.get_neighbors('A'))
        self.assertNotIn('A', self.graph.get_neighbors('B'))

    def test_remove_edge_directed(self):
        self.directed_graph.add_edge('A', 'B')
        self.directed_graph.remove_edge('A', 'B')
        self.assertNotIn('B', self.directed_graph.get_neighbors('A'))
        self.assertNotIn('A', self.directed_graph.get_neighbors('B'))

    def test_remove_node(self):
        self.graph.add_edge('A', 'B')
        self.graph.add_edge('A', 'C')
        self.graph.remove_node('A')
        self.assertNotIn('A', self.graph.graph)
        self.assertNotIn('A', self.graph.get_neighbors('B'))
        self.assertNotIn('A', self.graph.get_neighbors('C'))

    def test_get_neighbors_existing_node(self):
        self.graph.add_edge('A', 'B')
        self.graph.add_edge('A', 'C')
        neighbors = self.graph.get_neighbors('A')
        self.assertIn('B', neighbors)
        self.assertIn('C', neighbors)

    def test_get_neighbors_non_existing_node(self):
        neighbors = self.graph.get_neighbors('X')
        self.assertEqual(neighbors, [])

    def test_string_representation(self):
        self.graph.add_edge('A', 'B')
        self.graph.add_edge('B', 'C')
        expected_output = "A: ['B']\nB: ['A', 'C']\nC: ['B']"
        self.assertEqual(str(self.graph), expected_output)

    def test_directed_graph_string_representation(self):
        self.directed_graph.add_edge('A', 'B')
        self.directed_graph.add_edge('B', 'C')
        expected_output = "A: ['B']\nB: ['C']\nC: []"
        self.assertEqual(str(self.directed_graph), expected_output)

if __name__ == '__main__':
    unittest.main()

