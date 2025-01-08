import unittest
from linked_list import Node
from partition import partition

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
        # Creating a linked list: 1 -> 4 -> 3 -> 2 -> 5 -> 2
        head = create_linked_list([1, 4, 3, 2, 5, 2])
        k = 3
        
        # Partition the list around k = 3
        partitioned_head = partition(head, k)

        # Convert back to list to verify results
        result = linked_list_to_list(partitioned_head)

        # Expected: Elements less than 3 should come before elements >= 3
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

if __name__ == "__main__":
    unittest.main()

