import unittest
from linked_list import Node
from partition import partition
from intersection import intersection
from loop_detection import loop_dections

def create_linked_list(values):
    if not values:
        return None
    head = Node(values[0])
    current = head
    for value in values[1:]:
        current.next = Node(value)
        current = current.next
    return head

def linked_list_to_list(head):
    values = []
    while head:
        values.append(head.value)
        head = head.next
    return values

class TestPartitionFunction(unittest.TestCase):
    def test_partition_basic(self):
        head = create_linked_list([1, 4, 3, 2, 5, 2])
        k = 3
        partitioned_head = partition(head, k)
        result = linked_list_to_list(partitioned_head)
        self.assertEqual(result, [1, 2, 2, 4, 3, 5])

    def test_all_less_than_k(self):
        head = create_linked_list([1, 2, 1])
        k = 3
        result = linked_list_to_list(partition(head, k))
        self.assertEqual(result, [1, 2, 1])

    def test_all_greater_than_k(self):
        head = create_linked_list([5, 6, 7])
        k = 3
        result = linked_list_to_list(partition(head, k))
        self.assertEqual(result, [5, 6, 7])

    def test_empty_list(self):
        head = create_linked_list([])
        k = 3
        result = linked_list_to_list(partition(head, k))
        self.assertEqual(result, [])

    def test_single_element(self):
        head = create_linked_list([4])
        k = 3
        result = linked_list_to_list(partition(head, k))
        self.assertEqual(result, [4])

class TestIntersectionFunction(unittest.TestCase):
    def setUp(self):
        self.common = Node(7)
        self.common.next = Node(8)
        
        self.l1 = create_linked_list([3, 1, 5])
        self.l1.next.next.next = self.common

        self.l2 = create_linked_list([2, 4])
        self.l2.next.next = self.common

        self.l3 = create_linked_list([9, 10]) 

    def test_intersection_exists(self):
        result = intersection(self.l1, self.l2)
        self.assertEqual(result, self.common)

    def test_no_intersection(self):
        result = intersection(self.l1, self.l3)
        self.assertIsNone(result)

    def test_one_list_empty(self):
        result = intersection(self.l1, None)
        self.assertIsNone(result)

    def test_both_lists_empty(self):
        result = intersection(None, None)
        self.assertIsNone(result)

    def test_intersection_at_head(self):
        result = intersection(self.common, self.l2)
        self.assertEqual(result, self.common)

class TestLoopDetectionFunction(unittest.TestCase):
    def test_cycle_exists(self):
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        node4 = Node(4)

        node1.next = node2
        node2.next = node3
        node3.next = node4
        node4.next = node2

        self.assertTrue(loop_dection(node1))

    def test_no_cycle(self):
        head = create_linked_list([1, 2, 3, 4, 5])
        self.assertFalse(loop_dection(head))

    def test_cycle_at_head(self):
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)

        node1.next = node2
        node2.next = node3
        node3.next = node1

        self.assertTrue(loop_dection(node1))

    def test_single_node_no_cycle(self):
        node = Node(1)
        self.assertFalse(loop_dection(node))

    def test_single_node_with_cycle(self):
        node = Node(1)
        node.next = node 
        self.assertTrue(loop_dection(node))

if __name__ == "__main__":
    unittest.main()
   unittest.main()
